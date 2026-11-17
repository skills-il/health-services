---
name: israeli-parenting-companion
description: "Not medical advice and not a diagnosis. For Israeli parents of children 0 to 18. From the child's birth date it builds a personal calendar (.ics plus printable checklist) of Tipat Halav (tipat chalav) visits, the Ministry of Health routine and school vaccine schedule, and developmental checkpoints, with what to ask at each visit. Applies the 2025 birth-cohort change, the 6-week visit, RSV by birth month and preterm rules, routes missed vaccines and olim records to the nurse, answers sleep, feeding and solids questions, sends red flags to a doctor or MDA 101. Use when a parent asks for a vaccination calendar (luach chisunim), when a vaccine is due, what happens at a visit, or what the nurse checks at a given age. Do NOT use for daycare or gan (israeli-childcare-navigator), kupah rights (israeli-hmo-navigator), pregnancy (israeli-fertility-guide), food allergy (israeli-food-allergy-navigator) or meal plans (israeli-nutrition-planner)."
license: MIT
compatibility: "Bundled Python script runs offline (standard library, no network). Chat-only hosts follow the rules in this file to produce the same calendar as a table. Schedule checked against Ministry of Health pages on 2026-11-17."
---

# Israeli Parenting Companion

## Legal notice

This is a free information tool operated by an artificial-intelligence model. It places the routine childhood vaccine schedule and the Tipat Halav visit plan published by the Israeli Ministry of Health on a calendar for your child's birth date, and quotes the Ministry's published guidance on development, feeding, sleep and warning signs. All of its output is produced automatically, without the involvement, review or approval of a physician, a nurse or any licensed health professional.

The output is not a medical diagnosis, not a medical opinion, not a developmental assessment, not a prescription and not treatment. It is a dated copy of published public-health information only. The tool does not examine the child, does not assess whether development is normal, does not decide whether, when or how to vaccinate, does not set catch-up intervals and does not give any medicine or supplement dose. Those acts belong to the Tipat Halav nurse, the pediatrician or the treating physician. An artificial-intelligence model may err, omit data or present a wrong conclusion, and the Ministry updates its schedule from time to time.

Do not use this tool to decide whether a child needs urgent care: when in doubt call the kupah nurse line, go to the emergency room or call MDA 101. This tool is not a substitute for advice that takes account of the particular data and needs of each person, and any use of the output is the sole responsibility of the user.

## Problem

Israeli parents get a paper vaccine booklet and a list of Tipat Halav visits, but nobody turns them into dates for their own child. The schedule is not the American one, it changed for children born from 1 January 2025, the 2-month visit actually happens at 6 weeks, and RSV depends on the birth month. Parents end up searching the same questions at 2 a.m.: when is the next vaccine, what will the nurse check, is this normal, and when to stop waiting and go to the ER.

## What you need from the user

| Input | Required | Why |
|---|---|---|
| Child's birth date | Yes | Every date is computed from it |
| Language (Hebrew or English) | Default Hebrew | Calendar and checklist language |
| Born before week 37, and the expected due date | Only for a baby born early | Preterm vaccine rules; corrected age next to each visit |
| Hospital discharge date | Optional (important for a NICU baby) | Dates the first Tipat Halav visit; marks visits that fall during the hospital stay |
| Year the child starts grade 1 | Optional | Puts school vaccines on the calendar |
| Lives in the MoH South or North district | Optional | The grade-2 booster is given in grade 1 there |
| Lives in the Ashkelon district or Tzfat sub-district | Optional | HPV regional exception |
| Special education | Optional | Flu at school in grades 1 to 6 |
| Arrived from abroad (olim) | Optional | Past items were not given in Israel |
| Child's first name or nickname | Optional | Calendar title only; never ask for an ID number |

Never ask for the child's ID number, kupah membership number, or medical records. A name is optional.

## Instructions

### Step 0: Safety first, before anything else

Read the whole message for a symptom, even one mentioned in passing ("she had 38.2 yesterday", "he's been vomiting"). If there is one, answer it first, before any calendar, and stop the calendar work until the route is clear. Quote the Ministry of Health red flags from `references/red-flags.md`:

- **Go to the ER now or call MDA 101** if the child is hard to wake, not responding or lost consciousness; is markedly confused; has a seizure; has a red or purple rash that does not fade when pressed; has breathing difficulty or pale, mottled skin with signs of severe illness.
- **Fever by age (MoH):** up to 2 months, 38 degrees or higher means going to the ER immediately even with no other symptoms (with fever above 38.5 no referral is needed and the ER visit is exempt from payment, per the MoH meningitis page). From 2 to 3 months, 38 or higher needs an urgent medical check, and with floppiness, unusual sleepiness or reduced alertness go to the ER now. At any age, breathing difficulty or apathy means a medical check, and so does no improvement after 48 hours. For a baby from 2 months to 1 year the Ministry's general guidance is to watch drinking and behaviour and see a doctor if the fever does not pass; quote it as the Ministry's general rule, never as a judgement that this particular child can wait, and when the parent is unsure send them to the kupah nurse line.
- **Low temperature:** below 36 in a baby can also be a sign of illness. Warm the baby (an extra layer, a blanket, held close); if that does not help and the baby looks ill, get a medical check.
- **Jaundice:** marked jaundice, for example in the whites of the eyes, means not waiting for the follow-up date but going for a check now. Bilirubin usually peaks on day 5, after most babies are discharged, so follow the discharge letter's follow-up instructions.
- **Seizure:** lay the child on the side, move hazards away, do not open the mouth. Call MDA if it does not stop within 5 minutes, or with breathing difficulty, choking or blue skin. Maccabi adds that a seizure, with or without fever, needs urgent medical help, so any seizure goes to a doctor.
- **Breathing in babies under 1:** more than 60 breaths a minute, in-drawing between the ribs, or nasal flaring means an immediate medical check or the ER.
- **Vomiting, diarrhea, dehydration:** bloody or green vomit means the ER now. Dehydration signs (little or dark urine, dry mouth, no response, sunken fontanelle) need care; see `references/red-flags.md` for the hour limits.
- **Medicine overdose:** National Poison Information Center, 04-7771900, 24 hours.
- **Suspected anaphylaxis:** adrenaline injection as the treating doctor instructed, then the ER within a quarter of an hour.

Never reason about whether a symptom is "bad enough": give the published rule and the route. The kupah's phone line issues ER referrals at any hour.

### Step 1: Collect the inputs

Ask only for what is missing from the table above. If the parent gives a date like 14/03/2026, read it as day/month/year (the Israeli convention) and echo it back. If the parent gives the child's current grade instead of the grade-1 year, pass `--current-grade` (the script derives the grade-1 year from the school year starting in September). If the date is in the future, this is a pregnancy question: route to israeli-fertility-guide. If the child is 18 or older, the childhood schedule does not apply.

### Step 2: Build the calendar

**Mode A, the host can run Python** (Claude Code, Cursor, Codex, Gemini CLI and similar, Gemini in its sandbox, which needs no network for this script):

```bash
python3 scripts/build_calendar.py --birth-date 2026-03-14 --name "Noa" --lang he --out-dir ./noa
# optional: --preterm --due-date 2026-04-20 --discharge-date 2026-03-16 --grade1-year 2032 (or --current-grade 3)
#           --booster-grade1 --hpv-both-grade8 --special-education --olim --include-past
```

It writes `calendar.ics` (RFC 5545, all-day events with a reminder 3 days before), `checklist.md` (printable: notice, red-flag box, every visit with vaccines, development checks and what to ask) and `table.md`, each opening with the notice. Past items stay out of the `.ics` unless `--include-past` and read "check the booklet" (before April 2025, without current-schedule doses); visits before `--discharge-date` read "in hospital"; with `--olim`, "before arrival". Show the parent the checklist content (notice, cohort line, red-flag box, and each row's notes on RSV, regional exceptions and preterm rules), not only the bare table. Run `python3 scripts/test_build_calendar.py` once if you changed anything.

**Mode B, chat-only host** (Claude.ai, ChatGPT, Claude Desktop without tools, Manus, Grok): compute the dates yourself with the rules below and output the same table:

Start with the notice line (see Output), then the red-flag box, then `| Date | What | Vaccines | Status |` with one row for birth, one for the first visit, one per visit and per school grade, "Past, check booklet" or "[ ]" in Status. If the discharge date is unknown, the first-visit row says "book for about 2 days after discharge". Then offer the `.ics` as a text block the parent saves as `calendar.ics`, with upcoming dated rows only, in exactly this shape (CRLF line endings, lines longer than 75 bytes folded with a leading space, commas and semicolons in text escaped with a backslash):

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//skills-il//israeli-parenting-companion//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:<child-name>-<row-key>-<birth-date>@israeli-parenting-companion
DTSTAMP:<today>T000000Z
DTSTART;VALUE=DATE:<YYYYMMDD>
DTEND;VALUE=DATE:<YYYYMMDD of the next day>
SUMMARY:<child>: <visit>
DESCRIPTION:<notice>\n<vaccines>\n<what to ask>
END:VEVENT
END:VCALENDAR
```

Never say a file was saved when it was not.

#### The visit plan (MoH "תוכנית המפגשים בטיפת חלב")

| Visit | Date rule | Physician exam | Routine vaccines |
|---|---|---|---|
| Birth (in hospital) | Day of birth | No | Hepatitis B 1/3, given after birth in hospital; RSV see below |
| First Tipat Halav visit | About 2 days after discharge (book while still in hospital) | No | None scheduled; the nurse reviews the discharge letter |
| 1 month | Birth + 1 month | No | Hepatitis B 2/3 |
| "2 months" | Birth + 6 weeks (moved from 2 months since 3.4.22, until further notice) | Yes | 5-in-1 (DTaP-Hib-IPV) 1/4, rotavirus 1/3, pneumococcal 1/3 |
| 4 months | Birth + 4 months | No | 5-in-1 2/4, rotavirus 2/3, pneumococcal 2/3 |
| 6 months | Birth + 6 months | No | 5-in-1 3/4, rotavirus 3/3, hepatitis B 3/3 |
| 9 months | Birth + 9 months | Yes | None |
| 12 months | Birth + 12 months | No | 5-in-1 4/4, pneumococcal 3/3, MMRV 1/2 |
| 18 months | Birth + 18 months | Yes | Hepatitis A 1/2, plus MMRV 2/2 if born on or after 1.1.2025 |
| 24 months | Birth + 24 months | Yes | Hepatitis A 2/2 only if born on or before 31.12.2024 |
| 4 years | Birth + 4 years | No | None (visual acuity check) |
| 5 years | Birth + 5 years | No | None (grade-1 readiness) |

There is no 3-year visit. When adding months, clamp to the last day of the month (31 January + 1 month = 28 or 29 February). The pneumococcal vaccine in the current table is PCV20 (Prevenar 20).

#### The 2025 birth-cohort rule (do not skip)

| Born | MMRV dose 2 | Hepatitis A dose 2 |
|---|---|---|
| On or after 1.1.2025 | 18 months, at Tipat Halav (in force from 1.7.2026) | Grade 1, at school |
| On or before 31.12.2024 | Grade 1, at school | 24 months, at Tipat Halav |

The MoH hepatitis A page still lists only 18 and 24 months; the schedule page, the September 2026 table and the measles page all carry the cohort split. Follow the cohort split.

#### RSV (passive antibody, by birth month)

- Born 1.9 to 31.3: given in hospital before discharge. Per the Ministry, babies who should have had it in hospital and did not can get it at Tipat Halav during the routine visits.
- Born 1.4 to 31.8: given at the routine Tipat Halav visit at the end of summer or start of autumn, before the RSV season, not in hospital. The MoH table gives the Tipat Halav months as September to 31 March.
- High-risk infants and toddlers also get a dose in their second RSV season.
- The calendar shows only this rule, on the birth row. It never works out whether a particular baby is still eligible or by when: for a missing dose, the parent checks the booklet and asks the Tipat Halav nurse.

#### School vaccines (given by the school health service)

| Grade | Vaccines |
|---|---|
| 1 | MMRV 2/2 (born on or before 31.12.2024) or hepatitis A 2/2 (born from 1.1.2025) |
| 2 | Diphtheria, tetanus, pertussis and polio booster, plus flu (in the MoH South and North districts, for children born before 1.1.2025, the booster is given in grade 1) |
| 3 | Flu |
| 4 | Flu |
| 7 | HPV 1/2 |
| 8 | Diphtheria, tetanus and pertussis booster, plus HPV 2/2 |

In the Ministry's South and North districts the grade-2 booster is given in grade 1 instead (`--booster-grade1`). The MoH site shows this exception only for children born before 1.1.2025, so the script applies it only to that cohort and tells parents of younger children to confirm with the school nurse. If the parent does not know their district, the school nurse does. In the Ashkelon district and the Tzfat sub-district both HPV doses are given in grade 8, about half a year apart (`--hpv-both-grade8`). In special education, flu is given in grades 1 to 6. The school asks for the booklet about two weeks before, a reservation is written on the health declaration, and a lost booklet does not block vaccination. Grade dates come only from the parent's `--grade1-year`; never infer a school-entry year from the birth date.

Beyond vaccines, the school health service for grades 1 to 9 includes screening for early detection (vision, hearing and a growth assessment by weighing and measuring) and dental services (a dental check, a health lesson and a free toothbrush and toothpaste). Results go to the parents. Parents who object to some or all of the screenings note it in the health declaration.

Outside Tipat Halav the Ministry also recommends a yearly flu vaccine from 6 months (free at the kupah before winter) and meningococcal B, mainly for infants and toddlers (not in the health basket, paid at the kupah with a referral).

### Step 3: What to ask at each visit

Use `references/visit-guide.md`, which holds the MoH wording for every visit: the development items the nurse checks, the guidance topics, and the physician exam. Put them in the checklist as "what the nurse checks", never as a pass/fail test. Key reminders, with no doses:

- Vitamin D is given daily from birth to age 1 (the same for preterm babies). A forgotten day is not made up.
- An iron supplement starts at 4 completed months and stops at 18 months; the amount goes up at 6 months. Amounts come from the nurse. Preterm babies differ: see Step 4.
- At 9 months the family gets a blood count referral for the 12-month visit.
- At 4 years visual acuity is checked; at 5 years, readiness for grade 1.
- From the first tooth to age 6, about 70 Tipat Halav stations offer free caries prevention (booking *6362).
- The first visit takes about an hour. Bring the discharge letter, the vaccine booklet, a cloth diaper, spare diapers and clothes, and formula and a bottle if not breastfeeding.

### Step 4: Special cases

**Missed or late vaccine.** The Ministry's rule for clinicians is that doses given at longer than recommended intervals still count, so there is no restart. Route: under school age, the Tipat Halav nurse; up to grade 9, the school health service, free; grade 10 to 18, the health bureau vaccine clinics, free, booked via *5400. From 18 (21 in special education) catch-up is paid, except HPV, which is free up to and including age 26. Never compute catch-up intervals or minimum ages: the nurse does that from the booklet.

**Olim children with a foreign schedule.** The Ministry's catch-up guideline names new-immigrant children explicitly. Status is set from medical records or reliable information, and with no record or a doubtful one the child is treated as unvaccinated. Tell the parent not to wait for the next age-based visit: a child under 6 registers with a Tipat Halav station now (Ministry of Health stations serve everyone, regardless of kupah), and a school-age child goes through the school nurse. Bring the foreign record. You may line up the foreign record against the Israeli table to prepare questions, but never declare which doses "count". Run the script with `--olim` so past items read "before arrival" instead of "check the booklet".

**Born early.** Preterm means born before 37 completed weeks (`--preterm`). The NICU discharge letter sets feeding and follow-up for the first months; visits before the discharge date are marked "in hospital". Vaccines go by chronological age, with MoH exceptions. Rotavirus: a baby still hospitalised at 2 months gets dose 1 after discharge, and the Ministry allows dose 1 only up to age 14 weeks and 6 days (the last dose up to 8 months). State that published rule and leave the timing to the NICU team or the Tipat Halav nurse: for a preterm baby still in hospital at 6 weeks (or with no discharge date given) the calendar shows rotavirus rows without dose numbers, and it never computes a deadline. Hepatitis B: for a preterm baby under 2 kg the series starts at discharge, 2 kg or 1 month of age, whichever comes first; dose 2 comes one month after dose 1 and the booster 5 months after dose 2, so those rows say the nurse sets the dates. If the mother is a hepatitis B carrier, a birth dose given to a baby under 2 kg does not count toward the routine series. For visits that fell during the hospital stay, check the discharge letter for those vaccines and ask the NICU team or the nurse about anything not listed. If the parent gives weeks of gestation instead of a due date, ask for the due date from the discharge letter rather than computing one. Most preterm babies start an iron supplement from 2 weeks of age, with the amount set by body weight by the Tipat Halav nurse, so the term-baby "iron from 4 months" line does not apply. If the parent asks for the calendar "by corrected age", say plainly that vaccine dates follow the birth date and show corrected age only alongside each visit. Growth curves are read by corrected age (MoH); for development Maccabi uses it mainly in the first year, up to age 3 for very small preemies. The script shows corrected age from `--due-date`; the nurse reads it.

**Contact with someone who has measles.** Call Kol HaBriut *5400 or the district health bureau as soon as possible; by age and vaccination status, they decide whether a vaccine is needed (MoH measles page). Do not decide it in the chat.

**Measles outbreak (MoH update, 9 November 2026).** For anyone living in or visiting a locality with an active outbreak, and before any trip abroad, the Ministry recommends an extra early dose at 6 to 11 months on top of the 2 routine doses, and for children over age 1 who had only one dose, bringing the second dose forward. It matters most for children born before 2025 (routine dose 2 in grade 1). Mark it "check current status with Tipat Halav".

**Sick on vaccine day.** MoH: with an acute illness and fever above 38 the child is not vaccinated that day; a mild illness, a cold, mild diarrhea or a local infection is not a reason to postpone. The nurse decides.

**Parent wants to split, delay or skip.** Do not help plan it. Quote the Ministry: splitting does not make it easier and delays protection, leaving the child exposed. Suggest raising every concern with the Tipat Halav nurse or the pediatrician. Stay respectful; the decision is the parent's, made with the nurse.

**After a vaccine.** Contact the kupah if the baby seems apathetic or a fever does not pass after 24 to 48 hours. In the week after rotavirus dose 1 or 2, abdominal pain with extreme crying, vomiting, blood in the stool, legs drawn to the chest or weakness means the ER now (MoH rotavirus page). Up to 2 months, any fever over 38 is the Step 0 rule, vaccine or not.

### Step 5: Everyday questions

Answer from the Ministry's published guidance, then hand the specific child to the nurse.

**"Is it normal that...?" (milestones).** Work in this order:

1. Ask the child's age (and corrected age if born early).
2. Check `references/developmental-referral-signs.md` (Maccabi's published warning signs, for example: at 8 months does not sit without support; after 12 months does not crawl or stand without support; at 18 months does not walk). If a sign fits the child's age, or an item the nurse checked at an earlier visit is still missing (this includes language and social items, for example "says 2 to 3 words" at 12 months or "responds to own name" at 9 months), or the child has lost a skill they had, do not reassure: tell the parent to contact the pediatrician or the Tipat Halav nurse now, not at the next routine visit. Maccabi notes that, as needed, the child is referred to a child development institute; rights and copays there go to israeli-hmo-navigator.
   For a worry about speech or language, mention that the Ministry notes hearing problems can delay speech and language development, and that a developmental assessment starts by checking that the senses work, so a hearing and vision check may be part of it. The pediatrician or the nurse decides on the referral.
3. Otherwise, quote what the nurse checks at the nearest visit from `references/visit-guide.md`, say that the Ministry describes the range of normal development as wide, and suggest raising it at that visit or with the nurse line.

Never declare a child normal or delayed, and never invent an age that is not in the two reference files. For a worry between visits, the Tipat Halav nurse line at Kol HaBriut *5400 (extension 1, then 9) answers Sunday to Thursday 16:00 to 21:00 and Friday 08:00 to 13:00 (from abroad 972-8-6241010).

**Feeding and solids.** Exclusive breastfeeding for 6 months (no added water), continuing to age 2 and beyond. Solids around 6 months by readiness (interest in food, sitting independently, head control), not before 4 months; coarser texture from 7 months, small pieces from 9 months. Until age 1, no cow's milk as a drink and no honey (botulism). Water for formula is boiled until age 1. Under 5, no nuts, peanuts, almonds, seeds or popcorn unless ground completely smooth, and no hard candy or gummy sweets. In families with atopy, see a dietitian and a doctor before 6 months to plan complementary feeding; specifics of allergy go to israeli-food-allergy-navigator.

**Sleep.** Safe sleep: on the back only; an Israeli-standard mattress, not too soft, no incline; only a sheet and a tucked blanket; the crib in the parents' room at least to 6 months, preferably to 1 year, no bed sharing; offer a pacifier; no smoking, alcohol or drugs; supervised tummy time when awake. Most SIDS cases happen before 6 months. Night waking to eat is normal in the first year; around 3 months a 4 to 5 hour night stretch usually forms, with 14 to 16 hours of sleep a day. The Ministry says online sleep-hour tables are not reliable for every child. Ages 2 to 5: no screens in the 2 hours before sleep.

**Crying.** The Ministry's rule: "crying does not kill, shaking does." If a parent feels they are losing control, the Ministry suggests putting the baby in the crib, going to another room and coming back every few minutes, and asking someone trusted to take over for a short break.

**Out of scope, route instead:** daycare subsidies, gan registration, child allowance or special-education committees (israeli-childcare-navigator); kupah rights, copays and supplementary insurance (israeli-hmo-navigator); pregnancy and IVF (israeli-fertility-guide); food allergy (israeli-food-allergy-navigator); meal plans (israeli-nutrition-planner); a teenager's mental health (israeli-mental-health-navigator). Medicine or supplement doses: the label, the pharmacist or the nurse.

## Output

1. The notice FIRST, before any date or table: "This is Ministry of Health published information placed on your child's dates. It is not medical advice, not a diagnosis and not a developmental assessment. Decisions on vaccinating, catching up or postponing are made with the Tipat Halav nurse or the doctor."
2. A short header: child, birth date, which cohort rule applies, the schedule version ("MoH routine schedule, September 2026, checked 17/11/2026").
3. The red-flag box from Step 0 and the nurse line.
4. The calendar table (Mode A files, or the Mode B table plus optional `.ics` text).
5. Per-visit details from `references/visit-guide.md`.

## Examples

### Example 1: Calendar from a birth date

User says: "My son was born on 2026-03-14, make me the Tipat Halav and vaccination calendar."
Actions: born between 1.9 and 31.3, so RSV was due in hospital; 2025 cohort, so MMRV 2 at 18 months and hepatitis A 2 in grade 1. Run the script (or build the Mode B table): notice, red-flag box, past rows marked "check the booklet", then upcoming: 9 months (14/12/2026, physician exam, blood count referral), 12 months (14/03/2027), 18 months (14/09/2027), 24 months (14/03/2028), 4 years, 5 years. Ask for the grade-1 year to add school vaccines.
Result: `calendar.ics`, `checklist.md`, `table.md`, with the red-flag box.

### Example 2: "When does my daughter get the MMRV, and what should I ask at 12 months?"

Actions: ask the birth date. Born from 1.1.2025: MMRV 2 at 18 months. Born on or before 31.12.2024: grade 1, unless an outbreak or travel abroad brings it forward. Then list the 12-month visit from the visit guide: vaccines, development items, stop vitamin D, continue iron, bring the blood count from the 9-month referral.

### Example 3: "Is it normal that my 9-month-old isn't crawling yet?"

Actions: ask whether the baby was born early, then check the referral signs first (Maccabi: "at 8 months does not sit without support"; any lost skill). If one fits, contact the pediatrician or the nurse now. If not, quote the 9-month items the nurse checks (crawling among them), note that Maccabi's crawling sign is "after 12 months", and suggest raising it at the 9-month visit (physician exam) or with the nurse line. No verdict either way.

## Bundled Resources

### Scripts
- `scripts/build_calendar.py`: offline calendar builder (`.ics`, checklist, table). Standard library only, no network, validates dates.
- `scripts/test_build_calendar.py`: rule tests and an RFC 5545 structure check.

### References
- `references/visit-guide.md`: every visit in MoH wording (Hebrew) with an English translation: development items, guidance, exam.
- `references/red-flags.md`: the sourced red-flag list in Hebrew and English.
- `references/developmental-referral-signs.md`: Maccabi's published developmental warning signs, used only to escalate.
- `references/domain-checklist.md`: coverage checklist and known conflicts between sources.

## Recommended MCP Servers

| MCP | Use | When |
|---|---|---|
| `il-health` (https://agentskills.co.il/en/mcp/il-health) | Ministry of Health dashboard data, including child health checkup and development metrics | Only if the parent asks for national statistics. The calendar never needs it. |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| MoH Tipat Halav visit plan | https://me.health.gov.il/parenting/raising-children/infant-and-child-development/tipat-halav/tipat-halav-schedule/ | Visits, physician exams, development items, both cohorts |
| MoH routine vaccine schedule | https://me.health.gov.il/parenting/raising-children/immunization-schedule/babies-immunization-schedule/ | Doses by age and grade, cohort toggle |
| MoH schedule table, September 2026 (PDF) | https://www.gov.il/BlobFolder/policy/luah/he/files_publications_units_epidemiology_vaccine_guidelines_120_LUAH.pdf | 6-week footnote, cohort footnotes, PCV20 |
| MoH RSV immunization | https://me.health.gov.il/parenting/raising-children/immunization-schedule/children-vaccines/rsv-vaccine-beyfortus/ | Birth-month rule |
| MoH catch-up | https://me.health.gov.il/parenting/raising-children/immunization-schedule/routine-vaccinations-completion/ | Routes, ages, payment |
| MoH school vaccines | https://me.health.gov.il/parenting/raising-children/immunization-schedule/vaccine-schedule-6-to-18-years/ | Grades, booklet, illness rule |
| MoH meningitis (101 list) | https://me.health.gov.il/parenting/raising-children/common-childhood-diseases-and-symptoms/viral-diseases/meningitis/ | Red flags, fever by age |

## Gotchas

- **Copying the US/CDC schedule.** Israel gives the 2-month vaccines at 6 weeks, has no 3-year visit, gives hepatitis A at 18 months, and gives the RSV antibody by birth month. Never fill gaps from CDC tables.
- **Forgetting the regional exceptions.** In the South and North districts the grade-2 booster is given in grade 1 (children born before 1.1.2025, per the MoH site); in the Ashkelon district and Tzfat sub-district both HPV doses are in grade 8. Ask where the family lives before dating school rows.
- **Reassuring past a warning sign.** "The range is wide" is the answer only when no referral sign fits the child's age and no skill was lost. Otherwise route now.
- **Ignoring the 2025 cohort split.** Born 31.12.2024 and born 1.1.2025 get MMRV 2 and hepatitis A 2 at different ages.
- **Shifting vaccines to corrected age.** For preterm babies vaccines go by the birth date; only growth and developmental reading use corrected age. Hepatitis B and iron are the exceptions that do change, and the discharge letter rules.
- **Using 3 months as the infant-fever cut-off.** The Ministry's ER-now rule is up to 2 months; 2 to 3 months is an urgent check. Many English sources say 3 months.
- **Inventing catch-up intervals, school-entry years or doses.** Ask for the grade-1 year or current grade; send intervals and supplement or medicine amounts to the nurse, the label or the pharmacist.

## Troubleshooting

### Error: "the birth date is in the future"
Cause: a due date was entered as the birth date. Solution: this skill starts at birth; pregnancy questions go to israeli-fertility-guide.

### The calendar app shows no school vaccines
Cause: no `--grade1-year` or `--current-grade`. Solution: ask the parent and re-run.

### The booklet shows a vaccine the table does not list
Cause: the calendar applies today's schedule and lists no doses for past items before April 2025; older booklets follow the schedule of their time, for example oral polio drops (bOPV), stopped in March 2025. Solution: that is expected; the digital registry is complete only from 15 March 2025, so keep the paper booklet and ask the nurse about anything unclear.
