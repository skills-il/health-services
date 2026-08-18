# State Schema: profile.md and log.jsonl

This skill keeps its memory in two plain files inside a `workout-coach/` folder in
the user's working directory. Read BOTH at the start of every session before doing
anything else. Never guess the user's program or history from context: read the files.

## Folder layout

```
workout-coach/
  profile.md     # human-readable program + settings (you and the user both edit this)
  log.jsonl      # append-only training history, one JSON object per line
```

If the folder does not exist, you are on a first run: onboard the user (see SKILL.md
Step 1) and create both files. Never overwrite `log.jsonl`; only append to it.

## profile.md

A readable Markdown file. Keep it short so a human can edit it directly. Suggested shape:

```markdown
# Profile

- goal: strength            # strength | hypertrophy | fat-loss | general-fitness | endurance
- experience: intermediate  # beginner | intermediate | advanced
- equipment: gym            # gym | home | both
- units: kg                 # kg | lb
- bodyweight_kg: 78         # optional; only if the user volunteered it
- progression: double       # linear | double | rpe   (how loads advance; see references/progression-models.md)
- injuries:
  - right shoulder: avoid heavy overhead press, barbell dips
- health_flags:             # from the Step 1 screening; drives the safety rules
  - heart_or_bp_condition: false     # heart disease, uncontrolled high blood pressure
  - chest_pain_or_dizziness: false   # on exertion, ever
  - pregnant_or_postpartum: false
  - other_medical: none              # relevant conditions or medications
  - cleared_by_doctor: unknown       # yes if a doctor cleared them to train

# Program
split: PPL                  # PPL | upper-lower | full-body | custom
rotation: [A, B, C]         # the order days cycle in

## Day A - Pull
- barbell row: 4x8
- lat pulldown: 3x10
- face pull: 3x15
- barbell curl: 3x10

## Day B - Push
- bench press: 4x6
- overhead press: 3x8
- incline dumbbell press: 3x10
- triceps pushdown: 3x12

## Day C - Legs
- back squat: 4x6
- romanian deadlift: 3x8
- leg press: 3x12
- standing calf raise: 4x15
```

`rotation` is the source of truth for "what's next". The Coach role finds the last
`day` in `log.jsonl` and advances to the next entry in `rotation` (wrapping around).

## log.jsonl

One JSON object per line, appended in chronological order. One line = one session.
Schema:

```json
{
  "date": "2026-07-23",
  "day": "A",
  "exercises": [
    {"name": "barbell row",   "sets": [{"reps": 8, "kg": 70, "rpe": 8}, {"reps": 8, "kg": 70, "rpe": 8.5}, {"reps": 7, "kg": 70, "rpe": 9}]},
    {"name": "lat pulldown",  "sets": [{"reps": 10, "kg": 55, "rpe": 8}]}
  ],
  "cardio": {"type": "run", "distance_km": 5, "duration_min": 27},
  "notes": "felt strong, grip gave out on last row set",
  "feel": 4
}
```

Field rules:

| Field | Type | Notes |
|---|---|---|
| `date` | string `YYYY-MM-DD` | The session date. Ask the user if not "today". |
| `day` | string | Must match a label in `profile.md` rotation (e.g. `A`), or `cardio`/`custom`. |
| `exercises[]` | array | Empty for a pure-cardio session. |
| `exercises[].name` | string | Canonical English name (map Hebrew input, see references/hebrew-exercise-map.md). |
| `sets[].reps` | number | Reps completed in that set. |
| `sets[].kg` | number | Load in kg. If the user logs in lb, convert and store kg (keep `units` for display). Pure bodyweight moves (pull-ups, dips, push-ups): use `0`. Weighted bodyweight (a pull-up with a 10 kg belt): store the ADDED load, `10`, so it counts. Pass `--bodyweight <kg>` to `analyze_log.py` to fold bodyweight into volume and estimated 1RM. |
| `sets[].rpe` | number | 6-10 scale (see references/progression-models.md). Optional but strongly encouraged. |
| `cardio` | object or omit | `type`, `distance_km`, `duration_min`. Compute pace on read; do not store it. |
| `notes` | string | Free text, verbatim from the user. |
| `feel` | 1-5 | Subjective session quality. Feeds the overtraining/plateau signals. |

## Read-first protocol (every session)

1. Read `profile.md` -> know the program, goal, injuries, units, progression model.
2. Read `log.jsonl` -> know history and the last `day` trained.
3. Only then act in whichever role the user's message calls for.

## Write protocol (Logger role only)

- Parse the user's free text into ONE object matching the schema above.
- Append it as a single line to `log.jsonl` (never rewrite existing lines).
- Read the parsed line back to the user in plain language and ask them to confirm or correct.
- Prefer to get the parse right BEFORE writing: confirm ambiguous items with the user first.
- If a wrong line was already written, do not rewrite history. Append a new corrected line for
  the same date and day, and note in its `notes` that it supersedes the earlier entry. The
  analyst reads the latest matching entry.
