#!/usr/bin/env python3
"""Analyze a workout-coach log.jsonl and print progression trends and warning flags.

Usage:
    python3 analyze_log.py path/to/workout-coach/log.jsonl
    python3 analyze_log.py path/to/log.jsonl --exercise "bench press"
    python3 analyze_log.py path/to/log.jsonl --bodyweight 78   # weight calisthenics volume

Helper for the Analyst role. Per exercise it computes:
  - estimated 1RM over time for LOADED lifts (Epley: 1RM = w * (1 + reps/30))
  - a rep-based progression proxy for BODYWEIGHT lifts (pull-ups, dips, etc.)
  - weekly training volume (loaded sets = reps*kg; bodyweight sets = reps*bodyweight
    if --bodyweight given, else reps)
  - load-conditioned RPE creep: the SAME working load drifting to a higher RPE
It then flags, using the definitions in SKILL.md / references/progression-models.md:
  - PLATEAU: at a held load, top reps and e1RM not improving across >=3 sessions
  - OVERTRAINING (overreaching): a CLUSTER of >=2 of {RPE creep at constant load,
    flat/declining e1RM on the tracked lift, low session feel}
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
    return sessions


def is_bodyweight_exercise(ex: dict) -> bool:
    return all(not (st.get("kg") or 0) for st in ex.get("sets", []))


def top_loaded_set(ex: dict):
    """Return (best_e1rm, load_of_best, top_reps_at_working_load). Loaded lifts only."""
    best_e1rm, best_load = 0.0, 0.0
    for st in ex.get("sets", []):
        kg, reps = st.get("kg") or 0, st.get("reps") or 0
        if kg and reps:
            e = epley_1rm(kg, reps)
            if e > best_e1rm:
                best_e1rm, best_load = e, kg
    return best_e1rm, best_load


def working_load(ex: dict):
    """The heaviest load used for >=1 set (the 'working' load for creep tracking)."""
    loads = [st.get("kg") or 0 for st in ex.get("sets", []) if (st.get("kg") or 0)]
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
        if s.get("feel") is not None:
            feels.append((d, s["feel"]))
        wk = iso_week_ordinal(d) if d else None
        for ex in s.get("exercises", []):
            name = ex.get("name", "?")
            if is_bodyweight_exercise(ex):
                total_reps = sum(st.get("reps") or 0 for st in ex.get("sets", []))
                if total_reps:
                    per_ex_bw_reps[name].append((d, total_reps))
                vol = total_reps * (bodyweight or 1)  # if no bodyweight given, count reps
            else:
                e1, load_at = top_loaded_set(ex)
                if e1:
                    per_ex_e1rm[name].append((d, round(e1, 1)))
                wl = working_load(ex)
                top_reps = max((st.get("reps") or 0) for st in ex.get("sets", [])
                               if (st.get("kg") or 0) == wl) if wl else 0
                if wl:
                    per_ex_topreps[name].append((d, top_reps, wl))
                rpes = [st["rpe"] for st in ex.get("sets", [])
                        if st.get("rpe") is not None and (st.get("kg") or 0) == wl]
                if rpes and wl:
                    per_ex_load_rpe[name][wl].append((d, round(sum(rpes) / len(rpes), 2)))
                vol = sum((st.get("kg") or 0) * (st.get("reps") or 0) for st in ex.get("sets", []))
            if wk is not None:
                if wk not in weekly_volume:
                    weekly_volume[wk] = [iso_week(d), 0.0]
                weekly_volume[wk][1] += vol
        c = s.get("cardio")
        if c and c.get("type") == "run" and c.get("distance_km") and c.get("duration_min"):
            runs.append((d, round(c["duration_min"] / c["distance_km"], 2)))

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
            loads = [ld for _, _, ld in tr[-3:]]
            reps_series = [(d, r) for d, r, _ in tr]
            if len(set(loads)) == 1 and trend(reps_series) in ("flat", "down") and e1_trend in ("flat", "down"):
                print(f"      ^ PLATEAU FLAG: load held at {loads[-1]:.0f}kg, reps and e1RM not "
                      f"improving over the last 3 sessions -> time for a controlled variation")

    if per_ex_bw_reps:
        print("\n== Bodyweight lifts: total reps per session ==")
        for name in (only or sorted(per_ex_bw_reps)):
            series = per_ex_bw_reps.get(name, [])
            if not series:
                continue
            print(f"  {name:24s} latest {series[-1][1]:4d} reps  trend {trend(series):4s}  (n={len(series)})")
        if args.bodyweight is None:
            print("  (pass --bodyweight <kg> to include these in volume and e1RM)")

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

    # Overtraining (overreaching) = CLUSTER of >=2 signals, per the SKILL definition
    low_feel = False
    if feels:
        recent = [f for _, f in feels][-3:]
        low_feel = len(recent) >= 3 and sum(recent) / len(recent) <= 2.0
    creep = any(load_conditioned_rpe_creep(per_ex_load_rpe[n]) for n in per_ex_load_rpe)
    declining_e1rm = any(trend(per_ex_e1rm[n]) in ("flat", "down") and len(per_ex_e1rm[n]) >= 3
                         for n in per_ex_e1rm)
    signals = []
    if creep:
        signals.append("RPE creep at a constant load")
    if declining_e1rm:
        signals.append("flat/declining estimated 1RM")
    if low_feel:
        signals.append("low session feel (<=2/5) for 3+ sessions")
    if len(signals) >= 2:
        print("\n== Overtraining ==")
        print("  OVERREACHING FLAG (>=2 signals): " + "; ".join(signals))
        print("  Consider a deload (cut working-set volume about in half for a week). This is a "
              "training judgment, not a medical diagnosis; if symptoms are pain/illness, route to a doctor.")


if __name__ == "__main__":
    main()
