---
name: israeli-elder-care-navigator
description: "Navigate the Israeli elder care system: long-term care benefits from Bituach Leumi (gimlat siud), private nursing care insurance (bituach siudi), old-age pension (kiztavat zikna), nursing homes (beit avot), home care (tipul bayit), assisted living (diur mugan), and enduring power of attorney (yipuy koach mitmashech). Use when user asks about caring for aging parents, siudi insurance, long-term care hours, nursing home costs, retirement pension amounts, guardian appointment (apotropus), or elderly rights in Israel. Helps the sandwich generation make informed decisions about elder care. Do NOT use for general Bituach Leumi benefits (use israeli-bituach-leumi), private pension funds or keren hishtalmut (use israeli-pension-advisor), or health insurance and HMO questions (use israeli-hmo-navigator)."
license: MIT
---

# Israeli Elder Care Navigator

## Problem

Adult children in Israel often face elder care decisions suddenly, with no preparation and no single source of truth. The system is split between Bituach Leumi (long-term care benefit), the Health Ministry (nursing home licensing), kupot cholim (siudi insurance), the courts (guardianship), and PIBA (foreign caregiver permits). Most families don't know the difference between gimlat siud (government benefit) and bituach siudi (private insurance), that siudi premiums are cheapest before age 49, that Holocaust survivors have extra Claims Conference benefits, that gimlat siud can be taken as cash since the 2018 reform, or that subsidised institutional care is means-tested on the children too. By the time a parent needs care, it's too late to plan.

## Instructions

### Step 1: Assess the Situation

Determine which aspect the user needs:

| Situation | Relevant Steps |
|-----------|----------------|
| Parent is aging but independent | Steps 2 (pension), 6 (POA), 7 (assisted living) |
| Parent needs help with daily activities | Steps 3 (Bituach Leumi long-term care), 4 (siudi insurance) |
| Parent needs full-time nursing care | Steps 5 (nursing homes), 3 (government benefit) |
| Planning ahead for aging parents | Steps 4 (siudi insurance), 6 (POA), 2 (pension) |
| Parent lost mental capacity, no POA | Step 6 (guardianship/apotropus) |

### Step 2: Old-Age Pension (Kiztavat Zikna)

**Paid by Bituach Leumi to residents who reached retirement age.**

Retirement age (2026):
- Men: 67
- Women: 63 in 2026 (born 1962). Born 1963 reach retirement at 63 years 3 months, then +3 months per year until those born 1970 reach 65. Phasing per the 2021 reform that replaced the old age-62 baseline. Women born before 1962 reached retirement age under that earlier baseline and are already retired; check the individual cohort against the Bituach Leumi schedule rather than the phase-in table.

Monthly pension amounts (January 2026):

| Status | Amount | Notes |
|--------|--------|-------|
| Individual (up to age 80) | 1,838 NIS | Basic pension |
| Individual age 80+ | 1,941 NIS | Includes age 80 supplement of 103 NIS |
| Couple base (one earner) | 2,762 NIS | Individual + spouse supplement |
| Spouse supplement | 924 NIS | For dependent spouse |
| Child supplement | 581 NIS | Per child, first 2 only |
| Seniority supplement | up to +50% of the basic pension | 2% per insured year, paid for up to 25 years |
| Deferral increment | +5% per deferred year | Of the full pension including the seniority supplement, for each year between retirement age and eligibility age in which payment was deferred because of work income. Ask anyone who kept working past 67. |
| Health insurance deduction | -237 NIS | Individual |
| Health insurance deduction | -340 NIS | Couple |

**Income test:** Until age 70, pension is means-tested based on income from work. After 70, everyone receives the pension regardless of income.

**Income supplement (hashlamat hachnasa):** Low-income elderly may qualify for a supplement that tops income up to a minimum level. The ceilings are set **per income type**, not as one household figure (2026):

| Income source | Individual | Couple |
|---|---|---|
| BL pension only (old-age and/or survivors) | 4,375 NIS | 6,912 NIS |
| From work | 3,236 NIS | 3,786 NIS |
| From an occupational pension | 1,790 NIS | 2,823 NIS |

Above the work ceiling, 60% of the excess is deducted from the supplement. Kibbutz and moshav shitufi members are not eligible. Apply through Bituach Leumi.

The amount the supplement tops the household up TO is a separate table that varies by household composition and by age band (individual 4,375 NIS up to 70, 4,418 at 70-80, 4,460 at 80+). Rows also exist for a couple and for either status plus one or two children. Full table in `references/elder-care-benefits.md`. Never quote the individual figure to a household with children.

**Free public transport from age 67:** Since April 2025, citizens aged 67+ ride all public transport free with a Rav-Kav loaded with the "Zahav-Kav" (gold profile). Women aged 62-67 get 50% discount. Setup: upload ID + sefach to the Rav-Kav profile.

### Step 3: Long-Term Care Benefit from Bituach Leumi (Gimlat Siud)

This is a **government benefit** (not insurance). It provides home care hours for elderly who need help with daily activities (ADL).

**Eligibility:**
- Reached retirement age (67 men, 63 women in 2026, phasing to 65 by 2032)
- Lives at home (not in a nursing institution)
- Needs assistance with daily activities (bathing, dressing, eating, mobility, personal hygiene)
- Passes an ADL assessment by a Bituach Leumi assessor
- Passes the means test (see below)

**Benefit levels (weekly home care hours, based on ADL assessment score):**

| Level | ADL Points | Hours/Week | With Foreign Worker | Max hours convertible to cash |
|-------|-----------|------------|---------------------|-------------------------------|
| Level 1 | 2.5-3 | 5.5 hours | 5.5 hours | see the Level 1 election below |
| Level 2 | 3.5-4.5 | 10 hours | 10 hours | 4 |
| Level 3 | 5-6 | 17 hours | 14 hours | 4, or 6 with social worker approval |
| Level 4 | 6.5-7.5 | 21 hours | 18 hours | 4, or 7 with social worker approval |
| Level 5 | 8-9 | 26 hours | 22 hours | 4, or 9 with social worker approval |
| Level 6 | 9.5-10.5 | 30 hours | 26 hours | 4, or 10 with social worker approval |

**Reduced (50%) benefit:** anyone above the full-benefit income band but under the cut-off receives **half the units at every level, in every option**. A level 6 recipient on the reduced rate gets 15 hours (13 with a foreign worker), not 30.

**Level 1 is a four-way election, not a flat 5.5 hours.** A level 1 recipient chooses one of: 5.5 weekly hours of personal home care; services worth **9 service units** that exclude personal home care (day centre, supportive community, absorbent products, panic button, laundry); the whole benefit as cash at 1,705 NIS/month; or a mix of cash and services worth 5.5 units.

Day centre converts per level (level 1: one day = 2 units; level 6: 2.45 units). Weekly caps and pre-2018 grandfathering: `references/elder-care-benefits.md`.

**Cash benefit option (kitzva b'kesef):** Since the 2018 reform, part of the benefit can be taken as monthly cash instead of caregiving hours. **The conversion is capped: at levels 2 to 6 you may convert up to 4 weekly hours, or up to a third of your hours with the approval of a Bituach Leumi social worker.** Taking the benefit entirely as cash is possible only at level 1, or where a live-in caregiver is employed on the terms below, or by exception (see below). The table shows the maximum cash payable in the live-in-caregiver case (from April 2026):

| Level | Max Cash (Foreign Worker) | Max Cash (Israeli Worker) |
|-------|---------------------------|---------------------------|
| 1 | 1,705 NIS | 1,705 NIS |
| 2 | 2,480 NIS | 2,480 NIS |
| 3 | 3,472 NIS | 4,216 NIS |
| 4 | 4,464 NIS | 5,208 NIS |
| 5 | 5,456 NIS | 6,448 NIS |
| 6 | 6,448 NIS | 7,440 NIS |

Hour-to-cash conversion rate (April 2026): 310 NIS/hour for Level 1, 248 NIS/hour for Levels 2-6. Full cash requires a documented full-time caregiver (12+ hours/day, 6 days/week, non-family member, written contract). Where personal care at home is impossible because of the elder's distress, full cash can be requested by exception with medical documents, on **\*2637**.

Mixed packages are allowed: at Level 3 you can take 13 hours/week + 992 NIS cash instead of 17 hours. Full-cash recipients may still add a day centre, panic button, absorbent products and laundry. Choose on **\*2637** (Sun-Thu 08:00-17:00) or in the BL service-basket calculator, changeable any time.

**Means test (mivchan hachnasot).** Income is averaged over the three months before the claim, and the thresholds depend on the month the claim is filed. Filing April to December 2026:

| Family status | Full benefit | Reduced (50%) | No benefit |
|---|---|---|---|
| Individual | up to 13,769 NIS | 13,769 to 20,654 NIS | above 20,654 NIS |
| Couple | up to 20,654 NIS | 20,654 to 30,980 NIS | above 30,980 NIS |
| Add per child | up to 6,885 NIS | 6,885 to 10,327 NIS | |

**Couples get the full benefit up to 1.5x the individual threshold, not the individual figure.** January, February and March each have their own slightly lower ceilings. See `references/elder-care-benefits.md` for all four monthly bands. Half benefit pays half the units, or 829 NIS at Level 1 and 3,618 NIS at Level 6 if taken as cash.

**Income NOT counted:** private siudi payouts, mobility allowance, attendance allowance (shirutim meyuchadim), child allowances, and every Holocaust survivor payment (Finance Ministry rente, Claims Conference Article 2, ZRBG, French and Dutch).

**Expenses deducted:** court-ordered alimony; rent paid (including in diur mugan) up to the rent received; the cost of maintaining a spouse, parent or child in an institution.

If **both spouses** qualify for the benefit, each is assessed as an individual on half the joint income.

**What the benefit provides:** personal care at home, adult day centre (merkaz yom), laundry at designated facilities, absorbent products, emergency button, and supportive-community services. Full list in `references/elder-care-benefits.md`.

**Important:** the benefit is for people living in the community, and it never covers a live-in caregiver's full salary. It provides agency hours, or cash that offsets part of the salary.

**Moving into a facility does not automatically end the benefit.** Diur mugan is fine. For a beit avot, the National Labour Court held that a supervised beit avot is not automatically a "nursing institution" under section 227(a) and that BL must examine each case rather than apply a blanket rule, so a resident of a support or independent wing can keep the benefit (Nat. Labour Court, avl 33417-10-12). Only genuine placement in a nursing institution or nursing ward ends it.

**Hospitalisation:** a recipient admitted to a general hospital keeps the caregiver at the hospital for the **first 30 days**. After a longer stay, or after discharge from a nursing institution, eligibility is **restored as it was before admission**, with no condition on how long the stay lasted.

**Application:** Bituach Leumi, *6050 or a local branch. An assessor visits to evaluate functional level. Decision typically 30-60 days.

### Step 4: Private Nursing Care Insurance (Bituach Siudi)

This is **private insurance**, most commonly purchased through the kupat cholim (HMO), NOT through Bituach Leumi.

**Key facts:**
- Purchased through the kupot cholim group plans (Clalit, Maccabi, Meuhedet, Leumit). **Standalone private policies are effectively no longer available: most insurers stopped marketing individual siudi cover in 2019**, so anyone who did not buy one by then can only insure through a kupat cholim. Do not send a user shopping for a Migdal or Harel individual policy.
- **No statutory age cap, but enrolling by age 49 guarantees maximum benefits.** Older applicants can usually still enroll, subject to medical underwriting (a pre-existing condition exam). Premiums rise sharply with age; for someone over 70 the cost may exceed the expected benefit.
- **Since December 2023, new joiners can only buy the "basic tier" (maslul bsisi).** The expanded and supplementary tiers are frozen for new enrollees through January 2028. Existing policyholders keep their tier.
- Free for minors under 18
- Pays a monthly benefit if the insured becomes dependent on help with ADL (activities of daily living)
- You can switch between kupot cholim without underwriting, waiting period, or loss of rights

**What siudi covers.** Basic tier monthly benefit, by age at joining and where the insured is (2026):

| Where the insured is | Joined by 49 | Joined 50-59 | Joined 60+ |
|---|---|---|---|
| At home | 5,000 NIS | 4,100 NIS | 3,200 NIS |
| In an institution | 10,000 NIS | 6,500 NIS | 4,500 NIS |

Four terms that decide whether the policy is worth buying:
- The benefit is paid for **5 years only**, not for life (the frozen expanded tier added 10 more).
- There is a **60-day waiting period** after becoming ADL-dependent before anything is paid.
- The institutional payout is **indemnity capped at 80% of what was actually paid** to the institution.
- The policy **excludes** nursing dependency caused by road accidents or work accidents.

It acts as a supplement to the Bituach Leumi long-term care benefit and is not counted as income in that benefit's means test.

### Step 5: Nursing Homes and Residential Care

**Types of facilities:**

| Type | Hebrew | For Whom | Cost structure |
|------|--------|----------|----------------|
| Nursing home (full care) | בית אבות סיעודי | Serious health conditions, limited mobility | Monthly fee only, no deposit |
| Retirement home | דיור מוגן (diur mugan) | Independent elderly | Large refundable deposit plus a monthly management fee |
| Assisted living | דיור מוגן עם סיוע | Semi-independent with some help | Similar to a retirement home |
| Dementia ward | מחלקת תשושי נפש | Alzheimer's, cognitive decline | Monthly fee, the most expensive option |

Prices vary sharply by region, so take current figures from the facility. Ask for the full monthly fee, deposit refund terms, and what is charged extra.

**Government-subsidized placement ("code" / tzofan):**
- Apply to the district health office (lishkat habriut), not only local social services. A nurse or social worker visits within 14 working days of a complete file, then a classification committee (vaadat siyug) decides "siudi", "tashush nefesh", or other. The Ministry of Welfare handles "frail" (tashush) elderly.
- **The co-payment is means-tested on the elder, their spouse, AND their adult children** (from age 21). Each child files a sworn declaration signed before a lawyer or court clerk, disclosing income, savings, deposits and any private siudi policy. Governing rule: MoH circular 08/2018, still operative.
- **How much a child pays is a credit-point lookup, not a percentage of income.** Per-capita income after the housing deduction is expressed in income-tax credit points, looked up in the circular's charging table, then multiplied by 125%. The full table, the housing deduction, the excluded income, the family cap, the 37% floor and the kibbutz and welfare tracks are in `references/institutional-copayment.md`. Size it with the official calculator at https://me.health.gov.il/nursing-calculator/ .
- **The parent's home is not shielded.** Rent from it is charged as part of the co-payment, and where the property cannot be let a charge for six months' cost is registered against it in favour of the Ministry of Health. Details in the reference.
- **Two figures you must not guess.** Pocket money (demei kis) has no published shekel amount; it comes from the Bituach Leumi benefit-splitting regulations. And there is no national monthly tariff: "full actual cost" is per institution under its own MoH agreement, so ask the district health office treasury.
- Appeal the classification in writing to the committee, then to the Head of the Geriatrics Division at the MoH (\*5400).
- A classification expires if the elder is not admitted within 3 months.
- Verify the facility's MoH licence first. Waiting lists are long, especially in central Israel.

### Step 5b: Foreign Caregivers (Ovedet Zara)

Many families employ a live-in foreign caregiver instead of, or in addition to, a nursing home or gimlat siud hours.

**Permit requirement:** You need a permit (heter ha'asaka) from the Population and Immigration Authority (PIBA / Rashut Ha'ochlosin). The permit is granted to people who need assistance or supervision most hours of the day and are not in an institutional setting. The Bituach Leumi ADL assessment is typically what unlocks the permit.

**Minimum wage (April 2026):** 6,443.85 NIS/month gross for a full 24/6 position (daily rate 257.75 NIS, hourly 35.40 NIS). On top of the gross salary, budget for social benefits, pension and severance reserves, and for topping the post up to a full week if the caregiver comes through a siud company. Room and board are provided in kind.

**Gimlat siud interaction:** If you employ a foreign caregiver, the cash benefit at Level 3+ is reduced (see the "with foreign worker" column in Step 3). Caregiver-fee scales also reduce some agency-hour benefits.

**Where to find a worker:** Through licensed manpower companies (lishkat ha'asaka prati be'siyud) authorized by PIBA. Direct hiring of someone already legally in Israel is allowed with proper paperwork.

### Step 6: Power of Attorney and Guardianship

**Enduring Power of Attorney (Yipuy Koach Mitmashech):**

This is the preferred option. Set it up BEFORE the parent loses capacity.

- Allows the parent to appoint someone to manage their affairs if they lose mental competence
- **Must be registered with the Apotropus Haklali (Administrator General).** Without registration, it's not legally valid
- Covers three areas: personal matters, medical matters, property/financial matters
- Must be drafted by a lawyer who has completed special training
- The appointed person (memunaneh) only steps in when the parent loses capacity

**Guardianship (Apotropsut):**

This is the fallback when no POA exists and the person has already lost capacity.

- Court-appointed (through the Family Court)
- The court appoints an apotropus (guardian) to manage the person's affairs
- The guardian must report to the court on decisions
- More restrictive and less flexible than a POA
- Can be for personal matters, property, or both
- Application through a lawyer, with involvement of the Apotropus Haklali

**Recommendation:** Always encourage families to set up an enduring POA while the parent is still competent. Court-appointed guardianship is slower, more expensive, and less respectful of the parent's wishes.

### Step 6b: Advance Medical Directives (Hok HaCholeh HaNote LaMut)

Israel's Terminally Ill Patient Law (2005) lets adults specify in advance what medical care they accept or refuse if they are declared a terminally ill patient (life expectancy under 6 months, even with treatment) and lose decision-making capacity.

**Two tools, often filed together:**
- **Hanchayot refuiyot mukdamot** (advance medical directives): you write what care you want or refuse.
- **Yipuy koach refuei** (medical power of attorney under this law): you appoint a person to make decisions for you. This is different from the general yipuy koach mitmashech in Step 6, though many people sign both.

**Filing:** Submit to the Center for Advance Medical Directives at the Ministry of Health. Forms are available at `gov.il/he/service/dying-patient-request`. Valid for 5 years and renewable. Anyone aged 17+ who is lucid can file.

**Hospice care (tipul tomech / hospice):** Available at home (hospice bayit) or in inpatient hospice units. Covers pain management, psychological and spiritual support. Covered under the basic basket (sal briut) when the person is medically classified as terminally ill. Each kupat cholim has a designated hospice referral pathway.

### Step 6c: Equipment, Emergency, and Support Services

**Yad Sarah** (national volunteer organization, *6444 or 02-6444444), 127 branches, no income test:
- Medical equipment loans (walkers, wheelchairs, oxygen machines, hospital beds, bath chairs), free or against a nominal deposit
- Emergency button (lachtzan mitzuka), 24/7 monitored, from ~18 NIS/month
- Loneliness-prevention visits

**Ezer Mizion** (volunteer transport): free or low-cost transport to medical appointments. Arrange at least 30 minutes ahead, ideally days.

**Eshel - JDC Israel** (02-655-7400): community elder care programs, supportive community (kehila tomechet).

### Step 6d: Holocaust Survivors and Special Populations

Many Israeli elders are Holocaust survivors (nitzolei sho'ah), entitled to benefits families often miss:

- **Claims Conference Article 2 Fund (Keren Sa'if 2):** monthly pension for survivors persecuted under the Nazi regime, paid every 3 months, on German government criteria.
- **Annual grant (Claims Conference Hardship Fund):** €1,350/year for survivors without monthly Section 2 payments.
- **Israeli Ministry of Finance supplements (Rashut Lezchuyot Nitzolei HaShoah):** Israeli residents receiving Article 2 Fund payments get a further Israeli supplement, up to the level paid to disabled victims of Nazi persecution (tagmul lefi hachnasa).
- **Free dental and additional medical care.**

Survivors who never claimed may still be eligible. Refer the family to the Holocaust Survivors' Rights Authority (Rashut Lezchuyot Nitzolei HaShoah).

**Russian-speaking elders:** many Bituach Leumi, kupat cholim and Misrad HaBri'ut documents exist in Russian. Eshel and the Ministry of Aliyah and Integration offer Russian-language elder care navigators. Aliyah-related benefits may still apply.

### Step 7: Planning Ahead

Key milestones and deadlines for elder care planning:

| Age | Action |
|-----|--------|
| Any adult age | Enduring power of attorney (yipuy koach mitmashech), plus advance medical directives and the medical POA under the Terminally Ill Patient Law |
| Before age 49 | Enroll in siudi insurance through kupat cholim to lock in maximum benefits and the lowest premium |
| 62-67 | Check old-age pension eligibility with Bituach Leumi (early retirement option) |
| 67 (men) / 63-65 (women, by birth year) | Apply for the Zahav-Kav (free public transport from 67) and full old-age pension |
| When ADL decline begins | Apply for long-term care benefit (gimlat siud) from Bituach Leumi |
| When home care is insufficient | Research nursing homes and assisted living, and size the family co-payment before applying for a code |
| If Holocaust survivor | Check Claims Conference Article 2 Fund + Rashut Lezchuyot Nitzolei HaShoah benefits |

## Examples

### Example 1: Planning for Aging Parents
User says: "My parents are in their 60s and still healthy. What should we do now to prepare?"
Actions:
1. Check for siudi insurance. If none, get a quote but run the cost/benefit: joining in their 60s means a high premium for a limited benefit. Do not answer with a generic "yes, buy it"
2. Set up enduring power of attorney for both while they're competent, plus advance medical directives and the medical POA under Hok HaCholeh HaNote LaMut
3. Review old-age pension eligibility with Bituach Leumi (men 67, women born 1962 retire at 63), and the Zahav-Kav from 67
4. If Holocaust survivors, check Article 2 Fund eligibility
5. Discuss their preferences for future care (home vs. facility)
Result: Family has a plan before a crisis hits.

### Example 2: Parent Needs Daily Help
User says: "My mother is 75 and can't bathe or dress herself anymore"
Actions:
1. Apply for gimlat siud (long-term care benefit) from Bituach Leumi by calling *6050
2. An assessor will visit to evaluate her ADL level
3. Based on level (1-6), she'll receive 5.5-30 hours/week of home care
4. Check if she has siudi insurance through her kupat cholim for additional monthly benefit
5. If home care isn't enough, research nursing homes and check for Ministry of Health subsidized placement
Result: Mother receives appropriate care support.

### Example 3: Emergency Guardianship
User says: "My father had a stroke and can't make decisions. He never set up power of attorney."
Actions:
1. Explain that court-appointed guardianship (apotropsut) is needed, filed through a lawyer at the Family Court with the Apotropus Haklali involved
2. Apply in parallel for gimlat siud if he needs daily care assistance
3. Emphasize this takes time. For urgent medical decisions, consult the hospital social worker
Result: Family understands the legal process and immediate care options.

## Bundled Resources

### References
- `references/elder-care-benefits.md`. Detailed breakdown of Bituach Leumi long-term care benefit levels, old-age pension amounts, and eligibility criteria.
- `references/institutional-copayment.md`. How the family's co-payment for subsidised institutional care is computed: the credit-point charging table for adult children, the housing deduction, excluded income, the family cap and the 37% floor.
- `references/housing-options.md`. Comparison of nursing homes, assisted living, and retirement homes with cost ranges and what to look for.

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [Kolzchut (All-Rights)](https://agentskills.co.il/en/mcp/kolzchut) | Israel's authoritative rights knowledge base: elder care rights, eligibility, procedures |
| [IL Health](https://agentskills.co.il/en/mcp/il-health) | MoH data on hospital quality, health funds, elder services |

## Gotchas

1. **Gimlat siud vs. bituach siudi: two completely different things.** Agents routinely confuse these. Gimlat siud is a government benefit from Bituach Leumi providing home care hours. Bituach siudi is private insurance purchased through kupot cholim providing money. They are from different systems, have different eligibility rules, and can be received simultaneously.

2. **Siudi insurance has no hard age cap, but age 49 is the practical deadline.** Earlier guidance circulated an "age 65 cutoff," but in fact the kupat cholim group plans accept new joiners at any age, subject to medical underwriting. The real deadline is age 49: enrolling by then guarantees the maximum benefit and the lowest premium. For someone in their 70s, the premium often exceeds the expected benefit, and underwriting may decline. Also, since December 2023, new joiners get only the "basic tier"; the expanded tier is frozen until January 2028.

3. **Women's retirement age is not 62 in 2026.** It's 63 (for women born 1962, reaching 65 by 2032 for those born 1970+). The 2021 reform gradually increases women's retirement age by 4 months/year then 3 months/year. Using 62 gives wrong eligibility dates for long-term care benefits and old-age pension.

4. **Enduring POA must be registered.** Unlike some countries where a signed POA is valid on its own, Israeli yipuy koach mitmashech must be registered with the Apotropus Haklali. An unregistered POA is not legally valid. Agents should never say "just have a lawyer draft a POA" without mentioning registration.

5. **"Moving to a facility ends the benefit" is too broad.** The benefit stops on genuine placement in a nursing institution or nursing ward, but diur mugan does not affect it, and a supervised beit avot is not automatically a nursing institution: BL must examine the specific ward and services rather than apply a blanket rule. Agents should not tell a family the benefit is lost the moment a beit avot is mentioned, and should not tell them it is lost during a hospital stay (the first 30 days are covered, and eligibility is restored on discharge).

6. **Holocaust survivors often miss benefits they're entitled to.** Many survivors never claimed Article 2 Fund or the Israeli Ministry of Finance supplement (tagmul lefi hachnasa). If the elderly person was in Europe during 1939-1945, in a ghetto, in hiding, or fled, check eligibility with the Rashut Lezchuyot Nitzolei HaShoah and the Claims Conference. Family members can apply on behalf of the elder.

7. **Free public transport for elderly is a 2025 change, not 2026.** Since April 25, 2025, citizens 67+ ride all public transport (buses, trains, light rail) for free with a Zahav-Kav loaded Rav-Kav. Some agents still cite the old 50% discount. Women 62-67 still get only 50%.

8. **Yipuy koach mitmashech is not the same as the medical POA under Hok HaCholeh HaNote.** The general yipuy koach mitmashech (Step 6) covers ongoing affairs once capacity is lost. The medical POA under the Terminally Ill Patient Law (Step 6b) covers only the end-of-life scenario after a 6-months-to-live diagnosis. People often sign both.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Bituach Leumi (Long-Term Care) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/default.aspx | Eligibility, application |
| Bituach Leumi (Cash benefit option) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/money.aspx | Cash amounts, conversion rates |
| Bituach Leumi (benefit levels 1-6) | https://www.btl.gov.il/benefits/Long_Term_Care/benefit_level/Pages/level1.aspx | Hours and cash caps per level (level1 to level6) |
| Bituach Leumi (siud income test) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/income.aspx | Income bands by filing month |
| Bituach Leumi (Old-Age Pension) | https://www.btl.gov.il/benefits/old_age/Pages/default.aspx | Amounts, retirement age, income test |
| Bituach Leumi (pension supplements) | https://www.btl.gov.il/benefits/old_age/Shum/Pages/Tosafot.aspx | Seniority and deferral increments |
| Bituach Leumi (income supplement amounts) | https://www.btl.gov.il/benefits/old_age/hashHachZ/Pages/schumim.aspx | Guaranteed amount by household and age |
| MoH circular 08/2018 (co-payment) | https://www.gov.il/he/pages/mk08-2018 | Family's share of institutional care cost |
| MoH nursing-code calculator | https://me.health.gov.il/nursing-calculator/ | Estimate of the family co-payment |
| Ministry of Health (Elder Services) | https://www.gov.il/he/departments/ministry_of_health/govil-landing-page | Nursing home licensing, placement codes |
| Kolzchut (Siudi insurance) | https://www.kolzchut.org.il/he/ביטוח_סיעודי_קבוצתי_אחיד_של_קופות_החולים | Unified group siudi plan rules |
| Kolzchut (Elderly Rights) | https://www.kolzchut.org.il/he/קשישים | Rights guide for elderly in Israel |
| Apotropus Haklali (POA) | https://www.gov.il/he/service/edit_and_deposit_continuous_power_of_attorney | POA registration |
| Ministry of Health (Advance Directives) | https://www.gov.il/he/service/dying-patient-request | Hok HaCholeh HaNote forms |
| PIBA (Foreign Caregiver Permits) | https://www.gov.il/he/service/nursing_foreign_worker | Caregiver employment permit |
| Claims Conference Article 2 Fund | https://www.claimscon.org/what-we-do/compensation/background/article2/ | Survivor monthly pension |
| Rashut Lezchuyot Nitzolei HaShoah | https://www.gov.il/he/departments/holocaust-survivors-rights | Israeli survivor supplements |
| Yad Sarah | https://yad-sarah.net | Equipment loans, emergency button |
| Women's retirement age schedule | https://www.gov.il/he/pages/women_retirement_age_news | Retirement age by birth year |

## Troubleshooting

### Problem: "Bituach Leumi denied the long-term care benefit"
Cause: The ADL assessment scored the person below the threshold for eligibility.
Solution: Families can request a reassessment. Prepare by documenting the person's worst days, not their best. Have the family doctor write a detailed letter. Consider hiring an occupational therapist to prepare a functional assessment. Appeal through Bituach Leumi's appeals process.

### Problem: "Parent is over 65 and has no siudi insurance"
Cause: Premiums are now high and benefits are reduced because they didn't lock in early. Underwriting may also be a problem if there are pre-existing conditions.
Solution: Check whether enrollment is still worthwhile (it usually is not after age 70, since the premium often exceeds the expected benefit). Focus instead on maximizing the Bituach Leumi long-term care benefit (gimlat siud) including the cash option. Check the Ministry of Health for subsidized nursing home placement. For Holocaust survivors, check Article 2 Fund payments as a partial substitute.

### Problem: "Nursing home costs exceed the family budget"
Cause: Private nursing home fees are the largest recurring cost most families ever face, and a dementia ward costs more than a standard nursing ward.
Solution: Apply for a subsidized placement through the Ministry of Health (code/tzofan). Check if the parent qualifies for income supplement from Bituach Leumi. The Ministry of Welfare assists "frail" elderly through local social services. Some families combine gimlat siud home care hours with family caregiving to avoid nursing home costs.
