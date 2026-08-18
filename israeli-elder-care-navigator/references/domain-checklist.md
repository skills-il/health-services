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
| Cash amounts per level, foreign vs Israeli worker | covered, Step 3 |
| Income test: four filing-month bands, individual / couple / per-child | covered, Step 3 + benefits reference |
| Income NOT counted; expenses deducted; both-spouses rule | covered, Step 3 |
| Hospitalisation: 30 days, and restore on discharge | covered, Step 3 |
| Beit avot vs nursing institution (avl 33417-10-12) | covered, Step 3 + Gotcha 5 |
| Full-time top-up to 42h/week via a siud company | covered, housing reference |
| Temporary benefit (gimlat siud zmanit) | NOT COVERED, open |
| Pre-siud services (trom siud) | NOT COVERED, open |
| Fast track without an ADL test | NOT COVERED, open |
| Geriatrician ADL for ages 90+; Alzheimer's-specific ADL | NOT COVERED, open |
| Blind-person automatic level 2 | NOT COVERED, open |
| Extra care hours for Holocaust survivors (+9 weekly) | NOT COVERED, open, high priority |
| Arnona / water / electricity discounts for recipients | NOT COVERED, open |
| Escort free entry; queue exemption at levels 4-6 | NOT COVERED, open |
| Appeal of a benefit decision | partly, Troubleshooting |

## Bituach Leumi, other

| Item | Status |
|---|---|
| Old-age pension amounts, seniority, deductions | covered, Step 2 |
| Retirement age by birth year; absolute entitlement age 70 | covered, Step 2 + benefits reference |
| Income supplement, per income type | covered, Step 2 |
| Attendance allowance (shirutim meyuchadim) and its 6-month post-retirement deadline | NOT COVERED, open, high priority |
| Deferral bonus; old-age pension for a disabled person; special pension for olim | NOT COVERED, open |
| Death grant; survivors | out of scope, belongs to israeli-bituach-leumi |
| BL counselling service for seniors; national seniors hotline | NOT COVERED, open |

## Kupot cholim / private insurance

| Item | Status |
|---|---|
| Group siudi is the only real route since 2019 | covered, Step 4 |
| Basic-tier benefit table by joining age and place | covered, Step 4 |
| 5-year payout limit; 60-day wait; 80% indemnity cap; accident exclusions | covered, Step 4 |
| Dec 2023 basic-tier-only freeze through 01.01.2028 | covered, Step 4 |
| Switching kupot without underwriting, and the Clalit caveat | partly, Step 4. Caveat not yet stated |
| Hospice under the basic basket | covered, Step 6b |

## Ministry of Health / Welfare

| Item | Status |
|---|---|
| Code placement: district health office route | covered, Step 5 |
| Classification committee, 14-day visit, appeal path, 3-month expiry | covered, Step 5 |
| Adult children means-tested for the co-payment | covered, Step 5 |
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

## Legal capacity

| Item | Status |
|---|---|
| Enduring POA and the registration requirement | covered, Step 6 |
| Guardianship | covered, Step 6 |
| Supported decision-making (tomech hachlatot) | NOT COVERED, open, high priority |
| Expression-of-wishes document (mismach haba'at ratzon) | NOT COVERED, open |
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
