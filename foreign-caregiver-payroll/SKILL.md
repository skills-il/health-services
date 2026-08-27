---
name: foreign-caregiver-payroll
description: >-
  Not legal advice and not a binding payroll calculation.
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

## Legal notice

This is a free information tool operated by an AI model. It collects the rules that apply to
employing a foreign nursing caregiver in the patient's home and computes an estimated monthly
cost from figures you supply, with no involvement, review, or approval by a labour lawyer. The
output is not legal advice and not a legal opinion; it is general explanation and an arithmetic
estimate only. It does not examine your employment contract, does not check actual payslips,
does not decide entitlement to severance pay or to a global wage supplement, and does not
represent you before the Population and Immigration Authority, the National Insurance Institute,
or the Tax Authority. An AI model may err, omit data, or present a wrong conclusion, and the
rates and amounts in this field are revised annually, sometimes with retroactive effect.

Do not rely on the output as the basis for a deduction from the worker's wage, for ending the
employment, or for computing the final payment on termination. A deduction not permitted by law
is a criminal offence, and under-computing severance, recuperation pay, or leave redemption can
trigger a claim. This tool is not a substitute for advice that takes account of the particular
data and needs of each person; before any deduction, dismissal, or final payment, consult a
labour lawyer and verify every amount against the current Population Authority circular and
against the National Insurance Institute. Any use of the output is at your sole responsibility.

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
| Weekly rest | 25 hours continuous | Work during it is paid at 150% ON TOP of the full monthly wage. For a worker on minimum wage Kol Zchut states the supplement as **439.73 NIS per rest day worked**. Re-read that page rather than deriving it, since it moves with the minimum wage. A rest shorter than 25 hours is paid the same way for the hours not taken |

The "no overtime" rule comes from the Yolanda Gluten litigation: **HCJ 1678/07 Gluten v.
National Labour Court** (2009), reheard by an expanded panel in **HCJFH 10007/09**, which is the
operative authority. It holds that the Hours of Work and Rest Law 5711-1951 does not apply to
live-in caregivers, so a live-in caregiver is paid a monthly global wage rather than clocked
hourly overtime. Note the scope: this is about the caregiver living in the patient's home, where
hours cannot be supervised. Work outside that setting, and caregivers in an institution, are a
different question.

Be careful with the "+20%" figure. It is **not** law: it comes from a judicial proposal in that
litigation that did not become the holding, so do not present it as a guaranteed entitlement.

But do not present its absence as safety either. A labour court may still award a global
supplement on the facts of a particular case. This skill states no figure, because there is no
percentage that can be quoted in advance; the reliable number is the one in the judgment a
particular claim is measured against.
Treat a supplement as a real litigation risk to be priced with a labour lawyer, not as a settled
entitlement and not as a settled non-entitlement.

### Step 4: Add the recurring employer costs

These are real monthly costs on top of the wage:

| Component | Rate / amount | Who bears it | Notes |
|-----------|---------------|--------------|-------|
| National Insurance | 3.6% of wage | Employer | From January 2025 (was 2%). The old 5,500 NIS reduced ceiling ended 03.08.2022, so 3.6% now applies to the full wage |
| In lieu of pension | 6.5% of wage | Employer | Owed to the worker, and it accrues only **from the seventh month** of employment. It is not remitted to a fund: see Step 5 |
| Severance reserve | one month's salary per year worked | Employer | Accrues monthly (about one twelfth of the wage). See Step 5 |
| Medical insurance | Premium varies by insurer | Employer | Mandatory for the whole period. Part is recoverable from the wage: at most half the premium, and not more than the current annual cap (168.80 NIS/month from January 2026). See Step 4a |

**Do NOT withhold a pension share from the worker.** A foreign worker cannot be insured in an Israeli pension fund at all ("בישראל לא ניתן לבטח בביטוח פנסיוני עובדים זרים"), so there is nothing to pass a withheld share on to. The employer instead OWES the worker the amounts it would have contributed, paid at the end of employment (or monthly into a separate account for the worker). Deducting a "pension share" from wages would be an unlawful deduction. See Step 5 for the exact amounts and when they start.

Foreign workers are not covered by the National Health Insurance Law, which is exactly why
the employer must buy private medical insurance, and why there is no health-tax deduction.

### Step 4a: What you may deduct from the worker's wage, and what you may not

Families get this wrong in both directions: they invent deductions that are not permitted, and
they miss ones that are. The heads and caps below are set by the Foreign Workers Law s.1E(b) and
the Foreign Workers (Rate of Wage Deductions for Suitable Accommodation) Regulations 5760-2000,
with the shekel amounts updated annually by a Population Authority director's circular
(חוזר ראש מינהל). Take the current year's figures from that circular, not from this table.

**One overall cap governs the whole discretionary list: total deductions may not exceed 25% of
the wage in any one month**, and each requires the worker's written consent, disclosed in the
employment contract before work starts.

| Head | Cap for a nursing caregiver living in the patient's home |
|------|-----------------------------------------------------------|
| National Insurance (worker's share) | **Prohibited.** An employer of a nursing caregiver in the patient's home may not deduct ANY amount for National Insurance. The 3.6% is the employer's own cost, not a shared one |
| Income tax | Withheld per wage and credit points. Often nil at minimum wage, but credit-point entitlement varies by status, so confirm with the tax authority rather than assuming zero |
| Medical insurance | Up to HALF the premium the employer paid or undertook to pay, and **not more than 168.80 NIS/month from January 2026** (164.91 in 2025). Note the caregiver-terms page still shows an older 154.29 figure stamped January 2023; use the current year's circular |
| Accommodation, housing NOT owned by the employer | Regional: Jerusalem 508.62, Tel Aviv 578.36, Haifa/centre 385.61, south 342.80, north 315.41 NIS/month (2026) |
| Accommodation, housing OWNED by the employer, **which is the patient's-own-home case** | Exactly HALF the above: Jerusalem 254.31, Tel Aviv 289.18, Haifa/centre 192.81, south 171.40, north 157.71 NIS/month (2026) |
| Related expenses (electricity, water, arnona) | **94.34 NIS/month (2026)** under the line written specifically for a foreign nursing caregiver living in the employer's home (92.16 in 2025). Other sectors use a different figure |
| Advances against wages | Permitted, with the excess over three months' wage needing written consent and capped at a quarter of the wage |
| Board (food) | Permitted only if actually agreed and taken in the month; no fixed statutory figure for this sector |
| Union dues / organisational handling fee, disciplinary fine | Only where an applicable collective agreement or extension order provides for it |
| Debts owed to the employer | Written consent required, inside the 25% overall cap, with a further quarter-of-wage sub-cap during employment. On the final salary an UNDISPUTED debt balance may be deducted |
| Work-permit extension fee and re-entry visa | Borne by the worker |

**Correcting an earlier version of this skill:** it said housing and utility deductions
"generally do not apply" in the patient's own home. That is wrong: the accommodation table has a
dedicated employer-owned column at half rate and the utilities line is written for exactly this
worker. The amounts are small, regional and capped, but they apply. See
`references/domain-checklist.md`.

Two rules that bite:

- **A deduction not taken cannot be taken retroactively.** If you did not deduct accommodation,
  utilities, medical insurance or board in the month, you cannot recover it later.
- **Over-deducting is a criminal offence**, not a civil dispute. Check the current circular
  amount before deducting, and put the agreed deductions in the written contract.

### Step 5: Handle the deposit fund correctly (the big misconception)

The standard foreign-worker arrangement is a monthly deposit of 12.5% of wages (6% in lieu of
severance + 6.5% in lieu of pension contributions) into a central government-managed fund.

**The exemption is narrower than "private households are exempt".** It is the INTERSECTION of two
conditions: the worker is in the **nursing sector** AND is employed **by an individual otherwise
than in the course of that individual's business or occupation**. A care company employing the
same worker still deposits. Where the patient and a company employ the worker in parallel, each
side carries its share pro rata to the portion of the post it holds.

**What the home employer owes instead, and from when.** Because a foreign worker cannot be
insured in an Israeli pension fund, the employer does not "contribute" anywhere: it owes the
worker a sum at the end of employment, and the amount depends on how the employment ended.

| How employment ends | What the worker gets |
|---------------------|----------------------|
| Resigns, or is dismissed before completing one year | 12.5% of monthly wage (6% severance component plus 6.5% in lieu of contributions), for months **from the seventh month of employment onward**. See the warning below before relying on this row for a dismissal |
| Entitled to severance: dismissed after a year, the employer dies, or a resignation in circumstances that carry severance | **8.33%** of monthly wage x every month worked **from the first month**, PLUS **6.5%** of monthly wage for months **from the seventh month onward** |

Three consequences families miss:

- **The 6.5% leg starts in month 7, not month 1.** Reserving it from the first month over-reserves
  by six months' worth. The severance leg does start in month 1.
- **A dismissal shortly before the first anniversary does NOT reliably avoid severance.**
  The Severance Pay Law 5723-1963, under the heading "when dismissal does not prejudice rights",
  presumes that a dismissal "close to the end of the first year of employment" was made in order
  to avoid severance, and unless the employer proves otherwise the worker keeps the full
  entitlement. So a dismissal at month 10 or 11 should be
  reserved on the SECOND row of the table, not the first. Never advise a family that ending the
  employment before twelve months caps the exposure at 12.5%.
- **8.33% is one twelfth**, so a severance reserve of wage / 12 is the right magnitude. Because
  severance is computed on the LAST (usually higher) salary, top the reserve up after any raise.
- The money may be paid monthly into a separate account in the worker's name, or held and paid at
  the end. Either way it is the worker's, so set it aside rather than treating it as headroom.

### Step 6: Add leave entitlements

**Recuperation pay (havraa)** becomes PAYABLE only after the worker completes 12 full months,
but it is then paid **retroactively from the first day of work**, so the liability ACCRUES from
month one. Reserve it monthly and pay it at the anniversary. Treating it as a zero-cost item in
year one is the single most common under-reserving error: five days at the current tariff all
fall due in one month. The
private-sector tariff is **451.50 NIS per day** for havraa-year 2026 (1.7.2025 to 30.6.2026).
**This was updated on 18.08.2026, retroactively.** An employer who already paid this havraa
year at the previous 418 NIS tariff owes the differential up to 451.50. Check the tariff before
quoting: it is reset annually and the update can land mid-year and reach backwards. Days are
paid by seniority:

"Seniority" below means COMPLETED years. There is no entitlement at all during the first 12
months; the 5-day row is the first year of entitlement, after 12 months are complete.

| Completed years | Havraa days |
|-----------------|-------------|
| 1 | 5 |
| 2-3 | 6 |
| 4-10 | 7 |
| 11-15 | 8 |
| 16-19 | 9 |
| 20+ | 10 |

**Annual leave** accrues by seniority. For a 6-day work week (typical for a live-in
caregiver), quote BOTH columns. The gross figure includes the weekly rest day; the NET figure is
how many days the worker is actually absent, and it is the one that answers "how many days off
does she get" and the one leave redemption is computed on:

| Seniority | Net days absent | Gross days |
|-----------|-----------------|------------|
| Years 1-5 | 14 | 16 |
| Year 6 | 16 | 18 |
| Year 7 | 18 | 21 |
| Year 8 | 19 | 22 |
| Year 9 | 20 | 23 |
| Year 10 | 21 | 24 |
| Year 11 | 22 | 25 |
| Year 12 | 23 | 26 |
| Year 13 | 24 | 27 |
| Year 14+ | 24 | 28 |

**Holidays by country of origin.** This is the "medinat hamotza" angle: a foreign caregiver is
entitled to pay for 9 holidays a year, and may choose their own religion's holidays instead of the
Israeli ones. The choice is made once and stays fixed for the whole employment, so settle it at
the start. Three rules that change what the 9 days actually cost:

- A holiday is a **25-hour** period, like the weekly rest, not a calendar day.
- Work on a holiday is paid at **150% on top of** the full monthly wage. Kol Zchut puts this at the same **439.73 NIS** per day worked for a minimum-wage worker as for a worked rest day.
- **A holiday that falls on the weekly rest day carries no separate payment.** Some of the 9 will,
  so do not budget all nine as extra cost automatically.

**Bereavement leave** is a separate entitlement of up to 7 days, taken according to the custom of
the worker's own community.

### Step 7: Offset with the Bituach Leumi long-term-care benefit

The relative's nursing (long-term-care) benefit reduces the family's out-of-pocket cost. It is
paid in 6 levels. Bituach Leumi publishes **two columns**, and they are not the same: the maximum
cash benefit differs between an employer of a FOREIGN caregiver and an employer of an Israeli
caregiver from level 3 upward. Use the foreign column for this skill.

| Level | Employing a FOREIGN caregiver | Employing an Israeli caregiver |
|-------|------------------------------|--------------------------------|
| 1 | 1,705 NIS | 1,705 NIS |
| 2 | 2,480 NIS | 2,480 NIS |
| 3 | 3,472 NIS | 4,216 NIS |
| 4 | 4,464 NIS | 5,208 NIS |
| 5 | 5,456 NIS | 6,448 NIS |
| 6 | 6,448 NIS | 7,440 NIS |

All amounts as of 01.04.2026. **Watch the collision: 6,448 NIS is level 6 in the foreign column
and level 5 in the Israeli one.** An agent that reads a Bituach Leumi page without noticing which
column it is in will be one level out, which is roughly a thousand shekels a month.

A recipient may employ a foreign caregiver directly (taking the benefit as cash) or through a care
company. When estimating net cost, subtract the level's benefit from the gross monthly cost.

### Step 8: Your ongoing legal obligations as the employer

Beyond paying correctly, the family carries employer duties. A "legal employment" answer is
incomplete without these:

- **Register as an employer with Bituach Leumi within two weeks** of the day employment starts.
  Knowing the 3.6% rate is not enough; the
  household must register and report and pay National Insurance on the household-employer track
  (maasik oved bemeshek bayit), on the Bituach Leumi schedule, not as monthly PAYE.
- **Written employment contract** in a language the worker understands, given at the start,
  stating wage, hours, deductions, leave, and living arrangements.
- **Monthly payslip (tlush sachar).** A wage slip must be issued every month.
- **Sick days (dmei machala).** The worker accrues 1.5 sick days per month (up to 90). The first
  day of illness is unpaid, the second and third days are paid at 50%, and from the fourth day
  the full wage is paid. This is a real obligation and a cost when the worker is ill.
- **Deductions have their own table and their own criminal exposure.** See Step 4a. Over-deducting
  is an offence, and a deduction you did not take cannot be taken later.
- **Housing does not end with the job.** Foreign Workers Law s.1E(a) requires the employer to
  provide suitable accommodation at its own expense for the whole employment **and for at least
  seven days after it ends** (or the days left on the permit, if fewer).
- **Termination and the patient's death.** On ending employment the worker is owed severance,
  notice (or pay in lieu, up to one month), and payout of unused annual leave (pidyon chufsha),
  plus a final payslip. Leave redemption reaches back over the last part-year plus up to three
  preceding years, not the whole employment history. If the patient passes away, the Severance Pay Law
  provision headed "an employer who died" treats the worker as dismissed, so severance is owed, and the bureau relocates the worker.
  Warn the family about the money mechanics: these sums come out of the **deceased's estate**, and
  if no one else is authorised on the bank account it is frozen until a probate or inheritance
  order, which takes weeks. Keep the reserve somewhere that stays reachable.
- **Income tax.** At minimum-wage level the caregiver is generally below the income-tax
  threshold, so usually no income tax is withheld and no tax-deduction file is opened; National
  Insurance is the main statutory deduction. Confirm if the wage is well above minimum.

### Step 9: Produce the monthly cost estimate

Build the figure from components rather than quoting a single bundled percentage (no
authoritative source sums them into one rate, and the timing differs):

```
gross wage              = max(minimum wage, agreed wage)
national insurance      = 3.6%   x gross wage         (employer, monthly, NOT deductible from the worker)
in-lieu-of-pension      = 6.5%   x gross wage         (owed to the worker, ACCRUES FROM MONTH 7)
severance reserve       = 8.33%  x gross wage         (= wage/12, accrues from month 1, conditional on the exit route)
havraa (monthly equiv.) = 451.50 x havraa_days / 12   (ACCRUES from month 1; PAYABLE after 12 full
                                                       months, retroactively to day one. Check the tariff)
medical insurance       = insurer premium             (minus the permitted deduction, up to half the premium
                                                       and not more than the current annual cap)
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
2. National Insurance: 3.6% = about 232 a month.
3. In lieu of pension: 6.5% = about 419 a month, but **only from the seventh month**.
4. Severance reserve: 8.33% = about 537 a month, accruing from month 1, payable only on a severance-triggering exit.
5. Havraa: accrue 451.50 x 5 / 12 = about 188 a month from month 1. Nothing is PAID until 12 full months are complete, and it is then paid retroactively from the first day, so the money must already be set aside.
6. Medical insurance: ask for the insurer quote; up to half the premium may be deducted, within the current annual cap.
7. Subtract the **foreign-caregiver** level-5 benefit, 5,456 NIS, from the gross monthly cost to get net out-of-pocket. Do not use 6,448, which is the level-5 figure in the ISRAELI-caregiver column.

Result: an itemized estimate with each component labeled, the six-month pension delay stated, and
the reminder that the in-lieu-of-pension and severance amounts are accrued for termination rather
than paid monthly.

### Example 2: Choosing the holiday list

User: "Our caregiver is from the Philippines. Which holidays does she get?"

Actions: she is entitled to pay for 9 holidays a year and may choose her own religion's holidays
instead of the Israeli ones. The list is fixed once chosen, so agree the 9 days in writing at the
start. Result: a lawful holiday list settled up front, avoiding a dispute later.

## Bundled Resources

### Scripts
- `scripts/calc_caregiver_cost.py` -- optional helper that itemizes the monthly employer cost from wage, completed years, month of employment, care level and an insurance premium. It applies the month-7 start for the in-lieu-of-pension leg, accrues havraa from month one while labelling it not-yet-payable, applies the accommodation (`--region`) and utilities (`--utilities`) deductions against the 25% cap, and refuses to compute on a zero, negative or implausible wage, or on a month and seniority that contradict each other. Every constant it uses is also stated in prose above, so an agent without a shell can reproduce it by hand. Run: `python scripts/calc_caregiver_cost.py --help`

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
  It is a judicial proposal that did not become the holding. A labour court may still award a
  global supplement on the facts of a particular case, so its absence is not guaranteed either,
  but there is no percentage you can quote in advance.
- **Havraa is not free in year one.** It becomes payable only after 12 full months, but it is
  then paid retroactively from the first day of work. Accrue it from month one and pay it at the
  anniversary. Reserving nothing for it is the error, not reserving it.
- **Use the 3.6% National Insurance rate, not 2%, and apply it to the full wage.** The rate rose
  in January 2025 and the 5,500 NIS ceiling was abolished in 2022. And it is entirely the
  employer's: deducting any part of it from a nursing caregiver's wage is prohibited.
- **Never withhold a pension share from the worker.** A foreign worker cannot be insured in an
  Israeli pension fund, so there is no fund to remit it to. The employer OWES the amount at the
  end of employment; withholding it from wages is an unlawful deduction, and unlawful deduction
  is a criminal offence rather than a civil dispute.
- **Housing and utility deductions DO apply to a live-in caregiver in the patient's own home.**
  An earlier version of this skill said they generally do not. They do, at the reduced
  employer-owned-housing rate, plus a utilities line written specifically for this worker. See
  Step 4a, and note the 25% overall cap and that an un-taken deduction cannot be taken later.
- **Check the havraa tariff every time.** It resets annually and the update can be published
  mid-year with retroactive effect: the 2026 tariff moved from 418 to 451.50 NIS on 18.08.2026,
  reaching back to 1.7.2025, with a duty to pay differentials on havraa already paid.
- **Read the right benefit column.** Bituach Leumi publishes separate maximum amounts for
  employing a foreign versus an Israeli caregiver, diverging from level 3, and 6,448 NIS appears
  in both at different levels.
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
| Recuperation pay (Kol Zchut) | https://www.kolzchut.org.il/he/דמי_הבראה | The CURRENT havraa tariff and days by seniority. It resets annually and can be updated mid-year with retroactive effect, so read it every time |
| Permitted deductions (Kol Zchut) | https://www.kolzchut.org.il/he/ניכויים_מותרים_משכר_עובד_זר | The 25% overall cap, the medical-insurance cap for a nursing worker, the prohibition on deducting National Insurance, and the no-retroactive-deduction rule |
| Housing and utilities deduction (Kol Zchut) | https://www.kolzchut.org.il/he/ניכוי_הוצאות_מגורים_לעובד_זר | The regional accommodation table, the half rate where the housing is the employer's own, and the utilities line for a caregiver living in the employer's home |
| In lieu of pension (Kol Zchut) | https://www.kolzchut.org.il/he/תשלומים_במקום_ביטוח_פנסיוני_לעובד_זר_בסיעוד_שמועסק_בבית_המטופל | That a foreign worker cannot be insured in an Israeli pension fund, and the 12.5% / 8.33% + 6.5% split with the month-7 start |
| Sick days (Kol Zchut) | https://www.kolzchut.org.il/he/דמי_מחלה | Accrual and the 0/50/full payment ladder |
| Annual leave, 6-day week (Kol Zchut) | https://www.kolzchut.org.il/he/חישוב_מספר_ימי_החופשה_השנתית_לעובדים_במקומות_עבודה_שבהם_מונהג_שבוע_עבודה_בן_6_ימים | Vacation days by seniority |
| Employment permit (Kol Zchut) | https://www.kolzchut.org.il/he/קבלת_היתר_להעסקת_עובד_זר_בסיעוד | Eligibility groups and the permit process |
| Long-term-care benefit (Bituach Leumi) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/ovedZar.aspx | Benefit levels, amounts, direct vs care-company |

## Troubleshooting

### Error: "The cost looks too high / too low"
Cause: A component was applied wrong. The usual suspects: havraa treated as zero in year one, the 6.5% in-lieu-of-pension charged from month 1 instead of month 7, a 20% supplement, the deposit fund, a stale havraa tariff, or the Israeli-caregiver benefit column.
Solution: Re-check Steps 4 to 7. havraa accrues from month 1 and is paid at 12 months retroactively to day one, at 451.50 for havraa-year 2026; the 6.5% starts in month 7; there is no statutory +20%; a private household in the nursing sector does not deposit; and the level-5 foreign-caregiver benefit is 5,456, not 6,448.

### Error: "Which minimum wage figure is current?"
Cause: Minimum wage updates on a set date and stale figures circulate.
Solution: Use 6,443.85 NIS/month (35.40 NIS/hour) from 01.04.2026, and confirm against the Kol Zchut minimum-wage page before quoting for back-pay.

### Error: "Is this for a caregiver from a care company too?"
Cause: The obligations differ when the company is the employer.
Solution: This skill covers the private home employer. If a care company employs the worker, the company carries the deposit and payroll duties instead.
