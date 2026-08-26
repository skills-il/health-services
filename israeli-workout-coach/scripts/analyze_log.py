#!/usr/bin/env python3
"""Analyze a workout-coach log.jsonl and print progression trends and warning flags.

Usage:
    python3 analyze_log.py path/to/workout-coach/log.jsonl
    python3 analyze_log.py path/to/log.jsonl --exercise "bench press"
    python3 analyze_log.py path/to/log.jsonl --bodyweight 78   # weight calisthenics volume

Helper for the Analyst role. Per exercise it computes:
  - estimated 1RM over time for LOADED lifts (Epley: 1RM = w * (1 + reps/30))
  - a rep-based progression proxy for BODYWEIGHT lifts (pull-ups, dips, etc.), plus an
    e1RM for them too when --bodyweight is given (effective load = bodyweight + added kg)
  - weekly training volume (loaded sets = reps*kg; bodyweight sets = reps*(bodyweight+added)
    if --bodyweight given, else raw reps, which mixes units: pass --bodyweight)
  - load-conditioned RPE creep: the SAME working load drifting to a higher RPE
Lines are de-duplicated by (date, day) first, so a corrected session logged per the
supersede protocol counts once, not twice.
It then flags, using the definitions in SKILL.md / references/progression-models.md:
  - PLATEAU: at a held load, top reps and e1RM not improving across >=3 sessions
  - OVERTRAINING (overreaching): RPE creep at a constant load AND a flat/declining e1RM
    on the SAME lift, plus a second independent signal (low session feel, or a second
    fatigued lift). Same-lift pairing is deliberate: accessories plateau by design.
  - ACUTE LOAD SPIKE: consecutive-calendar-week volume jump (injury-risk, NOT overtraining)
  - DETRAINING: a gap since the last session, so loads should be regressed
  - low-feel run
The script does math only; it invents no coaching advice. The agent interprets the
output in context (profile goal, injuries, Israeli-summer heat, the user's words).
"""
import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta


def num(v, default=0.0):
    """Coerce a log value to a number. The log is written by an agent, so a numeric
    field routinely arrives quoted ("80"). Accept that; refuse anything else instead
    of crashing the whole analysis on one bad field."""
    if v is None:
        return default
    if isinstance(v, bool):
        return default
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).strip().replace(",", ""))
    except (ValueError, AttributeError):
        print(f"[warn] unreadable numeric value {v!r} treated as {default}; that set will "
              f"not count toward volume or estimated 1RM", file=sys.stderr)
        return default


def epley_1rm(weight_kg: float, reps: int) -> float:
    """Estimated one-rep max, Epley 1985. reps<=1 returns the weight itself."""
    if reps <= 1:
        return weight_kg
    return weight_kg * (1 + reps / 30)


def parse_date(d: str):
    return datetime.strptime(d, "%Y-%m-%d").date()


def _valid_date(d) -> bool:
    if not d:
        return False
    try:
        parse_date(d)
        return True
    except (ValueError, TypeError):
        return False


def iso_week(d: str) -> str:
    y, w, _ = parse_date(d).isocalendar()
    return f"{y}-W{w:02d}"


def iso_week_ordinal(d: str) -> int:
    """The proleptic-ordinal of the ISO week's Monday. Same ISO week -> same value;
    adjacent calendar weeks differ by exactly 7, correctly across year boundaries."""
    dt = parse_date(d)
    monday = dt - timedelta(days=dt.weekday())
    return monday.toordinal()


def load(path: str):
    sessions = []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                sessions.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"[warn] skipping malformed line {i}: {e}", file=sys.stderr)
    sessions.sort(key=lambda s: s.get("date", ""))
    return dedupe_superseded(sessions)


def dedupe_superseded(sessions):
    """SKILL.md and references/state-schema.md define the correction protocol as
    'append a corrected line for the same date and day; the analyst reads the latest
    matching entry'. Honour it here: for each (date, day) keep only the LAST line.
    Without this, correcting one typo double-counts that session in weekly volume
    (tripping the acute-load-spike flag) and leaves the wrong load in the e1RM series."""
    by_date = {}
    for s_ in sessions:
        by_date.setdefault(s_.get("date"), set()).add(s_.get("day"))
    for date_, days in by_date.items():
        if len(days) > 1 and None in days:
            print(f"[warn] {date_} has lines both with and without a `day` label. If one was "
                  f"meant to correct the other, it must repeat the SAME day label or it will "
                  f"be counted as a separate session.", file=sys.stderr)
    latest = {}
    for s_ in sessions:
        latest[(s_.get("date"), s_.get("day"))] = s_
    kept = list(latest.values())
    dropped = len(sessions) - len(kept)
    if dropped:
        print(f"[info] {dropped} superseded session line(s) ignored "
              f"(same date+day logged more than once; the latest line wins)", file=sys.stderr)
    kept.sort(key=lambda s_: s_.get("date", ""))
    return kept


def is_bodyweight_exercise(ex: dict) -> bool:
    """True only when the exercise has sets AND none of them carry external load.
    An empty `sets` array is not a bodyweight lift, it is a missing record."""
    sets = ex.get("sets", [])
    return bool(sets) and all(not num(st.get("kg")) for st in sets)


# Movements performed against bodyweight, where a logged kg is an ADDED load
# (a belt, a vest, a dumbbell between the feet) rather than the whole load.
CALISTHENIC_NAMES = (
    "pull-up", "pull up", "chin-up", "chin up", "dip", "push-up", "push up",
    "muscle-up", "muscle up", "inverted row", "ring row", "pistol squat",
    "bodyweight squat", "sit-up", "sit up", "plank", "leg raise", "hanging leg raise",
    "back extension", "nordic curl", "handstand push-up", "handstand push up",
    "australian pull-up", "burpee", "lunge",
)


def bodyweight_pattern(ex: dict) -> bool:
    """True for a lift performed against the user's own bodyweight (pull-up, dip,
    push-up), whether or not a belt load was added.

    Deliberately NOT "any set at kg=0". SKILL.md tells the Coach to prescribe ramp-up
    sets "climbing from an empty or light bar", so a barbell lift routinely carries a
    kg=0 warm-up set. Treating that as a bodyweight lift silently removes the user's
    main lift from the e1RM series, the plateau flag and the fatigue cluster, and
    collapses weekly volume to raw reps. Classify by name where the log carries any
    load, and fall back to all-sets-unloaded otherwise."""
    sets = ex.get("sets", [])
    if not sets:
        return False
    if all(not num(st.get("kg")) for st in sets):
        return True
    name = (ex.get("name") or "").strip().lower()
    return any(k in name for k in CALISTHENIC_NAMES)


def effective_load(st: dict, bodyweight) -> float:
    """Load actually moved in this set. For a bodyweight-pattern lift that is the
    user's bodyweight plus any added load; without --bodyweight we cannot know it."""
    return num(st.get("kg")) + (bodyweight or 0.0)


def top_loaded_set(ex: dict):
    """Return (best_e1rm, load_of_best, top_reps_at_working_load). Loaded lifts only."""
    best_e1rm, best_load = 0.0, 0.0
    for st in ex.get("sets", []):
        kg, reps = num(st.get("kg")), num(st.get("reps"))
        if kg and reps:
            e = epley_1rm(kg, reps)
            if e > best_e1rm:
                best_e1rm, best_load = e, kg
    return best_e1rm, best_load


def working_load(ex: dict):
    """The heaviest load used for >=1 set (the 'working' load for creep tracking)."""
    loads = [num(st.get("kg")) for st in ex.get("sets", []) if num(st.get("kg"))]
    return max(loads) if loads else 0.0


def trend(series):
    """series: list of (date, value). Sign of the least-squares slope over the last 4
    points. Needs >=3 points to call a direction; returns up/down/flat/'n/a'."""
    pts = series[-4:]
    if len(pts) < 3:
        return "n/a"
    ys = [v for _, v in pts]
    xs = list(range(len(ys)))
    n = len(ys)
    mx, my = sum(xs) / n, sum(ys) / n
    denom = sum((x - mx) ** 2 for x in xs) or 1
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / denom
    scale = max(abs(my), 1)
    if slope > 0.01 * scale:
        return "up"
    if slope < -0.01 * scale:
        return "down"
    return "flat"


def analyze(sessions, bodyweight):
    per_ex_e1rm = defaultdict(list)     # loaded lift -> [(date, e1rm)]
    per_ex_topreps = defaultdict(list)  # loaded lift -> [(date, top_reps_at_working_load, load)]
    per_ex_bw_reps = defaultdict(list)  # bodyweight lift -> [(date, total_reps)]
    per_ex_load_rpe = defaultdict(lambda: defaultdict(list))  # lift -> load -> [(date, avg_rpe)]
    weekly_volume = {}                  # week_ordinal -> [label, volume]
    feels = []
    runs = []

    for s in sessions:
        d = s.get("date", "")
        if s.get("feel") is not None and num(s.get("feel")):
            feels.append((d, num(s["feel"])))
        wk = iso_week_ordinal(d) if d else None
        for ex in s.get("exercises", []):
            name = ex.get("name", "?")
            if bodyweight_pattern(ex):
                total_reps = sum(num(st.get("reps")) for st in ex.get("sets", []))
                if total_reps:
                    per_ex_bw_reps[name].append((d, int(total_reps)))
                if bodyweight:
                    # Bodyweight known: fold it in so calisthenics reach volume AND e1RM,
                    # which is what SKILL.md and state-schema.md promise --bodyweight does.
                    vol = sum(effective_load(st, bodyweight) * num(st.get("reps"))
                              for st in ex.get("sets", []))
                    best = 0.0
                    for st in ex.get("sets", []):
                        r = num(st.get("reps"))
                        if r:
                            best = max(best, epley_1rm(effective_load(st, bodyweight), r))
                    if best:
                        per_ex_e1rm[name].append((d, round(best, 1)))
                else:
                    vol = total_reps  # reps only; see the unit warning printed below
            else:
                e1, load_at = top_loaded_set(ex)
                if e1:
                    per_ex_e1rm[name].append((d, round(e1, 1)))
                wl = working_load(ex)
                top_reps = max(num(st.get("reps")) for st in ex.get("sets", [])
                               if num(st.get("kg")) == wl) if wl else 0
                if wl:
                    per_ex_topreps[name].append((d, top_reps, wl))
                rpes = [num(st["rpe"]) for st in ex.get("sets", [])
                        if st.get("rpe") is not None and num(st.get("kg")) == wl
                        and num(st["rpe"])]
                if rpes and wl:
                    per_ex_load_rpe[name][wl].append((d, round(sum(rpes) / len(rpes), 2)))
                vol = sum(num(st.get("kg")) * num(st.get("reps")) for st in ex.get("sets", []))
            if wk is not None:
                if wk not in weekly_volume:
                    weekly_volume[wk] = [iso_week(d), 0.0]
                weekly_volume[wk][1] += vol
        c = s.get("cardio")
        if c and c.get("type") == "run" and num(c.get("distance_km")) and num(c.get("duration_min")):
            runs.append((d, round(num(c["duration_min"]) / num(c["distance_km"]), 2)))

    return per_ex_e1rm, per_ex_topreps, per_ex_bw_reps, per_ex_load_rpe, weekly_volume, feels, runs


def load_conditioned_rpe_creep(load_rpe):
    """True if, at the most-used working load, avg RPE is trending up across >=3 sessions."""
    if not load_rpe:
        return False
    # pick the load with the most sessions logged
    best_load = max(load_rpe, key=lambda k: len(load_rpe[k]))
    return trend(load_rpe[best_load]) == "up"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--exercise")
    ap.add_argument("--bodyweight", type=float, default=None,
                    help="bodyweight in kg, to weight calisthenics volume")
    args = ap.parse_args()

    try:
        sessions = load(args.log)
    except FileNotFoundError:
        print(f"[error] no log at {args.log}. Onboard the user first.", file=sys.stderr)
        sys.exit(1)
    # Keep only sessions with a usable date; warn about the rest instead of crashing.
    dated = [s for s in sessions if _valid_date(s.get("date"))]
    if len(dated) != len(sessions):
        print(f"[warn] {len(sessions) - len(dated)} session(s) had no valid date and were skipped",
              file=sys.stderr)
    sessions = dated
    if not sessions:
        print("Log is empty (or no dated sessions). Nothing to analyze yet.")
        return

    (per_ex_e1rm, per_ex_topreps, per_ex_bw_reps,
     per_ex_load_rpe, weekly_volume, feels, runs) = analyze(sessions, args.bodyweight)

    print(f"Sessions logged: {len(sessions)}  ({sessions[0]['date']} -> {sessions[-1]['date']})")

    # Detraining: gap since last session
    gap = (datetime.now().date() - parse_date(sessions[-1]['date'])).days
    if gap >= 14:
        print(f"\nDETRAINING FLAG: {gap} days since the last logged session. Regress working "
              f"loads (start about 10-15 percent lighter) and rebuild, do not resume at old numbers.")

    only = [args.exercise] if args.exercise else None

    print("\n== Loaded lifts: estimated 1RM (Epley) ==")
    for name in (only or sorted(per_ex_e1rm)):
        series = per_ex_e1rm.get(name, [])
        if not series:
            continue
        e1_trend = trend(series)
        print(f"  {name:24s} latest e1RM {series[-1][1]:6.1f}  trend {e1_trend:4s}  (n={len(series)})")
        # Plateau: at a held load, top reps not improving AND e1RM not improving, >=3 sessions
        tr = per_ex_topreps.get(name, [])
        if len(tr) >= 3:
            # Window BOTH trends to the current constant-load block. Reading the trend
            # across a load increase makes the normal post-increase rep dip look like a
            # stall, so a textbook double progression (80x12, 80x12, 85x8, x9, x10) would
            # otherwise be flagged as a plateau while it is working exactly as intended.
            held = tr[-1][2]
            block = []
            for entry in reversed(tr):
                if entry[2] != held:
                    break
                block.append(entry)
            block.reverse()
            if len(block) >= 3:
                block_dates = {d for d, _, _ in block}
                block_reps = [(d, r) for d, r, _ in block]
                block_e1rm = [(d, v) for d, v in series if d in block_dates]
                block_e1_trend = trend(block_e1rm)
                if trend(block_reps) in ("flat", "down") and block_e1_trend in ("flat", "down"):
                    print(f"      ^ PLATEAU FLAG: load held at {held:.0f}kg for {len(block)} "
                          f"sessions, reps and e1RM not improving -> time for a controlled variation")

    if per_ex_bw_reps:
        print("\n== Bodyweight lifts: total reps per session ==")
        for name in (only or sorted(per_ex_bw_reps)):
            series = per_ex_bw_reps.get(name, [])
            if not series:
                continue
            print(f"  {name:24s} latest {series[-1][1]:4d} reps  trend {trend(series):4s}  (n={len(series)})")
        if args.bodyweight is None:
            print("  (pass --bodyweight <kg> to include these in volume and estimated 1RM; "
                  "without it they contribute raw reps, so the weekly volume below mixes units "
                  "and the acute-load-spike ratio is unreliable)")

    if weekly_volume:
        print("\n== Weekly volume ==")
        ordered = [weekly_volume[k] for k in sorted(weekly_volume)]
        for label, vol in ordered[-6:]:
            print(f"  {label}  {vol:,.0f}")
        # Acute load spike: only between ADJACENT calendar weeks (not across a gap)
        keys = sorted(weekly_volume)
        if len(keys) >= 2 and keys[-1] - keys[-2] == 7:
            prev, curr = weekly_volume[keys[-2]][1], weekly_volume[keys[-1]][1]
            if prev > 0 and curr > 1.5 * prev:
                print(f"  ^ ACUTE LOAD SPIKE: volume up over 1.5x vs last week (injury-risk, not "
                      f"overtraining) -> consider easing the ramp")

    if runs:
        print("\n== Run pace (min/km) ==")
        for d, pace in runs[-6:]:
            mm, ss = int(pace), int(round((pace - int(pace)) * 60))
            if ss == 60:
                mm, ss = mm + 1, 0
            print(f"  {d}  {mm}:{ss:02d}/km")
        pace_trend = trend(runs)  # lower pace = faster; "down" trend = improving
        if pace_trend != "n/a":
            word = {"down": "improving (getting faster)", "up": "slowing", "flat": "flat"}[pace_trend]
            print(f"  pace trend: {word}")

    # Overtraining (overreaching) = CLUSTER of >=2 signals, per the SKILL definition.
    #
    # The two lift-based signals must come from the SAME lift. Evaluating them with a
    # bare any() over every exercise made the flag near-permanent: accessories such as
    # face pulls, calf raises and lateral raises plateau by design, so "some lift has a
    # flat e1RM" is true of any mature log, and a false deload is an expensive answer.
    low_feel = False
    if feels:
        recent = [f for _, f in feels][-3:]
        low_feel = len(recent) >= 3 and sum(recent) / len(recent) <= 2.0

    scope = [args.exercise] if args.exercise else sorted(per_ex_e1rm)
    fatigued = []
    for name in scope:
        series = per_ex_e1rm.get(name, [])
        if len(series) < 3:
            continue
        if (trend(series) in ("flat", "down")
                and load_conditioned_rpe_creep(per_ex_load_rpe.get(name, {}))):
            fatigued.append(name)

    signals = []
    if fatigued:
        signals.append("RPE creep at a constant load WITH a flat/declining estimated 1RM on "
                       + ", ".join(fatigued))
    if low_feel:
        signals.append("low session feel (<=2/5) for 3+ sessions")
    if len(signals) >= 2 or (fatigued and len(fatigued) >= 2):
        print("\n== Overtraining ==")
        print("  OVERREACHING FLAG: " + "; ".join(signals))
        print("  Consider a deload (cut working-set volume about in half for a week). This is a "
              "training judgment, not a medical diagnosis; if symptoms are pain/illness, route to a doctor.")
        print("  Rule out the cheaper explanations FIRST: Israeli-summer heat, a fast day, sleep "
              "debt, a return from miluim. If the user is also eating less than the training "
              "demands, this pattern can be low energy availability (RED-S), which a deload does "
              "not fix; see the Safety section in SKILL.md.")
    elif signals:
        print("\n== Overtraining ==")
        print("  Single fatigue signal only, no cluster: " + "; ".join(signals))
        print("  Not enough to call overreaching. Keep logging.")
    else:
        # Silence must not read as "you are fine". RPE creep needs >=3 sessions at ONE
        # constant load, which linear progression (load up every session) and double
        # progression (2-3 sessions per load) structurally rarely produce, so for many
        # users the cluster is not evaluable rather than negative.
        evaluable = [n for n in scope
                     if len(per_ex_e1rm.get(n, [])) >= 3
                     and any(len(v) >= 3 for v in per_ex_load_rpe.get(n, {}).values())]
        print("\n== Overtraining ==")
        if evaluable:
            print("  No fatigue cluster on " + ", ".join(evaluable) + ".")
        else:
            print("  NOT EVALUABLE: no lift yet has 3+ sessions at one constant load with RPE "
                  "logged, so the RPE-creep signal cannot be computed. This is not evidence "
                  "that the user is fine. Judge from session feel, sleep, and what they tell "
                  "you, and encourage logging RPE at a held load.")


if __name__ == "__main__":
    main()
