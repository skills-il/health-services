---
name: foreign-caregiver-payroll
description: >-
  Guides Israeli families through legally employing a foreign nursing caregiver
  (metapel siudi zar) at home and computes the real monthly cost. Use when a user
  asks how to hire a foreign caregiver, "kama oleh metapel zar", "ma ha'sachar shel
  ovedet siudit", needs to calculate caregiver salary, social provisions, havraa,
  vacation days, or wants to understand the permit and bureau process. Explains the
  Population and Immigration Authority permit, minimum wage, National Insurance,
  pension and severance, recuperation pay, annual leave, holidays by country of
  origin, and how the Bituach Leumi long-term-care benefit offsets the cost. Do NOT
  use for caregivers hired through a care company as the company's employees, for
  Israeli (non-foreign) caregivers, or for general elder-care service navigation
  (use israeli-elder-care-navigator for that).
license: MIT
allowed-tools: ''
compatibility: >-
  Knowledge and calculation skill. No special tools required; any agent can compute
  the cost from the documented rates. An optional Python helper script is bundled
  for users with a local shell. Works with Claude Code, Claude.ai, Cursor, and other
  agents.
---

# Foreign Caregiver Payroll and Employment (Israel)

## Problem

Israeli families who bring a foreign caregiver home for an aging or disabled relative
are suddenly an employer, with a stack of obligations almost nobody explains in one
place: a permit, a licensed bureau, minimum wage, National Insurance, pension and
severance, recuperation pay, vacation, and holidays the worker may take by their own
religion. The numbers are scattered across the Population Authority, Bituach Leumi, and
labor law, and a single wrong assumption (for example, that the home employer pays into
the foreign-worker deposit fund, which is false) can cost thousands or trigger a claim.
This skill lays out the legal process and turns the rules into one honest monthly-cost
figure.

## Instructions

Work through whichever parts the user needs. Most users want either "how do I do this
legally" (Steps 1-2) or "what will it actually cost" (Steps 3-5). You do not have to run
them in order.

### Step 1: Confirm eligibility and get the permit

A family may only employ a foreign caregiver for a relative who is NOT in an institution
and needs essentially full-time care. Eligible recipients include seniors aged 85 and
over, recipients of the special-services benefit (sherutim meyuchadim, "שר\"מ") at a rate
below 112%, work-injury and cancer patients, and a disabled child, among others.

Employing a foreign worker requires an employment permit (heter haasaka) from the
Population and Immigration Authority (Rashut HaUchlusin VeHaHagira). Without it the whole
arrangement is illegal. Some requests are referred to a professional advisory committee.

### Step 2: Register with a licensed private bureau

After (or alongside) the permit, both the employer and the worker must be registered with
one of the licensed private placement bureaus (lishka pratit) for the nursing sector. The
bureau handles recruitment, work visas, and stands in on worker illness or death. Going
around the bureau is not an option for this sector.

### Step 3: Set the wage floor correctly

| Rule | Value | Note |
|------|-------|------|
| Monthly minimum wage (full-time) | 6,443.85 NIS (from 01.04.2026) | The floor; you may pay more |
| Hourly minimum wage | 35.40 NIS | |
| Live-in overtime | None | Live-in caregivers are NOT entitled to hourly overtime |
| Weekly rest | 25 hours continuous | Work during it is paid at 150% |

The "no overtime" rule comes from the Yolanda Gluten Supreme Court ruling: the Hours of
Work and Rest Law does not apply to live-in caregivers, so a live-in caregiver is paid a
monthly global wage rather than clocked hourly overtime. Be careful here: a widely
repeated claim that live-in caregivers are legally owed "minimum wage plus 20%" is a
non-binding dissent in that case, not law. Do not present it as a guaranteed entitlement.
Some bureaus pay a contractual supplement by custom, which is a separate matter.

### Step 4: Add the recurring employer costs

These are real monthly costs on top of the wage:

| Component | Rate / amount | Who bears it | Notes |
|-----------|---------------|--------------|-------|
| National Insurance | 3.6% of wage | Employer | From January 2025 (was 2%). The old 5,500 NIS reduced ceiling ended 03.08.2022, so 3.6% now applies to the full wage |
| Pension | 6.5% of wage | Employer | Mandatory employer pension contribution |
| Severance reserve | one month's salary per year worked | Employer | Accrues monthly (about one twelfth of the wage). See Step 5 |
| Medical insurance | Premium varies by insurer | Employer | Mandatory for the whole period. May deduct from wages at most half the cost, capped at 154.29 NIS/month |

The employer also withholds the worker's own 6% pension share from wages and passes it on; that is the worker's money, not an extra employer cost.

Foreign workers are not covered by the National Health Insurance Law, which is exactly why
the employer must buy private medical insurance, and why there is no health-tax deduction.

### Step 5: Handle the deposit fund correctly (the big misconception)

The standard foreign-worker arrangement is a monthly deposit of 12.5% of wages (6% in lieu
of severance + 6.5% pension) into a central government-managed fund. The critical point for
families: a nursing patient who employs a caregiver in their OWN home is EXEMPT from this
fund. Care companies and institutions deposit into the fund; a private household does not.

Instead, the private home employer owes these directly: the 6.5% pension, and severance
equal to one last-month salary multiplied by the number of years worked. Be careful here:
the 6% "in lieu of severance" inside the fund's 12.5% only fully discharges severance when
the money sits in a formal pension-fund arrangement. A home employer paying in cash has no
such arrangement, so the worker can still claim full statutory severance, which is one
month per year, higher than 6%. The safe reserve is therefore pension (6.5%) plus the full
severance accrual (about one twelfth of each month's wage), not the 6% the fund uses. Set
this money aside each month so it is there at termination. Because severance is computed on
the last (usually higher) salary, top it up after any raise.

### Step 6: Add leave entitlements

**Recuperation pay (havraa)** starts only after the worker completes 12 full months. The
private-sector tariff is 418 NIS per day, paid by seniority:

| Seniority | Havraa days |
|-----------|-------------|
| Year 1 | 5 |
| Years 2-3 | 6 |
| Years 4-10 | 7 |
| Years 11-15 | 8 |
| Years 16-19 | 9 |
| Year 20+ | 10 |

**Annual leave** accrues by seniority. For a 6-day work week (typical for a live-in
caregiver), the gross day entitlement is:

| Seniority | Gross vacation days |
|-----------|---------------------|
| Years 1-5 | 16 |
| Year 6 | 18 |
| Year 7 | 21 |
| Year 8 | 22 |
| Year 9 | 23 |
| Year 10 | 24 |
| Year 11 | 25 |
| Year 12 | 26 |
| Year 13 | 27 |
| Year 14+ | 28 |

**Holidays by country of origin.** This is the "medinat hamotza" angle: a foreign caregiver
is entitled to pay for 9 holidays a year, and may choose their own religion's holidays
instead of the Israeli ones. The choice is made once and stays fixed for the whole
employment, so settle it at the start.

### Step 7: Offset with the Bituach Leumi long-term-care benefit

The relative's nursing (long-term-care) benefit reduces the family's out-of-pocket cost. It
is paid in 6 levels; the monthly cash amount runs from 1,705 NIS at level 1 to 6,448 NIS at
level 6 (as of 01.04.2026). A recipient may employ a foreign caregiver directly (taking the
benefit as cash) or through a care company. When estimating net cost, subtract the level's
benefit from the gross monthly cost.

### Step 8: Your ongoing legal obligations as the employer

Beyond paying correctly, the family carries employer duties. A "legal employment" answer is
incomplete without these:

- **Register as an employer with Bituach Leumi.** Knowing the 3.6% rate is not enough; the
  household must register and report and pay National Insurance on the household-employer track
  (maasik oved bemeshek bayit), on the Bituach Leumi schedule, not as monthly PAYE.
- **Written employment contract** in a language the worker understands, given at the start,
  stating wage, hours, deductions, leave, and living arrangements.
- **Monthly payslip (tlush sachar).** A wage slip must be issued every month.
- **Sick days (dmei machala).** The worker accrues 1.5 sick days per month (up to 90). The first
  day of illness is unpaid, the second and third days are paid at 50%, and from the fourth day
  the full wage is paid. This is a real obligation and a cost when the worker is ill.
- **Watch deductions.** Beyond the medical-insurance cap (154.29 NIS), do not assume you can
  deduct "rent" from a live-in caregiver who lives in the patient's own home; the usual
  housing and utility deductions generally do not apply there. Verify any deduction before taking it.
- **Termination and the patient's death.** On ending employment the worker is owed severance,
  notice (or pay in lieu, up to one month), and payout of unused annual leave (pidyon chufsha),
  plus a final payslip. If the patient passes away, severance is still owed and the bureau steps
  in to relocate the worker; the permit lapses.
- **Income tax.** At minimum-wage level the caregiver is generally below the income-tax
  threshold, so usually no income tax is withheld and no tax-deduction file is opened; National
  Insurance is the main statutory deduction. Confirm if the wage is well above minimum.

### Step 9: Produce the monthly cost estimate

Build the figure from components rather than quoting a single bundled percentage (no
authoritative source sums them into one rate, and the timing differs):

```
gross wage              = max(minimum wage, agreed wage)
national insurance      = 3.6%  x gross wage          (employer, monthly)
pension                 = 6.5%  x gross wage          (employer, set aside)
severance reserve       = gross wage / 12             (one month per year; set aside, paid on termination)
havraa (monthly equiv.) = 418 x havraa_days / 12      (only after 12 months)
medical insurance       = insurer premium             (minus up to 154.29 deducted from wage)
---------------------------------------------------------------
gross monthly cost      = sum of the above
net monthly cost        = gross monthly cost - nursing benefit for the recipient's level
```

State assumptions explicitly (seniority year, care level, whether the first year is complete)
and label any number the user has not given you as an estimate.

## Examples

### Example 1: First-year cost estimate

User says: "My mother is 87 and just got a foreign caregiver. She is at care level 5. What
does it cost me a month?"

Actions:
1. Wage: assume minimum wage 6,443.85 NIS (ask if they pay more).
2. National Insurance: 3.6% x 6,443.85 = about 232 a month.
3. Pension: 6.5% x 6,443.85 = about 419 a month.
4. Severance reserve: 6,443.85 / 12 = about 537 a month (one month per year).
5. Havraa: 0 in year 1 (not yet entitled; begins after 12 months).
6. Medical insurance: ask for the insurer quote; note up to 154.29 NIS may be recovered from wage.
7. Subtract the level-5 nursing benefit from the gross monthly cost to get net out-of-pocket.

Result: an itemized estimate with each component labeled, plus the reminder that the pension and
severance (about 956 together) are accrued for termination, not a cash transfer to the worker each
month.

### Example 2: Choosing the holiday list

User says: "Our caregiver is from the Philippines. Which holidays does she get?"

Actions:
1. Explain she is entitled to pay for 9 holidays a year.
2. She may choose her own religion's holidays (for example Christian holidays) instead of the
   Israeli holidays, her choice.
3. The list is fixed once chosen, so agree on the 9 days in writing at the start.

Result: a clear, lawful holiday list set up front, avoiding a dispute later.

## Bundled Resources

### Scripts
- `scripts/calc_caregiver_cost.py` -- optional helper that itemizes the monthly employer cost
  from wage, seniority, care level, and an insurance premium. Run: `python scripts/calc_caregiver_cost.py --help`

### References
- `references/employment-process.md` -- the permit, eligibility groups, and bureau steps in detail.
- `references/pay-and-cost-components.md` -- every rate, the full leave tables, and the benefit levels with sources.

## Gotchas

- **The home employer does NOT pay into the deposit fund.** Agents routinely assume the
  monthly 12.5% deposit applies to everyone. For a caregiver employed in the patient's own
  home it does not; the family pays the worker directly at termination. Stating it the wrong
  way creates a phantom monthly payment.
- **Do not reserve only 6% for severance.** The 6% inside the fund's 12.5% discharges severance
  only inside a formal pension-fund arrangement. A home employer paying directly owes full
  statutory severance, one month per year (about one twelfth of wage), so reserve pension 6.5%
  plus that full severance accrual, not 6%. Reserving 12.5% under-funds the eventual payout.
- **No hourly overtime for live-in caregivers, and no statutory "+20%".** Do not compute
  time-and-a-half on a daily clock, and do not add a 20% live-in supplement as if it were law.
  It is a non-binding dissent in the Yolanda Gluten ruling, though a labour court may still
  award a global supplement case by case, so it is not guaranteed absent either.
- **Havraa is zero in year one.** Entitlement starts only after 12 full months. Including it
  from month one overstates the cost.
- **Use the 3.6% National Insurance rate, not 2%, and apply it to the full wage.** The rate rose
  in January 2025 and the 5,500 NIS ceiling was abolished in 2022.
- **Vacation and holiday days are entitlements, not automatic monthly cash.** They become a cash
  cost mainly when paid out (unused leave on termination, or a holiday worked). Do not double-count
  them as a flat monthly line unless the user asks for accrued value.

## Reference Links

| Source | URL | What to check |
|--------|-----|---------------|
| Minimum wage (Kol Zchut) | https://www.kolzchut.org.il/he/שכר_מינימום | Current monthly and hourly minimum wage |
| Caregiver employment terms (Kol Zchut) | https://www.kolzchut.org.il/he/תנאי_העסקה_של_עובד_זר_בסיעוד_המועסק_בבית_המטופל | Wage floor, no overtime, weekly rest, medical insurance, 9 holidays |
| Foreign-worker deposit (Kol Zchut) | https://www.kolzchut.org.il/he/הפקדת_פיקדון_חודשי_עבור_עובדים_זרים | 12.5% breakdown and the private-home exemption |
| National Insurance for caregiver (Kol Zchut) | https://www.kolzchut.org.il/he/דיווח_ותשלום_דמי_ביטוח_לאומי_עבור_עובד_זר_בסיעוד | 3.6% rate and the abolished ceiling |
| Recuperation pay (Kol Zchut) | https://www.kolzchut.org.il/he/דמי_הבראה | 418 NIS tariff and days by seniority |
| Sick days (Kol Zchut) | https://www.kolzchut.org.il/he/דמי_מחלה | Accrual and the 0/50/full payment ladder |
| Annual leave, 6-day week (Kol Zchut) | https://www.kolzchut.org.il/he/חישוב_מספר_ימי_החופשה_השנתית_לעובדים_במקומות_עבודה_שבהם_מונהג_שבוע_עבודה_בן_6_ימים | Vacation days by seniority |
| Employment permit (Kol Zchut) | https://www.kolzchut.org.il/he/קבלת_היתר_להעסקת_עובד_זר_בסיעוד | Eligibility groups and the permit process |
| Long-term-care benefit (Bituach Leumi) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/ovedZar.aspx | Benefit levels, amounts, direct vs care-company |

## Troubleshooting

### Error: "The cost looks too high / too low"
Cause: A component was applied wrong, usually havraa in year one, a 20% supplement, or the deposit fund.
Solution: Re-check Steps 4-6. Havraa is zero until 12 months; there is no statutory +20%; the home employer does not pay into the fund.

### Error: "Which minimum wage figure is current?"
Cause: Minimum wage updates on a set date and stale figures circulate.
Solution: Use 6,443.85 NIS/month (35.40 NIS/hour) from 01.04.2026, and confirm against the Kol Zchut minimum-wage page before quoting for back-pay.

### Error: "Is this for a caregiver from a care company too?"
Cause: The obligations differ when the company is the employer.
Solution: This skill covers the private home employer. If a care company employs the worker, the company carries the deposit and payroll duties instead.
