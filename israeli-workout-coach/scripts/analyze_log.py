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
supersede protocol counts once, not twice. A second line for the same date and day that
is merged into it (a session interrupted by a siren and finished later) when it carries
`"continues": true`, or when it shares no exercise with the first and has no supersede
note; a line with `"supersedes": true` or a supersede/correction note replaces it.
Trend checks read only the CURRENT block of a lift: the most recent run of sessions at
its current working load, skipping deload sessions (`"deload": true`, or a session with
at most half the usual working sets at that load and a lower RPE than usual there) and stopping at a gap of 14+ days.
e1RM ignores sets above 12 reps, where Epley is unreliable.
It then flags, using the definitions in SKILL.md / references/progression-models.md:
  - PLATEAU: in the current block (>=3 sessions), total reps at the held load and e1RM
    not improving, and RPE (when logged) not falling
  - OVERTRAINING (overreaching): RPE creep in the current block (last working set's RPE
    rising, reps not rising) AND a flat/declining e1RM on the SAME lift, plus a second
    independent signal (feel <=2 on each of the last 3 sessions, or a second fatigued
    lift). Same-lift pairing is deliberate: accessories plateau by design.
  - ACUTE LOAD SPIKE: this week's volume over 1.5x the average of the previous (up to 4)
    weeks (injury-risk, NOT overtraining)
  - DETRAINING: a gap since the last session, so loads should be regressed
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


MAX_E1RM_REPS = 12   # Epley is unreliable above this; such sets are left out of e1RM
GAP_DAYS = 14        # a gap this long ends a lift's current block (detraining)


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


def sanitize(obj, lineno: int):
    """A line that parses as JSON can still have the wrong SHAPE (a hand edit, or an
    agent that wrote a list or a string where an object belongs). Skip what cannot be
    read and say so, rather than crashing the whole analysis on one bad line."""
    if not isinstance(obj, dict):
        print(f"[warn] skipping line {lineno}: not a session object", file=sys.stderr)
        return None
    date_ = obj.get("date")
    if not (isinstance(date_, str) and _valid_date(date_)):
        print(f"[warn] skipping line {lineno}: missing or invalid `date` (YYYY-MM-DD)",
              file=sys.stderr)
        return None
    exercises = obj.get("exercises") or []
    if not isinstance(exercises, list):
        print(f"[warn] line {lineno}: `exercises` is not a list, ignoring it", file=sys.stderr)
        exercises = []
    kept = []
    for ex in exercises:
        if not isinstance(ex, dict):
            print(f"[warn] line {lineno}: skipping an exercise that is not an object",
                  file=sys.stderr)
            continue
        sets = ex.get("sets") or []
        if not isinstance(sets, list):
            sets = []
        good = [st for st in sets if isinstance(st, dict)]
        if len(good) != len(sets):
            print(f"[warn] line {lineno}: skipping set(s) of {ex.get('name', '?')!r} that "
                  f"are not objects", file=sys.stderr)
        kept.append({**ex, "sets": good})
    obj = {**obj, "exercises": kept}
    if not isinstance(obj.get("cardio"), dict):
        obj["cardio"] = None
    return obj


def load(path: str):
    sessions = []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[warn] skipping malformed line {i}: {e}", file=sys.stderr)
                continue
            clean = sanitize(obj, i)
            if clean is not None:
                sessions.append(clean)
    sessions.sort(key=lambda s: s.get("date", ""))
    return dedupe_superseded(sessions)


SUPERSEDE_WORDS = ("supersede", "correction", "מחליף", "מחליפה", "תיקון")


def _is_continuation(prev, new) -> bool:
    """Decide whether a second line for the same date and day CONTINUES the session
    (a siren, an interruption) or CORRECTS it.

    Explicit fields win: `"continues": true` merges, `"supersedes": true` replaces. A
    correction is also recognised from its notes, which the protocol tells the Logger to
    write. Without either, a line that shares no exercise with the first one (or where
    one side is cardio only) is a continuation; an overlapping line is treated as a
    correction, as before, with a hint."""
    if new.get("continues"):
        return True
    notes = str(new.get("notes") or "").lower()
    if new.get("supersedes") or any(w in notes for w in SUPERSEDE_WORDS):
        return False
    names_prev = {(e.get("name") or "").strip().lower() for e in prev.get("exercises", [])}
    names_new = {(e.get("name") or "").strip().lower() for e in new.get("exercises", [])}
    if not names_prev or not names_new or not (names_prev & names_new):
        return True
    print(f"[warn] {new.get('date')} {new.get('day')}: a second line repeats an exercise with no "
          f"supersede note, so it is read as a CORRECTION. If the session was interrupted and "
          f"resumed, log the second part with \"continues\": true.", file=sys.stderr)
    return False


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
    merged = 0
    explicit = 0
    for s_ in sessions:
        key = (s_.get("date"), s_.get("day"))
        prev = latest.get(key)
        if prev is not None and _is_continuation(prev, s_):
            s_ = {**prev, **s_,
                  "exercises": prev.get("exercises", []) + s_.get("exercises", []),
                  "cardio": s_.get("cardio") or prev.get("cardio")}
            merged += 1
            explicit += bool(s_.get("continues"))
        latest[key] = s_
    if merged:
        print(f"[info] {merged} same-day line(s) MERGED into the earlier line as one split session "
              f"({explicit} marked \"continues\", {merged - explicit} inferred from having no "
              f"exercise in common)", file=sys.stderr)
    kept = list(latest.values())
    dropped = len(sessions) - len(kept) - merged
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


# A name containing one of these is an external-load lift even if it also contains a
# calisthenic word ("dumbbell walking lunge", "barbell hip thrust").
LOADED_IMPLEMENTS = ("dumbbell", "barbell", "kettlebell", "smith", "cable", "machine")


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
    if any(num(st.get("kg")) < 0 for st in sets):
        return True  # negative kg = assistance (assisted pull-up / dip machine)
    name = (ex.get("name") or "").strip().lower()
    if any(k in name for k in LOADED_IMPLEMENTS):
        return False
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
        if kg and reps and reps <= MAX_E1RM_REPS:
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
    per_ex_bw_reps = defaultdict(list)  # bodyweight lift -> [(date, total_reps)]
    per_ex_bw_added = defaultdict(list) # bodyweight lift -> [(date, heaviest added kg)]
    per_ex_records = defaultdict(list)  # loaded lift -> [record per session], see below
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
                added = max((num(st.get("kg")) for st in ex.get("sets", [])), default=0.0)
                if added > 0:
                    per_ex_bw_added[name].append((d, added))
                if bodyweight:
                    # Bodyweight known: fold it in so calisthenics reach volume AND e1RM,
                    # which is what SKILL.md and state-schema.md promise --bodyweight does.
                    vol = sum(effective_load(st, bodyweight) * num(st.get("reps"))
                              for st in ex.get("sets", []))
                    best = 0.0
                    for st in ex.get("sets", []):
                        r = num(st.get("reps"))
                        if r and r <= MAX_E1RM_REPS:
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
                if wl:
                    at_wl = [st for st in ex.get("sets", []) if abs(num(st.get("kg")) - wl) <= 0.5]
                    rpes = [num(st["rpe"]) for st in at_wl
                            if st.get("rpe") is not None and num(st["rpe"])]
                    e1s = [epley_1rm(wl, num(st.get("reps"))) for st in at_wl
                           if 0 < num(st.get("reps")) <= MAX_E1RM_REPS]
                    per_ex_records[name].append({
                        "date": d, "wl": wl, "n_sets": len(at_wl),
                        "total_reps": sum(num(st.get("reps")) for st in at_wl),
                        # Same-position comparison: the LAST working set that carries an
                        # RPE. Averaging over "whichever sets had RPE" creates fake creep
                        # when RPE is logged on every set one day and only the top set
                        # the next.
                        "rpe": rpes[-1] if rpes else None,
                        "e1rm": max(e1s) if e1s else None,
                        "deload_flag": bool(s.get("deload")),
                    })
                vol = sum(num(st.get("kg")) * num(st.get("reps")) for st in ex.get("sets", []))
            if wk is not None:
                if wk not in weekly_volume:
                    weekly_volume[wk] = [iso_week(d), 0.0]
                weekly_volume[wk][1] += vol
        c = s.get("cardio")
        if c and str(c.get("type", "")).strip().lower() == "run":
            if num(c.get("distance_km")) and num(c.get("duration_min")):
                runs.append((d, round(num(c["duration_min"]) / num(c["distance_km"]), 2)))
            else:
                print(f"[warn] run on {d} has no distance or duration, left out of pace",
                      file=sys.stderr)

    return (per_ex_e1rm, per_ex_bw_reps, per_ex_bw_added, per_ex_records,
            weekly_volume, feels, runs)


def current_block(records):
    """The lift's most recent run of sessions at its CURRENT working load, oldest first.

    Skips deload sessions (explicit `"deload": true`, or at most half the usual number of
    working sets at that load AND a lower RPE than usual there) and stops at a load change
    or a gap of GAP_DAYS or more.
    Reading across a deload or a layoff made the normal return to RPE 8 look like
    'RPE creep', which flagged overreaching right after the deload meant to fix it."""
    if not records:
        return []
    # mark volume deloads: n_sets <= half the median of earlier sessions at the same load
    marked = []
    for i, r in enumerate(records):
        same = [x for x in records[:i] if abs(x["wl"] - r["wl"]) <= 0.5]
        sets_ = sorted(x["n_sets"] for x in same)
        rpes = sorted(x["rpe"] for x in same if x["rpe"] is not None)
        med_sets = sets_[len(sets_) // 2] if sets_ else None
        med_rpe = rpes[len(rpes) // 2] if rpes else None
        # An inferred deload must be SHORTER and EASIER. Fewer sets at a HIGHER effort is
        # a lifter who could not finish, which is exactly the fatigue the creep check
        # looks for, so it stays in the block. Without RPE only an explicit flag counts.
        inferred = (med_sets is not None and med_sets >= 2 and r["n_sets"] <= med_sets / 2
                    and r["rpe"] is not None and med_rpe is not None and r["rpe"] < med_rpe)
        marked.append((r, r["deload_flag"] or inferred))
    held = None
    block = []
    later_date = None
    for r, is_deload in reversed(marked):
        if later_date is not None and (parse_date(later_date) - parse_date(r["date"])).days >= GAP_DAYS:
            break
        if is_deload:
            later_date = r["date"]
            continue
        if held is None:
            held = r["wl"]
        elif abs(r["wl"] - held) > 0.5:
            break
        block.append(r)
        later_date = r["date"]
    block.reverse()
    return block


def rpe_creep(block):
    """Last working set's RPE trending up across >=3 sessions of the current block,
    with total reps at that load NOT trending up ('higher RPE with no rep gain')."""
    rpe_series = [(r["date"], r["rpe"]) for r in block if r["rpe"] is not None]
    if len(rpe_series) < 3:
        return False
    reps_series = [(r["date"], r["total_reps"]) for r in block]
    return trend(rpe_series) == "up" and trend(reps_series) != "up"


def rpe_evaluable(block):
    return len([r for r in block if r["rpe"] is not None]) >= 3


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

    (per_ex_e1rm, per_ex_bw_reps, per_ex_bw_added,
     per_ex_records, weekly_volume, feels, runs) = analyze(sessions, args.bodyweight)

    print(f"Sessions logged: {len(sessions)}  ({sessions[0]['date']} -> {sessions[-1]['date']})")

    # Detraining: gap since last session
    gap = (datetime.now().date() - parse_date(sessions[-1]['date'])).days
    if gap < 0:
        print(f"[warn] the last session is dated {sessions[-1]['date']}, in the future; check for a typo",
              file=sys.stderr)
    if gap >= GAP_DAYS:
        print(f"\nDETRAINING FLAG: {gap} days since the last logged session. Regress working "
              f"loads (start about 10-15 percent lighter) and rebuild, do not resume at old numbers.")

    only = None
    if args.exercise:
        want = args.exercise.strip().lower()
        known = set(per_ex_e1rm) | set(per_ex_bw_reps) | set(per_ex_records)
        only = [n for n in known if n.strip().lower() == want] or [args.exercise]

    print("\n== Loaded lifts: estimated 1RM (Epley) ==")
    for name in (only or sorted(per_ex_e1rm)):
        series = per_ex_e1rm.get(name, [])
        if not series:
            continue
        e1_trend = trend(series)
        print(f"  {name:24s} latest e1RM {series[-1][1]:6.1f}  trend {e1_trend:4s}  (n={len(series)})")
        # Plateau, read on the CURRENT block only (see current_block): reading across a
        # load increase, a deload, or a layoff turns normal training into a fake stall.
        # Progress at a held load is TOTAL reps over the working sets, not the top set:
        # double progression grows the lower sets first (8/6/6 -> 8/8/8), which a
        # top-set reading calls a plateau. Falling RPE at the same load and reps is
        # getting stronger, not stalling.
        block = current_block(per_ex_records.get(name, []))
        if len(block) >= 3:
            reps_t = trend([(r["date"], r["total_reps"]) for r in block])
            e1_t = trend([(r["date"], r["e1rm"]) for r in block if r["e1rm"]])
            rpe_pts = [(r["date"], r["rpe"]) for r in block if r["rpe"] is not None]
            rpe_t = trend(rpe_pts) if len(rpe_pts) >= 3 else "n/a"
            if reps_t in ("flat", "down") and e1_t in ("flat", "down", "n/a") and rpe_t != "down":
                print(f"      ^ PLATEAU FLAG: load held at {block[-1]['wl']:g}kg for {len(block)} "
                      f"sessions, reps and e1RM not improving -> time for a controlled variation")

    if per_ex_bw_reps:
        print("\n== Bodyweight lifts: total reps per session ==")
        for name in (only or sorted(per_ex_bw_reps)):
            series = per_ex_bw_reps.get(name, [])
            if not series:
                continue
            print(f"  {name:24s} latest {series[-1][1]:4d} reps  trend {trend(series):4s}  (n={len(series)})")
            added = per_ex_bw_added.get(name, [])
            if added:
                # A weighted pull-up progresses by adding load, so total reps can fall while
                # the lifter gets stronger. Show the added-load trend so that is not misread.
                print(f"  {'':24s} added load latest +{added[-1][1]:g}kg  trend {trend(added):4s}  "
                      f"(read reps and added load together)")
        if args.bodyweight is None:
            print("  (pass --bodyweight <kg> to include these in volume and estimated 1RM; "
                  "without it they contribute raw reps, so the weekly volume below mixes units "
                  "and the acute-load-spike ratio is unreliable)")

    if weekly_volume:
        print("\n== Weekly volume ==")
        ordered = [weekly_volume[k] for k in sorted(weekly_volume)]
        for label, vol in ordered[-6:]:
            print(f"  {label}  {vol:,.0f}")
        # Acute load spike: this week against the AVERAGE of the previous up-to-4
        # calendar weeks (weeks with no session count as zero, so returning at full volume
        # after 1-3 empty weeks does flag, in line with the DETRAINING advice; after 4+
        # empty weeks the average is zero and only DETRAINING speaks). Comparing with the single previous week flagged every
        # return from a deload week or a one-session holiday week as a spike.
        keys = sorted(weekly_volume)
        if len(keys) >= 2:
            curr_k = keys[-1]
            prior = [weekly_volume.get(curr_k - 7 * k, [None, 0.0])[1]
                     for k in range(1, 5) if curr_k - 7 * k >= keys[0]]
            chronic = sum(prior) / len(prior) if prior else 0.0
            if prior and chronic > 0 and weekly_volume[curr_k][1] > 1.5 * chronic:
                print(f"  ^ ACUTE LOAD SPIKE: this week's volume is over 1.5x the average of the "
                      f"previous {len(prior)} week(s) (injury-risk, not overtraining) -> consider "
                      f"easing the ramp")

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
        low_feel = len(recent) >= 3 and all(f <= 2 for f in recent)

    scope = only if only else sorted(per_ex_e1rm)
    fatigued = []
    for name in scope:
        series = per_ex_e1rm.get(name, [])
        if len(series) < 3:
            continue
        block = current_block(per_ex_records.get(name, []))
        e1_block = [(r["date"], r["e1rm"]) for r in block if r["e1rm"]]
        if (trend(e1_block) in ("flat", "down") and rpe_creep(block)):
            fatigued.append(name)

    signals = []
    if fatigued:
        signals.append("RPE creep at a constant load WITH a flat/declining estimated 1RM on "
                       + ", ".join(fatigued))
    if low_feel:
        signals.append("low session feel (<=2/5) on each of the last 3 sessions")
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
                     if rpe_evaluable(current_block(per_ex_records.get(n, [])))]
        print("\n== Overtraining ==")
        if evaluable:
            print("  No fatigue cluster on " + ", ".join(evaluable) + ".")
        else:
            print("  NOT EVALUABLE: no lift has 3+ recent sessions at its current load with RPE "
                  "logged, so the RPE-creep signal cannot be computed. This is not evidence "
                  "that the user is fine. Judge from session feel, sleep, and what they tell "
                  "you, and encourage logging RPE at a held load.")


if __name__ == "__main__":
    main()
