# Domain Coverage Checklist  - israeli-workout-coach (health-services)

Generated: 2026-07-23. Reviewed and extended 2026-08-26 (v1.2.0). Via research on: Wikipedia (1RM formulas), NASM (RPE/RIR), MOH health.gov.il (heat), eran.org.il, iaed.org.il, kolzchut.org.il, physioclick.co.il

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

| 27 | **Israeli gym paperwork: health declaration, medical certificate, minors** - the gym must obtain a signed הצהרת בריאות before admitting a trainee; a yes answer requires a doctor's תעודה רפואית; declaration renews every two years and the certificate every year; a minor needs written parental consent AND a specifically qualified מדריך לאימון קטינים present. | חוק מכוני כושר (רישוי ופיקוח), תשנ"ד-1994 ss.3-4; see references/israeli-gym-rules.md |
| 28 | **Per-kupah physiotherapy access** - naming which fund needs a doctor's referral. Maccabi allows direct booking at its own institutes; Clalit, Meuhedet and Leumit require a referral. A generic "usually needs a referral" hedge sends a Maccabi member to an appointment they do not need. | Maccabi physiotherapy-without-doctor page; Clalit / Leumit rights pages |
| 29 | **Screening answers must change the program** - high BP or cardiac history caps Valsalva and grinding singles; anticoagulants restrict contact/impact; each stored flag needs a behaviour attached to it, not just a record. | (structural, safety); flags defined in row 19 |
| 30 | **RED-S / low energy availability distinguished from overtraining** - under-eating relative to load produces the same signal cluster the Analyst reads as overreaching, and a deload does not fix it. Amenorrhoea in a training woman is a medical finding to route, not a training outcome. | (structural, safety); interacts with rows 7, 11, 16 |
| 31 | **State durability** - back up log.jsonl before any write, append-only enforced in practice not just stated, trailing-newline check, single-writer rule, stable folder location (~/workout-coach/) rather than per-project, search-before-onboard, and a read-window for very long logs. | (structural); the log is the one irreplaceable artifact |
| 32 | **Hand-edited profile.md contract** - validate rotation against day headings, detect orphan day labels, and re-run the health screen when health_flags are missing, since their absence silently disables the safety gates. | (structural, safety) |
| 33 | **Superseded-line semantics are enforced by the analyzer** - a corrected session must count once. Documented-but-unenforced correction protocols corrupt every downstream number. | (structural); scripts/analyze_log.py dedupes by (date, day) |

## Should cover (advanced / edge cases)

| # | Topic | Basis |
|---|-------|-------|
| S1 | **Cardio / running-pace tracking**  - log runs and trend pace as the running analogue of est-1RM. | (structural); heat rules apply outdoors |
| S2 | **Mobility / flexibility work**  - allow logging and light programming without medicalizing. | (structural) |
| S3 | **Beginner vs advanced autoregulation**  - beginners on linear progression + fixed RPE targets; advanced use RIR-based autoregulation. | fact #2 |
| S4 | **Bodyweight-trend tracking without triggering the guardrail**  - allow neutral logging of a bodyweight number; do NOT solicit weight-loss goals or comment on appearance; watch red flags. | facts #4-#5 |
| S6 | **Fasting days and the Israeli calendar** - Yom Kippur, Tisha B'Av and Ramadan interrupt training for a large share of Israeli users; no rule yet. Deferred 2026-08-26. | (structural) |
| S7 | **Return from miluim as its own ramp** - distinct from a holiday layoff (sleep debt, load-carriage complaints, weeks of unaccustomed volume). Currently folded into the generic 10 to 15 percent regression. Deferred 2026-08-26. | (structural) |
| S8 | **Training toward a dated fitness test** (מבחן בר-אור, IDF/sherut-leumi standards) - no goal value, no test-date field, no taper logic. Deferred 2026-08-26. | (structural) |
| S9 | **Female-athlete programming beyond the RED-S red flag** - menstrual-cycle context, menopause and bone density, pelvic floor outside pregnancy. The `sex` field added in v1.2.0 is the prerequisite; the programming guidance is deferred. | (structural) |
| S10 | **Air quality (אובך) and extreme-heat regions (Eilat, Dead Sea)** - the outdoor-training section handles heat nationally but has no location field and no sandstorm rule. Deferred 2026-08-26. | (structural) |
| S5 | **RPE-creep + heat interaction**  - distinguish genuine fatigue from heat-driven performance dips before recommending a deload. | facts #2 + #3 |

## Out of scope (explicit, with rationale)

| Topic | Why | Where it belongs |
|-------|-----|------------------|
| **Clinical rehab prescription** | Requires licensed physiotherapist + physician oversight, a regulated profession under חוק הסדרת העיסוק במקצועות הבריאות, תשס"ח-2008. Re-litigated 2026-08-26: still out of scope; the skill now routes per-kupah instead. | Kupah physiotherapy (referral required, fact #6-#7); `israeli-hmo-navigator`. |
| **Medical dietary therapy / eating-disorder treatment** | Needs a multidisciplinary medical team. | `israeli-mental-health-navigator`; eating-disorder association (fact #5); ERAN 1201 (fact #4). |
| **General nutrition / meal & calorie planning** | Separate competency. | `israeli-nutrition-planner`. |
| **PED / anabolic-steroid guidance** | Illegal/harmful; refuse. | Physician. |
| **Competition prep (peaking, weight-cutting)** | Specialized, high-risk, eating-disorder overlap. | Qualified human coach. |
| **HMO coverage specifics** | Dedicated navigator exists, beyond the referral-yes/no question in row 28 which the coach must answer itself. Re-litigated 2026-08-26: still out of scope. | `israeli-hmo-navigator`. |
| **Real-time between-sets tracking** | Wrong surface; the skill is a plan-and-review coach and a logbook. Re-litigated 2026-08-26: still out of scope, and stated explicitly in the skill body. | A phone gym-tracker app. |

## Authoritative sources

- https://en.wikipedia.org/wiki/One-repetition_maximum  - Epley `w(1+r/30)` and Brzycki formulas.
- https://www.nasm.org/resource-center/blog/training/how-to-use-rpe-and-rir-to-autoregulate-client-training  - RPE/RIR mapping.
- https://me.health.gov.il/older-adult/specialist-advice/managing-extreme-weather/heat-protection/  - MOH heat thresholds, shift activity out of peak hours, 8 to 10 cups/day, heat-exhaustion vs heat-stroke.
- https://www.eran.org.il/services/  - ERAN hotline 1201.
- https://www.iaed.org.il/  - Israeli eating-disorder professional association + provider directory.
- https://www.kolzchut.org.il/he/טיפולי_פיזיותרפיה_בבתי_חולים  - physiotherapy referral made by a physician.
- https://www.physioclick.co.il/blog/physiotherapy-lower-back-pain-health-fund-reimbursements/  - kupah physiotherapy needs a doctor referral. NOTE: a private-clinic marketing blog, retained only as a secondary cross-check. It is not authoritative for a statutory entitlement and is now wrong for Maccabi.
- https://www.maccabi4u.co.il/maccabi_circles/exercise/physiotherapy-without-doctor/  - Maccabi direct-access physiotherapy, and the cases that still need a referral.
- https://www.gov.il/BlobFolder/generalpage/add-zav-doc/he/home_main_business-licensing_add-zav_add-zav-doc-018.pdf  - חוק מכוני כושר, full updated text; ss.3-4 health declaration, medical certificate, minors.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/  - ISSN position stand, 1.4 to 2.0 g/kg/day.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5867436/  - Morton et al., 1.62 g/kg/day break point.
