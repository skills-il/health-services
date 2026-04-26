---
name: israeli-oncology-navigator
description: "Bureaucracy navigator for cancer patients and caregivers in Israel. Covers Bituach Leumi (disability, full 4-rate שר\"מ table 50/112/188/235% + child-under-3 supplement, pediatric ילד נכה at 235%, Section 9(5) tax exemption, 40% arnona, 60-day appeal); 2026 sal habriut (drugs, exceptions committee, severe-illness co-pay exemption, dental funding, surgery wait-time + Form 17, hereditary-cancer genetic testing, home chemo, post-2024 cannabis reform, site-specific post-surgical rehab); supplementary tiers (Mushlam Platinum, Sheli, Si, Gold); palliative; fertility preservation and gonadal protection across all genders/ages; family caregiver sick days (60/90/110); cancer-type NGOs; experimental, off-label, treatment-abroad. Use when a patient or caregiver needs to understand entitlements, file applications, or appeal a refusal. Do NOT use for medical diagnosis, treatment decisions, drug dosing, or non-Israeli healthcare systems."
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

A cancer diagnosis in Israel triggers weeks of bureaucracy at the worst possible time. Entitlements are split across **four separate systems** that do not talk to each other: Bituach Leumi (nechut, special services, child-nechha, tax exemption, arnona discount), the health basket (drugs, co-pay exemptions, dental, surgery wait-time, home chemo, post-surgical rehab), the HMO supplementary insurance (non-basket drugs, second opinions, transport), and dozens of NGOs with overlapping but different eligibility. Patients and caregivers routinely discover entitlements months after they could have been claimed, or fight a valid claim through an appeal because nobody told them about the 60-day deadline. This skill consolidates the bureaucracy map so the family can act in the first weeks, while routing the hard decisions to the hospital oncology social worker who files the actual paperwork.

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
| Child diagnosed with cancer | Steps 3 (child-nechha), 9 (pediatric NGOs), 7 (fertility) |
| Drug NOT in the 2026 basket | Steps 4a, 5 |
| Co-pay exemption, dental, surgery wait-time, home chemo, cannabis, post-surgical rehab | Step 4b |
| Hereditary cancer (BRCA, Lynch, Li-Fraumeni, FAP) | Steps 4b (genetic testing), 9 (Bracha) |
| Preserve fertility before treatment (any gender, any age) | Step 7 |
| Patient in terminal stage | Step 6 (palliative) + Step 11 (living will) |
| Family caregiver sick days | Step 8b |
| Summoned by NII for a שר"מ review, or self-requesting a higher rate | Step 3b + 3b-ii |
| Threatened at work / accommodations | Step 8a |
| Other NII-linked benefits (arnona, transport) | Step 3g |
| Clinical trial or treatment abroad | Step 10 |
| Emotional / logistical NGO help | Step 9 |

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

Monthly cash benefit for adults who need help with daily activities. **Four rates are currently in effect** (2026 amounts, source: Kolzchut "קצבת שירותים מיוחדים"):

| Situation | Rate | Monthly (2026) | How determined |
|-----------|------|----------------|----------------|
| Active chemo / radiation / listed biological treatments | 50% | ₪1,943 | Paper only, no committee |
| Help with ALL ADLs most hours OR constant supervision | 112% | ₪4,501 | Committee hearing |
| Help with ALL ADLs all hours | 188% | ₪7,181 | Committee hearing |
| Home hospice or inpatient hospice (terminal) | 235% | ₪9,126 | Committee or paper |

**The 50% paper track is the starting point, not the ceiling.** After the minimum 6 months, NII may summon for a committee review OR the patient can self-request a higher rate based on functional decline. Many active-treatment patients with severe side effects (neutropenia, neuropathy, fatigue, incontinence isolation, cognitive fog) qualify for 112% or 188% -- the difference between 50% and 188% is over ₪62,000/year.

**Child-under-3 supplement:** שר"מ recipients with children under 3 get an extra **₪1,215/month per child, max 2 children = ₪2,429/month**.

##### 3b-ii. Preparing for the שר"מ committee (ADL framework)

The committee scores 6 ADL categories (mobility, dressing, bathing, eating, toileting, continence) and a constant-supervision criterion. **Evaluate based on worst-case days, not averages**: for a chemo patient that means cycle days 1-7, not 14-21. Active-treatment side effects (neutropenia isolation, neuropathy, mucositis, post-surgical mobility, cognitive fog, seizure-supervision) count as functional impairments.

**Full prep guide:** `references/sherum-committee-preparation.md` -- ADL-to-side-effect mapping by treatment type, "summoned vs self-requested" framing, document checklist for the committee package.

**Who helps prepare:** the hospital oncology social worker is the first port of call. The **ICA Rights Center** (helpdesk 03-5721678, embedded in 10+ hospitals) and disease-specific NGO attorneys (One in Nine 03-602-1717 ext 2 for breast cancer) help build the evidence package.

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

The statutory appeal window is **60 days** from receiving the written decision, for both general disability (נכות כללית) and special services allowance (שר"מ) medical committees. File a written appeal to the Medical Appeals Committee (ועדה רפואית לעררים). Bituach Leumi in practice does not reject filings submitted within **90 days**, but this is informal grace, not law -- file by the 60-day statutory deadline whenever possible. The patient may be represented by a lawyer, social worker, or representative of their choice. A further appeal on legal grounds only lies to the Regional Labor Court. Source: Kolzchut, "ערר על החלטה רפואית בעניין נכות כללית" and "ערר על החלטה בעניין קצבת שירותים מיוחדים".

#### 3g. Other Bituach-Leumi-linked benefits

**Arnona discount:** 40% off municipal property tax for cancer patients with either (a) general disability pension at 75%+ earning-capacity loss, or (b) 90%+ medical disability. Auto-applied via NII lists, but verify with the municipality. Source: Kolzchut "הנחה בארנונה לחולי סרטן".

**Volunteer transport:** ICA runs a national volunteer-driver program for chemo/radiation appointments -- via Telemeda 1-800-599-995 or the oncology social worker. Reimbursement of out-of-pocket travel: ask the hospital social worker or ICA Rights Center.

### Step 4: Health basket coverage (drugs, exemptions, supportive services)

The basket covers far more than cancer drugs alone. **Full per-cancer-type detail** for sections 4b-4h is in `references/cancer-type-equity-rights.md`.

#### 4a. Cancer drugs in the 2026 basket

The **2026 basket** added 107 drugs and technologies at ₪650M total, of which ~₪337M (52%) went to oncology. Notable verified additions (full list in `references/health-basket-and-hmo-coverage.md`):
- **Solid tumors:** Imfinzi (bladder/gastric peri-op), Tagrisso (post-op EGFR NSCLC), Keytruda (head-and-neck; endometrial), Enhertu (HER2-low breast)
- **Hodgkin lymphoma:** Adcetris (first line)

Bispecific-antibody and ADC additions for R/R MM and lymphoma have been reported -- verify against the MOH 2026 PDF before quoting. Drugs in the basket are dispensed by the HMO at standard co-pay; no separate application needed. **For a drug NOT in the basket,** the patient needs either the HMO exceptions committee (Step 5) OR a supplementary-insurance payout (also Step 5).

#### 4b. Supportive services (apply across all cancer types)

- **Co-pay exemption (severe illness):** free specialist visits, imaging, diagnostics, dietitian. Auto-applied by HMO on diagnosis code; request with specialist letter if missing.
- **Dental treatment:** HMO covers 50% before chemo/radiation, 100% after (24-month window). **Head/neck radiation = no time limit. Jaw resection = full coverage incl. implants.**
- **Surgery wait-time + Form 17:** if HMO can't meet the legally-mandated wait window, contact מוקד הסדרים -- they have 24h to find a date or issue Form 17 (התחייבות) for any authorized facility.
- **Genetic testing (hereditary cancer):** BRCA, Lynch, Li-Fraumeni, FAP, MEN1/2, VHL, PTEN. Free for patients + first-degree relatives. Positive carriers get structured surveillance.
- **Home chemotherapy:** selected regimens delivered at home via HMO nurse or portable infuser pump. Ask the oncologist about regimen eligibility.
- **Medical cannabis (post-April 2024):** cancer patients need only a prescription from a certified physician -- no license process. ~₪186/year.
- **Post-surgical rehab and prosthetics:** site-specific (breast reconstruction, stoma supplies, voice/swallowing rehab, prosthetic limbs, continence supplies, cognitive rehab, wigs). Activate via HMO rehabilitation coordinator (רכז שיקום).

Sources for all: Kolzchut + ICA + gov.il -- full URLs in Reference Links.

### Step 5: HMO exceptions committee and supplementary insurance

#### 5a. Exceptions committee (ועדת חריגים)

Each HMO has a committee that reviews one-off requests to fund a drug or treatment outside the basket. Trigger: **formal refusal by the HMO** to fund the treatment.

Application package:
- Committee-review request form (from the HMO)
- Treating physician's detailed recommendation with medical literature and evidence that basket alternatives were exhausted
- All relevant medical records

Committee members: physicians (including oncologists), pharmacologist, legal advisor, economic advisor.

There is NO statutory response time. **Escalation ladder when refused** -- go in this order, NOT straight to court:

1. **Internal HMO appeals committee (ועדת ערר / בירורים)** -- fast, free, no lawyer required. Clalit example: https://www.clalit.co.il/he/info/Pages/berurim.aspx
2. **MOH Public Complaints Commissioner for the National Health Insurance Law** if internal appeal fails (12,809 inquiries handled in 2024)
3. **Regional Labor Court** -- request an interim order (צו ביניים) if life is at stake; these can issue within days

**Landmark precedent** to cite (full discussion: `references/exceptions-committee-precedents-and-appeals.md`): **חב"ר (ת"א) 5942-09-12** (Tel Aviv Regional Labor Court, October 2012, biliary-tract cancer) established that a drug's exclusion from the basket is not by itself grounds for refusal -- the exceptions committee must evaluate clinical efficacy, consider whether basket alternatives exist, and document budget arguments with calculations rather than assertions.

The **Patients' Rights Association** (https://www.patients-rights.org/) and **One in Nine** in-house attorney (03-602-1717 ext 2 for breast cancer) help with the package and representation. The **ICA Rights Center** is embedded in 10+ Israeli hospitals (rights helpdesk **03-5721678**, shikum@cancer.org.il) and specializes in NII rights, basket entitlements, exceptions committees, and Form 17.

#### 5b. Supplementary insurance (ביטוח משלים) -- cancer coverage by HMO

Each HMO sells a basic + top tier. Top tier covers non-basket oncology drugs (full table + 2025 caps in `references/health-basket-and-hmo-coverage.md`). Quick map:

| HMO | Top tier (where non-basket oncology coverage sits) |
|-----|---|
| Clalit | **Mushlam Platinum** -- up to ₪1M cap, includes drugs unregistered in Israel if registered in a recognized Western country |
| Maccabi | **Maccabi Sheli** -- up to ₪1M cap, drug must be registered in IL/US/CA/AU/NZ/CH/NO/IS/EU |
| Meuhedet | **Meuhedet Si (שיא)** -- broader off-label and non-basket coverage; verify regulations PDF for 2026 caps |
| Leumit | **Leumit Zahav (Gold)** -- life-extending oncology drug coverage historically offered; verify regulations PDF |

**Second opinion in Israel or abroad** is a supplementary benefit, NOT a basic-basket right -- only patients on the top tiers above have it.

### Step 6: Hospice and palliative care

Since **2009**, every HMO must provide supportive palliative care **24/7, free of charge under the basic basket** for patients with a life-threatening illness in the terminal stage (treating physician estimates 6 months or less). The team includes a physician, nurse, and social worker. It covers cancer and non-cancer terminal illnesses (end-stage heart, lung, kidney disease, dementia).

**How to access:** family doctor referral → HMO home-treatment unit (or the hospital HMO representative if the patient is hospitalized). Source: wikirefua, "Palliative Service (Hospice) Director General Circular"; Clalit "Home Hospice" page.

### Step 7: Fertility preservation and gonadal protection

Fertility-related rights apply across **all genders and pediatric/adult ages**. Two pathways:

**Preservation (basket-covered):**
- **Women:** egg, embryo, ovarian tissue freezing. Up to age 41 (birthday 42) or 2 children. Egg freezing capped at 4 cycles / 20 eggs total.
- **Men:** sperm banking before any gonadotoxic treatment (chemo, pelvic/testicular radiation, TBI). Multiple deposits recommended.
- **Children/adolescents:** ovarian tissue freezing (pre-pubertal girls); egg freezing (post-pubertal girls); sperm banking (post-pubertal boys); testicular tissue banking (pre-pubertal boys, experimental).

**Gonadal protection during treatment** (distinct from preservation):
- **Women:** GnRH agonists (Decapeptil / Triptorelin) suppress ovarian function during gonadotoxic chemo, reducing premature ovarian failure risk. Runs concurrent with chemo, does not delay treatment. Basket-covered.
- **Men:** testicular shielding during pelvic radiation when anatomically feasible.

**Time-critical.** All preservation must start BEFORE treatment begins -- even one cycle of chemo can foreclose options. Sources: gov.il "Oocyte cryopreservation"; Kolzchut "הקפאת ביצית, הפקדת זרע".

### Step 8: Work rights during cancer treatment

#### 8a. Patient's own sick leave and job protection

- **Sick leave (own illness):** Full sick pay from day 1 under the chronic-illness exception since June 2022 (see Step 3e).
- **Job protection:** The **Equal Rights for Persons with Disabilities Law, 1998 (section 8)** prohibits discrimination in hiring, promotion, dismissal, or employment conditions on the basis of disability. It applies to employers with **more than 25 employees**.
- **Resignation because of illness:** Under Severance Pay Law section 6, resignation forced by illness is treated as dismissal for severance purposes.
- **Reasonable accommodation:** Employers with more than 25 employees must make reasonable accommodations (adjusted hours, remote work, physical adjustments) unless it would be an undue burden. Escalation: the Commission for Equal Rights of Persons with Disabilities.

#### 8b. Family sick days for cancer caregiving

Cancer caregivers have entitlements deducted from their own accrued sick balance:
- **Spouse:** up to **60 sick days/year** for care of a spouse with cancer
- **Parent of a child under 18 with cancer:** up to **90/year** (110 if single parent / sole caregiver)

No employer pre-approval beyond standard sick-leave procedures. Sources: Kolzchut "ימי מחלה בגין טיפול בבן משפחה" + chemo rights guide. The base 8-day parent-sick-day rule (child to 16) is superseded by the cancer-specific cap above.

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
| Haverim LeRefuah | חברים לרפואה | **Free Pharmacy Project** -- collects unused prescription medications via 1,075+ collection points, redistributes free of charge to chronic patients including cancer patients. **"Save A Life" Funds** earmark donations for individual patient cases. | https://www.haverim.org.il/ |
| Yad Sarah | יד שרה | Medical-rehabilitative equipment loans via 100+ branches across Israel -- relevant for cancer patients in end-stage home care, post-surgical recovery, and long-term outpatient treatment. | https://www.kolzchut.org.il/he/%D7%99%D7%93_%D7%A9%D7%A8%D7%94 |
| Bracha | עמותת ברכה | **Hereditary cancer carriers.** Peer support, awareness, and surveillance guidance for BRCA1/BRCA2 carriers and other hereditary breast/ovarian cancer mutations. Founded 2009. | Guidestar registry: https://www.guidestar.org.il/organization/580508075 |
| Chali"l HaOr | חלי"ל האור | **Blood cancer patients (leukemia, lymphoma, myeloma, MDS).** Mentoring program (Maagilim) pairing veteran patients with new patients, psychological support funding, rights help with in-house lawyer + insurance agent, professional conferences, disease-specific support groups. | https://halil.org.il/ |

**Agent notes:** "Larger Than Life" in Hebrew is **גדולים מהחיים** (NOT "לרגיש שוב" -- common error). **Bracha's homepage 404s** -- verify via the Guidestar link and route content questions to Kolzchut hereditary-cancer pages or ICA BRCA section (https://www.cancer.org.il/subcategories/brca/). **Do NOT confuse Road to Recovery (theroadtorecovery.org.il) with general Israeli cancer transport** -- that org transports Palestinian patients from West Bank/Gaza to Israeli hospitals; for Israeli cancer transport, use ICA volunteers via Telemeda 1-800-599-995.

**Cancer-type routing:** breast → One in Nine + ICA. Hereditary → Bracha + ICA BRCA section. Pediatric → Larger Than Life + Zichron Menachem + Ezer Mizion. Hematological (leukemia/lymphoma/MM/MDS) → Chali"l HaOr + Ezer Mizion bone-marrow. All others → ICA + the oncology social worker for diagnosis-specific referrals. Transport → ICA volunteers. Equipment → ICA / Yad Sarah / Ezer Mizion. Full per-cancer-type breakdown: `references/cancer-type-equity-rights.md` section 11.

### Step 10: Experimental, off-label, and unregistered treatments

Patients with advanced or refractory cancer often hear phrases like "compassionate use", "Form 29c", "off-label", "expanded access", and "Named Patient Program" -- and these pathways are **not interchangeable**. Picking the wrong one wastes weeks.

**See `references/experimental-and-off-label-treatments.md` for the full reference -- the summary below is the decision-critical information.**

#### 10.1 Form 29c (טופס 29ג') -- individual import of an unregistered drug

- **Legal basis**: Regulation 29 of the Pharmacists Regulations (Preparations), 5746-1986. Patient-level application is Form 29c.
- **Who files**: the **treating physician** via the MOH **Pharmacy Division (אגף הרוקחות)**.
- **Requirements**: medical justification; drug registered in a recognized country for the same indication; no registered Israeli alternative.
- **CRITICAL**: **Form 29c is an import permit, NOT funding.** Funding must be secured separately (exceptions committee, supplementary, private, NGO). LLMs routinely say "file 29c and the HMO will pay" -- this is wrong.

#### 10.2 Compassionate use / טיפול חמלה

- Pharma company provides an unregistered/experimental drug **free of charge** with MOH pre-approval.
- **Three-party process**: physician → pharma sponsor → MOH Pharmacy Division.
- **Not a right** -- "לא קיימת חובה לספק". Companies can refuse.
- Different from a clinical trial (which has a protocol and Helsinki approval). Israel has no separate "Named Patient Program" category -- sponsor-provided experimental access is folded into טיפול חמלה.

#### 10.3 Off-label use

- Drug IS registered in Israel for one indication, prescribed for a different indication.
- **Legal** in Israel; basket generally does NOT fund off-label.
- **Exceptions committee** is the main public route.
- **Supplementary plans cover off-label within caps**:
  - Clalit Mushlam Gold/Platinum: package > ~₪356.98, 50% co-pay capped ~₪358/pack/month, monthly total ~₪713.97 (https://mushlam.clalit.co.il/he/medications/Pages/kisuy_murhav_trufot.aspx)
  - Maccabi Zahav: serious diseases, prior approval, 24-month waiting period (https://www.maccabi4u.co.il/eligibilites/4327/)
  - Meuhedet and Leumit have similar clauses -- verify the tier's regulations PDF
- **2008 reform boundary**: Israeli supplementary plans cannot cover life-saving/life-extending drugs as their primary benefit. Off-label clauses cover off-label and unregistered-indication scenarios only.

#### 10.4 Clinical trials

- **Legal basis**: People's Health Regulations (Medical Research on Human Subjects), 1980.
- **Helsinki committee** -- ethics for **research**, NOT the HMO funding exceptions committee. Institutional (per hospital) + National Supreme (elevated-risk categories).
- Find Israeli oncology trials: MyTrial (MOH) via https://www.gov.il/he/departments/general/clinical-trials-website and ClinicalTrials.gov filtered to Israel.
- **Sponsor pays** for investigational drug and trial-specific procedures; HMO continues standard of care.
- **Post-trial drug access** (MOH procedure 14, chapter 4) is NOT automatic -- raise with the PI before signing consent.

#### 10.5 Decision tree -- which route for which situation

| Situation | Route |
|-----------|-------|
| Drug is in the 2026 basket for my indication | Standard prescription; HMO dispenses at basket co-pay |
| Drug is registered in Israel for my indication but HMO refused funding | Exceptions committee (Section 5a) + supplementary if enrolled |
| Drug is registered in Israel for a DIFFERENT indication (off-label) | Supplementary plan's off-label clause FIRST (fastest), parallel exceptions committee |
| Drug is unregistered in Israel but registered abroad for my indication | Form 29c filed by physician + funding via exceptions / supplementary / private / NGO |
| Drug is still experimental (in Phase 2/3 trials, not registered anywhere yet) | טיפול חמלה -- physician finds a pharma sponsor, MOH pre-approval |
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

For an oncology patient, the right time to set this up is **before** terminal-stage capacity loss -- typically when starting late-line treatment for advanced disease. Two NGOs help with the paperwork:
- **LILACH (ליל"ך)** -- https://www.lilach.org.il/living_will/ -- leading Israeli end-of-life NGO
- **Ematai** -- https://www.ematai.org/netivotil/ -- bilingual (Hebrew/English) advance-care planning, faith-sensitive options

Source for the Dying Patient Law procedure: https://www.kolzchut.org.il/en/Registering_a_Living_Will

Coordinate this with the oncology social worker and the palliative-care team (Step 6) -- these conversations are part of standard advanced-disease care.

### Step 12: Do-NOT list for experimental pathways

Common agent and patient mistakes:

1. **Do NOT equate "Form 29c approved" with "HMO will pay".** Form 29c is an import permit. Funding is separate.
2. **Do NOT confuse טיפול חמלה with a clinical trial.** Compassionate use is individual and outside a protocol; a trial is structured and Helsinki-approved.
3. **Do NOT confuse the Helsinki committee (research ethics) with the exceptions committee (HMO funding).** LLMs swap these routinely. Helsinki = ניסויים; ועדת חריגים = מימון.
4. **Do NOT assume supplementary insurance covers life-saving drugs as the primary benefit.** The 2008 reform prohibited that. Supplementary covers off-label, unregistered-indication, and second opinions -- not life-saving oncology drugs as the headline benefit.
5. **Do NOT promise a patient post-trial access to the investigational drug.** It is negotiated per protocol and requires Helsinki + MOH sign-off.



## Examples

### Example 1: Newly diagnosed adult, starting chemo next week

"My wife was diagnosed with breast cancer; chemo starts next week."

1. **First call today**: oncology ward → oncology social worker (עו"ס אונקולוגי). They file paperwork for you free.
2. Social worker files **special services allowance 50% paper-only** (Step 3b) -- no committee visit needed for active chemo.
3. Check Section 9(5) tax exemption (Step 3d), sick-pay-from-day-1 (Step 3e), fertility preservation if relevant (Step 7).
4. Call **ICA Telemeda 1-800-599-995** for transport + rights help.
5. If a prescribed drug is not in the 2026 basket: check supplementary tier (Step 5b) + prepare exceptions-committee package (Step 5a). If a Bituach Leumi committee refusal arrives later, the **60-day appeal clock** starts (Step 3f).

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
4. Escalate via the **internal HMO appeals committee first**, then MoH Public Complaints Commissioner, then Regional Labor Court interim order if life is at stake (Step 5a). Cite the 5942-09-12 precedent.
5. Patients' Rights Association (patients-rights.org) and One in Nine attorney (03-602-1717 ext 2 for breast cancer) help with representation.

### Examples 4-6: Other cancer types

The skill includes worked examples for **colorectal cancer with stoma**, **pediatric leukemia**, **head and neck cancer starting radiation**, and **hereditary cancer (BRCA carrier without diagnosis)** in `references/cancer-type-equity-rights.md` section 12. Each example walks the same Step 0-9 sequence but with cancer-type-specific entitlements (stoma supplies, dental-before-radiation, BRCA surveillance program, pediatric fertility preservation).

The pattern across all three: oncology social worker first → Step 3 (Bituach Leumi) + Step 4 supportive services (co-pay, dental for head/neck, stoma supplies for colorectal, fertility for pediatric) → cancer-type-matched NGO from Step 9 (Halil HaOr for hematological, Bracha for hereditary, Larger Than Life for pediatric).

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

5. **Appeal window is 60 days, not 30 or 90.** Older skills and even some legal articles misstate this. The statutory window is **60 days** from receiving the written decision, for BOTH general disability (נכות כללית) and שר"מ committees. NII does not reject filings within 90 days as informal grace, but never rely on it. Filing a partial appeal on time preserves the right and extends the deadline for reasons by 30 more days.

6. **שר"מ 50% is the starting point, not the ceiling.** Agents tell active-treatment patients "50% is what you get" and stop. Patients with significant functional impairment qualify for **112% (₪4,501)** or **188% (₪7,181)** through a committee. The difference between 50% and 188% is over ₪62,000/year. After 6 months on the paper track, always re-assess. Use the ADL framework in Step 3b-ii; the ICA Rights Center and NGO attorneys build the evidence package.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kolzchut -- Cancer Patients (EN) | https://www.kolzchut.org.il/en/Cancer_Patients | Authoritative consolidated rights entry point |
| Kolzchut -- Special Services Allowance | https://www.kolzchut.org.il/en/Special_Services_Benefit_(Attendance_Allowance) | Full 4-rate table (50/112/188/235), child-under-3 supplement, ADL committee process |
| Kolzchut -- Rights Guide for Chemotherapy Patients | https://www.kolzchut.org.il/en/Rights_Guide_for_Chemotherapy_Patients | Family sick days, home chemotherapy, work rights for cancer patients |
| Bituach Leumi -- Disability Pension Amounts | https://www.btl.gov.il/benefits/Disability/Pages/%D7%A9%D7%99%D7%A2%D7%95%D7%A8%D7%99%20%D7%94%D7%A7%D7%A6%D7%91%D7%94.aspx | 2026 monthly amounts by earning-capacity loss percentage |
| Bituach Leumi -- 2026 Rate Update | https://www.btl.gov.il/About/news/Pages/hadasaidkonkitzva2026.aspx | Annual rate update announcement |
| Bituach Leumi -- Disabled Child (Malignancy) | https://www.btl.gov.il/benefits/Disabled_Child/likuilist/Pages/cancer.aspx | Pediatric cancer child-nechha eligibility and rates |
| Kolzchut -- Appealing General Disability Decision (EN) | https://www.kolzchut.org.il/en/Appealing_a_General_Disability_Medical_Committee_Decision | 60-day appeal window, process, representation rules |
| Kolzchut -- Appealing Special Services Decision (EN) | https://www.kolzchut.org.il/en/Appealing_a_Special_Services_Benefit_(Attendance_Allowance)_Decision | 60-day שר"מ appeal window |
| Kolzchut -- Health Plan Fee Exemptions for the Seriously Ill | https://www.kolzchut.org.il/en/Health_Plan_Fee_Exemptions_for_the_Seriously_Ill | Co-pay exemption scope for cancer patients (Step 4b) |
| Kolzchut -- Municipal Property Tax (Arnona) Discount for Cancer Patients | https://www.kolzchut.org.il/en/Municipal_Property_Tax_(Arnona)_Discount_for_Cancer_Patients | 40% arnona discount eligibility (Step 3g) |
| ICA -- Medical Cannabis for Cancer Patients | https://www.cancer.org.il/articles/13264/ | Post-April-2024 reform: prescription-only flow for cancer patients (Step 4g) |
| Halil HaOr (חלי"ל האור) | https://halil.org.il/ | Blood-cancer patient organization for leukemia, lymphoma, MM (Step 9) |
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
Solution: File a written appeal within **60 days** to the Medical Appeals Committee (ועדה רפואית לעררים) -- same window for general disability (נכות כללית) and שר"מ committees. The patient may be represented by a lawyer or social worker. Strengthen the appeal with: the treating oncologist's detailed functional assessment, an occupational-therapy report, and evidence of worst-case days (not best). Bituach Leumi in practice accepts filings up to 90 days as informal grace, but do not rely on this window.

### Problem: "My prescribed drug is not in the 2026 basket and the HMO refused to fund it"
Cause: Drug is not yet in the basket, or is in the basket but for a different indication, or the HMO's internal protocol rejected it.
Solution: Two parallel tracks. (1) **Exceptions committee** (Step 5a): ask for a written refusal, then submit a committee-review package (oncologist recommendation with medical literature, proof basket alternatives were tried, medical records). (2) **Supplementary insurance** (Step 5b) if enrolled in Mushlam Platinum, Maccabi Sheli, Meuhedet Si, or Leumit Gold -- check the plan's non-basket oncology-drug cap and foreign-registration rules. Route through the hospital oncology social worker and optionally the Patients' Rights Association for exceptions-committee representation.

### Problem: "I want to preserve fertility but I am over 41" or "My employer pressured me to resign during treatment"
Both cases are handled in the relevant step (Step 7 fertility, Step 8 work rights). Route to the oncology social worker first; for fertility specifically the HMO fertility unit can discuss private/supplementary options without delaying treatment; for work rights the ICA rights helpdesk (03-5721678) refers to employment counsel.
