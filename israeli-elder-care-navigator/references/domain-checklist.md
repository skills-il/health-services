# Coverage contract: Israeli elder care

Purpose: this skill spans six agencies. Without an explicit contract, whole named benefits
went missing for three review cycles. Re-check every row on each update. A row marked
"covered" must point at a real section; a row marked "out of scope" must say why.

## Bituach Leumi, long-term care (gimlat siud)

| Item | Status |
|---|---|
| 6 benefit levels, ADL point bands | covered, Step 3 |
| Weekly hours per level, default and with foreign worker | covered, Step 3 |
| Reduced (50%) benefit hours | covered, Step 3 |
| Level 1 four-way election, 9 units vs 5.5 units | covered, Step 3 |
| Day-centre conversion rate and weekly caps | covered, Step 3 |
| Cash election caps (4 hours, or a third with social worker approval) | covered, Step 3 |
| Full cash for live-in caregiver employers, and the exceptional route | covered, Step 3 |
| Cash amounts per level, foreign vs Israeli worker | covered, Step 3 (re-rated 01.08.2026; re-check the effective date every cycle, BTL indexes mid-year) |
| Income test: four filing-month bands, individual / couple / per-child | covered, Step 3 + benefits reference |
| Income NOT counted; expenses deducted; both-spouses rule | covered, Step 3 |
| Hospitalisation: 30 days, and restore on discharge | covered, Step 3 |
| Beit avot vs nursing institution (avl 33417-10-12) | covered, Step 3 + Gotcha 5 |
| Full-time top-up to 42h/week via a siud company | covered, housing reference |
| Temporary benefit (gimlat siud zmanit) and re-examination | covered, `references/more-entitlements.md` (v1.6.0) |
| Pre-siud services (trom siud): 6 free weekly hours, at most a month | covered, Step 3 + `references/more-entitlements.md` (v1.6.0, after expert r1) |
| Eligibility on medical documents alone; assessment mainly from documents | covered, Step 3 + `references/more-entitlements.md` (v1.6.0). No named siud "fast track" found on BTL; the attendance-allowance fast track is a different benefit |
| Geriatrician ADL for ages 90+, and 90+ with 6 points set at level 4 | covered, Step 3 (v1.6.0). Alzheimer's-specific ADL still open |
| Blind-person automatic level | NOT COVERED, open. BTL claim page only asks for the certificate; no automatic level found in primary text on 2026-10-01, so do not assert one |
| Extra care hours for Holocaust survivors (+9 weekly, cash variants), the 2,000 NIS income-excess reading, the 1.5-2 point cash band, home-only rule, post-hospital 50 hours | covered, Step 3 + Step 6d + `references/more-entitlements.md` (v1.6.0, after expert r1) |
| Arnona discount up to 70% for recipients | covered, `references/more-entitlements.md` (v1.6.0). Water / electricity still open |
| Escort free entry; queue exemption at levels 4-6 | covered, Step 6c + `references/more-entitlements.md` (v1.6.0) |
| Appeal of a benefit decision (advisory committee within 60 days, or Labour Court; no reduction) | covered, Step 3 + Troubleshooting (v1.6.0) |

## Bituach Leumi, other

| Item | Status |
|---|---|
| Old-age pension amounts, seniority, deductions | covered, Step 2 |
| Retirement age by birth DATE (born 1963 = 63y3m, so "turning 63" is not retirement age); absolute entitlement age 70 | covered, Step 2 + Gotcha 3 + benefits reference (corrected v1.6.0 after expert r1) |
| Income supplement, per income type | covered, Step 2 |
| Income supplement guaranteed amount by household composition and age band | covered, Step 2 + `references/elder-care-benefits.md` (added v1.5.0) |
| Attendance allowance (shirutim meyuchadim): must-choose rule vs gimlat siud, continuation past retirement age, first claim up to half a year after retirement age | covered, Step 3 + `references/more-entitlements.md` (v1.6.0) |
| Deferral increment (5% per deferred year) | covered, Step 2 + `references/elder-care-benefits.md` (added v1.5.0) |
| Old-age pension for a disabled person (disability-pension guarantee, tosefet hashlama lenechut); special pension for olim | NOT COVERED, open. Expert r1 MAJOR, deferred: needs the BTL transition page read before writing |
| Death grant; survivors | out of scope, belongs to israeli-bituach-leumi (route there explicitly) |
| BL seniors line *9696 (assisted claim filing) | covered, Step 3 (v1.6.0). In-person counselling service still open |

## Kupot cholim / private insurance

| Item | Status |
|---|---|
| Group siudi is the only real route since 2019 | covered, Step 4 |
| Basic-tier benefit table by joining age and place | covered, Step 4 |
| 5-year payout limit; 60-day wait; 80% indemnity cap; accident exclusions | covered, Step 4 |
| Dec 2023 basic-tier-only freeze through 01.01.2028 | covered, Step 4 |
| Switching kupot without underwriting, the 180-day proof window and the Clalit caveat | covered, Step 4 (v1.6.0). Clalit mechanism itself not stated on the source; hedged |
| Hospice under the basic basket | covered, Step 6b |
| Post-acute rehabilitation after a stroke or fall (kupa responsibility, minimum inpatient days, rehab setting bars gimlat siud) | covered, Step 3 + `references/more-entitlements.md` (v1.6.0, after expert r1) |
| Complex-nursing (siudi murkav) placement through the kupa, distinct from the MoH code | covered, Step 5 + `references/institutional-copayment.md` (v1.6.0, after expert r1) |

## Ministry of Health / Welfare

| Item | Status |
|---|---|
| Code placement: district health office route | covered, Step 5 |
| Classification committee, 14-day visit, appeal path, 3-month expiry | covered, Step 5 |
| Adult children means-tested for the co-payment | covered, Step 5 + `references/institutional-copayment.md` |
| Order of payment sources (patient income, rent, patient assets, then children); child abroad not charged | covered, Step 5 + `references/institutional-copayment.md` (v1.6.0) |
| Children's divisor is the s.3.2 fixed person scale (3 / 3 / 2, +1 per child under 21, +1/4 per child 21-26), NOT a head count | covered, Step 5 + reference (corrected v1.6.0 after expert r1: the head count overstated a single child's charge several-fold) |
| Protected savings: 100 credit points for last expenses; joint savings with an at-home spouse untouched to 350, 350 kept to 700, half above 700; maturing plans not broken | covered, Step 5 + reference (added v1.6.0 after expert r2: the order-of-sources repair had implied all savings are drained) |
| The home counts only if no spouse or dependant lives in it; lien only for an ariri or publicly guarded patient; gift to a relative within 5 years | covered, Step 5 + reference (corrected v1.6.0 after arithmetic r2: earlier text charged or encumbered the home even with a spouse living in it) |
| Credit-point charging table for adult children, housing deduction, excluded income, 125% multiplier | covered, `references/institutional-copayment.md` (added v1.5.0; v1.4.2 asserted coverage but carried no scale at all) |
| Family cap at full actual cost, 37% patient floor, both-parents-once rule | covered, `references/institutional-copayment.md` |
| Welfare-funded-spouse 60/40 split and kibbutz 40% no-means-test track | covered, `references/institutional-copayment.md` |
| Pocket money (demei kis) shekel amount | covered, Step 5 (v1.6.0). REOPENED 2026-10-01: the 2026-08-19 out-of-scope rationale was wrong. MoH publishes no figure, but Bituach Leumi does (HalukatKitzva.aspx: 662 NIS, 607 NIS with income supplement, from 01.01.2026). Re-read each January |
| National institutional tariff | Out of scope (explicit), re-reviewed 2026-10-01: a user would ask, but no published national figure was found; the circular defines the cost per institution. Previously reviewed 2026-08-19. No such figure exists: "full actual cost" is per institution under its MoH agreement. The skill routes to the district health office treasury. |
| Licence check before choosing a facility | covered, Step 5 |
| Facility types and cost ranges | covered, Step 5 + housing reference |

## PIBA / foreign caregivers

| Item | Status |
|---|---|
| Permit point thresholds, 85+ and 90+ routes | covered, housing reference |
| ADL test for the permit even when income disqualifies from the benefit | covered, housing reference |
| Permit allowed in diur mugan | covered, Step 3 + housing reference |
| Minimum wage and total employer cost | covered, Step 5b |
| One worker for two family members | NOT COVERED, open |
| Permit processing time (about 14 working days), *3450, hospital-discharge declaration (Form E) | covered, Step 5b (v1.6.0) |
| Temporary post-discharge permit up to 3 months; PIBA fees 370 / 340 NIS | covered, Step 5b (v1.6.0) |
| Gimlat siud cash kept while awaiting the PIBA humanitarian committee | covered, Step 3 (v1.6.0) |

## Legal capacity

| Item | Status |
|---|---|
| Enduring POA and the registration requirement | covered, Step 6 |
| Guardianship | covered, Step 6 |
| Supported decision-making (tomech bekabalat hachlatot, s.67B) and the least-restrictive rule (s.33A) | covered, Step 6 + `references/more-entitlements.md` (v1.6.0) |
| Advance directives naming a guardian (s.35A) | covered, Step 6 + reference (v1.6.0) |
| Medical-only enduring POA signed before a physician, psychologist, nurse or social worker | covered, Step 6 (v1.6.0) |
| Expression-of-wishes document (mismach haba'at ratzon, s.64A) | covered, reference (v1.6.0). It is the instrument of a guardian of a RELATIVE (including a de facto guardian) naming a successor guardian, not the elder's own planning tool and not a parent-of-a-minor document |
| Advance directives and medical POA under the Terminally Ill Patient Law | covered, Step 6b |

## Rules for this skill

- Every NIS amount, percentage, age, deadline, form number and phone number needs an
  evidence.json entry whose claim carries the English form and whose raw_snippet carries the
  Hebrew source text. The gate matches per locale, so both must be present.
- Never write a rate that was not read in a text layer or transcribed from an image. If a
  page renders client-side, say so rather than inferring the number.
- Do not put percent-encoded Hebrew URLs in SKILL.md or SKILL_HE.md: the evidence gate reads
  the %XX sequences as phantom percentage claims. Use literal Hebrew URLs in the body and
  keep encoded forms in evidence.json only.
- A rate table with many rows must be reproduced in full. Quoting only the common case is the
  defect class that has already shipped a doubled-rate error elsewhere in this catalog.
- BTL re-rates gimlat siud cash amounts mid-year (the current table carries 01.08.2026). Every figure
  must carry its effective date, and each cycle must re-read money.aspx and the level pages
  rather than trusting January figures.
