---
name: israeli-emergency-guide
description: >-
  Guide to Israeli emergency services, hospitals, trauma centers, and urgent care.
  Use when a user needs information about calling MDA (Magen David Adom), visiting
  Terem urgent care, navigating hospital ERs, understanding triage, or learning about
  patient rights during emergencies in Israel. Covers the 5 Level-1 trauma centers,
  ER copay rules, blood donation through MDA, and when to call 101 vs go to Terem.
  Do NOT use for non-Israeli emergency systems or medical diagnosis.
license: MIT
compatibility: "Works with all major AI coding agents"
metadata:
  author: skills-il
  version: 1.0.0
  category: health-services
  tags:
    he:
      - חירום
      - מדא
      - בית-חולים
      - טראומה
      - עזרה-ראשונה
      - ישראל
    en:
      - emergency
      - mda
      - hospital
      - trauma
      - first-aid
      - israel
  display_name:
    he: "מדריך חירום ישראלי"
    en: "Israeli Emergency Guide"
  display_description:
    he: "מדריך לשירותי חירום, בתי חולים ומרכזי טראומה בישראל"
    en: "Guide to Israeli emergency services, hospitals, and trauma centers including MDA, Terem, and patient rights during emergencies."
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli Emergency Guide

## Instructions

### Step 1: Emergency Phone Numbers

Israel has dedicated emergency numbers. Provide the correct number based on the situation.

| Number | Service | Hebrew Name | When to Call |
|--------|---------|-------------|--------------|
| 101 | MDA (Magen David Adom) | מגן דוד אדום | Medical emergencies, ambulance |
| 100 | Israel Police | משטרת ישראל | Crime, security threats, accidents |
| 102 | Fire and Rescue | כיבוי אש והצלה | Fires, hazardous materials, rescues |
| 112 | Unified Emergency | מספר חירום אחיד | Works from any phone, routes to correct service |

Key facts about MDA:
- National emergency medical service, operating since 1950
- 189 stations across Israel with over 2,000 ambulances
- Average response time: 8.3 minutes nationwide
- Staffed by approximately 4,000 EMTs and paramedics plus 26,000 volunteers
- Supplies 100% of IDF blood needs through MDA Blood Services

### Step 2: When to Call MDA vs Visit Terem vs Go to ER

Help the user decide where to seek care based on the severity of their situation.

| Severity | Where to Go | Examples |
|----------|-------------|---------|
| Life-threatening | Call 101 (MDA) immediately | Chest pain, severe bleeding, difficulty breathing, loss of consciousness, suspected stroke |
| Urgent but not life-threatening | Terem Urgent Care (טרם) | Broken bone (stable), deep cut needing stitches, high fever in children, ear infection with severe pain |
| Requires hospital resources | Hospital ER (חדר מיון) | Head injury with confusion, suspected appendicitis, allergic reaction with swelling |
| Non-urgent | Kupat Cholim clinic (קופת חולים) | Cold/flu symptoms, mild rash, routine follow-up |

Decision guide:
1. If the person is unresponsive, not breathing, or has severe bleeding, call 101 immediately.
2. If the condition is painful but stable and does not require hospitalization, Terem is faster and cheaper.
3. If unsure, call 101. The MDA dispatcher will advise whether an ambulance is needed.

### Step 3: Israel's Hospital System and Trauma Centers

Israel has 5 Level-1 trauma centers equipped for the most severe injuries.

| Hospital | Hebrew Name | City | Region | Specialties |
|----------|-------------|------|--------|-------------|
| Rambam Health Care Campus | רמב"ם | Haifa | North | Underground emergency hospital, mass casualty |
| Hadassah Medical Center (Ein Kerem) | הדסה עין כרם | Jerusalem | Center | Organ transplants, complex surgeries |
| Sheba Medical Center (Tel Hashomer) | שיבא תל השומר | Ramat Gan | Center (Tel Aviv area) | Largest hospital in Israel, national referral |
| Soroka Medical Center | סורוקה | Beer Sheva | South (Negev) | Only Level-1 trauma in the Negev |
| Rabin Medical Center (Beilinson) | רבין (בילינסון) | Petach Tikva | Center | Major cardiac and pediatric center |

Additional major hospitals:
- Ichilov (Sourasky), Tel Aviv: major ER, central location
- Kaplan, Rehovot: serves southern coastal area
- Ziv, Tzfat: serves upper Galilee
- Wolfson, Holon: southern Tel Aviv metropolitan area

### Step 4: ER Process (Chadar Miyun)

When arriving at a hospital ER (chadar miyun, חדר מיון), expect the following process:

| Stage | What Happens | Typical Duration |
|-------|-------------|------------------|
| Registration (קבלה) | Present teudat zehut (ID) and kupat cholim card | 5-15 minutes |
| Triage (מיון) | Nurse assesses severity, assigns priority level | 5-10 minutes |
| Waiting | Wait based on triage priority (not arrival order) | 30 minutes to several hours |
| Examination | Doctor examines, may order tests | 15-60 minutes |
| Treatment/Discharge | Treatment given, discharge or admission decision | Varies |

Cost information:
- ER copay (ishtalmut): approximately 100 NIS
- Copay is waived if the patient is admitted to the hospital
- Copay is waived if referred by MDA ambulance
- Children under 18 and pregnant women may have reduced or waived copays depending on kupat cholim

Triage priority levels:
1. Immediate (red): life-threatening, seen immediately
2. Urgent (orange): serious, seen within 15-30 minutes
3. Less urgent (yellow): stable but needs ER care, may wait 1-2 hours
4. Non-urgent (green): could be seen at clinic, longest wait

### Step 5: Terem Urgent Care Clinics

Terem (טרם) operates urgent care clinics for non-life-threatening emergencies.

| Location | Address Area | Hours |
|----------|-------------|-------|
| Jerusalem (Romema) | Romema neighborhood | 24/7 |
| Jerusalem (Bnei Brit) | City center | Extended hours |
| Modi'in | Industrial zone | Evening/weekend |
| Lod | City center | Evening/weekend |
| Be'er Sheva | City center | Evening/weekend |

When to use Terem:
- Fractures and sprains (not compound fractures)
- Cuts requiring stitches
- High fever, especially in young children
- Ear and eye infections with acute pain
- Minor burns
- Urinary tract infections

Advantages over hospital ER:
- Shorter wait times (typically under 1 hour)
- Lower cost than ER visit
- X-ray and basic lab services available
- No referral needed
- Accepted by all kupot cholim

### Step 6: Patient Rights During Emergencies

Under Israeli law (Patient Rights Law, חוק זכויות החולה), patients have the following rights even during emergencies:

| Right | Description |
|-------|-------------|
| Right to emergency care | No hospital or MDA crew can refuse emergency treatment regardless of payment status |
| Informed consent (הסכמה מדעת) | Patient must be informed of procedures, risks, and alternatives (except when unconscious) |
| Right to refuse treatment | Competent adults can refuse treatment, even in emergencies, with documented informed refusal |
| Privacy (פרטיות) | Medical information is confidential; treatment areas should provide reasonable privacy |
| Accompaniment (ליווי) | Patient may have a family member present unless medically contraindicated |
| Medical records (רשומה רפואית) | Patient has right to access their medical records |
| Language access | Hospitals must provide interpretation services for patients who do not speak Hebrew |

Important: If a patient is unconscious or unable to give consent, medical staff may perform life-saving procedures under the emergency exception (pikuach nefesh, פיקוח נפש).

### Step 7: Blood Donation Through MDA

MDA Blood Services (שירותי הדם של מד"א) manages Israel's entire blood supply.

| Detail | Information |
|--------|-------------|
| Who can donate | Ages 17-65, weight over 50 kg, in good health |
| How often | Every 3 months (whole blood) |
| Where to donate | MDA blood donation centers, mobile blood drives |
| Scheduling | Via MDA website or call 101 |
| Time required | Approximately 30-45 minutes total |

Key facts:
- MDA supplies 100% of blood products for Israeli hospitals and the IDF
- Israel needs approximately 800 blood donations per day
- Blood types O-negative and B-negative are in constant high demand
- Donors receive a free health screening (blood pressure, hemoglobin, pulse)
- Donation is voluntary and unpaid in Israel

## Examples

### Example 1: Someone Collapses in the Street
User says: "Someone just collapsed near me and isn't responding. What do I do?"

Actions:
1. Call 101 (MDA) immediately
2. Tell the dispatcher your exact location (street name, landmark, or building)
3. Check if the person is breathing; the dispatcher will guide you through CPR if needed
4. Do not move the person unless they are in immediate danger (fire, traffic)
5. Stay on the line until the ambulance arrives (average response: 8.3 minutes)

Result: MDA dispatches the nearest ambulance. If in a public area, nearby defibrillators (AED) may be available (ask the dispatcher).

### Example 2: Child Has a High Fever on Shabbat
User says: "My 3-year-old has a fever of 39.5 and it's Friday night. Where do I go?"

Actions:
1. For a fever of 39.5 in a young child, Terem urgent care is the most appropriate option
2. Locate the nearest Terem clinic (Jerusalem Romema is open 24/7 including Shabbat)
3. Bring the child's teudat zehut and kupat cholim card
4. If the child has difficulty breathing, is lethargic, or has a rash, call 101 instead

Result: Terem can evaluate the child, run basic tests, and prescribe medication. Wait times are typically under 1 hour.

### Example 3: Tourist Breaks an Arm
User says: "I'm a tourist in Tel Aviv and I think I broke my arm. What should I do?"

Actions:
1. If the bone is not protruding and bleeding is controlled, go to Terem or a hospital ER
2. In Tel Aviv, Ichilov (Sourasky Medical Center) is centrally located
3. Bring your passport and travel insurance documents
4. ER copay is approximately 100 NIS; travel insurance should cover this
5. Hospitals are required to treat you regardless of insurance status

Result: X-ray and treatment at Terem or the hospital. Non-residents may be billed at higher rates, so having travel insurance is important.

### Example 4: Locating the Nearest Trauma Center
User says: "There's been a serious car accident near Beer Sheva. Which hospital handles major trauma?"

Actions:
1. Call 101 (MDA). For major trauma, MDA will transport to the nearest Level-1 trauma center
2. In the Beer Sheva area, Soroka Medical Center is the Level-1 trauma center
3. Soroka is the only Level-1 trauma center in the Negev region
4. Do not attempt to transport a severely injured person yourself unless MDA instructs you to

Result: MDA dispatches a Mobile Intensive Care Unit (MICU) staffed by paramedics for major trauma cases.

## Bundled Resources

### References
- `references/hospital-directory.md` -- Complete directory of Israeli hospitals by region (North, Center, South, Jerusalem), including all 5 Level-1 trauma centers, emergency department phone numbers, clinical specialties, and pediatric and psychiatric facilities. Consult when a user needs to find the nearest hospital, identify which hospital handles specific specialties, or locate a trauma center.
- `references/first-aid-basics.md` -- Quick reference for basic first aid procedures (CPR for adults/children/infants, severe bleeding, burns, choking, heatstroke) with Israeli-specific context including desert snake bite response, Mediterranean jellyfish sting treatment, earthquake procedures, and regional heat risks. Consult when a user needs step-by-step first aid instructions or faces a region-specific emergency.

## Troubleshooting

### Error: "I called 101 but no one answers in English"
Cause: MDA dispatchers primarily speak Hebrew. English availability varies by region and time.
Solution: Say "English" or "Anglit" (אנגלית) clearly. If no English-speaking dispatcher is available, try calling 112 (the unified European emergency number), which may route to an English-capable operator. Alternatively, ask a nearby Hebrew speaker to assist with the call.

### Error: "The ER is charging me even though I came by ambulance"
Cause: Not all ambulance transports automatically waive the ER copay. The waiver typically applies when MDA determines the transport is medically necessary.
Solution: Ask the billing department (mishrad haheshbonot, משרד החשבונות) to verify your case. If MDA transported you and marked the call as an emergency, the copay should be waived. Keep your MDA transport documentation as proof.

### Error: "I don't know which kupat cholim I belong to"
Cause: Many residents, especially new immigrants (olim), are unsure of their health fund registration.
Solution: Check your kupat cholim membership by calling the National Insurance Institute (Bituach Leumi, ביטוח לאומי) at *6050 or visiting any kupat cholim branch with your teudat zehut. You can also check online through the Ministry of Health website. In an emergency, hospitals will treat you regardless of kupat cholim membership.
