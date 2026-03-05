---
name: israeli-hmo-navigator
description: >-
  Navigate Israel's four HMOs (kupot cholim) and healthcare system for service
  comparisons, referrals, and coverage decisions. Use when user asks about
  Clalit, Maccabi, Meuhedet, Leumit, "kupat cholim", health basket (sal
  briut), specialist referrals (hafnaya), supplementary insurance (biituach
  mashlim), or switching HMOs. Covers service tiers, digital platforms,
  copayments, and rights under the National Health Insurance Law. Do NOT use
  for emergency medical advice or pharmaceutical drug information.
license: MIT
compatibility: No network required. Works offline with reference data.
metadata:
  author: skills-il
  version: 1.0.0
  category: health-services
  tags:
    he:
      - קופת-חולים
      - בריאות
      - סל-בריאות
      - ביטוח-משלים
      - הפניה
      - ישראל
    en:
      - hmo
      - healthcare
      - health-basket
      - supplementary-insurance
      - referral
      - israel
  display_name:
    he: ניווט קופות החולים
    en: Israeli HMO Navigator
  display_description:
    he: השוואת שירותים, כיסויים וזכויות בקופות החולים בישראל
    en: >-
      Navigate Israel's four HMOs (kupot cholim) and healthcare system for
      service comparisons, referrals, and coverage decisions. Use when user
      asks about Clalit, Maccabi, Meuhedet, Leumit, health basket, specialist
      referrals, supplementary insurance, or switching HMOs.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli HMO Navigator

## Instructions

### Step 1: Understand Israel's Healthcare Structure
Israel's National Health Insurance Law (Chok Bituach Briut Mamlachti, 1995) guarantees universal healthcare through four competing HMOs (kupot cholim):

| HMO | Hebrew | Members (approx.) | Market Share | Founded |
|-----|--------|-------------------|-------------|---------|
| Clalit Health Services | כללית שירותי בריאות | ~4.8 million | ~52% | 1911 (Histadrut) |
| Maccabi Healthcare Services | מכבי שירותי בריאות | ~2.6 million | ~27% | 1941 |
| Meuhedet | מאוחדת | ~1.3 million | ~14% | 1974 |
| Leumit Health Fund | לאומית שירותי בריאות | ~0.7 million | ~7% | 1933 |

**Key principles:**
- Every Israeli resident MUST belong to one HMO
- HMOs cannot refuse membership (open enrollment)
- Switching between HMOs: once per year, effective after transition period
- Funding: National Health Insurance tax (mas briut) collected by Bituach Leumi, distributed to HMOs per capita with risk-adjusted formula
- Basic health basket (sal briut) services are identical across all HMOs by law

### Step 2: Compare Service Tiers
Each HMO offers multiple service levels:

| Tier | Hebrew | Coverage | Monthly Cost (approx.) |
|------|--------|----------|----------------------|
| Basic (Sal Briut) | סל בריאות בסיסי | Mandated by law, identical across HMOs | Covered by health tax |
| Supplementary (Mashlim) | ביטוח משלים | Extended coverage: surgeons of choice, faster access, additional medications | 30-80 NIS/person |
| Gold/Platinum (Zahav/Platina) | זהב/פלטינה | Premium: private hospitals, abroad treatments, dental, alternative medicine | 80-200 NIS/person |

**Basic Sal Briut includes:**
- Primary care physician (rofeh mishpacha) visits
- Specialist consultations (with referral/hafnaya)
- Hospitalization in general wards
- Prescription medications (with copayment/hishttatfut atzmit)
- Maternity and prenatal care
- Pediatric care and vaccinations
- Mental health services (expanded since 2015 reform)
- Chronic disease management
- Preventive screenings (age-appropriate)

**NOT included in basic basket (common gaps):**
- Dental care for adults (children covered until age 18)
- Cosmetic procedures
- Most fertility treatments after age limits
- Private room hospitalization
- Choice of specific surgeon
- Alternative/complementary medicine

### Step 3: Navigate Specialist Referrals (Hafnaya)
The referral process (hafnaya) varies by HMO:

| Step | Process | Notes |
|------|---------|-------|
| 1. See primary care physician | rofeh mishpacha / rofeh rishoni | First point of contact |
| 2. Get referral (hafnaya) | הפניה | Electronic referral in HMO system |
| 3. Schedule specialist appointment | tor le'moomcheh | Through HMO call center or app |
| 4. Wait time varies | zman hamtana | Basic: weeks-months; Mashlim: faster |
| 5. Follow-up as needed | ma'akav | Results sent to primary care |

**Maximum wait times (Sal Briut, per MOH guidelines):**
- Dermatologist (rofe or): Up to 30 days
- Orthopedist (ortoped): Up to 30 days
- Ophthalmologist (rofe einayim): Up to 30 days
- Cardiologist (kardiyolog): Up to 14 days for urgent
- Oncologist: Up to 14 days
- Gastroenterologist: Up to 30 days

**With supplementary insurance:** Wait times typically 3-14 days for most specialties.

### Step 4: Compare HMO Digital Services
| Feature | Clalit | Maccabi | Meuhedet | Leumit |
|---------|--------|---------|----------|--------|
| App Name | כללית Online | Maccabi Online | Meuhedet Online | Leumit Online |
| Online appointment booking | Yes | Yes | Yes | Yes |
| Video consultations (Telemedicine) | Yes | Yes | Yes | Yes |
| Lab results online | Yes | Yes | Yes | Yes |
| Prescription renewal online | Yes | Yes | Yes | Yes |
| Referral requests online | Partial | Yes | Yes | Partial |
| Chat with doctor | Yes | Yes | Yes | Limited |
| Medical record access | Yes | Yes | Yes | Yes |
| COVID/flu vaccine scheduling | Yes | Yes | Yes | Yes |

### Step 5: Understand Copayments (Hashtatfut Atzmit)
Standard copayments across kupot cholim (basic basket):

| Service | Copayment (approx.) | Notes |
|---------|---------------------|-------|
| Primary care visit | 0 NIS | Free under basic basket |
| Specialist visit (with hafnaya) | 20-30 NIS | Per visit |
| Emergency room (meurav) | ~100 NIS | Waived if admitted |
| Prescription medication (generic) | 10-15 NIS | Per item |
| Prescription medication (brand) | 15-50 NIS | Varies by medication |
| Blood tests (bdikot dam) | 0 NIS | Basic panels covered |
| Imaging (MRI/CT) | 0-50 NIS | With referral |
| Physiotherapy (fizioterapia) | 20-30 NIS | Per session, up to allocation |
| Mental health session | 0-30 NIS | Expanded coverage since reform |

**Exemptions from copayments:**
- Children under 18 for many services
- Chronic disease patients (machala kronit) for related medications
- Holocaust survivors (nitzolei shoah) for many services
- Income-based exemptions through Bituach Leumi

### Step 6: Switching HMOs (Ma'avar Kupat Cholim)
Process for switching between kupot cholim:

1. **Eligibility:** Any resident can switch once per calendar year
2. **How:** Visit target HMO branch or apply online (some HMOs)
3. **Timing:** Application processed, effective after transition period (typically 1-6 months)
4. **What transfers:** Basic basket coverage begins immediately at new HMO
5. **What doesn't transfer:** Supplementary insurance may have waiting periods at new HMO
6. **Pre-existing conditions:** Cannot be denied coverage for any condition (guaranteed acceptance)
7. **Records:** Medical records should be transferred; request from old HMO

**When to consider switching:**
- Better clinic locations near home/work
- Preferred doctors available at another HMO
- Better supplementary insurance packages
- Better digital services or appointment availability
- Dissatisfaction with service quality

### Step 7: Rights Under National Health Insurance Law
Key patient rights (zkhuyot ha'mevutach):

- **Free choice of HMO** and right to switch annually
- **Access to basic basket** regardless of health status
- **No discrimination** based on age, health, or pre-existing conditions
- **Complaint mechanism:** Netziv Kvulanot HaTzibur (Public Complaints Commissioner)
- **Second opinion:** Right to seek second opinion within the HMO
- **Information access:** Right to full medical record
- **Privacy:** Medical information confidentiality (Chok Haganat HaPratiyut)

## Examples

### Example 1: HMO Comparison for New Immigrant
**Input:** "I just made aliyah, which kupat cholim should I join?"
**Output:** Compare all four HMOs by: clinic locations near the user's city, language services (Russian, English, Amharic, Arabic support), oleh benefits, supplementary insurance pricing, digital platform quality. Recommend based on user's location and needs. Note that all HMOs must accept new members and basic coverage is identical.

### Example 2: Understanding a Referral
**Input:** "My doctor gave me a hafnaya to an orthopedist, what do I do?"
**Output:** Explain the referral process: log into HMO app, find available orthopedist appointments, compare wait times. If wait is too long under basic basket, explain supplementary insurance fast-track option. Mention copayment amount and what to bring to the appointment.

### Example 3: Supplementary Insurance Decision
**Input:** "Is it worth getting biituach mashlim at Maccabi?"
**Output:** Compare Maccabi Mashlim (Maccabi Sheli) vs Maccabi Zahav: coverage differences, monthly costs by age group, key benefits (surgeon choice, private hospitals, dental, abroad treatment). Help user assess based on age, health needs, and budget.

### Example 4: Dental Coverage
**Input:** "Does my kupat cholim cover dental?"
**Output:** Explain that basic basket covers dental for children until age 18 only. Adults need supplementary insurance (mashlim/zahav) or private dental insurance. Compare dental coverage across HMO supplementary plans. Note preventive dental program for children (Tipul Meuni) covered by basic basket.

## Troubleshooting

### Error: "Cannot schedule appointment - no available slots"
Cause: High demand for certain specialties, especially in basic basket
Solution: Try different clinic locations within same HMO. Ask about cancellation lists (reshimat hamilaot). Consider upgrading to supplementary insurance for faster access. If wait exceeds MOH guidelines, file complaint with HMO patient advocate (netziv pniyot hatzibur).

### Error: "Medication not covered by kupat cholim"
Cause: Medication not in the national health basket (sal briut)
Solution: Check if supplementary insurance covers it. Some medications require special approval (ishur meyuchad) from HMO medical committee. If denied, appeal process available. Check if generic alternative is in the basket.

### Error: "Supplementary insurance has waiting period for my condition"
Cause: Some conditions have 6-18 month waiting periods when joining new supplementary plan
Solution: This applies to supplementary/gold tiers only, not basic basket. Waiting periods are standard and cannot be waived. Plan ahead when switching HMOs. Basic basket coverage for the condition is immediate.
