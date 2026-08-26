# State Schema: profile.md and log.jsonl

This skill keeps its memory in two plain files inside a `workout-coach/` folder. Read
BOTH at the start of every session before doing anything else. Never guess the user's
program or history from context: read the files.

**Where the folder lives.** Default to `~/workout-coach/`, one stable location, and
confirm it with the user on the first run. Do NOT default to the current working
directory: these agents run per-project, so a user who trains and also codes ends up with
several disconnected half-logs. Before treating anything as a first run, look for an
existing folder (`~/workout-coach/`, then the working directory, then ask).

## Folder layout

```
workout-coach/
  profile.md     # human-readable program + settings (you and the user both edit this)
  log.jsonl      # append-only training history, one JSON object per line
```

If the folder does not exist anywhere, you are on a first run: onboard the user (see
SKILL.md Step 1) and create both files. Never overwrite `log.jsonl`; only append to it.

Four states are possible, and only one of them is a first run:

| State | What to do |
|---|---|
| Neither file exists | First run. Onboard and create both. |
| Both exist and parse | Normal. Read both, then act. |
| `profile.md` exists, `log.jsonl` missing or empty | Not a first run. Keep the profile, create an empty log, and coach from the profile. |
| `log.jsonl` exists, `profile.md` missing or broken | Do NOT onboard over the top of it. The log is the irreplaceable half. Rebuild the profile with the user, using the log to remind them what they have been training. |

## profile.md

A readable Markdown file. Keep it short so a human can edit it directly. Suggested shape:

```markdown
# Profile

- goal: strength            # strength | hypertrophy | fat-loss | general-fitness | endurance
- experience: intermediate  # beginner | intermediate | advanced
- equipment: gym            # gym | home | both
- units: kg                 # kg | lb
- age: 34                   # drives the screening thresholds
- sex: f                    # optional, only if volunteered; f | m | na. Enables the
                            # amenorrhoea / RED-S red flag in SKILL.md Safety.
- bodyweight_kg: 78         # optional; only if the user volunteered it
- progression: double       # linear | double | rpe   (how loads advance; see references/progression-models.md)
- injuries:
  - right shoulder: avoid heavy overhead press, barbell dips
- health_flags:             # from the Step 1 screening; drives the safety rules
  - heart_or_bp_condition: false     # heart disease, uncontrolled high blood pressure
  - chest_pain_or_dizziness: false   # on exertion, ever
  - pregnant_or_postpartum: false
  - other_medical: none              # relevant conditions or medications
  - family_sudden_cardiac_death: false  # first-degree relative, under 50
  - anticoagulants: false            # blood thinners; see SKILL.md Step 1
  - diabetes: false                  # and whether on insulin / sulfonylurea
  - eating_disorder_flag: none       # set to the ISO date a red flag appeared. Role 3 must
                                     # read this before ANY nutrition talk. Only the user
                                     # clears it, in a later session, by saying so.
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

### Validating profile.md before you rely on it

The user is invited to edit this file by hand, so it can come back inconsistent. Before
coaching from it, check that every label in `rotation` has a matching `## Day X` heading,
and that any `day` value appearing in recent log lines still exists in `rotation` (a user
who switched split from PPL to upper-lower leaves orphan day labels behind). If something
does not line up, name the specific inconsistency and ask; do not guess a rotation.

If `health_flags` is missing or empty, re-run the SKILL.md Step 1 health screen before
prescribing any load. The heat rules, the RPE cap for at-risk users, and the emergency
branch all read those flags, so a profile without them silently disables the safety gates.

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
| `sets[].rpe` | number | 6-10 scale (see references/progression-models.md). Optional but strongly encouraged. Write numbers, not strings. |
| `cardio` | object or omit | `type`, `distance_km`, `duration_min`. Compute pace on read; do not store it. |
| `notes` | string | Free text, verbatim from the user. |
| `feel` | 1-5 | Subjective session quality. Feeds the overtraining/plateau signals. |

Write every numeric field as a JSON number, not a quoted string. `analyze_log.py` will
coerce `"80"` rather than crash, but a value it cannot read at all is silently treated as
zero, which quietly deletes that set from volume and estimated 1RM.

## Read-first protocol (every session)

1. Read `profile.md` -> know the program, goal, injuries, units, progression model.
2. Read `log.jsonl` -> know history and the last `day` trained.
3. Only then act in whichever role the user's message calls for.

## Write protocol (Logger role only)

The log is the one thing here the user cannot reconstruct. Treat every write as
potentially destructive.

- **Copy first, to a DATED file:** `cp log.jsonl log.jsonl.$(date +%F).bak` before any
  write. Never a single fixed `.bak` name: corruption is normally noticed a session later,
  by which time a fixed backup has already been overwritten with the broken file, so the
  documented recovery fails exactly when it is needed. Keep the last several. If the file
  you are about to back up has FEWER lines than the newest existing backup, stop and tell
  the user before copying anything over it.
- Parse the user's free text into ONE object matching the schema above.
- **Check the file ends with a newline** before appending, or the new session merges into
  the previous line and both become unparseable.
- Append it as a single line to `log.jsonl` (never rewrite existing lines). Do not read the
  whole file, regenerate it, and write it back. If your tooling only offers whole-file
  writes, re-read afterwards and confirm the line count grew by exactly one.
- **One writer at a time.** If two sessions or terminals are open, log from one. If the last
  line is truncated, do not delete it: show it to the user and ask what that session was.
- **Long logs:** read the most recent 20 to 30 sessions for coaching, plus anything the user
  asks for by date. `analyze_log.py` reads the whole file for trends. Never rotate or trim
  the file unless the user asks.
- Read the parsed line back to the user in plain language and ask them to confirm or correct.
- Prefer to get the parse right BEFORE writing: confirm ambiguous items with the user first.
- If a wrong line was already written, do not rewrite history. Append a new corrected line for
  the same date and day, and note in its `notes` that it supersedes the earlier entry.
  `analyze_log.py` enforces this: it keeps only the LAST line for each (date, day) pair, so
  a correction counts once rather than double-counting the session into weekly volume.
  This means a genuinely separate second session on the same date must use a different
  `day` label (for example `B` in the morning and `cardio` in the evening), or the earlier
  one will be treated as superseded.
