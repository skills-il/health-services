# Domain Coverage Checklist  - israeli-workout-coach (health-services)

Generated: 2026-07-23 via research on: Wikipedia (1RM formulas), NASM (RPE/RIR), MOH health.gov.il (heat), eran.org.il, iaed.org.il, kolzchut.org.il, physioclick.co.il

## Must cover (core)

| # | Topic | Source / basis |
|---|-------|----------------|
| 1 | **Program-structure onboarding**  - capture split type (PPL / Upper-Lower / Full-body / custom), per-day definitions, available equipment (gym vs home vs minimal), primary goal (strength / hypertrophy / endurance / general health), experience level, current injuries/limitations, and units (kg default for Israel). Must ask, never assume. | (structural) |
| 2 | **Persistent-log schema + read-first-each-session**  - `profile.md` (static: splits, goals, injuries, PRs) + `log.jsonl` (append-only per-set records: date, exercise, weight, reps, RPE, notes). The Coach/Analyst MUST read the log before proposing or analyzing anything; the log is the system-of-record. | (structural) |
| 3 | **Progressive-overload / progression models**  - linear progression (add load when target reps hit), double-progression (grow reps within a range, then add load and reset reps), and RPE/RIR autoregulation (adjust today's load to a target effort). Explain when each fits (beginner vs intermediate). | RPE/RIR: NASM RIR/RPE scale (fact #2). Linear/double-progression models are (structural) reasoning patterns. |
| 4 | **Role 1  - Coach**  - proposes today's session by position in the user's rotation, with prescribed sets/reps/target-RPE, plus a home-equipment variant of every prescribed lift. | (structural) |
| 5 | **Role 2  - Logger**  - parses Hebrew free-text into structured `log.jsonl` records; must handle Hebrew/standard exercise-name mapping. | (structural) |
| 6 | **Role 3  - Nutrition advisor (framework only + guardrail)**  - general macro/hydration framing ONLY, then hands off specific meal/calorie planning to `israeli-nutrition-planner`; must run the disordered-eating guardrail before giving any weight/calorie advice. | Routing target: israeli-nutrition-planner. Guardrail: rows 16. |
| 7 | **Role 4  - Analyst**  - computes estimated-1RM trend, weekly volume, run-pace trend, and RPE creep (same load feeling harder = fatigue flag); flags overtraining and plateau. | est-1RM: fact #1. RPE creep: fact #2. |
| 8 | **Role 5  - Controlled routine-breaker**  - proposes ONE bounded variation without altering the base program's main lifts or progression. | (structural) |
| 9 | **Estimated-1RM formula**  - Epley `1RM = weight * (1 + reps/30)`; Brzycki as alternative; estimates degrade above ~10 reps. | fact #1 |
| 10 | **RPE / RIR scale (6-10)**  - RIR = reps left before technical failure; RPE 10 = 0 RIR, 9 = 1, 8 = 2, 7 = 3, 6 = 4+. | fact #2 |
| 11 | **Deload / overtraining detection**  - RPE creep at constant load, stalled/declining est-1RM, elevated fatigue, low session feel; recommend a deload. Not a medical diagnosis. | fact #2 + (structural) |
| 12 | **Plateau detection**  - no est-1RM or rep progress on a lift across sessions at target RPE, then propose a fix via Role 5. | (structural), grounded on facts #1-#2 |
| 13 | **Warm-up guidance**  - general to specific: light cardio, dynamic mobility, ramp-up sets. | (structural) |
| 14 | **Home-vs-gym substitution**  - every gym lift needs a home/minimal-equipment equivalent. | (structural) |
| 15 | **Safety scope boundary**  - a training assistant, NOT a medical provider, physiotherapist, or dietitian; does not diagnose or treat. | (structural) + rows 16-17 |
| 16 | **Disordered-eating warning signs + guardrail + routing**  - detect red-flag language (extreme restriction, compulsive exercise to burn off food, rapid-loss goals, purging, body-image distress); STOP calorie/weight targets, respond supportively, route to a real Israeli eating-disorder resource + ERAN + israeli-mental-health-navigator. | Resource: fact #5. ERAN 1201: fact #4. |
| 17 | **Injury / pain to physiotherapy via kupat cholim**  - stop loading the area and route to the family/kupah doctor for a physiotherapy referral (הפניה), because physiotherapy in the basket requires a doctor's referral. | facts #6-#7 |
| 18 | **Israeli-summer heat and hydration rules**  - during a heat wave (גל חום) / heavy heat load (עומס חום כבד), move training to early morning or evening, hydrate (MOH baseline 8 to 10 cups/day, more with exertion), recognize heat-exhaustion vs heat-stroke signs (exertional heat stroke can present WITH sweating), flag at-risk users. | facts #3-#5 + sports-med (exertional caveat) |
| 19 | **Pre-exercise health screening (PAR-Q)**  - onboarding must screen cardiac/BP risk, chest pain or dizziness on exertion, fainting, pregnancy/postpartum, and medications, store them in the profile, and program conservatively or defer to medical clearance for at-risk users. | (structural, safety) |
| 20 | **Acute-emergency routing (call 101)**  - a stop-and-call-מד"א-101 branch for chest pain, one-sided weakness, fainting, severe breathlessness, or confusion/collapse in heat during training. | (structural, safety) |
| 21 | **Return-from-layoff / detraining**  - after a gap over ~2 weeks (miluim, travel, illness), regress loads instead of resuming at old numbers plus an increment. | (structural) |
| 22 | **Rhabdomyolysis red flag**  - severe unrelenting soreness + swelling + dark/cola urine after hard or unaccustomed work routes to the ER, not a rest day. | (structural, safety) |
| 23 | **Form as the stopping rule + technique cues**  - end a set when technique breaks down even before target reps/RPE; give brief cues on new/heavy lifts. | (structural, safety) |
| 24 | **Training frequency / recovery spacing**  - do not prescribe the same muscle group hard on back-to-back days. | (structural) |
| 25 | **Special populations**  - pregnancy/postpartum, youth, deconditioned older beginners get medical clearance and conservative programming, not the generic plan. | (structural, safety) |
| 26 | **Bodyweight-lift progression is tracked**  - pull-ups/dips tracked by reps (and weighted bodyweight by added load) so calisthenics progress is not invisible to the analyst. | (structural) |

## Should cover (advanced / edge cases)

| # | Topic | Basis |
|---|-------|-------|
| S1 | **Cardio / running-pace tracking**  - log runs and trend pace as the running analogue of est-1RM. | (structural); heat rules apply outdoors |
| S2 | **Mobility / flexibility work**  - allow logging and light programming without medicalizing. | (structural) |
| S3 | **Beginner vs advanced autoregulation**  - beginners on linear progression + fixed RPE targets; advanced use RIR-based autoregulation. | fact #2 |
| S4 | **Bodyweight-trend tracking without triggering the guardrail**  - allow neutral logging of a bodyweight number; do NOT solicit weight-loss goals or comment on appearance; watch red flags. | facts #4-#5 |
| S5 | **RPE-creep + heat interaction**  - distinguish genuine fatigue from heat-driven performance dips before recommending a deload. | facts #2 + #3 |

## Out of scope (explicit, with rationale)

| Topic | Why | Where it belongs |
|-------|-----|------------------|
| **Clinical rehab prescription** | Requires licensed physiotherapist + physician oversight. | Kupah physiotherapy (referral required, fact #6-#7); `israeli-hmo-navigator`. |
| **Medical dietary therapy / eating-disorder treatment** | Needs a multidisciplinary medical team. | `israeli-mental-health-navigator`; eating-disorder association (fact #5); ERAN 1201 (fact #4). |
| **General nutrition / meal & calorie planning** | Separate competency. | `israeli-nutrition-planner`. |
| **PED / anabolic-steroid guidance** | Illegal/harmful; refuse. | Physician. |
| **Competition prep (peaking, weight-cutting)** | Specialized, high-risk, eating-disorder overlap. | Qualified human coach. |
| **HMO coverage specifics** | Dedicated navigator exists. | `israeli-hmo-navigator`. |

## Authoritative sources

- https://en.wikipedia.org/wiki/One-repetition_maximum  - Epley `w(1+r/30)` and Brzycki formulas.
- https://www.nasm.org/resource-center/blog/training/how-to-use-rpe-and-rir-to-autoregulate-client-training  - RPE/RIR mapping.
- https://me.health.gov.il/older-adult/specialist-advice/managing-extreme-weather/heat-protection/  - MOH heat thresholds, shift activity out of peak hours, 8 to 10 cups/day, heat-exhaustion vs heat-stroke.
- https://www.eran.org.il/services/  - ERAN hotline 1201.
- https://www.iaed.org.il/  - Israeli eating-disorder professional association + provider directory.
- https://www.kolzchut.org.il/he/טיפולי_פיזיותרפיה_בבתי_חולים  - physiotherapy referral made by a physician.
- https://www.physioclick.co.il/blog/physiotherapy-lower-back-pain-health-fund-reimbursements/  - kupah physiotherapy needs a doctor referral.
