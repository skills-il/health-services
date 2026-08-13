---
name: israeli-oncology-navigator
description: "Bureaucracy navigator for cancer patients and caregivers in Israel. Covers Bituach Leumi (disability, 4-rate שר\"מ table 50/112/188/235%, pediatric ילד נכה, Section 9(5) tax exemption, arnona, vocational rehabilitation, occupational-cancer work-injury track, appeal windows of 60 days for נכות כללית and 90 days for שר\"מ); the 2026 health basket (drugs, exceptions committee, severe-illness co-pay exemption, dental funding, surgery wait-time and Form 17, hereditary-cancer genetic testing, home chemo, medical cannabis, statutory travel reimbursement, hospital parking exemption, post-surgical rehab and wigs); supplementary tiers; palliative care; fertility preservation; family caregiver sick days; cancer-type NGOs; experimental, off-label and treatment-abroad pathways. Use when a patient or caregiver needs to understand entitlements, file applications, or appeal a refusal. Do NOT use for medical diagnosis, treatment decisions, drug dosing, or non-Israeli healthcare systems."
license: MIT
---

# Israeli Oncology Navigator

## Critical Disclaimer

**Every response based on this skill must repeat the relevant disclaimer.**

This is a **bureaucracy navigator**, not medical or legal advice.

1. **Route the user to the oncology social worker (עו"ס אונקולוגי) first.** They file most Bituach Leumi paperwork free. Sending a patient to the Bituach Leumi website first is a failure mode.
2. **Never give medical advice.** Treatment, dosing and clinical questions go to the oncologist.
3. **Figures are 2026 values** and change every January. Cite the year and the source URL.
4. **שב"ן caps vary by tier and renewal date.** The patient must read their own תקנון PDF before acting on a figure.
5. **Never invent a law section, form number, court citation or amount.** If you cannot verify it, say so plainly.

## Problem

A cancer diagnosis in Israel triggers weeks of bureaucracy at the worst possible time. Entitlements are split across **five systems** that do not talk to each other: Bituach Leumi, the health basket, the HMO supplementary plan, the Tax Authority plus Ministry of Transport (Section 9(5), תג חניה, pension withdrawal), and Ministry of Health rules on parking and wait times, plus dozens of NGOs with overlapping eligibility. Families discover entitlements months late or lose a valid claim to a missed deadline. This skill consolidates the map and routes hard decisions to the oncology social worker.

## Instructions

### Step 0: Route to the hospital oncology social worker FIRST

> Your first call, before Bituach Leumi and before the NGOs, is the **oncology social worker (עו"ס אונקולוגי)** at the treating hospital. They hold the current forms, file most Bituach Leumi claims for you at no cost, and refer to the right NGO. Ask the ward or switchboard for "the oncology social worker".

If the patient is hospitalized, Bituach Leumi's **"מחלקה ראשונה"** service lets the hospital social worker file the נכות כללית and שר"מ claims with the medical file, no branch visit. In parallel: **Kolzchut**, https://www.kolzchut.org.il, and the **ICA Telemeda** free line, Hebrew 1-800-599-995 / Arabic 1-800-36-36-55 / Russian 1-800-34-33-44. Bituach Leumi's **יד מכוונת** (*2496) prepares claimants for committees free.

### Step 1: Assess which track applies

| Situation | Relevant Steps |
|-----------|----------------|
| Just diagnosed, active treatment | 2, 3, 4, 7 |
| Child diagnosed with cancer | 3c, 7, 9 |
| Drug NOT in the 2026 basket, or a refusal | 4a, 5 |
| Co-pay, dental, wait-time, home chemo, cannabis, rehab, genetic testing | 4b |
| Terminal stage | 6, 11 |
| Caregiver sick days; work threats or accommodations | 8 |
| Arnona, travel costs, hospital parking, תג חניה | 3g |
| Workplace-caused cancer; cannot return to the old job | 3h |
| Clinical trial or treatment abroad | 10 |
| NGO support | 9 |

### Step 2: Nechut Refuit (medical disability) -- paper track for active patients

**Cancer does not set a fixed disability percentage.** A medical committee (ועדה רפואית) determines it per cancer type, stage and treatment. But:

**Paper-only track:** a patient receiving a drug **from the closed list Bituach Leumi publishes, administered intravenously** (`ולא בטיפול פומי`, so oral regimens are excluded) gets **50% of the special services allowance for six months on medical documents alone**, no committee appearance. A regimen outside that list means a dependency committee instead, so check the list rather than promising the paper track. The oncology social worker files it.

When treatment ends, submit updated documents on the physical and psychological after-effects so eligibility can be re-examined. There is no automatic continuation period.

### Step 3: Bituach Leumi core entitlements

#### 3a. General disability pension (קצבת נכות כללית) -- 2026 amounts

Eligible when medical disability is at least 60%, **or at least 40% where one single impairment is 25% or more**, AND earning-capacity loss is at least 50%. A married woman who has not worked 12 consecutive months in the last 48 is assessed on the **housewife track**: 50% medical disability plus **50%** loss of ability to function in the household, not 75%.

| Earning-capacity loss | Monthly (individual) | With spouse supplement |
|-----------------------|----------------------|------------------------|
| 100% / 75% (full rate) | ₪4,711 | ₪6,229 |
| 74% | ₪3,211 | ₪4,334 |
| 65% | ₪2,894 | ₪3,881 |
| 60% | ₪2,718 | ₪3,629 |

The spouse supplement (₪1,518 / ₪1,123 / ₪987 / ₪911) is **conditional**: the spouse's gross monthly income must not exceed **₪7,848** and the spouse must not receive another allowance. A child supplement is paid separately for the first two children. Effective 01.01.2026, indexed annually.

#### 3b. Special services allowance (גמלת שירותים מיוחדים / שר"מ)

Monthly cash benefit for adults needing help with daily activities. **Age limit: from 18 to retirement age.** Anyone already eligible on the day they reach retirement age keeps the allowance; a first claim is accepted up to six months after retirement age. Four rates (2026):

| Situation | Rate | Monthly |
|-----------|------|---------|
| Listed IV chemo / biological treatment, active (paper only) | 50% | ₪1,943 |
| Help with ALL ADLs most hours, OR constant supervision | 112% | ₪4,501 |
| Help with ALL ADLs all hours | 188% | ₪7,181 |
| Home or inpatient hospice (terminal) | 235% | ₪9,126 |

**50% is the starting point, not the ceiling.** After the six-month minimum, Bituach Leumi may summon a review or the patient may self-request a higher rate. Patients with severe side effects (neutropenia isolation, neuropathy, fatigue, incontinence, cognitive fog) **are assessed under the ADL framework** and may reach 112% or 188%; the gap between 50% and 188% is over ₪62,000 a year.

**Child-under-3 supplement:** ₪1,215/month per child, maximum 2 children = **₪2,430/month**. Secondary sources say שר"מ and גמלת סיעוד cannot be held at once; check that with Bituach Leumi rather than stating it.

**Committee prep:** six ADL categories plus a constant-supervision criterion. **Evaluate on worst-case days, not averages** (for a chemo patient, cycle days 1-7). Mapping and the document checklist are in `references/sherum-committee-preparation.md`. One in Nine's attorney (03-602-1717 ext 2) and the ICA Rights Center build the evidence package.

#### 3c. Disabled-child allowance for pediatric cancer (גמלת ילד נכה)

Eligible from birth to age 18 years and 3 months. Rates (2026):

| Situation | Rate | Monthly |
|-----------|------|---------|
| During **chemotherapy** | 235% | ₪9,126 |
| **First** month after chemotherapy ends | 235% | ₪9,126 |
| The **following five** months | 100% | ₪3,820 |
| Active disease on biological treatment | 100% | ₪3,820 (6 months minimum, or duration of treatment) |
| Non-active disease on biological treatment | 50% | ₪1,943 (one year) |

The 100% rate continues beyond those five months if the child has a prolonged, permanent, severe condition caused by the treatment. The source names chemotherapy, not radiation; a child on radiation alone may qualify under other criteria, so check rather than assume.

#### 3d. Income tax exemption -- Section 9(5) of the Income Tax Ordinance

Threshold: a Bituach Leumi or Ministry of Finance medical committee determined **at least 90% medical disability, permanent or for 185 days or more**. Patients who had tumour-removal surgery followed by chemo or radiation often qualify. The route is **טופס 169 with a fee of roughly ₪679** filed with the פקיד שומה. ("גל ירוק" is a narrow Tax Authority fast-track, not the name of this route.)

#### 3e. Sick pay from day 1

Narrow and often overstated. Since 1 June 2022, an employee with a **malignant illness or an illness requiring permanent dialysis** who is absent **for periodic treatment or periodic tests** relating to that illness is entitled to sick pay **from the first day of absence**, overriding the 0/50/50/100 ladder, on presenting a written medical certificate. It is charged to the accrued sick-day balance and does not cover absence for unrelated reasons. Source: חוק דמי מחלה, תשל"ו-1976, סעיף 2(א1).

#### 3f. Right to appeal (ערר) -- two different windows

The two tracks are **not** the same. Getting this wrong costs the claim.

| Decision | Window | Body |
|----------|--------|------|
| נכות כללית medical committee | **60 days** | ועדה רפואית לעררים |
| שר"מ decision (amount, rejection, start date) | **90 days** | **ועדת עררים לשירותים מיוחדים** (a separate body) |
| Claim rejected on a statutory ground only | 12 months | Regional Labour Court |

For שר"מ: `ערר מנומק בכתב יש להגיש בתוך 90 יום מיום שהתקבל מכתב ההחלטה`, filed at the local branch. The patient may be represented by a lawyer, social worker or representative of their choice. Do not carry over the "partial appeal now, reasons within 30 more days" rule -- that belongs to נכות מעבודה.

#### 3g. Arnona, travel, parking

**Arnona discount** (תקנות ההסדרים במשק המדינה (הנחה מארנונה), התשנ"ג-1993, תקנה 2). Municipalities are *permitted*, not obliged, and set the actual rate. These are ceilings (`הנחה שאינה עולה על`) on up to 100 m²: **up to 80%** on a full disability pension with 75%+ earning-capacity loss; **up to 40%** with 90%+ medical disability and no pension; 33% for a parent of a child on גמלת ילד נכה. Apply to the מדור להנחות מיוחדות with a Bituach Leumi certificate. Between the medical determination and the start of the pension, the 40% band can already be claimed.

**Travel costs are a statutory HMO obligation**, not a favour. Section 28 of the second addendum to the National Health Insurance Law: `חולה אונקלוגי או חולה דיאליזה הנוסע לטיפול בבית חולים יקבל החזר כספי מלא של הוצאות הנסיעה מביתו לביה"ח ובחזרה בגובה דמי תחבורה ציבורית. חולה כנ"ל המוסע באמבולנס או במונית יקבל החזר של 50% מן ההוצאה`. Full public-transport fare both ways, 50% for taxi or ambulance. **A private car is not in the statute**, so do not promise mileage. Claim through the HMO. Travelling two or three times a week for months is among the largest out-of-pocket costs and least-claimed rights. ICA also runs a volunteer-driver programme via Telemeda 1-800-599-995.

**Hospital parking:** at **government general hospitals** the Ministry of Health caps parking at ₪25 per 24 hours and grants a **full exemption for one vehicle** to oncology patients in chemotherapy or radiation **and their escorts** (also dialysis patients, parents of premature babies, תג חניה holders). Other hospitals set their own arrangements, so ask on site. **תג חניה לנכה** and reduced licensing fees are separate Ministry of Transport entitlements.

#### 3h. Two tracks the skill's users most often miss

**Occupational cancer (מחלת מקצוע / נפגעי עבודה).** If the cancer is plausibly linked to workplace exposure (asbestos, benzene, ionising radiation, certain solvents), file under the **work-injury** branch, not נכות כללית. The threshold is far lower and it pays more: a permanent work-injury **pension starts at 20% medical disability** (9-19.99% gets a lump sum), against 60% plus a 50% earning-capacity loss for נכות כללית. Raise it at diagnosis, while the occupational history is easy to document.

**Vocational rehabilitation (שיקום מקצועי).** Open to anyone a Bituach Leumi committee assessed at **at least 20% disability**, aged 18 to retirement age, who cannot return to their previous work. **It does not require receiving a disability pension.** It funds occupational assessment, academic or vocational tuition, travel, books, equipment, rent, subsistence, accessibility supports and job placement. Studying **at least 16 hours a week** also brings **דמי שיקום**, equal for a non-pensioner to the pension at the 100% rate (work income under ₪8,261), plus exemption from HMO fees for specialists, outpatient clinics and hospital referrals. This is the whole survivorship lane and it is almost never mentioned at discharge.

### Step 4: Health basket coverage

Full per-cancer-type detail for 4b is in `references/cancer-type-equity-rights.md`.

#### 4a. Cancer drugs in the 2026 basket

The 2026 basket added 107 drugs and technologies at ₪650M, roughly ₪337M of it oncology. Indications are narrow and a drug can be in the basket for a different stage than the patient's, so before saying a named drug is "in the basket", open MOH circular 2/2026 or the 2026 list PDF, search by **generic** name, and read the indication. Two commonly misstated 2026 entries:

- **Tagrisso (osimertinib)** was added for **unresectable locally advanced stage III NSCLC that has not progressed after platinum-based chemoradiation** (EGFR ex19del or ex21 L858R): `בשלב מתקדם מקומי לא נתיח (שלב III) שמחלתו לא התקדמה במהלך או לאחר טיפול משולב או עוקב של כימותרפיה מבוססת פלטינום והקרנות`. This is **not** the adjuvant post-resection setting, which is a separate, older entry. The patient receives osimertinib or durvalumab, not both.
- **Pluvicto (lutetium-177 vipivotide tetraxetan)**, the first radioligand therapy in the basket, for **PSMA-positive metastatic castration-resistant prostate cancer after both an androgen-receptor inhibitor and taxane chemotherapy**, SUV 10 or more, **maximum 6 cycles**, on an oncologist's prescription. Patients routinely assume this one is not funded.

Basket drugs are dispensed at standard co-pay with no separate application. For a drug not in the basket, see Step 5.

#### 4b. Supportive services (all cancer types)

- **Co-pay exemption (severe illness):** specialist visits, outpatient clinics, imaging, diagnostics. The HMOs list it as something to **apply for** with a specialist letter confirming the diagnosis, so do not tell a patient it is automatic.
- **Dental treatment:** 50% before chemo/radiation, 100% after, referral within **24 months** of the end of treatment. **Head/neck radiation: no time limit. Jaw resection for a tumour: full coverage including implants.**
- **Surgery wait-time + Form 17:** oncology surgery is capped at **30 days** under MOH circular מנהל רפואה 1/2020. There is **no blanket guarantee for elective surgery generally**. If the HMO cannot meet the window, מוקד הסדרים has 24 hours to find a date or issue **Form 17 (התחייבות)** for any authorised facility.
- **Genetic testing:** BRCA, Lynch, Li-Fraumeni, FAP, MEN1/2, VHL, PTEN, for patients and first-degree relatives of known carriers, with structured surveillance for carriers.
- **Home chemotherapy:** selected regimens via HMO nurse through an existing port, or a portable pump.
- **Medical cannabis (post-April 2024):** cancer patients need only a prescription from a certified physician, no licence process. Annual prescription fee **₪192** (the licence track, for other indications, is ₪384).
- **Rehab and prosthetics:** site-specific (breast reconstruction and external prosthesis, lymphoedema garments, stoma supplies, voice and swallowing rehab, limb prostheses, continence supplies, cognitive rehab). **Wigs are HMO-funded**; ICA also lends and fits them. Activate via the HMO rehabilitation coordinator (רכז שיקום).

### Step 5: HMO exceptions committee and supplementary insurance

#### 5a. Exceptions committee (ועדת חריגים)

Reviews one-off requests to fund a treatment outside the basket. Trigger: a **written refusal**. Package: the committee form, the physician's recommendation with medical literature and evidence that basket alternatives were exhausted, and the medical records. There is **no statutory response time**.

**Escalation when refused**, in this order and not straight to court: (1) the **internal HMO appeals committee (ועדת ערר / בירורים)**, fast, free, no lawyer; (2) the **MOH Public Complaints Commissioner** for the National Health Insurance Law (12,809 inquiries concluded in 2024); (3) the **Regional Labour Court**, where an interim order (צו ביניים) can issue within days if life is at stake.

Labour Court case law holds that exclusion from the basket is not by itself a ground for refusal: the committee must assess clinical efficacy for this patient, consider basket alternatives, and support a budget argument with calculations rather than assertions. Ask a lawyer for the current authorities rather than citing a case number from memory. See `references/exceptions-committee-precedents-and-appeals.md`. The **Patients' Rights Association** and the **ICA Rights Center** (Telemeda 1-800-599-995) help build the package.

#### 5b. Second opinion, and supplementary insurance (ביטוח משלים)

**A second opinion is a statutory right for every patient, on the basic basket, with no supplementary plan required.** חוק זכויות החולה, התשנ"ו-1996, סעיף 7: `מטופל זכאי להשיג מיוזמתו דעה נוספת לענין הטיפול בו; המטפל והמוסד הרפואי יסייעו למטופל בכל הדרוש למימוש זכות זו`. What the top שב"ן tiers add is **funding and free choice of a private consultant**, not the right itself. Never tell a basic-basket patient they have no second-opinion right.

Non-basket oncology coverage sits on the top tier: **Clalit Mushlam Platinum**, **Maccabi Sheli**, **Meuhedet Si (שיא)**, **Leumit Zahav**. Caps for non-basket oncology drugs run into the **millions of shekels per insured**, are launch-year figures indexed annually, and differ per tier; Clalit's also carries a רצף טיפולי exception. Foreign-registration rules differ per plan, and Clalit's condition is that the drug is `רשומות בישראל או שהוגשה בקשה לרישומן`. **Never quote a cap or a list of recognised countries from memory. Open the tier's תקנון PDF.**

### Step 6: Hospice and palliative care

Since **2009** every HMO must provide supportive palliative care **24/7, free under the basic basket**, to patients with a life-threatening illness in the terminal stage (physician estimates six months or less). The team is physician, nurse and social worker, and it covers non-cancer terminal illness too. Access via family doctor referral to the HMO home-treatment unit, or the hospital HMO representative if admitted.

### Step 7: Fertility preservation and gonadal protection

Applies across **all genders and all ages**, and is **time-critical**: one cycle of chemotherapy can foreclose options, so the referral to the HMO fertility unit must not wait.

**Preservation (basket-covered):**
- **Women:** egg, embryo and ovarian tissue freezing, up to age 41 (the 42nd birthday) or two children, whichever first. Egg freezing capped at 4 cycles / 20 eggs.
- **Men:** sperm banking before any gonadotoxic treatment (chemotherapy, pelvic or testicular radiation, TBI). The number of deposits is a decision for the fertility unit.
- **Children and adolescents:** ovarian tissue freezing (pre-pubertal girls), egg freezing (post-pubertal girls), sperm banking (post-pubertal boys), testicular tissue banking (pre-pubertal boys, experimental).

**Gonadal protection during treatment** is a different thing. Testicular shielding during pelvic radiation is used where anatomically feasible. GnRH agonists are sometimes discussed for ovarian protection during chemotherapy; **their Israeli registration is for other indications, so this use is off-label and is not basket-funded for it.** Never let a patient forgo preservation believing protection is covered.

### Step 8: Work rights during treatment

#### 8a. Sick leave and job protection

- **Sick leave:** see Step 3e for the narrow day-1 rule.
- **Non-discrimination and accommodations:** the **Equal Rights for Persons with Disabilities Law, 1998, section 8** bars discrimination in hiring, conditions, promotion, training, dismissal and severance, and defines discrimination to *include* failing to make the accommodations a disabled employee needs (`"הפליה" - לרבות אי-ביצוע התאמות הנדרשות מחמת צרכיו המיוחדים של אדם עם מוגבלות אשר יאפשרו את העסקתו`). Section 8 has **no employee-count threshold**; the only limit is נטל כבד מדי. It also extends to family members caring for a disabled person. **Section 9** is a different duty, to promote proper representation, and *that* one applies only to an employer with **more than 25 employees**. Do not import the 25-employee threshold into the individual accommodation right.
- **Resignation because of illness:** under Severance Pay Law section 6, resignation forced by illness counts as dismissal for severance.
- **Escalation:** Commission for Equal Rights of Persons with Disabilities, *6763.

#### 8b. Family sick days for cancer caregiving

These are **not extra days.** Statute lets the caregiver charge the absence `על חשבון תקופת המחלה הצבורה שלו או על חשבון ימי החופשה המגיעים לו, לפי בחירת העובד` -- their own accrued sick or vacation balance. The figures are annual ceilings on that balance, and the trigger is **מחלה ממארת or an illness requiring permanent dialysis** generally, not cancer specifically. Both need at least one year with the employer.

- **Spouse:** up to **60 days/year** (חוק דמי מחלה (היעדרות בשל מחלת בן זוג), התשנ"ח-1998, סעיף 1א).
- **Parent of a child under 18:** up to **90 days/year**, or **110** where the employee is a sole caregiver, a single parent, or has sole custody (חוק דמי מחלה (היעדרות בשל מחלת ילד), התשנ"ג-1993, סעיף 1א).

Days taken under the general 6-to-8-day rules count toward these ceilings.

### Step 9: NGOs and support services

Never say "contact an NGO" without naming one. See `references/ngos-and-support-services.md`.

| Focus | Organisation |
|-------|--------------|
| All cancers, all ages; transport, wigs, lodging, rights desk | **ICA (האגודה למלחמה בסרטן)** https://www.cancer.org.il/, Telemeda 1-800-599-995 |
| Pediatric | **גדולים מהחיים** https://gdolim.org.il/, **עמותת חיים** https://www.hayim.org.il/, **זכרון מנחם** https://zichron.org/ |
| Young adults | **חלאסרטן** https://www.stop-cancer.co.il/ |
| Breast | **אחת מתשע** https://www.onein9.org.il/ |
| Hereditary carriers | **עמותת ברכה** + ICA BRCA https://www.cancer.org.il/subcategories/brca/ |
| Blood cancers | **חלי"ל האור** https://halil.org.il/ |
| Marrow registry, lodging | **Ezer Mizion** https://ezermizion.org/ |
| Rights representation | **Patients' Rights Association** https://www.patients-rights.org/ |
| Free leftover medication | **חברים לרפואה** https://www.haverim.org.il/ |
| Equipment loans | **יד שרה** |

**Agent notes:** Larger Than Life in Hebrew is **גדולים מהחיים**, NOT "לרגיש שוב". **Bracha's homepage 404s** -- verify via Guidestar. **Road to Recovery** (theroadtorecovery.org.il) is not Israeli cancer transport; it transports Palestinian patients.

### Step 10: Experimental, off-label and unregistered treatments

"Compassionate use", "Form 29c", "off-label" and "expanded access" are **not interchangeable**, and the wrong one wastes weeks. Full reference: `references/experimental-and-off-label-treatments.md`.

#### 10.1 Form 29c (טופס 29ג') -- individual import of an unregistered drug

- **Legal basis:** תקנה 29(ג) of the Pharmacists Regulations (Preparations), 5746-1986.
- **Who files:** the application to the MOH Pharmacy Division (אגף הרוקחות) is filed by the **importer's responsible pharmacist**; the treating physician signs the clinical justification but is not the filer.
- **Requirements:** medical justification, registration in a recognised country for the same indication, no registered Israeli alternative.
- **CRITICAL: it is an import permit, NOT funding.** Funding is separate. "File 29c and the HMO will pay" is wrong.

#### 10.2 Compassionate use (טיפול חמלה) and off-label

**טיפול חמלה:** the manufacturer supplies an unregistered or experimental drug **free** with MOH pre-approval, in a three-party process (physician, sponsor, Pharmacy Division). **Not a right** -- `לא קיימת חובה לספק`, and companies do refuse. Different from a clinical trial. Israel has no separate "Named Patient Program".

**Off-label:** the drug IS registered here for one indication and is prescribed for another. **Legal**; the basket generally does not fund it, so the **exceptions committee** is the main public route. Supplementary off-label clauses differ per tier in co-pay, cap and waiting period -- verify the תקנון PDF rather than quoting a figure.

#### 10.3 Clinical trials

Legal basis: People's Health Regulations (Medical Research on Human Subjects), 1980. The **Helsinki committee** is research ethics, **NOT** the HMO exceptions committee; it is institutional per hospital plus a National Supreme committee for elevated-risk categories. Search **MyTrial** (MOH) and ClinicalTrials.gov filtered to Israel. The **sponsor pays** for the investigational drug and trial-specific procedures while the HMO continues standard of care. **Post-trial access is not automatic and no published entitlement guarantees it.** Continued supply depends on the sponsor and protocol: settle it in writing with the principal investigator **before** signing consent.

#### 10.4 Decision tree

| Situation | Route |
|-----------|-------|
| In the basket for my indication | Prescription at basket co-pay |
| Registered in Israel for my indication, HMO refused | Exceptions committee (5a) + supplementary |
| Registered for a DIFFERENT indication | Supplementary off-label clause first, exceptions committee in parallel |
| Unregistered here, registered abroad for my indication | Form 29c + separate funding |
| Still experimental | טיפול חמלה, sponsor plus MOH pre-approval |
| A trial I might qualify for | MyTrial + oncologist referral + Helsinki enrolment |

#### 10.5 Treatment abroad funded by the basket

Governed by תקנות ביטוח בריאות ממלכתי (שירותי בריאות במדינות חוץ), התשנ"ה-1995. Covered when both: the insured cannot receive the treatment or a reasonable alternative in Israel, AND it is **life-saving**. Permitted fields include **tumours** explicitly, subject to a **ceiling of USD 250,000**. Apply to the HMO; on refusal, appeal to its internal appeals committee.

The regulations fund the **medical treatment**. Flights, accommodation, food and an escort are **not** part of the statutory entitlement. Where they are covered it is under a שב"ן plan, so check the tier and do not attribute them to the 1995 regulations.

#### 10.6 Proton therapy and CAR-T

**Proton therapy:** availability in Israel is changing and any blanket statement dates fast. There is **no routinely funded proton-therapy service**; where local access exists it is limited and not a substitute for the treatment-abroad track (10.5). **Verify current status with the treating hospital** before telling a patient either that it is available or that it is not. **CAR-T** is delivered at several major Israeli centres; rather than a list that goes stale, ask the treating department about availability and referral paths.

### Step 11: Advance directives (Dying Patient Law, 2005)

Advance medical directives (הנחיות רפואיות מקדימות) become operative only when both (a) the patient is defined as terminally ill with under six months' life expectancy and (b) capacity is lost. Registered with the Ministry of Health. The right time is **before** capacity loss, typically when starting late-line treatment. **LILACH (ליל"ך)** https://www.lilach.org.il/living_will/ and **Ematai** https://www.ematai.org/netivotil/ help with the paperwork. Coordinate with the social worker and the palliative team (Step 6).

## Examples

### Example 1: Newly diagnosed adult, chemo next week

1. **Today:** the oncology social worker.
2. Social worker files **שר"מ 50% on documents** if the regimen is on the IV list (2).
3. Check Section 9(5) (3d), sick pay (3e), fertility preservation (7), travel reimbursement and parking exemption (3g).
4. Call **ICA Telemeda 1-800-599-995** for transport and rights help.
5. If a drug is not in the basket: check the שב"ן tier (5b), prepare the exceptions package (5a). On refusal note which clock started: **60 days** נכות כללית, **90 days** שר"מ (3f).

### Example 2: Pediatric diagnosis

1. Pediatric oncology social worker first.
2. **גמלת ילד נכה at 235% = ₪9,126** during chemotherapy, still 235% for the **first** month after it ends, then 100% = ₪3,820 for five months (3c).
3. Parent sick days: up to 90/year from the parent's own accrued balance, 110 if sole caregiver (8b). NGOs and fertility preservation before treatment starts (7, 9).

### Example 3: HMO refused a drug

1. Get the **written refusal**, then build the exceptions package (5a).
2. Check the שב"ן tier and read its תקנון PDF for the actual cap (5b).
3. Escalate: internal appeals committee, MOH Commissioner, then a Labour Court interim order if life is at stake.
4. A **second opinion is a statutory right on the basic basket** (5b). Patients' Rights Association and One in Nine (03-602-1717 ext 2) assist with representation.

### Examples 4-6

Worked examples for **colorectal cancer with a stoma**, **head and neck cancer starting radiation**, and **a BRCA carrier without a diagnosis** are in `references/cancer-type-equity-rights.md` section 12.

## Bundled Resources

- `references/bituach-leumi-oncology-rights.md` -- nechut, שר"מ, ילד נכה, tax, appeals.
- `references/health-basket-and-hmo-coverage.md` -- basket, exceptions committee, שב"ן.
- `references/cancer-type-equity-rights.md` -- per-cancer-type entitlements, worked examples.
- `references/exceptions-committee-precedents-and-appeals.md` -- escalation, package assembly.
- `references/experimental-and-off-label-treatments.md` -- 29c, חמלה, off-label, trials, abroad.
- `references/sherum-committee-preparation.md` -- ADL mapping, document checklist.
- `references/ngos-and-support-services.md` -- NGO list and contact channels.

## Recommended MCP Servers

[Kolzchut](https://agentskills.co.il/he/mcp/kolzchut) for rights articles, [Israel Drugs](https://agentskills.co.il/he/mcp/israel-drugs) for basket status and indications, [IL Health](https://agentskills.co.il/he/mcp/il-health) for MOH and HMO data, [Israel Medical Research](https://agentskills.co.il/he/mcp/israel-medical-research) for Israeli oncology research.

## Gotchas

1. **Never send an active-treatment patient to book a committee.** The 50% שר"מ rate is granted on documents for six months if the regimen is on the IV list.
2. **A second opinion is a statutory right for every patient** (חוק זכויות החולה סעיף 7). שב"ן adds funding and choice of consultant, not the right. The opposite claim is wrong.
3. **The appeal windows differ: 60 days for נכות כללית, 90 days for שר"מ, to a different body.** Sources giving one number for both are wrong.
4. **Caregiver sick days come out of the caregiver's own accrued balance.** 60/90/110 are ceilings, not a separate budget.
5. **The 25-employee threshold belongs to section 9 (representation), not to the individual accommodation right under section 8**, which has no size threshold.
6. **Arnona is up to 80% with a full pension, up to 40% on medical disability alone**, and the municipality sets the rate.
7. **Do NOT equate "Form 29c approved" with "the HMO will pay"**, confuse טיפול חמלה with a clinical trial, confuse the Helsinki committee (ניסויים) with the exceptions committee (מימון), or promise post-trial drug access.
8. **Do NOT cite a court case, law section, form number or shekel figure you have not verified.** In oncology a fabricated entitlement is the worst thing this skill can produce.

## Reference Links

| Source | URL |
|--------|-----|
| Kolzchut -- Cancer Patients (portal) | https://www.kolzchut.org.il/he/%D7%97%D7%95%D7%9C%D7%99_%D7%A1%D7%A8%D7%98%D7%9F |
| Bituach Leumi -- Oncology patients and survivors (hub for שיקום מקצועי, ילד נכה) | https://www.btl.gov.il/benefits/Disability/Pages/HolimONkologim.aspx |
| Bituach Leumi -- שר"מ appeal, 90 days | https://www.btl.gov.il/benefits/Attendance_Allowance/Pages/%d7%a2%d7%a8%d7%a2%d7%95%d7%a8%20%d7%a2%d7%9c%20%d7%94%d7%97%d7%9c%d7%98%d7%aa%20%d7%94%d7%9e%d7%95%d7%a1%d7%93.aspx |
| Bituach Leumi -- Pension amounts 2026 | https://www.btl.gov.il/benefits/Disability/Pages/%D7%A9%D7%99%D7%A2%D7%95%D7%A8%D7%99%20%D7%94%D7%A7%D7%A6%D7%91%D7%94.aspx |
| Patient Rights Law 1996 (second opinion, s.7) | https://www.nevo.co.il/law_html/law00/71833.htm |
| Equal Rights for Persons with Disabilities Law 1998 (s.8, s.9) | https://www.nevo.co.il/law_html/law01/p214m2_001.htm |
| Arnona discount regulations 1993, reg. 2 | https://www.nevo.co.il/law_html/law01/297_032.htm |
| National Health Insurance Law, second addendum (s.28 travel) | https://www.nevo.co.il/law_html/Law01/036_001.htm |
| MOH circular 2/2026, 2026 basket additions (PDF) | https://www.gov.il/BlobFolder/policy/mk02-2026/he/files_circulars_mk_mk02-2026.pdf |

## Troubleshooting

- **"Bituach Leumi denied my claim"** -- appeal in writing: **60 days** to the ועדה רפואית לעררים (נכות כללית), **90 days** to the ועדת עררים לשירותים מיוחדים (שר"מ). יד מכוונת (*2496) prepares claimants free. Strengthen with the oncologist's functional assessment, an occupational-therapy report, and documentation of worst-case days.
- **"My drug is not in the basket and the HMO refused"** -- run 5a and 5b in parallel, and read the תקנון PDF rather than trusting a remembered cap.
- **"I am over 41 and want to preserve fertility"** -- Step 7; the HMO fertility unit can discuss private or שב"ן options without delaying treatment.
- **"My employer pressured me to resign"** -- Step 8a, document in writing, escalate to the Commission for Equal Rights of Persons with Disabilities (*6763).
