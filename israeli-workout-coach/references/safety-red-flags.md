# Safety Red Flags: Emergency, Urgent, and Route-to-a-Doctor

The Safety section of SKILL.md carries the decision branches. This file carries the
detail behind them. Read it whenever a user reports a symptom, an injury, heat illness,
a pregnancy, diabetes, or distress around food or mood. Nothing here is a diagnosis or a
treatment: every branch ends in "stop training and get the user to the right level of
care", which is the only clinical act this skill performs.

Three tiers, and getting the tier wrong is the expensive error:

| Tier | Meaning | Action |
|---|---|---|
| Emergency | Call 101 now | Stop, call מד"א 101, do not keep coaching |
| Urgent | Today, not a routine queue | Send to מיון or urgent care (מוקד), not to a physiotherapy waiting list |
| Routine | Days to weeks is fine | Family or kupah doctor, then physiotherapy per the kupah table in SKILL.md |

## Emergency: call מד"א 101

During or right after training:

- Chest pain or pressure, or pain spreading to the arm or jaw.
- Sudden severe breathlessness.
- Fainting or near-fainting.
- Sudden one-sided weakness, facial droop, or slurred speech.
- Confusion or collapse in the heat.
- **Sudden, severe, "worst headache of my life" during or right after a maximal or
  heavily-braced effort.** A lifter will rationalise this as a blood-pressure headache
  and rest through it. It is the classic exertional presentation of a subarachnoid
  haemorrhage or an arterial dissection, and it is time-critical. This is why the
  screening rules in SKILL.md cap maximal breath-holding for at-risk users.
- Active suicidal thoughts or intent, disclosed at any point. ERAN 1201 is emotional
  first aid, not an emergency service. If the user says they intend to act, or you
  believe they are in immediate danger, tell them to call 101 or go to the nearest ER,
  and stay with the conversation rather than returning to training talk.

## Urgent: today, and not via a physiotherapy referral queue

Most non-soreness pain is a routine doctor-then-physiotherapy matter. These are not, and
sending them into a queue that starts with a GP appointment loses time that matters:

- **Suspected tendon or muscle rupture.** An audible pop or snap with immediate loss of
  function, a visible deformity or a lump where the muscle bunched, or inability to bear
  weight. Pec major during bench, distal biceps during a heavy pull or a curl, quadriceps
  or patellar tendon during a squat, and Achilles during jumping or sprinting are the
  classic gym ones, and several are time-sensitive surgical repairs.
- **Neurological signs after a deadlift, squat, or any loaded spinal effort:** numbness
  in the saddle area (inner thighs, buttocks, genitals), a new problem controlling
  bladder or bowel, or weakness in both legs or weakness that is getting worse. This
  picture is treated as a same-day emergency; send them to מיון immediately, do not wait
  for a referral.
- **Suspected fracture:** severe pain with obvious swelling or deformity, or a joint that
  will not take any weight.

Say plainly which tier you think this is and why, and that you are not examining them.

## Heat illness: what "cool the person" actually means

Heat exhaustion (heavy sweating, cold clammy skin, dizziness, weakness): stop, get them
into shade or air conditioning, lie them down with legs raised, cool them, and give
fluids if they are fully alert.

Heat stroke is an emergency (see SKILL.md for the signs). Outcome tracks how long the
body stays hot, so **cool first and cool aggressively while help is on the way**:

- Cold-water immersion is best where anything can serve as a tub.
- Otherwise: strip excess clothing and douse continuously with cold water, fan them, and
  put ice or cold packs on the neck, armpits, and groin.
- Keep cooling while waiting for מד"א and during transport.
- **Do not give anything to drink to someone who is confused, vomiting, or not fully
  alert.** They can aspirate it.

## Drinking too much is also a risk

The MOH hydration baseline in SKILL.md is a general daily figure, and "drink more in the
heat" needs a ceiling. On prolonged sessions (roughly over an hour, and especially long
outdoor runs), drinking large volumes of plain water beyond thirst can dilute blood
sodium and cause exercise-associated hyponatremia, which presents as headache, nausea,
confusion, and collapse: the same picture as heat illness, treated in the opposite
direction. Guide the user to drink to thirst rather than on a schedule, and to include
salt or an electrolyte drink on long or very sweaty sessions. If someone collapses after
drinking heavily through a long session, say explicitly that more water is not the
answer and that this needs medical assessment.

## Diabetes

Ask about it in the Step 1 screen and store it in `health_flags`. If the user takes
insulin or a sulfonylurea, exercise can drop blood glucose low, including hours later or
overnight. Stay out of the clinical lane, and give only the standard general advice:
check glucose before and after training, carry fast-acting carbohydrate, avoid training
alone or fasted while doses are being adjusted, and take any dose changes to their doctor
or diabetes nurse. Note that at Maccabi an exercise consultation for diabetes is one of
the cases that still requires a doctor's referral.

## Pregnancy and postpartum

Beyond medical clearance and avoiding maximal effort and breath-holding under heavy load,
give the user the standard stop-and-call list. Stop training and contact their doctor or
go to מיון for any of:

- Vaginal bleeding, or fluid leaking.
- Regular painful contractions.
- Calf pain, or swelling in one leg (a clot sign).
- Breathlessness before any exertion, chest pain, or dizziness that does not settle.
- Headache with visual changes.
- Reduced fetal movement.

## Rhabdomyolysis

Severe, unrelenting muscle pain with swelling plus dark brown or cola-coloured urine, or
passing much less urine than usual, after hard or unaccustomed work. Route to מיון, not
to a rest day. The common Israeli triggers are not only barbell work: a first high-rep
spin or functional-fitness class, a brutal unaccustomed eccentric session, or a return
from a long break are where most cases come from.

## Disordered eating and mood

The guardrail and its routing live in SKILL.md. Two additions:

- **Persist the flag.** Once a red flag has appeared, write it into `profile.md`
  `health_flags.eating_disorder_flag` with the date. A guardrail that resets when the
  session ends barely protects anyone, because the pattern it guards against repeats
  across sessions. Only the user clears it, in a later session, by saying so.
- **Escalate on suicidality**, per the Emergency tier above.
