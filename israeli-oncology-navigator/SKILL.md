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

The **2026 basket** added 107 drugs and technologies at a total of ₪650M, of which roughly ₪337M (about 52%) went to oncology. Notable verified additions (full list in `references/health-basket-and-hmo-coverage.md`):
- **Solid tumors**: Imfinzi (bladder/gastric peri-op), Tagrisso (post-op EGFR NSCLC), Keytruda (head-and-neck; endometrial advanced/recurrent), Enhertu (HER2-low breast)
- **Hodgkin lymphoma**: Adcetris (first line)

Bispecific-antibody and ADC additions for R/R MM and lymphoma have been reported — verify per-drug names against the MOH 2026 PDF before quoting.

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

There is NO statutory response time. **Escalation ladder when refused** — go in this order, NOT straight to court:

1. **Internal HMO appeals committee (ועדת ערר / בירורים)** — fast, free, no lawyer required. Clalit example: https://www.clalit.co.il/he/info/Pages/berurim.aspx
2. **MOH Public Complaints Commissioner for the National Health Insurance Law** if internal appeal fails (12,809 inquiries handled in 2024)
3. **Regional Labor Court** — request an interim order (צו ביניים) if life is at stake; these can issue within days

**Landmark precedent** to cite (full discussion: `references/exceptions-committee-precedents-and-appeals.md`): **חב"ר (ת"א) 5942-09-12** (Tel Aviv Regional Labor Court, October 2012, biliary-tract cancer) established that a drug's exclusion from the basket is not by itself grounds for refusal — the exceptions committee must evaluate clinical efficacy, consider whether basket alternatives exist, and document budget arguments with calculations rather than assertions.

The **Patients' Rights Association** (https://www.patients-rights.org/) and **One in Nine** in-house attorney (03-602-1717 ext 2 for breast cancer) help with the package and representation. The **ICA Rights Center** is embedded in 10+ Israeli hospitals (rights helpdesk **03-5721678**, shikum@cancer.org.il) and specializes in NII rights, basket entitlements, exceptions committees, and Form 17.

#### 5b. Supplementary insurance (ביטוח משלים) -- cancer coverage by HMO

Each HMO sells a basic + top tier. Top tier covers non-basket oncology drugs (full table + 2025 caps in `references/health-basket-and-hmo-coverage.md`). Quick map:

| HMO | Top tier (where non-basket oncology coverage sits) |
|-----|---|
| Clalit | **Mushlam Platinum** — up to ₪1M cap, includes drugs unregistered in Israel if registered in a recognized Western country |
| Maccabi | **Maccabi Sheli** — up to ₪1M cap, drug must be registered in IL/US/CA/AU/NZ/CH/NO/IS/EU |
| Meuhedet | **Meuhedet Si (שיא)** — broader off-label and non-basket coverage; verify regulations PDF for 2026 caps |
| Leumit | **Leumit Zahav (Gold)** — life-extending oncology drug coverage historically offered; verify regulations PDF |

**Second opinion in Israel or abroad** is a supplementary benefit, NOT a basic-basket right — only patients on the top tiers above have it.

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
| Haverim LeRefuah | חברים לרפואה | **Free Pharmacy Project** — collects unused prescription medications via 1,075+ collection points, redistributes free of charge to chronic patients including cancer patients. **"Save A Life" Funds** earmark donations for individual patient cases. | https://www.haverim.org.il/ |
| Yad Sarah | יד שרה | Medical-rehabilitative equipment loans via 100+ branches across Israel — relevant for cancer patients in end-stage home care, post-surgical recovery, and long-term outpatient treatment. | https://www.kolzchut.org.il/he/%D7%99%D7%93_%D7%A9%D7%A8%D7%94 |

**Correction note to agents:** If the user (or an internal note) says the Hebrew name for "Larger Than Life" is **לרגיש שוב**, that is incorrect. The correct Hebrew name is **גדולים מהחיים**.

### Step 10: Experimental, off-label, and unregistered treatments

Patients with advanced or refractory cancer often hear phrases like "compassionate use", "Form 29c", "off-label", "expanded access", and "Named Patient Program" — and these pathways are **not interchangeable**. Picking the wrong one wastes weeks.

**See `references/experimental-and-off-label-treatments.md` for the full reference — the summary below is the decision-critical information.**

#### 10.1 Form 29c (טופס 29ג') — individual import of an unregistered drug

- **Legal basis**: Regulation 29 of the Pharmacists Regulations (Preparations), 5746-1986. Patient-level application is Form 29c.
- **Who files**: the **treating physician** via the MOH **Pharmacy Division (אגף הרוקחות)**.
- **Requirements**: medical justification; drug registered in a recognized country for the same indication; no registered Israeli alternative.
- **CRITICAL**: **Form 29c is an import permit, NOT funding.** Funding must be secured separately (exceptions committee, supplementary, private, NGO). LLMs routinely say "file 29c and the HMO will pay" — this is wrong.

#### 10.2 Compassionate use / טיפול חמלה

- Pharma company provides an unregistered/experimental drug **free of charge** with MOH pre-approval.
- **Three-party process**: physician → pharma sponsor → MOH Pharmacy Division.
- **Not a right** — "לא קיימת חובה לספק". Companies can refuse.
- Different from a clinical trial (which has a protocol and Helsinki approval). Israel has no separate "Named Patient Program" category — sponsor-provided experimental access is folded into טיפול חמלה.

#### 10.3 Off-label use

- Drug IS registered in Israel for one indication, prescribed for a different indication.
- **Legal** in Israel; basket generally does NOT fund off-label.
- **Exceptions committee** is the main public route.
- **Supplementary plans cover off-label within caps**:
  - Clalit Mushlam Gold/Platinum: package > ~₪356.98, 50% co-pay capped ~₪358/pack/month, monthly total ~₪713.97 (https://mushlam.clalit.co.il/he/medications/Pages/kisuy_murhav_trufot.aspx)
  - Maccabi Zahav: serious diseases, prior approval, 24-month waiting period (https://www.maccabi4u.co.il/eligibilites/4327/)
  - Meuhedet and Leumit have similar clauses — verify the tier's regulations PDF
- **2008 reform boundary**: Israeli supplementary plans cannot cover life-saving/life-extending drugs as their primary benefit. Off-label clauses cover off-label and unregistered-indication scenarios only.

#### 10.4 Clinical trials

- **Legal basis**: People's Health Regulations (Medical Research on Human Subjects), 1980.
- **Helsinki committee** — ethics for **research**, NOT the HMO funding exceptions committee. Institutional (per hospital) + National Supreme (elevated-risk categories).
- Find Israeli oncology trials: MyTrial (MOH) via https://www.gov.il/he/departments/general/clinical-trials-website and ClinicalTrials.gov filtered to Israel.
- **Sponsor pays** for investigational drug and trial-specific procedures; HMO continues standard of care.
- **Post-trial drug access** (MOH procedure 14, chapter 4) is NOT automatic — raise with the PI before signing consent.

#### 10.5 Decision tree — which route for which situation

| Situation | Route |
|-----------|-------|
| Drug is in the 2026 basket for my indication | Standard prescription; HMO dispenses at basket co-pay |
| Drug is registered in Israel for my indication but HMO refused funding | Exceptions committee (Section 5a) + supplementary if enrolled |
| Drug is registered in Israel for a DIFFERENT indication (off-label) | Supplementary plan's off-label clause FIRST (fastest), parallel exceptions committee |
| Drug is unregistered in Israel but registered abroad for my indication | Form 29c filed by physician + funding via exceptions / supplementary / private / NGO |
| Drug is still experimental (in Phase 2/3 trials, not registered anywhere yet) | טיפול חמלה — physician finds a pharma sponsor, MOH pre-approval |
| There is a clinical trial I might qualify for | MyTrial search + referral from oncologist + Helsinki-committee-approved enrollment |

#### 10.6 Treatment abroad funded by the basket (life-saving, unavailable in Israel)

Covered when both: (1) the insured cannot receive the treatment or a reasonable alternative in Israel, AND (2) the treatment is **life-saving**. Permissible fields include **tumors** explicitly (also congenital defects, organ transplants, cardiovascular, CNS).

When approved, the HMO funds: medical treatment, flights, accommodation, food, and **one escort**. Process: application to HMO → on refusal, appeal to HMO internal appeals committee. Supplementary plans (Mushlam Platinum, Sheli, Si, Gold) offer parallel, often more generous coverage.

#### 10.7 Proton therapy in Israel

As of 2026, **no proton-therapy center is operational in Israel**. A proton-therapy program at Ichilov (Tel Aviv Sourasky) has been in the planning and construction phase, but verify the current status with the treating hospital before assuming local availability. Patients needing proton therapy are typically funded abroad through the basket treatment-abroad track (Section 10.7).

#### 10.8 CAR-T cell therapy in Israel

CAR-T cell therapy is delivered at several major Israeli oncology centers. Rather than rely on a fixed list (which goes out of date), ask the treating oncology department about current CAR-T availability at their hospital and referral paths if they do not deliver it. The oncology social worker can coordinate referrals.

### Step 11: Advance directives and end-of-life (Dying Patient Law, 2005)

Israeli framework: **Dying Patient Law / חוק החולה הנוטה למות, 2005**. Advance medical directives (הנחיות רפואיות מקדימות / "living will") become operative only when both: (a) the patient is defined as a *terminally ill patient* with under 6 months life expectancy AND (b) the patient lacks capacity. Directives are registered with the Ministry of Health.

For an oncology patient, the right time to set this up is **before** terminal-stage capacity loss — typically when starting late-line treatment for advanced disease. Two NGOs help with the paperwork:
- **LILACH (ליל"ך)** — https://www.lilach.org.il/living_will/ — leading Israeli end-of-life NGO
- **Ematai** — https://www.ematai.org/netivotil/ — bilingual (Hebrew/English) advance-care planning, faith-sensitive options

Source for the Dying Patient Law procedure: https://www.kolzchut.org.il/en/Registering_a_Living_Will

Coordinate this with the oncology social worker and the palliative-care team (Step 6) — these conversations are part of standard advanced-disease care.

### Step 12: Do-NOT list for experimental pathways

Common agent and patient mistakes:

1. **Do NOT equate "Form 29c approved" with "HMO will pay".** Form 29c is an import permit. Funding is separate.
2. **Do NOT confuse טיפול חמלה with a clinical trial.** Compassionate use is individual and outside a protocol; a trial is structured and Helsinki-approved.
3. **Do NOT confuse the Helsinki committee (research ethics) with the exceptions committee (HMO funding).** LLMs swap these routinely. Helsinki = ניסויים; ועדת חריגים = מימון.
4. **Do NOT assume supplementary insurance covers life-saving drugs as the primary benefit.** The 2008 reform prohibited that. Supplementary covers off-label, unregistered-indication, and second opinions — not life-saving oncology drugs as the headline benefit.
5. **Do NOT promise a patient post-trial access to the investigational drug.** It is negotiated per protocol and requires Helsinki + MOH sign-off.



## Examples

### Example 1: Newly diagnosed adult, starting chemo next week

"My wife was diagnosed with breast cancer; chemo starts next week."

1. **First call today**: oncology ward → oncology social worker (עו"ס אונקולוגי). They file paperwork for you free.
2. Social worker files **special services allowance 50% paper-only** (Step 3b) — no committee visit needed for active chemo.
3. Check Section 9(5) tax exemption (Step 3d), sick-pay-from-day-1 (Step 3e), fertility preservation if relevant (Step 7).
4. Call **ICA Telemeda 1-800-599-995** for transport + rights help.
5. If a prescribed drug is not in the 2026 basket: check supplementary tier (Step 5b) + prepare exceptions-committee package (Step 5a). If a Bituach Leumi committee refusal arrives later, the **30-day appeal clock** starts (Step 3f).

### Example 2: Pediatric cancer diagnosis

"Our 7-year-old was diagnosed with leukemia."

1. Oncology social worker at pediatric hospital first.
2. **Disabled-child allowance** at **235% = ₪9,126/month** during active chemo/radiation (Step 3c).
3. Parent expanded sick leave for severe child illness (Step 8).
4. Pediatric NGOs: **Larger Than Life (גדולים מהחיים)** + **Zichron Menachem** (Step 9). Out-of-town families: Ezer Mizion's Oranit House.

### Example 3: HMO refused a drug

"Clalit refused to fund the drug my oncologist recommended."

1. Get **written refusal** from Clalit (triggers the exceptions process).
2. Build exceptions-committee package (Step 5a): refusal letter + oncologist recommendation with literature + medical records.
3. Check supplementary tier (Step 5b): Mushlam Platinum covers non-basket oncology up to ₪1M.
4. Escalate via the **internal HMO appeals committee first**, then MoH Public Complaints Commissioner, then Regional Labor Court interim order if life is at stake (Step 5a). Cite Tyro / Alyav / 5942-09-12 precedents.
5. Patients' Rights Association (patients-rights.org) and One in Nine attorney (03-602-1717 ext 2 for breast cancer) help with representation.

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
| Kolzchut -- Guide to Drugs Not in the Basket (HE) | https://www.kolzchut.org.il/he/%D7%9E%D7%93%D7%A8%D7%99%D7%9A_%D7%9C%D7%94%D7%A9%D7%92%D7%AA_%D7%AA%D7%A8%D7%95%D7%A4%D7%95%D7%AA_%D7%A9%D7%90%D7%99%D7%A0%D7%9F_%D7%91%D7%A1%D7%9C_%D7%94%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA | Form 29c, compassionate use (טיפול חמלה), off-label, all funding pathways |
| MyTrial -- Israeli Clinical Trials Registry | https://www.gov.il/he/departments/general/clinical-trials-website | Mandatory MOH clinical trial registry, search by condition |
| MOH Clinical Trials Procedure 14 (PDF) | https://www.gov.il/BlobFolder/policy/cth-14/he/files_publications_units_pharmaceutical_division_clinical_trials_cth-14.pdf | Helsinki, post-trial drug access, sponsor obligations |
| Clalit Mushlam -- Extended Drug Coverage | https://mushlam.clalit.co.il/he/medications/Pages/kisuy_murhav_trufot.aspx | Off-label and unregistered-indication coverage caps |
| Maccabi -- Non-Basket Drugs | https://www.maccabi4u.co.il/eligibilites/4327/ | Off-label and serious-disease drug coverage on Maccabi Zahav |

## Troubleshooting

### Problem: "Bituach Leumi denied my disability claim"
Cause: The medical committee decided the earning-capacity loss or disability percentage falls below threshold, or only paper documents were reviewed and key evidence was missing.
Solution: File a written appeal within **30 days** to the Medical Appeals Committee (ועדה רפואית לעררים). The patient may be represented by a lawyer or social worker. Strengthen the appeal with: the treating oncologist's detailed functional assessment, an occupational-therapy report, and evidence of worst-case days (not best). Bituach Leumi in practice accepts filings up to 90 days but do not rely on this window.

### Problem: "My prescribed drug is not in the 2026 basket and the HMO refused to fund it"
Cause: Drug is not yet in the basket, or is in the basket but for a different indication, or the HMO's internal protocol rejected it.
Solution: Two parallel tracks. (1) **Exceptions committee** (Step 5a): ask for a written refusal, then submit a committee-review package (oncologist recommendation with medical literature, proof basket alternatives were tried, medical records). (2) **Supplementary insurance** (Step 5b) if enrolled in Mushlam Platinum, Maccabi Sheli, Meuhedet Si, or Leumit Gold -- check the plan's non-basket oncology-drug cap and foreign-registration rules. Route through the hospital oncology social worker and optionally the Patients' Rights Association for exceptions-committee representation.

### Problem: "I want to preserve fertility but I am over 41" or "My employer pressured me to resign during treatment"
Both cases are handled in the relevant step (Step 7 fertility, Step 8 work rights). Route to the oncology social worker first; for fertility specifically the HMO fertility unit can discuss private/supplementary options without delaying treatment; for work rights the ICA rights helpdesk (03-5721678) refers to employment counsel.
