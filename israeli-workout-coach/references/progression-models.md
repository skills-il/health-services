# Progression Models, RPE, and Estimated 1RM

The Coach role prescribes loads and the Analyst role reads trends using the concepts
below. Use them to decide "add weight, add a rep, or hold", and to tell a real plateau
apart from a bad day.

## RPE and RIR (effort scale)

RPE (rate of perceived exertion) on the resistance-training scale runs 6 to 10 and maps
to RIR (reps in reserve, how many more reps you could do before technical failure):

| RPE | RIR | Meaning |
|-----|-----|---------|
| 10  | 0   | Could not do another rep (technical failure) |
| 9   | 1   | One rep left |
| 8   | 2   | Two reps left |
| 7   | 3   | Three reps left |
| 6   | 4+  | Four or more reps left |

Source: NASM, RIR/RPE autoregulation (RIR 0 corresponds to RPE 10, RIR 4+ to RPE 6).

Use RPE two ways:
- **Prescribe** a target: "work up to a top set of 5 at RPE 8" means stop with about 2 reps
  in the tank.
- **Read** fatigue: if the same load drifts from RPE 8 to RPE 9 to RPE 9.5 across sessions
  with no rep gain, that is RPE creep, a fatigue / plateau signal (see below).

## Estimated 1RM

To compare strength across different rep counts, estimate the one-rep max with the Epley
formula:

```
1RM = weight * (1 + reps / 30)
```

Brzycki is an alternative: `1RM = weight * 36 / (37 - reps)`. Both are estimates and lose
accuracy above about 10 reps, so prefer top sets of 1 to 8 reps when you want a clean 1RM
trend. Source: standard strength-and-conditioning reference (see Reference Links).

`scripts/analyze_log.py` computes the Epley estimate per exercise across the log and reports
the trend.

## Progression models (pick per experience level)

| Model | Who it fits | Rule |
|-------|-------------|------|
| **Linear progression** | Beginners | Hit all prescribed reps at target RPE, then add the smallest load increment next session (about 2.5 kg upper body, 5 kg lower body). Stall twice, then deload or switch models. |
| **Double progression** | Intermediate | Work a rep range (e.g. 3 sets of 8 to 12). Grow reps within the range at a fixed load until you hit the top of the range on all sets, then add load and reset to the bottom of the range. |
| **RPE autoregulation** | Intermediate to advanced | The prescription is an effort target, not a fixed load. Pick today's load so the top set lands at the target RPE. Auto-adjusts for good and bad days. |

Store the chosen model in `profile.md` (`progression:` field) and apply it consistently.

## Deload and overtraining signals

Recommend a deload week (cut working-set volume roughly in half, or drop intensity by about
10 percent) when you see a cluster of:

- RPE creep at a constant load across 2 to 3 sessions
- Estimated 1RM flat or declining on the main lifts across several sessions
- Session `feel` low (1 to 2 out of 5) for 3 or more sessions in a row
- The user reporting poor sleep, low mood, or persistent soreness

On the deload itself, pick ONE lever, not both: either cut working-set volume roughly in
half for a week, or hold volume and drop intensity by about 10 percent. Cutting both at once
is a layoff, and you lose the ability to read what the deload did.

This is a training decision, not a medical diagnosis. If symptoms are more than training
fatigue (pain, injury, illness), route the user to their doctor (see SKILL.md safety rules).

**Rule out low energy availability (RED-S) before you call it overtraining.** Under-eating
relative to training load produces the same picture: stalled or falling performance, RPE
creep, frequent illness, bone stress injuries, low mood, poor sleep, feeling cold, and
periods becoming irregular or stopping. A deload does not fix it and can delay the real
answer. Ask whether food has kept up with the training before prescribing one, and route
to a doctor where several of these signs are present. See the Safety section in SKILL.md.

`analyze_log.py` requires RPE creep and a flat or declining estimated 1RM to appear on the
SAME lift before it will call a cluster, because accessories such as face pulls and calf
raises plateau by design and would otherwise keep the flag permanently on.

Deloads are also worth scheduling proactively, not only reactively. Intermediate and advanced
lifters commonly plan a lighter week every 4 to 8 weeks of hard training to stay ahead of
accumulated fatigue, rather than waiting for the warning cluster to appear.

## Returning from a break (detraining)

Strength and work capacity fade during a layoff (miluim, travel, holidays, illness). After a
gap of more than about two weeks, do NOT resume at the last logged loads plus an increment.
Regress: start roughly 10 to 15 percent lighter, keep reps a touch higher, and rebuild over
one to two weeks back to the prior working weights. `analyze_log.py` prints a detraining flag
when it sees a long gap since the last session.

## Plateau vs bad day

One flat or worse session is noise. A plateau is no progress on a lift across several
sessions at the target RPE. Only then hand off to the routine-breaker (Role 5) for one
bounded change: reset reps via double progression, swap the accessory, or adjust volume.
Do not change the main lifts and the progression model at the same time, or you lose the
signal.

## Warm-up and the form stopping rule

**Warm-up, every session, and specific to the day's work.** Five to ten minutes of light
cardio, dynamic mobility for the day's main pattern (hips and ankles before squats,
shoulders before pressing), then 2 to 3 ramp-up sets on the first main lift climbing from
an empty or light bar to the working load. Warming up the body in general is not the same
as warming up the lift.

**Form is the stopping rule, not the RPE number.** End a set the moment technique breaks
down (bar path drifts, back rounds under load, reps get grindy and sloppy), even if the
target reps or RPE were not reached. Form failure under fatigue is the main injury cause in
barbell training. When prescribing a new or heavier lift, give one or two brief technique
cues (for example "brace and keep a neutral spine" on deadlift), and tell the user to drop
the weight and get a coach or a video check if a lift feels wrong. An Israeli gym is
legally required to have an instructor present whenever it is open, so "ask the floor
instructor to watch a set" is realistic advice, not a brush-off.
