---
name: israeli-elder-care-navigator
description: "Not legal advice and not a determination of your benefit eligibility. Navigate the Israeli elder care system: long-term care benefits from Bituach Leumi (gimlat siud), private nursing care insurance (bituach siudi), old-age pension (kiztavat zikna), nursing homes (beit avot), home care (tipul bayit), assisted living (diur mugan), and enduring power of attorney (yipuy koach mitmashech). Use when user asks about caring for aging parents, siudi insurance, long-term care hours, nursing home costs, retirement pension amounts, guardian appointment (apotropus), or elderly rights in Israel. Helps the sandwich generation make informed decisions about elder care. Do NOT use for general Bituach Leumi benefits (use israeli-bituach-leumi), private pension funds or keren hishtalmut (use israeli-pension-advisor), or health insurance and HMO questions (use israeli-hmo-navigator)."
license: MIT
---

# Israeli Elder Care Navigator

## Legal notice

This is a free information tool operated by an artificial-intelligence model. It explains the published rules of Israel's elder care system: Bituach Leumi benefits, the Ministry of Health co-payment for institutional care, kupat cholim siudi insurance, foreign-caregiver permits, and the legal-capacity instruments. All of its output is produced automatically, without the involvement, review or approval of a lawyer or a social worker. It is not legal advice, and it does not determine eligibility, a benefit level or a co-payment: Bituach Leumi, the Ministry of Health and the court decide those. An AI model may err or quote a superseded figure, so confirm every amount on the official page before relying on it.

Do not rely on the output to sign a power of attorney, to file a guardianship application, or in an appeal or other legal proceeding; consult a lawyer first. This tool is not a substitute for advice that takes into account the particular data and needs of each person. Any use of the output is at the user's sole responsibility.

## Problem

Adult children often face elder care decisions suddenly, with no single source of truth. The system is split between Bituach Leumi (long-term care benefit), the Health Ministry (nursing home licensing), kupot cholim (siudi insurance), the courts (guardianship), and PIBA (foreign caregiver permits). Most families don't know the difference between gimlat siud (government benefit) and bituach siudi (private insurance), that siudi premiums are cheapest before age 49, that Holocaust survivors get extra care hours, that gimlat siud can be taken partly as cash, or that subsidised institutional care is means-tested on the children too.

## Instructions

### Step 1: Assess the Situation

| Situation | Relevant Steps |
|-----------|----------------|
| Parent is aging but independent | Steps 2 (pension), 6 (POA), 7 (planning) |
| Parent needs help with daily activities | Steps 3 (Bituach Leumi long-term care), 4 (siudi insurance) |
| Parent is in hospital after a stroke or fall | Step 3 (file from the ward), Step 5b (permit), Step 6 (capacity) |
| Parent needs full-time nursing care | Steps 5 (nursing homes), 3 (government benefit) |
| Parent lost capacity, no POA | Step 6 (least restrictive route first) |

### Step 2: Old-Age Pension (Kiztavat Zikna)

**Paid by Bituach Leumi to residents who reached retirement age.**

Retirement age (2026):
- Men: 67
- Women: set by birth date, not by calendar year. Born 1962: 63. Born 1963: 63 years and 3 months, so a woman turning 63 this year has **not** yet reached retirement age. Then +3 months per birth year; born 1970 or later: 65. Compute from the exact date of birth against the Bituach Leumi table.

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
| Health insurance deduction | -237 NIS / -340 NIS | Individual / couple; -123 NIS for an income-supplement recipient |

**Income test:** Until age 70, pension is means-tested based on income from work. After 70, everyone receives the pension regardless of income.

**Income supplement (hashlamat hachnasa):** Low-income elderly may qualify for a supplement. The ceilings are set **per income type**, not as one household figure (2026):

| Income source | Individual | Couple |
|---|---|---|
| BL pension only (old-age and/or survivors) | 4,375 NIS | 6,912 NIS |
| From work | 3,236 NIS | 3,786 NIS |
| From an occupational pension | 1,790 NIS | 2,823 NIS |

Above the work ceiling, 60% of the excess is deducted. Kibbutz and moshav shitufi members are not eligible. The amount the supplement tops the household up TO varies by household composition and age band; full table in `references/elder-care-benefits.md`. Never quote the individual figure to a household with children.

**Free public transport from age 67:** since April 2025, with a Rav-Kav on the senior profile. Women aged 62-67 get 50%.

### Step 3: Long-Term Care Benefit from Bituach Leumi (Gimlat Siud)

This is a **government benefit** (not insurance). It provides home care for people past retirement age who need help with daily activities (ADL).

**Eligibility:**
- Reached retirement age (men 67; women by birth date, Step 2)
- Lives at home: not in a nursing, complex-nursing, dementia or long-term ventilation ward, nor in a MoH-supervised rehabilitation setting
- Needs assistance with daily activities (bathing, dressing, eating, mobility, personal hygiene)
- Passes the dependency (ADL) assessment and the means test (see below)
- Does not receive a benefit that must be chosen instead (see "Cannot be stacked" below)

**Benefit levels (weekly home care hours, based on the ADL score):**

| Level | ADL Points | Hours/Week | With Foreign Worker | Max hours convertible to cash |
|-------|-----------|------------|---------------------|-------------------------------|
| Level 1 | 2.5-3 | 5.5 hours | 5.5 hours | see the Level 1 election below |
| Level 2 | 3.5-4.5 | 10 hours | 10 hours | 4 |
| Level 3 | 5-6 | 17 hours | 14 hours | 4, or 6 with social worker approval |
| Level 4 | 6.5-7.5 | 21 hours | 18 hours | 4, or 7 with social worker approval |
| Level 5 | 8-9 | 26 hours | 22 hours | 4, or 9 with social worker approval |
| Level 6 | 9.5-10.5 | 30 hours | 26 hours | 4, or 10 with social worker approval |

**Reduced (50%) benefit:** anyone above the full-benefit income band but under the cut-off receives **half the benefit at every level, in every option**. A level 6 recipient on the reduced rate gets 15 hours (13 with a foreign worker), not 30.

**Level 1 is a four-way election, not a flat 5.5 hours.** A level 1 recipient chooses one of: 5.5 weekly hours of personal home care; services worth **9 service units** that exclude personal home care (day centre, supportive community, absorbent products, panic button, laundry); the whole benefit as cash at 1,708 NIS/month; or a mix of cash and services worth 5.5 units.

Day centre converts per level (level 1: one day = 2 units; level 6: 2.45 units). Weekly caps and pre-2018 grandfathering: `references/elder-care-benefits.md`.

**Cash option (kitzva b'kesef).** Part of the benefit can be taken as monthly cash. **The conversion is capped: at levels 2 to 6 you may convert up to 4 weekly hours, or (levels 3 to 6) up to a third of your hours with the approval of a Bituach Leumi social worker.** The whole benefit as cash is possible only at level 1, where a live-in caregiver is employed on the terms below, or by exception. Maximum cash in the live-in-caregiver case (amounts re-rated **from 01.08.2026**):

| Level | Max Cash (Foreign Worker) | Max Cash (Israeli Worker) |
|-------|---------------------------|---------------------------|
| 1 | 1,708 NIS | 1,708 NIS |
| 2 | 2,484 NIS | 2,484 NIS |
| 3 | 3,478 NIS | 4,223 NIS |
| 4 | 4,471 NIS | 5,217 NIS |
| 5 | 5,465 NIS | 6,458 NIS |
| 6 | 6,458 NIS | 7,452 NIS |

Hour value (from 01.08.2026): 311 NIS for Level 1, 248 NIS for Levels 2-6. Full cash requires a documented full-time caregiver (12+ hours/day, 6 days/week, non-family member, written contract). Someone awaiting a PIBA humanitarian-committee decision on the permit keeps the cash until it decides. Where personal care at home is impossible because of the elder's distress, full cash can be requested by exception with medical documents, on **\*2637**.

Mixed packages: at Level 3 you can take 13 hours/week + 994 NIS cash instead of 17 hours (BTL's printed figure; quote it rather than multiplying). Full-cash recipients may still add a day centre, panic button, absorbent products and laundry. Choose on **\*2637** (Sun-Thu 08:00-17:00), changeable any time.

**Means test (mivchan hachnasot).** Income is averaged over the three months before the claim, and the thresholds depend on the month the claim is filed. Filing April to December 2026:

| Family status | Full benefit | Reduced (50%) | No benefit |
|---|---|---|---|
| Individual | up to 13,769 NIS | 13,769 to 20,654 NIS | above 20,654 NIS |
| Couple | up to 20,654 NIS | 20,654 to 30,980 NIS | above 30,980 NIS |
| Add per child | up to 6,885 NIS | 6,885 to 10,327 NIS | |

**Couples get the full benefit up to 1.5x the individual threshold.** January, February and March have their own lower ceilings; all four bands are in `references/elder-care-benefits.md`. Half benefit pays half of whatever option is chosen; do not quote a fixed shekel figure for it.

**Income NOT counted:** private siudi payouts, mobility allowance, child allowances, and every Holocaust survivor payment (Finance Ministry rente, Claims Conference Article 2, ZRBG, French and Dutch). **Expenses deducted:** court-ordered alimony; rent paid (including in diur mugan) up to the rent received; the cost of maintaining a spouse, parent or child in an institution. If **both spouses** qualify, each is assessed as an individual on half the joint income.

**Cannot be stacked:** a person receiving the attendance allowance (shirutim meyuchadim), a Treasury personal-care allowance, or a Ministry of Defence ezrat hazulat benefit must **choose** between it and gimlat siud. A first attendance-allowance claim is possible only up to half a year after retirement age. Details: `references/more-entitlements.md`.

**Holocaust survivors:** with 6+ points and a full benefit, the Holocaust Survivors' Rights Authority or the Claims Conference adds **9 weekly care hours** on top of BL's, at home only (or fixed cash if the care plan has no home-care hours). Other bands get cash, **including a survivor refused gimlat siud for scoring only 1.5 or 2 points**. Table in `references/more-entitlements.md`.

**What the benefit provides:** home care, day centre, laundry, absorbent products, emergency button, supportive community. Never a live-in caregiver's full salary.

**Moving into a facility does not automatically end the benefit.** Diur mugan is fine. The National Labour Court held that a supervised beit avot is not automatically a "nursing institution" under section 227(a) and that BL must examine each case (Nat. Labour Court, avl 33417-10-12). Only genuine placement in a nursing institution or nursing ward ends it.

**Hospitalisation:** a recipient admitted to a general hospital keeps the benefit for the **first 30 days**. After a longer stay, or after discharge from a nursing institution, eligibility is **restored as it was before admission**.

**After a stroke or fall, settle rehabilitation first.** Medical rehabilitation is a kupat cholim responsibility, recommended in the discharge letter; inpatient rehab lasts at least 25 days for neurological and 14 for orthopaedic cases. While in a MoH-supervised rehabilitation setting the benefit is not paid, so plan the caregiver around that decision. While the claim is pending, a siud company contracted with BL gives **6 free weekly hours ("trom siud")** until BL decides, for at most a month; the hospital social worker has the list. Details: `references/more-entitlements.md`.

**Filing:**
- From retirement age. Call **\*6050**, or have BL's senior-citizen volunteers on **\*9696** fill in the claim by phone with you.
- **Still in hospital:** file from the ward through the hospital social worker ("Mahlaka Rishona"), attaching the interim medical summary (sikum beinayim). Do not wait for discharge.
- **The assessment is made mainly from the documents you send** (up-to-date medical summary, discharge summaries, tests, medication list). The assessor phones to fill gaps; ask for a home visit in that call if you want one. Say if the parent lives alone: it adds points.
- Age 90+: may choose a free assessment by a hospital or public-clinic geriatrician instead; 90+ with 6 points is set at level 4 automatically.
- Re-examination after deterioration and the appeal (advisory committee **within 60 days**, or the Labour Court; the level is not reduced on appeal): `references/more-entitlements.md`.

### Step 4: Private Nursing Care Insurance (Bituach Siudi)

This is **private insurance**, most commonly purchased through the kupat cholim (HMO), NOT through Bituach Leumi.

**Key facts:**
- Purchased through the kupot cholim group plans (Clalit, Maccabi, Meuhedet, Leumit). **Standalone private policies are effectively no longer available: most insurers stopped marketing individual siudi cover in 2019.** Do not send a user shopping for a Migdal or Harel individual policy.
- **No statutory age cap, but enrolling by age 49 guarantees maximum benefits.** Older applicants can usually still enroll, subject to medical underwriting. Premiums rise sharply with age.
- **Since December 2023, new joiners can only buy the "basic tier" (maslul bsisi).** The expanded tier is frozen for new enrollees through 01.01.2028. Existing policyholders keep their tier.
- Free for minors under 18
- Pays a monthly benefit if the insured becomes dependent on help with ADL
- **Switching kupot:** cover continues without new underwriting, but the move is not automatic: the insured must show proof of prior siudi cover within 180 days of the new kupah asking for it. Kol Zchut flags that, as of 2024, Clalit members' cover may be affected on a switch; check with the insurer before moving a parent out of Clalit.

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

It supplements the Bituach Leumi benefit and is not counted as income in that benefit's means test.

### Step 5: Nursing Homes and Residential Care

Facility types (nursing home, diur mugan, assisted living, dementia ward) and their cost structures: `references/housing-options.md`. Prices vary sharply by region; ask the facility for the full monthly fee, deposit refund terms and extras.

**First, which track?** A **complex-nursing patient (siudi murkav)** is placed through the **kupat cholim**, not the health office: hospital social worker, then the kupa liaison nurse, then kupa geriatrician approval (from home: the family doctor). The co-payment is the kupa's own, and the kupa may not refuse placement because it is not yet arranged. Details: `references/institutional-copayment.md`. The code route below is for siudi and tashush nefesh.

**Government-subsidized placement ("code" / tzofan):**
- Apply to the district health office (lishkat habriut). A nurse or social worker visits within 14 working days of a complete file, then a classification committee (vaadat siyug) decides "siudi", "tashush nefesh", or other. The Ministry of Welfare handles "frail" (tashush) elderly.
- **Sources are drawn in order:** the patient's and spouse's income, then rent from their property, then their savings, and only then the adult children's income. **Savings are protected:** the patient keeps 100 credit points for last expenses, and with a spouse at home, joint savings up to 350 credit points are not touched (350 to 700: 350 stay with the spouse; above 700: half). A child living abroad is not charged.
- **The co-payment is means-tested on the elder, their spouse, AND their adult children** (from age 21). Each child files a sworn declaration signed before a lawyer or court clerk, disclosing income, savings, deposits and any private siudi policy. Governing rule: MoH circular 08/2018, still operative.
- **How much a child pays is a credit-point lookup, not a percentage of income.** Income after the housing deduction is divided by the circular's **fixed person count, not a head count** (no spouse: 3; spouse without income: 3; spouse with income: 2; +1 per child of the payer or the payer's spouse under 21 at home, or under a maintenance order; +1/4 per child aged 21-26), expressed in income-tax credit points, looked up in the circular's charging table, then multiplied by 125%. The full table, excluded income, the family cap, the 37% floor and the kibbutz and welfare tracks are in `references/institutional-copayment.md`. Size it with the official calculator at https://me.health.gov.il/nursing-calculator/ .
- **The home counts only if no spouse or dependant lives in it.** Then its rent, or its rental value from two months after admission, is charged; for a patient with no family or under a public guardian, a lien for six months' cost is registered instead. A flat gifted to a relative within 5 years makes that relative liable for its rental value.
- **Pocket money:** when the old-age pension is paid to the funding body, the resident keeps 662 NIS a month (607 NIS with income supplement) from 01.01.2026. **There is no national monthly tariff:** "full actual cost" is per institution under its own MoH agreement, so ask the district health office treasury.
- Appeal the classification in writing to the committee, then to the Head of the Geriatrics Division at the MoH (\*5400). A classification expires if the elder is not admitted within 3 months.
- Verify the facility's MoH licence first. Waiting lists are long, especially in central Israel.

### Step 5b: Foreign Caregivers (Ovedet Zara)

**Permit:** a permit (heter ha'asaka) from the Population and Immigration Authority (PIBA, \*3450), applied for online; processing takes about 14 working days. It is granted to people who need help or supervision most hours of the day and are not in an institution. The Bituach Leumi ADL assessment is typically what unlocks it, and a patient being discharged from hospital files a dedicated discharge declaration (Form E); one who needs close care for continuity may get a **temporary permit for up to 3 months** even without the general criteria, for a worker already in Israel. Fees: 370 NIS per application, plus 340 NIS for the dependency test if income rules out gimlat siud. Point thresholds and the 85+/90+ routes: `references/housing-options.md`.

**Minimum wage (April 2026):** 6,443.85 NIS/month gross for a full 24/6 position (daily 257.75 NIS, hourly 35.40 NIS). Budget on top for social benefits, pension and severance reserves, and for topping the post up to a full week if the caregiver comes through a siud company. For payroll, severance and deductions, use the `foreign-caregiver-payroll` skill.

**Gimlat siud interaction:** with a foreign caregiver, hours and cash at Level 3+ are lower (the "with foreign worker" columns in Step 3).

**Where to find a worker:** licensed private bureaus in the nursing sector, authorized by PIBA.

### Step 6: Power of Attorney, Supported Decisions and Guardianship

**Explain, never draft.** Do not draft a power of attorney, advance directives, a guardianship or supporter application, or an appeal to Bituach Leumi or the Labour Court. Explain what the instrument must contain, who signs it and where it is filed, and list the facts the user takes to the lawyer or committee.

**Enduring Power of Attorney (Yipuy Koach Mitmashech):** the preferred option, made BEFORE the parent loses capacity.

- Lets the parent appoint someone to manage personal, medical and/or property matters if they lose capacity
- **Must be deposited with the Apotropus Haklali (Administrator General).** Without it, it is not valid
- Made before a lawyer trained by the Administrator General; a **medical-only** enduring POA may instead be signed before a physician, psychologist, nurse or social worker
- The appointed person only steps in when the parent loses capacity

**Before guardianship, check the less restrictive routes.** Under the Legal Capacity and Guardianship Law (2016 amendment) a court appoints a guardian only if the purpose cannot be achieved in a less restrictive way, including a **decision-making supporter** (tomech bekabalat hachlatot), who helps the person get and understand information but does not decide for them. A stroke does not by itself remove capacity: first ask whether the parent can still sign an enduring POA or decide with support. A competent person can also deposit **advance directives naming a preferred guardian**. Details: `references/more-entitlements.md`.

**Guardianship (Apotropsut):** the fallback when no POA exists and less restrictive routes do not suffice.

- Court-appointed (Family Court), for personal matters, property, or both
- The guardian reports to the court; more restrictive and less flexible than a POA
- Application through a lawyer, with the Apotropus Haklali involved

### Step 6b: Advance Medical Directives (Hok HaCholeh HaNote LaMut)

Under the Terminally Ill Patient Law (2005) an adult can set out in advance the care they accept or refuse if declared terminally ill (life expectancy under 6 months, even with treatment) and unable to decide: **advance medical directives**, and a **medical power of attorney** under this law (different from the Step 6 enduring POA). Filed with the MoH Center for Advance Medical Directives (`gov.il/he/service/dying-patient-request`), valid 5 years, from age 17. Hospice is in the basic basket, through the kupa.

### Step 6c: Equipment, Emergency, Support and Other Entitlements

Yad Sarah equipment loans and emergency buttons, Ezer Mizion transport, Eshel community programmes, the gimlat siud certificate (escort entry; queue exemption at levels 4-6), and the arnona discount of up to 70% for gimlat siud recipients: `references/more-entitlements.md`.

### Step 6d: Holocaust Survivors and Special Populations

Holocaust survivors (nitzolei sho'ah) have benefits families often miss: the extra long-term care hours (Step 3); **up to 50 care hours over up to two months after a hospital stay** for a survivor with no siud benefit, requested only through the hospital social worker during the stay; the Claims Conference Article 2 Fund pension and annual payment (1,350 euro in 2026); and the Rights Authority supplement. Survivors who never claimed may still be eligible. Details: `references/more-entitlements.md`.

### Step 7: Planning Ahead

| Age | Action |
|-----|--------|
| Any adult age | Enduring POA, advance directives for a guardian, advance medical directives and the medical POA |
| Before age 49 | Enroll in siudi insurance through kupat cholim to lock in maximum benefits and the lowest premium |
| 62-67 | Check old-age pension eligibility with Bituach Leumi |
| Retirement age + 6 months | Last date for a first attendance-allowance claim, if already severely dependent |
| When ADL decline begins | Apply for gimlat siud |
| When home care is insufficient | Research nursing homes and size the family co-payment before applying for a code |
| If Holocaust survivor | Check the extra care hours, Article 2 Fund and Rights Authority benefits |

## Examples

### Example 1: Planning for Aging Parents
User says: "My parents are in their 60s and still healthy. What should we do now to prepare?"
Actions:
1. Check for siudi insurance. If none, run the cost/benefit: joining in their 60s means a high premium for a limited benefit. Do not answer with a generic "yes, buy it"
2. Recommend that each parent make an enduring POA before an Administrator-General-trained lawyer, and deposit it, while they are competent; plus advance medical directives
3. Review old-age pension eligibility (men 67; women by birth date, e.g. born 1963 retire at 63 and 3 months)
4. If Holocaust survivors, check Article 2 Fund eligibility
Result: Family has a plan before a crisis hits.

### Example 2: Parent in Hospital After a Stroke
User says: "My father is 82, in hospital after a stroke. What is he entitled to and how do we arrange a caregiver?"
Actions:
1. Ask whether rehabilitation is recommended (the kupa arranges it), and file gimlat siud now, from the ward, through the hospital social worker, with the interim medical summary; ask for trom siud hours meanwhile
2. Expect a level from the documents plus a phone call from the assessor; ask for a home visit if the documents understate his needs
3. Start the PIBA foreign-caregiver permit with the hospital-discharge declaration, and weigh full cash against agency hours
4. Ask whether he is a Holocaust survivor (born about 1944: possibly a child survivor) for the extra 9 hours, or the post-hospital hours if no siud benefit
5. Check capacity before going to court (Step 6)
Result: Benefit and permit run in parallel with the hospital stay, not after it.

### Example 3: No Power of Attorney
User says: "My father had a stroke and can't make decisions. He never set up power of attorney."
Actions:
1. Ask what the treating team says about capacity. If he can still understand and decide, a lawyer can assess whether he can sign an enduring POA now
2. If he can decide with help, a court-appointed decision-making supporter is less restrictive than a guardian
3. Only if neither works, guardianship through a lawyer at the Family Court
4. Apply in parallel for gimlat siud; for urgent medical decisions, consult the hospital social worker
Result: Family uses the least restrictive route the law requires.

## Bundled Resources

### References
- `references/elder-care-benefits.md`: benefit levels, cash tables, income bands, old-age pension and income supplement.
- `references/more-entitlements.md`: assessment, appeal, rehab and bridging care, non-stackable benefits, Holocaust survivor care, legal-capacity routes, support services.
- `references/institutional-copayment.md`: the family co-payment under circular 08/2018, and the complex-nursing kupa track.
- `references/housing-options.md`: facility types and foreign-caregiver permit criteria.
- `references/domain-checklist.md`: coverage contract.

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [Kolzchut (All-Rights)](https://agentskills.co.il/en/mcp/kolzchut) | Israel's authoritative rights knowledge base: elder care rights, eligibility, procedures |
| [IL Health](https://agentskills.co.il/en/mcp/il-health) | MoH data on hospital quality, health funds, elder services |

## Gotchas

1. **Gimlat siud vs. bituach siudi.** The first is a Bituach Leumi benefit giving care hours; the second is kupa group insurance paying money. Different rules; both can be received together.

2. **Siudi insurance has no age cap; 49 is the practical deadline.** There is no "age 65 cutoff": the kupot accept joiners at any age, subject to underwriting. By 49 locks in the maximum benefit and lowest premium. Since December 2023, new joiners get only the basic tier.

3. **Women's retirement age follows the birth date, not the calendar year.** Born 1962: 63; born 1963: 63 and 3 months; born 1970 or later: 65. "She turns 63 this year" is not retirement age. A wrong date misplaces gimlat siud eligibility, the old-age pension start and the attendance-allowance window.

4. **Enduring POA must be deposited.** An Israeli yipuy koach mitmashech not deposited with the Apotropus Haklali is not valid. Never say "just have a lawyer draft a POA" without the deposit.

5. **"Moving to a facility ends the benefit" is too broad.** Only a genuine nursing institution or ward ends it; diur mugan does not, a supervised beit avot is not automatically one, and a hospital stay keeps it for 30 days.

6. **Gimlat siud cash figures were re-rated on 01.08.2026.** Earlier copies of this table (1,705 / 992 / 7,440) are superseded. Quote the BTL page's printed figure with its date; do not derive it from hours x rate, because BTL's 4-hour figure (994) is not 4 x 248.

7. **"He needs a guardian" is usually the wrong first answer.** The law requires the least restrictive route: a POA signed while he still can, or a decision-making supporter. Guardianship is the last resort.

8. **The attendance allowance and gimlat siud are a choice, not a stack.** Never tell a family to claim both. And a first attendance-allowance claim closes half a year after retirement age.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Bituach Leumi (Long-Term Care) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/default.aspx | Eligibility, filing, assessment, appeal |
| Bituach Leumi (Cash option) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/money.aspx | Cash amounts and their effective date |
| Bituach Leumi (siud income test) | https://www.btl.gov.il/benefits/Long_Term_Care/Pages/income.aspx | Income bands by filing month |
| Bituach Leumi (Old-Age Pension) | https://www.btl.gov.il/benefits/old_age/Pages/default.aspx | Amounts, retirement age, income test |
| MoH circular 08/2018 (co-payment) | https://www.gov.il/he/pages/mk08-2018 | Family's share of institutional care cost |
| Apotropus Haklali (POA) | https://www.gov.il/he/service/edit_and_deposit_continuous_power_of_attorney | POA making and deposit |
| PIBA (Foreign Caregiver Permits) | https://www.gov.il/he/service/nursing_foreign_worker | Caregiver employment permit |
| Kolzchut (Siudi insurance) | https://www.kolzchut.org.il/he/ביטוח_סיעודי_קבוצתי_אחיד_של_קופות_החולים | Unified group siudi plan rules |

## Troubleshooting

### Problem: "Bituach Leumi denied the long-term care benefit"
Cause: Several conditions can fail: not yet at retirement age, income above the cut-off, too few dependency points, or living in a nursing institution. The decision letter says which. Do not assume it was the ADL score.
Solution: For a points decision, send the missing medical documents (recent medical summary, discharge summaries, test results) and appeal to the advisory committee within 60 days, or to the Labour Court; the level is not reduced on appeal. If the condition has worsened, request a re-examination instead. For an income decision, re-check the three-month average and the deductions.

### Problem: "Parent is over 65 and has no siudi insurance"
Cause: The cheap joining window has passed; underwriting may decline pre-existing conditions.
Solution: Compare the premium over the expected years against the 5-year benefit. Maximise gimlat siud and check subsidised placement.

### Problem: "Nursing home costs exceed the family budget"
Cause: A private placement is paid in full by the family, at the facility's own price.
Solution: Apply for a subsidised placement (code). The family then pays the co-payment computed under circular 08/2018, capped at the institution's actual cost. Check income supplement from Bituach Leumi. The Ministry of Welfare assists "frail" elderly through local social services.
