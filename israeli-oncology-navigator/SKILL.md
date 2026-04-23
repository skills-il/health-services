---
name: israeli-oncology-navigator
description: "Bureaucracy navigator for cancer patients and caregivers in Israel: Bituach Leumi medical disability (nechut), special services allowance with paper-only fast-track for active oncology patients, child-disability allowance for pediatric cancer at 235% rate, Section 9(5) tax exemption, 2026 health basket oncology drugs, HMO exceptions committee (vaadat charigim), supplementary-insurance tiers (Clalit Mushlam Platinum, Maccabi Sheli, Meuhedet Si, Leumit Gold), free palliative home care, fertility preservation before chemo, work rights, and NGO support (Israeli Cancer Association / האגודה למלחמה בסרטן, Larger Than Life / גדולים מהחיים, Zichron Menachem, Ezer Mizion). Use when a patient or caregiver needs to understand entitlements, file applications, or appeal a refusal. Bureaucracy only, always route medical questions to the hospital oncology social worker and the oncologist. Do NOT use for medical diagnosis, treatment decisions, drug dosing, or non-Israeli healthcare systems."
license: MIT
---

# Israeli Oncology Navigator

## Critical Disclaimer

**Read this before using the skill. Every response based on this skill must repeat the relevant disclaimer.**

This skill is a **bureaucracy navigator** for Israeli cancer patients and their families. It is NOT medical advice, NOT legal advice, and NOT a substitute for professional help. Specifically:

1. **Always route the user to the hospital oncology social worker (עובד סוציאלי אונקולוגי / עו"ס אונקולוגי) as the first step.** Every oncology department in Israel has one. They know the current procedures at that specific hospital and file most of the paperwork on behalf of patients at no cost. Telling a patient to "apply on the Bituach Leumi site" before routing them to the social worker is a failure mode.
2. **Never give medical advice.** Do not recommend treatments, drug dosages, or clinical decisions. Redirect medical questions to the treating oncologist.
3. **Figures in this skill are 2026 values** and change annually. The 2026 health basket list, Bituach Leumi amounts, and HMO supplementary regulations all update every January. Always cite the effective year and point the user at the authoritative source URL.
4. **HMO supplementary caps and exclusions vary by plan tier and renewal date.** This skill gives the shape of coverage; the patient must verify the current regulations PDF for their specific plan before acting on any financial figure.
5. **Do not fabricate legal references.** If you cannot verify a law section, form number, or entitlement amount against the sources listed in the Reference Links section, say so plainly and point the user at the source, do not guess.

## Problem

A cancer diagnosis in Israel triggers weeks of bureaucracy at the worst possible time. Entitlements are split across **four separate systems** that do not talk to each other: Bituach Leumi (nechut, special services, child-nechha, tax exemption), the health basket (which drugs are funded), the HMO supplementary insurance (non-basket drugs, second opinions, transport), and dozens of NGOs with overlapping but different eligibility. Patients and caregivers routinely discover entitlements months after they could have been claimed, or fight a valid claim through an appeal because nobody told them about the 30-day deadline. This skill consolidates the bureaucracy map so the family can act in the first weeks, while routing the hard decisions to the hospital oncology social worker who files the actual paperwork.

## Instructions

### Step 0: Route to the hospital oncology social worker FIRST

Before anything else, tell the user:

> Your first call, before Bituach Leumi and before the NGOs, is the **oncology department social worker (עו"ס אונקולוגי)** at the treating hospital. They know your specific hospital's procedures, they have the current forms, they file most Bituach Leumi claims for you at no cost, and they refer to the right NGO based on your diagnosis and family situation. Ask the oncology ward or the hospital switchboard for "the oncology social worker".

For rights-portal research the user can do in parallel (while waiting for the social worker appointment), also mention:
- **Kolzchut (כל-זכות)** at https://www.kolzchut.org.il -- free, the most authoritative Israeli rights portal
- **Israeli Cancer Association (ICA / האגודה למלחמה בסרטן) Telemeda hotline** -- free phone information line:
  - Hebrew: 1-800-599-995
  - Arabic: 1-800-36-36-55
  - Russian: 1-800-34-33-44

### Step 1: Assess which track applies

| Situation | Relevant Steps |
|-----------|----------------|
| Just diagnosed, active treatment (chemo / radiation / biological) | Steps 2, 3, 4, 7 |
| Child diagnosed with cancer | Steps 3 (child-nechha), 8 (NGOs for pediatric), 7 (fertility) |
| Drug needed is NOT in the 2026 basket | Steps 4, 5 |
| Need to preserve fertility before treatment | Step 7 |
| Patient in terminal stage | Step 6 (palliative) |
| Wanting to keep working / been threatened at work | Step 8 |
| Looking for emotional / logistical NGO help | Step 9 |
| Considering a clinical trial or treatment abroad | Step 10 |

### Step 2: Nechut Refuit (medical disability) -- fast-track for active patients

**Cancer does NOT automatically set a fixed disability percentage.** A medical committee (ועדה רפואית) determines the percentage per cancer type, stage, and treatment. But:

**Paper-only fast-track for active oncology patients:** Patients receiving qualifying drug treatments (chemotherapy, radiation, biological therapy) can have their Bituach Leumi eligibility determined from **submitted medical documents alone**, without attending a committee hearing. This is the most important thing new patients miss. Source: Kolzchut, "Determining Eligibility for Special Services Allowance for Cancer Patients Without Attending a Medical Committee".

**What this unlocks:**
- Automatic eligibility at **50% of the special services allowance** (see Step 3) for the duration of active treatment
- Minimum eligibility period of **6 months** from the day treatment starts
- Continuation **1 month past** the end of treatment at 235% (home hospice) or dropping to the appropriate lower rate

The hospital oncology social worker files this. The patient does not need to visit a Bituach Leumi office in person.

### Step 3: Bituach Leumi core entitlements

#### 3a. General disability pension (קצבת נכות כללית) -- 2026 amounts

Eligible when medical disability is at least 60% AND earning-capacity loss is at least 50% (salaried) or 75% (housewife). Monthly amounts (January 2026):

| Earning-capacity loss | Monthly (individual) | With spouse supplement |
|-----------------------|----------------------|------------------------|
| 100% / 75% (full rate) | ₪4,711 | ₪6,229 |
| 74% | ₪3,211 | ₪4,255 |
| 65% | ₪2,894 | ₪3,840 |
| 60% | ₪2,718 | ₪3,609 |

Source: Bituach Leumi announcement of 2026 updates (see Reference Links). Amounts are indexed annually.

#### 3b. Special services allowance (גמלת שירותים מיוחדים / שר"מ)

Monthly cash benefit for adults who need help with daily activities. Cancer-specific tracks:

| Situation | Rate | Notes |
|-----------|------|-------|
| Active chemo / radiation / listed biological treatments | 50% (paper-only, no committee) | Minimum 6 months eligibility |
| Home hospice or inpatient hospice | 235% | Highest rate |

The 50%-paper-track is the most under-claimed benefit. The oncology social worker should file it automatically on diagnosis.

#### 3c. Disabled-child allowance for pediatric cancer (גמלת ילד נכה)

A child with a malignancy is eligible from birth to age 18 years and 3 months. Rates (January 2026):

| Situation | Rate | Monthly amount |
|-----------|------|----------------|
| Active chemo or radiation | 235% | ₪9,126 |
| Five months after active treatment ends | 100% | ₪3,820 |
| Biological treatments (separate track) | 100% | ₪3,820 -- minimum 6 months from day treatment starts |

Source: Bituach Leumi "Disabled Child" benefit page and Kolzchut parents' guide.

#### 3d. Income tax exemption -- Section 9(5) of the Income Tax Ordinance

Cancer patients often qualify for a large income-tax exemption. Threshold: the Bituach Leumi or Ministry of Finance medical committee has determined **at least 90% permanent disability, OR at least 90% temporary disability for 185 days or more**. Patients who had tumor-removal surgery followed by chemo or radiation typically qualify.

Filed digitally through the Tax Authority "Green Wave" (גל ירוק) form. Source: Kolzchut, "Cancer Patients".

#### 3e. Sick pay from day 1

Since 1 June 2022, an employee with a chronic illness absent for treatment or tests is entitled to full sick pay **from the first day of absence**, overriding the standard 0% / 50% / 50% / 100% ladder. Source: Kolzchut, "Cancer Patients".

#### 3f. Right to appeal (ערר)

The patient has **30 days** (not 90) from receiving the medical committee decision to file a written appeal to the Medical Appeals Committee (ועדה רפואית לעררים). Bituach Leumi in practice accepts filings up to 90 days but do NOT rely on this. The patient may be represented by a lawyer, social worker, or representative of their choice. A further appeal lies on legal grounds only to the Regional Labor Court. Source: Kolzchut, "Appealing a General Disability Medical Committee Decision".

### Step 4: Health basket (Sal HaBriut) cancer drugs for 2026

The **2026 basket** added 107 drugs and technologies at a total of ₪650M, of which roughly ₪337M (about 52%) went to oncology. Notable 2026 oncology additions include Imfinzi (bladder and gastric, peri-operative), Tagrisso (post-operative EGFR NSCLC), Keytruda (head-and-neck; advanced/recurrent endometrial), Enhertu (HER2-low breast cancer), and Adcetris (first-line Hodgkin lymphoma).

**Before claiming any specific drug is "in the basket":**
1. Open the official 2026 list of medicines PDF linked in Reference Links.
2. Search for the generic name (not the trade name) and verify the indication, dose, and co-pay.
3. Drugs in the basket are dispensed by the HMO at the standard drug co-pay. No separate application is needed.

**For a drug NOT in the basket,** the patient needs either the HMO exceptions committee (Step 5) OR a supplementary-insurance payout (also Step 5).

### Step 5: HMO exceptions committee and supplementary insurance

#### 5a. Exceptions committee (ועדת חריגים)

Each HMO has a committee that reviews one-off requests to fund a drug or treatment outside the basket. Trigger: **formal refusal by the HMO** to fund the treatment.

Application package:
- Committee-review request form (from the HMO)
- Treating physician's detailed recommendation with medical literature and evidence that basket alternatives were exhausted
- All relevant medical records

Committee members: physicians (including oncologists), pharmacologist, legal advisor, economic advisor.

There is NO statutory response time. Patients who are denied or waiting too long can escalate to the Patients' Rights Association (https://www.patients-rights.org/), which represents patients in exceptions-committee disputes.

#### 5b. Supplementary insurance (ביטוח משלים) -- cancer coverage by HMO

Each HMO sells two tiers. The top tier is where non-basket oncology drug coverage sits. **This section gives the shape of coverage only. Verify the specific regulations PDF for the patient's plan and renewal date before acting on any cap.**

| HMO | Basic tier | Top tier | Non-basket oncology drugs |
|-----|------------|----------|---------------------------|
| Clalit | Mushlam Zahav | Mushlam Platinum | Covered up to ₪1M cap, including drugs unregistered in Israel if registered in a recognized Western country for the indication |
| Maccabi | Maccabi Zahav | Maccabi Sheli | Covered up to ₪1M cap; drug must be registered in Israel, US, Canada, Australia, New Zealand, Switzerland, Norway, Iceland, or EU |
| Meuhedet | Meuhedet Adif | Meuhedet Si (שיא) | Non-basket drug discounts on Adif; broader coverage on Si. Specific 2026 oncology caps: verify the plan's regulations PDF |
| Leumit | Leumit Kesef (Silver) | Leumit Zahav (Gold) | Life-extending oncology drug coverage historically offered; verify the 2026 regulations PDF |

**Second opinion in Israel or abroad:** This is a **supplementary** benefit, not a basic-basket right. Clalit Platinum, Maccabi Sheli, Meuhedet Si, and Leumit Gold all offer second-opinion coverage, each with different rules. Verify the plan.

### Step 6: Hospice and palliative care

Since **2009**, every HMO must provide supportive palliative care **24/7, free of charge under the basic basket** for patients with a life-threatening illness in the terminal stage (treating physician estimates 6 months or less). The team includes a physician, nurse, and social worker. It covers cancer and non-cancer terminal illnesses (end-stage heart, lung, kidney disease, dementia).

**How to access:** family doctor referral → HMO home-treatment unit (or the hospital HMO representative if the patient is hospitalized). Source: wikirefua, "Palliative Service (Hospice) Director General Circular"; Clalit "Home Hospice" page.

### Step 7: Fertility preservation before cancer treatment

The health basket covers egg, embryo, and ovarian tissue freezing for women facing gonadotoxic therapy (chemotherapy, pelvic radiation). Limits: **up to age 41** (birthday 42) or until the woman has 2 children, whichever comes first. Egg-freezing treatments are capped at **4 cycles or 20 eggs total**.

Source: gov.il "Oocyte cryopreservation"; Kolzchut "Fertility Preservation"; individual HMO fertility-preservation pages.

**Sperm freezing for men facing the same treatments** is also widely covered under the same principle. Specific caps: verify with the treating oncology and the HMO fertility unit.

**This is time-critical.** Fertility preservation must be started before treatment begins. Do not delay the oncologist referral to fertility preservation.

### Step 8: Work rights during cancer treatment

- **Sick leave (own illness):** Full sick pay from day 1 under the chronic-illness exception since June 2022 (see Step 3e).
- **Sick leave (parent of a sick child):** Base entitlement is 8 days per year deductible from accrued balance for a child up to age 16. Single parents get an expanded quota. For a child under 18 with a severe illness (cancer, dialysis), the parent may use accrued sick plus vacation balance for expanded absence. State employees have separately expanded rights.
- **Job protection:** The **Equal Rights for Persons with Disabilities Law, 1998 (section 8)** prohibits discrimination in hiring, promotion, dismissal, or employment conditions on the basis of disability. It applies to employers with **more than 25 employees**.
- **Resignation because of illness:** Under Severance Pay Law section 6, resignation forced by illness is treated as dismissal for severance purposes.
- **Reasonable accommodation:** Employers with more than 25 employees must make reasonable accommodations (adjusted hours, remote work, physical adjustments) unless it would be an undue burden. Escalation: the Commission for Equal Rights of Persons with Disabilities.

### Step 9: NGOs and support services

Do not tell the user to "contact an NGO" without specifying which one. The oncology social worker will refer based on diagnosis and age, but the user can also reach out directly.

| Organization | Hebrew name | Focus | Primary channel |
|--------------|-------------|-------|-----------------|
| Israeli Cancer Association (ICA) | האגודה למלחמה בסרטן | All cancer types, all ages. Free transportation to hospitals with trained volunteers. Wig fitting and loans at Beit Mati (Givatayim) and ~60 branches. Accommodation near hospitals for out-of-town patients. Rights-realization helpdesk. | https://www.cancer.org.il/ -- Telemeda 1-800-599-995 (HE) / 1-800-36-36-55 (AR) / 1-800-34-33-44 (RU) -- rehabilitation helpdesk 03-5721678 / shikum@cancer.org.il |
| Larger Than Life | גדולים מהחיים | **Pediatric cancer families only.** Long-term support for children diagnosed with cancer and their families. | https://gdolim.org.il/ |
| Zichron Menachem | זכרון מנחם | Children and young adults aged 0-25 with cancer, plus families. Retreats, activities, parental and emotional support. | https://zichron.org/ |
| Ezer Mizion | עזר מציון | Broad health logistics. Operates a large Jewish Bone Marrow Donor Registry. "Oranit House" accommodation for cancer patients and families during treatment. | https://ezermizion.org/ |
| One in Nine | אחת מתשע | Breast cancer focus. | https://www.onein9.org.il/ |
| Patients' Rights Association | האגודה לזכויות החולה | General patient rights, representation in exceptions committee disputes. | https://www.patients-rights.org/ |

**Correction note to agents:** If the user (or an internal note) says the Hebrew name for "Larger Than Life" is **לרגיש שוב**, that is incorrect. The correct Hebrew name is **גדולים מהחיים**.

### Step 10: Clinical trials and treatment abroad

#### 10a. Clinical trials

The Ministry of Health maintains an Israeli clinical trials registry; patients can also search ClinicalTrials.gov for Israeli sites. Ask the treating oncology team whether a trial suitable for the specific case is open at the hospital or elsewhere in Israel. As a general principle (to be confirmed per trial), the trial sponsor pays for the investigational drug and trial-specific procedures, while the HMO continues to fund standard-of-care procedures the patient would otherwise receive. **Confirm cost allocation in writing before enrolling.**

#### 10b. Treatment abroad funded by the basket

Covered when the insured **cannot receive the treatment or a reasonable alternative in Israel**, and the treatment is **life-saving**. Permissible fields explicitly include: congenital defects, organ transplants, **tumors**, cardiovascular disease, and CNS disease.

When approved, the HMO funds the medical treatment, flights, accommodation, food, and one escort. Process: application to the HMO → on refusal, appeal to the HMO internal appeals committee.

Supplementary plans (Mushlam Platinum, Sheli, Si, Gold) offer parallel, often more generous coverage. Verify the specific plan's regulations.

#### 10c. Proton therapy in Israel

As of 2026, **no proton-therapy center is operational in Israel**. A proton-therapy program at Ichilov (Tel Aviv Sourasky) has been in the planning and construction phase, but patients should verify the current status with their treating hospital before assuming local availability. Patients needing proton therapy are typically funded abroad through the basket treatment-abroad track (Section 10b).

#### 10d. CAR-T cell therapy in Israel

CAR-T cell therapy is delivered at several major Israeli oncology centers. Rather than rely on a fixed list (which goes out of date as new centers come online and protocols change), the practical advice is: **ask the treating oncology department about current CAR-T availability at their hospital and, if they don't deliver it, which center they refer to**. The oncology social worker can also coordinate referrals.

## Examples

### Example 1: Newly diagnosed adult, starting chemo next week

User says: "My wife was just diagnosed with breast cancer. She starts chemo next week. What do we need to do in the first two weeks?"

Actions:
1. **First call today**: ask the oncology ward for the oncology social worker (עו"ס אונקולוגי). They file most of the paperwork for you at no cost.
2. Ask the social worker to file for the **special services allowance (50% paper-only track)** -- no committee visit needed for active chemo patients (Step 2, 3b).
3. Open Kolzchut's "Cancer Patients" page to understand tax exemption eligibility under Section 9(5) (Step 3d), sick-pay-from-day-1 rights at her workplace (Step 3e), and fertility preservation if relevant (Step 7).
4. Call the ICA Telemeda hotline (1-800-599-995) for free rights-realization help and transportation volunteers.
5. If the oncologist prescribes a drug not in the 2026 basket, check the supplementary-insurance tier (Step 5b) and prepare for an exceptions committee application (Step 5a) if needed.

Result: the family acts in the first two weeks, the major allowances are filed before the 30-day appeal window for any denials starts running, and medical and bureaucratic tracks run in parallel.

### Example 2: Pediatric cancer diagnosis

User says: "Our 7-year-old was just diagnosed with leukemia. What financial support is available?"

Actions:
1. Oncology social worker at the treating pediatric hospital is the first call. They file the paperwork for disabled-child allowance.
2. **Disabled-child allowance (גמלת ילד נכה)** under the malignancy category (Step 3c): **235% rate = ₪9,126/month** during active chemo/radiation, continuing for 1 month past treatment end.
3. Parent sick leave for a child with a severe illness (Step 8): the parent can use accrued sick plus vacation balance for expanded absence.
4. **Two pediatric NGOs to contact**: Larger Than Life (גדולים מהחיים, https://gdolim.org.il/) and Zichron Menachem (זכרון מנחם, https://zichron.org/) -- long-term family support, retreats, parental support.
5. Check with the pediatric oncology team about Ezer Mizion's Oranit House if the family travels for treatment.

Result: the family claims the 235% child-nechha rate from day one, has NGO logistical support, and the working parent has clarity on expanded leave.

### Example 3: HMO refused a drug

User says: "Clalit refused to fund the drug my oncologist recommended. What now?"

Actions:
1. Ask for the **formal written refusal** from Clalit (required to trigger the exceptions committee).
2. Package for the exceptions committee: the refusal letter, the oncologist's detailed recommendation with medical literature and evidence that basket alternatives were exhausted, and all relevant medical records (Step 5a).
3. Check whether the patient has **Mushlam Platinum** (top supplementary tier). If yes, non-basket oncology coverage up to ₪1M cap may apply including drugs unregistered in Israel if registered in a recognized Western country for the indication (Step 5b).
4. Parallel escalation: Patients' Rights Association (patients-rights.org) can help with exceptions committee representation.
5. Route the medical question ("is this the right drug for me?") back to the oncologist and optionally use the supplementary's second-opinion benefit.

Result: the patient has a clear 3-track plan (committee, supplementary, NGO advocacy) instead of a single refusal dead-end.

## Bundled Resources

### References
- `references/bituach-leumi-oncology-rights.md` -- Detailed breakdown of nechut, special services, disabled-child allowance, tax exemption, and appeals, with 2026 amounts.
- `references/health-basket-and-hmo-coverage.md` -- 2026 basket oncology additions, exceptions committee process, HMO supplementary-insurance comparison.
- `references/ngos-and-support-services.md` -- Verified list of cancer NGOs in Israel with Hebrew names, services, and contact channels.

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [Kolzchut (All-Rights)](https://agentskills.co.il/he/mcp/kolzchut) | Search Israel's authoritative rights and entitlements knowledge base for current cancer patient rights articles, including nechut, special services allowance, and treatment abroad eligibility |
| [IL Health](https://agentskills.co.il/he/mcp/il-health) | Ministry of Health hospital quality indicators and health-fund (kupat cholim) information for selecting oncology treatment centers |
| [Israel Drugs](https://agentskills.co.il/he/mcp/israel-drugs) | Full Israeli pharmaceutical database with health-basket status, HMO formulary alignment (Clalit, Maccabi, Meuhedet, Leumit), and drug indication lookups for verifying basket coverage of a specific cancer drug |
| [Israel Medical Research](https://agentskills.co.il/he/mcp/israel-medical-research) | Search 314K+ medical research papers from Israeli institutions (Sheba, Hadassah, Ichilov, Rambam, Weizmann, Technion) to compare oncology research depth across potential treating centers |

## Gotchas

1. **Wrong Hebrew name for Larger Than Life.** The user or an agent may write **לרגיש שוב** -- this is incorrect. The correct Hebrew name is **גדולים מהחיים** (Gdolim MeHaChaim). URL: https://gdolim.org.il -- always use this name when referring Israeli pediatric-cancer families.

2. **50% special services allowance is paper-only for active patients.** Agents routinely tell active-treatment patients to "book a Bituach Leumi committee appointment". This is wrong and wastes weeks. The oncology social worker files documents directly and the 50% rate is granted without a committee visit for at least 6 months. Never tell an active-treatment patient to wait for a committee.

3. **Second opinion is a supplementary benefit, not a basic-basket right.** Agents often claim cancer patients have a "right to a second opinion in Israel". This is only true for patients enrolled in Clalit Platinum, Maccabi Sheli, Meuhedet Si, or Leumit Gold. For a patient on the basic basket only, there is no codified second-opinion right.

4. **Proton therapy is not operational in Israel as of 2026.** Agents occasionally tell patients to "go to Ichilov for proton therapy". No proton-therapy center is clinically delivering treatment in Israel yet. Patients who need proton therapy today are funded abroad through the treatment-abroad track (Step 10b). Always verify the current status with the treating hospital.

5. **The 30-day appeal window is the most commonly missed deadline.** Agents may tell a patient to "take some time to prepare the appeal" after a Bituach Leumi medical committee refusal. The statutory window is 30 days from receiving the decision. Filing a partial appeal on time preserves the right and extends the deadline for reasons by another 30 days. Do not let patients miss the window.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kolzchut -- Cancer Patients (EN) | https://www.kolzchut.org.il/en/Cancer_Patients | Authoritative consolidated rights entry point |
| Bituach Leumi -- Disability Pension Amounts | https://www.btl.gov.il/benefits/Disability/Pages/%D7%A9%D7%99%D7%A2%D7%95%D7%A8%D7%99%20%D7%94%D7%A7%D7%A6%D7%91%D7%94.aspx | 2026 monthly amounts by earning-capacity loss percentage |
| Bituach Leumi -- 2026 Rate Update | https://www.btl.gov.il/About/news/Pages/hadasaidkonkitzva2026.aspx | Annual rate update announcement |
| Bituach Leumi -- Disabled Child (Malignancy) | https://www.btl.gov.il/benefits/Disabled_Child/likuilist/Pages/cancer.aspx | Pediatric cancer child-nechha eligibility and rates |
| Kolzchut -- Appealing General Disability Decision | https://www.kolzchut.org.il/en/Appealing_a_General_Disability_Medical_Committee_Decision | 30-day appeal window, process, representation rules |
| Kolzchut -- Exceptions Committee | https://www.kolzchut.org.il/en/Appealing_to_the_Health_Plan_Exceptions_Committee | Vaadat charigim process, package required |
| Ministry of Health -- 2026 List of Medicines PDF | https://www.gov.il/BlobFolder/reports/hbs2026/he/files_committees_hbs_2026_List-of-medicines-and-medical-food-2026.pdf | Official 2026 basket drugs list |
| Kolzchut -- Funding Medical Treatment Abroad | https://www.kolzchut.org.il/en/Funding_Medical_Treatment_Abroad | Criteria, process, appeal |
| Kolzchut -- Fertility Preservation | https://www.kolzchut.org.il/en/Fertility_Preservation | Age limits, cycle caps, eligibility |
| Kolzchut -- Supportive Home Care (Palliative) | https://www.kolzchut.org.il/en/Supportive_Home_Care_(Palliative_Care) | Free palliative care under the basket since 2009 |
| Israeli Cancer Association | https://www.cancer.org.il/ | Telemeda hotline, rights helpdesk, transportation, wigs, accommodation |

## Troubleshooting

### Problem: "Bituach Leumi denied my disability claim"
Cause: The medical committee decided the earning-capacity loss or disability percentage falls below threshold, or only paper documents were reviewed and key evidence was missing.
Solution: File a written appeal within **30 days** to the Medical Appeals Committee (ועדה רפואית לעררים). The patient may be represented by a lawyer or social worker. Strengthen the appeal with: the treating oncologist's detailed functional assessment, an occupational-therapy report, and evidence of worst-case days (not best). Bituach Leumi in practice accepts filings up to 90 days but do not rely on this window.

### Problem: "My prescribed drug is not in the 2026 basket and the HMO refused to fund it"
Cause: Drug is not yet in the basket, or is in the basket but for a different indication, or the HMO's internal protocol rejected it.
Solution: Two parallel tracks. (1) **Exceptions committee** (Step 5a): ask for a written refusal, then submit a committee-review package (oncologist recommendation with medical literature, proof basket alternatives were tried, medical records). (2) **Supplementary insurance** (Step 5b) if enrolled in Mushlam Platinum, Maccabi Sheli, Meuhedet Si, or Leumit Gold -- check the plan's non-basket oncology-drug cap and foreign-registration rules. Route through the hospital oncology social worker and optionally the Patients' Rights Association for exceptions-committee representation.

### Problem: "I want to preserve fertility before chemo but I am over 41"
Cause: Health-basket egg and embryo freezing is capped at age 41 (birthday 42) per the Ministry of Health rules.
Solution: Route to the HMO fertility unit to discuss private-pay fertility preservation or supplementary-insurance fertility benefits (varies by plan). Do not delay oncology treatment while pursuing this. The oncology team must be in the loop.

### Problem: "My employer pressured me to resign because of my treatment"
Cause: Discrimination based on illness or disability, prohibited for employers with more than 25 employees under the Equal Rights for Persons with Disabilities Law.
Solution: (1) Document everything in writing. (2) Under Severance Pay Law section 6, resignation forced by illness is treated as dismissal for severance purposes. (3) File a complaint with the Commission for Equal Rights of Persons with Disabilities. (4) Consult an employment lawyer -- the ICA rights-realization helpdesk (03-5721678) can refer.
