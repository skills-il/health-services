# Domain checklist: israeli-hmo-navigator (health-services)

Dated 2026-09-20. Scope: cost of services at Clalit / Maccabi / Meuhedet / Leumit, copayments and the
floating-quarter model, family ceilings and exemptions, the two-component ER bill and the statutory
waiver list, prescription copay schemes, ambulance refunds, Form 17, and switching kupot with שב"ן seniority.

Primary statutory table verified this cycle by extracting the text of
`חוזר סמנכ"ל לפיקוח על קופות החולים ושב"ן 1/2025` (published 12/08/2025, effective 1.4.2025) from the
gov.il BlobFolder PDF. Its top-level structure is: §1 Second-Schedule service payments, §2 Dead Sea
psoriasis, §3 hearing aids, §4 alopecia wig, §5 medical-food ceiling, §6 child dentistry, §7 preventive
dentistry 72+, §8 prosthetic dentistry 72+, §9 nuchal translucency, §§10-14 the four kupot's approved
collection plans (services + drugs), §15 הגדרות, §16 פטורים והנחות, §17 תקרות, §18 הבהרות,
§19 הגדרת גיל פרישה, §20 מדד יוקר הבריאות. Section numbers below were read from that PDF, not inferred.
gov.il HTML is Cloudflare-blocked from this machine; HTML-only claims are marked as such.

Because every amount in this domain is produced from a rate table, each **dimension a rate varies by**
is its own row. A skill that covers "copay" but not "copay by kupah" is not covered.

---

## Must cover (core)

### A. The two-vintage problem and the "as of" discipline

| # | Must cover | Source |
|---|---|---|
| A1 | Two live vintages: the §1/§§10-14 circular table (indexed to 2024, effective 1.4.2025) vs each kupah's own 2026-indexed tariff page, a few percent higher. Both must be stated, never averaged. | sbn01-2025 §1 ("החל מיום 1 באפריל 2025") vs kupah tariff pages below |
| A2 | No 2026 payments circular exists; the amounts are re-indexed by מדד יוקר הבריאות, so every figure is a dated snapshot. | sbn01-2025 §20 (מדד יוקר הבריאות 1996-2024) |
| A3 | Circular-series rename: the same series is now headed `חוזר האגף לפיקוח על קופות החולים ושירותי בריאות נוספים`. Search both names. | sbn01-2025 masthead |
| A4 | 1/2025 supersedes a named list of prior circulars (9/07 … 6/24). Do not quote a superseded circular's figure. | sbn01-2025 §4 |

### B. Copayment amount, every dimension it varies by

| # | Must cover | Source |
|---|---|---|
| B1 | **By kupah.** The four approved collection plans are separate tables; the basket of *services* is identical by law, the *copays and ceilings* are not. | sbn01-2025 §§10-14 (per-kupah תוכניות גבייה) |
| B2 | **By service type.** Distinct rate lines exist for: רופא שניוני, מרפאות חוץ, מכונים, מכוני פיזיותרפיה, מכוני הפרעה בתקשורת, מוקד לילה, ביקור בית. They are not one number. | sbn01-2025 §§10-14 line items (Maccabi, §14.2: שניוני 33.32, מרפאות חוץ 39.73. The figures 32.50, 105.02 and 202.26 belong to the Meuhedet block at §14.3, not to Maccabi: read the per-kupah block, never a neighbouring one) |
| B3 | **By primary vs secondary doctor.** רופא ראשוני (GP, family, paediatrics, internal medicine, gynaecology) = free; רופא שניוני (any other community specialist, **including psychiatrist, dietitian and podiatrist**) = charged. | sbn01-2025 §15.7, §15.8 (verbatim) |
| B4 | **By place of service.** מכונים = imaging/diagnostic institutes *outside* general hospitals (§15.2 enumerates רנטגן, US, nuclear, CT, echo, EMG, EEG, audiometry, ergometry, gastro, sleep); מרפאות חוץ = clinics *inside* general hospitals incl. their mental-health clinics. Same procedure, different line. | sbn01-2025 §15.2, §15.4 |
| B5 | **By exemption population** (see section D) and **by ceiling status** (section C). A quoted amount without checking these two is wrong by construction. | sbn01-2025 §16, §17 |
| B6 | **Doctor's home visit varies by whether the clinic is open**: 24.38 ₪ clinic-open vs 104.84 ₪ clinic-closed in the statutory table, and separately by kupah. Take each kupah's figure from its own block (the 202.26 out-of-hours home visit is the Meuhedet block, §14.3 item 18). | sbn01-2025 §1 items 1(א), 1(ב); per-kupah blocks §§14.2-14.3 |
| B7 | **Mid-quarter transfer between two secondary doctors is its own priced line**, not free. | sbn01-2025 §§10-14 ("מעבר/העברה מרופא שניוני האחד למשנהו במהלך רבעון") |
| B8 | **Independent (הסדר) provider** treatment is a defined category (מטפל עצמאי) with its own treatment. | sbn01-2025 §15.1 |

### C. The floating quarter, and the two clocks

| # | Must cover | Source |
|---|---|---|
| C1 | The exemption runs **three months from the date of the visit** and may cross a calendar boundary. | sbn01-2025 §15.6, verbatim |
| C2 | The **ceiling** for those same visits is computed on the **calendar** quarter. Two different clocks in one paragraph. | sbn01-2025 §15.6, second limb |
| C3 | For **all other services and for drugs**, "quarter" means calendar quarter only. | sbn01-2025 §15.6, closing sentence |
| C4 | Never state a specialist copay "per visit". | derived from §15.6 |

### D. Family ceiling and exemptions, every dimension they vary by

| # | Must cover | Source |
|---|---|---|
| D1 | **Which visits count toward the family ceiling**: רופא שניוני, מרפאות חוץ, מכונים, quarterly. Dental copays are expressly outside it. | sbn01-2025 §17.1; §6 clarification that child dentistry is excluded from the quarterly family ceiling |
| D2 | **Ceiling by kupah**: the figure differs per collection plan (e.g. Maccabi 283.17). Range under the circular ≈242.71-303.39; on kupot's 2026 pages ≈250-313.40. | sbn01-2025 §§10-14 ("תקרה למשפחה לרבעון") + kupah tariff pages |
| D3 | **Ceiling by population**: halved to 50% where a family member is a first-year oleh **or** above retirement age. | sbn01-2025 §17.2 |
| D4 | **The retirement-age trap.** §17.2 uses **גיל פרישה חובה** (mandatory); §16.1 and §16.8.2 use **גיל פרישה רשות** (optional). A member can qualify for one and not the other. | sbn01-2025 §17.2 vs §16.1 / §16.8.2, each flagged "יודגש" in the text; ages themselves in §19 |
| D5 | **Stacking rule.** Reductions *of the same kind* do not compound (oleh + over retirement age = 50%, not 25%); reductions *of different kinds* do stack; and a discount never removes the ceiling entitlement. | sbn01-2025 §18.1, §18.2, §18.3 |
| D6 | **Full exemption from secondary-doctor / outpatient / institute copay** for the §16.1 population list (retirement age + הבטחת הכנסה or אסירי ציון s.11, etc.). | sbn01-2025 §16.1 |
| D7 | **Disease-based exemption** from outpatient-clinic and institute copay for the named list (dialysis, oncology, AIDS, Gaucher, CF, thalassaemia, haemophilia, TB). | sbn01-2025 §16.2 |
| D8 | **Disease-based exemption from copay on the drugs specific to those diseases**, a separate sub-section from D7, different scope. | sbn01-2025 §16.3 |
| D9 | **Road-accident victims** exemption. Routes away from the kupah. | sbn01-2025 §16.4 |
| D10 | **Work-accident victims** exemption. Routes to NII. | sbn01-2025 §16.5 |
| D11 | **Organ donor** exemption (per חוק השתלת איברים 2008). | sbn01-2025 §16.6 |
| D12 | **התפתחות הילד** exemption for a member entitled to the listed allowance, and the mobility-allowance limb runs to 18 **and 3 months**, not 18. | sbn01-2025 §16.7 |
| D13 | **טיפות חלב / תחנות לבריאות המשפחה**: no charge since 2010. | sbn01-2025 §16.9 |
| D14 | **Occupational medicine**: no charge. (Numbered "15.10" in the PDF immediately after §16.9, an apparent numbering typo in the circular itself; cite it as "the occupational-medicine exemption in the §16 exemptions block" rather than asserting a clean number.) | sbn01-2025, exemptions block, numbering as printed |
| D15 | **Chronic-patient drug ceiling** is a *monthly individual* ceiling covering all drugs in the basket, not only the chronic-disease ones; chronic status is defined by a separate circular 1/2021 that updates independently. | sbn01-2025 §17.3.1 |
| D16 | **Half the chronic drug ceiling** for members at retirement age receiving הבטחת הכנסה, and here "retirement age" is again **optional**, unlike §17.2. | sbn01-2025 §17.3.2 |

### E. Prescription copay, every dimension it varies by

| # | Must cover | Source |
|---|---|---|
| E1 | **By kupah, four structurally different schemes, one per collection plan.** Clalit's is a percentage-or-floor "whichever is higher"; Maccabi, Meuhedet and Leumit use a flat minimum up to a threshold then switch to a percentage. | sbn01-2025 §§10-14 (תוכנית הגבייה בתרופות, one per kupah); Clalit tariff page (30.06.2026) |
| E2 | **By generic availability.** A registered generic changes the rate (Clalit 15% → 10%, same floor). | Clalit tariff page; per-kupah drug plans in §§10-14 |
| E3 | **By threshold.** The flat-minimum schemes only become percentage-based above a per-kupah threshold (circular-era ≈151.70-161.81; the kupot own 2026 pages give 156.30 at Leumit and 156.73 at Meuhedet). Below it the member pays the floor. | sbn01-2025 §§11-14 drug plans |
| E4 | **By whether the drug is in the basket / on the kupah's list.** Maccabi charges 50% of consumer price for drugs with cheap substitutes or off the list. | Maccabi drug plan, sbn01-2025 §11 |
| E5 | **By age: the senior discount is 10% from age 72**, in force since 1.1.2016. The widely-repeated "75" is superseded. | sbn01-2025 §16.8.3 (verbatim, "החל מה-1.1.16") |
| E6 | **50% drug discount populations**: oleh in the first 12 months; recipient of הבטחת הכנסה / אסירי ציון s.11; אזרח ותיק as defined; oleh in the period after the first 12 months. | sbn01-2025 §16.8.1, §16.8.1.1, §16.8.1.2, §16.8.1.2.1, §16.8.1.2.2 |
| E7 | **Holocaust-survivor full prescription exemption**, and it is gated on receiving one of an enumerated list of payments (8 items: נכי רדיפות הנאצים, נכי המלחמה בנאצים, הטבות לניצולי שואה s.3 and s.4, German monthly pension, other foreign persecution pension, Claims Conference quarterly, one-off compensation). Do not say "survivors" unqualified. | sbn01-2025 §2 and §16.8.4 with §§16.8.4.1-16.8.4.8; Gov. Decision 1568 of 27.4.14 |
| E8 | **Needy WWII veteran** (חוק מעמד ותיקי מלחמת העולם השנייה) carries its own drug entitlement. | sbn01-2025 §16.8.4 opening |
| E9 | **A שב"ן-only drug sold to a non-member of that שב"ן gets neither discount nor ceiling.** | per-kupah drug plans, §§10-14 (verbatim clause quoted in references/copay-tables.md) |
| E10 | Discount stacking on drugs is the **exception** to §18.1: drug discounts DO accumulate ("התקרות מאותו סוג אינן מצטברות **למעט ההנחות בתרופות**"). This is the single most missable clause in §18. | sbn01-2025 §18.1, verbatim |

### F. Emergency room, every dimension the charge varies by

| # | Must cover | Source |
|---|---|---|
| F1 | **The bill is always two components**: אגרת מיון + a charge for the treatment given. A single-number answer is always wrong. | gov.il ER-payment service page (HTML, Cloudflare-blocked this cycle; verbatim text preserved in SKILL.md and references/er-waiver-list.md) |
| F2 | **The MoH does not publish the amount in the circular.** Confirmed by extraction: sbn01-2025 contains no מלר"ד/מיון tariff line at all. The gov.il page points to תעריפון משרד הבריאות. | sbn01-2025, full-text extraction 2026-09-20 (negative result); gov.il ER-payment page |
| F3 | **By hour band.** 01:00-06:00 is agra-only at Clalit (269 ₪) vs up to 1,199 ₪ for a 06:00-01:00 unreferred visit. Meuhedet by contrast charges its 269.00 ₪ agra at any hour. | Clalit tariff page; Meuhedet copayments page |
| F4 | **By referral / Form 17 status.** An unreferred visit outside the waiver list is the full two-component charge. | Clalit tariff page; gov.il ER-payment page |
| F5 | **By waiver ground, three distinct trigger types**, routinely conflated: (a) the reason is on the statutory `פטור מלא` list → 0; (b) the **hour** trigger → agra only; (c) **retrospective medical justification**, which applies `ללא קשר לשעת הביקור` → agra only. | חוזר מנהל הרפואה 21/2016 (the statutory list); Clalit tariff page; call.gov.il/product-page/1002629 |
| F6 | **By kupah, for the non-statutory extensions.** Clalit blanket 19:00-07:00; Maccabi an all-hours list plus a separate partial-payment list; Meuhedet gates on referral validity windows and road-accident time bands; Leumit grants retrospectively via a moked doctor and caps a non-exempt visit at 600 ₪ vs Clalit's 1,199. | each kupah's tariff page; call.gov.il/product-page/1002629 |
| F7 | **Admission to hospital makes the visit free** regardless of referral. | gov.il ER-payment page; kupah tariff pages |
| F8 | **A psychiatric ER is free.** `הפונים למחלקה לרפואה דחופה – מלר"ד במרכז רפואי לבריאות הנפש פטורים מתשלום.` | gov.il ER-payment page, attributing חוזר מנכ"ל 06/2024 |
| F9 | **Do not state a count** for the waiver list: gov.il, Leumit and call.gov.il bullet the same statutory list into different numbers of items. | comparison of the three pages |
| F10 | **The retro-claim route**: discharge summary + receipt to the kupah secretariat; if justified the kupah issues the commitment form to the hospital. | kupah tariff pages; Meuhedet appeals text |
| F11 | The agra spread (259 Leumit / 269 Clalit / 269.00 Meuhedet) is **unexplained**, since all three claim to follow מחירון משרד הבריאות; Maccabi does not publish one retrievably. State the divergence rather than picking one. | three kupah pages, compared |

### G. Ambulance refunds

| # | Must cover | Source |
|---|---|---|
| G1 | **By ambulance type AND by admission outcome, a 2x2, and one cell is zero.** Regular ambulance + admitted = full refund; ICU ambulance + not admitted = 50%; **regular ambulance + not admitted = no refund at all**; ICU + admitted = full. | gov.il ambulance-evacuation service page (updated 26.05.2026), verbatim three bullets |
| G2 | **By payer route.** Work accident and terror-victim route to the NII; road accident routes to the motor insurer; not to the kupah. | gov.il ambulance-evacuation page; sbn01-2025 §16.4, §16.5 |
| G3 | **By indication**: oncology and dialysis transport is refunded at `50% מתעריף מגן דוד אדום או ממחיר הנסיעה בפועל (הנמוך מביניהם)`. | gov.il ambulance-evacuation page |
| G4 | **The 60-day deadline.** Not settling through the kupah within 60 days of the evacuation makes the member liable for the full amount. | gov.il ambulance-evacuation page, verbatim |
| G5 | **State no shekel ambulance tariff.** It sits in תקנות מגן דוד אדום (אגרות הסעת חירום באמבולנס), which could not be read from a primary source this cycle. | negative finding; do not substitute a secondary figure |
| G6 | Separately, **out-of-hours emergency services (מד"א, שר"ל) when the clinic is closed** carry a statutory 104.84 ₪ copay, a different thing from the evacuation refund, and Meuhedet is carved out of it. | sbn01-2025 §1 item 2 and its footnote ("למעט קופת חולים מאוחדת … ראה the section on that topic.3") |

### H. Form 17

| # | Must cover | Source |
|---|---|---|
| H1 | What it is: `"טופס 17" (טופס התחייבות מהקופה המבטחת)`, the kupah's **financial commitment to a provider**, issued **in advance**. | gov.il Form-17 content (HTML, Cloudflare-blocked this cycle; verbatim preserved in SKILL.md) |
| H2 | All four kupot issue it digitally via app or site. | four kupot's member sites |
| H3 | The four standard refusal grounds: attendance without a prior commitment, reason outside the exempt list, visit not urgent, treatment elective. | gov.il Form-17 content |
| H4 | Its financial effect: it converts a chargeable visit into a covered one, which is why obtaining one before an ER visit is worth several hundred shekels. | derived from F3/F4 |

### I. Switching kupot and שב"ן seniority

| # | Must cover | Source |
|---|---|---|
| I1 | The **six fixed effective dates** and their application windows (16.09-15.11→01.01, 16.11-15.01→01.03, 16.01-15.03→01.05, 16.03-15.05→01.07, 16.05-15.07→01.09, 16.07-15.09→01.11). | kolzchut, מעבר בין קופות חולים |
| I2 | **Two transfers maximum per 12 months.** | kolzchut, same page, verbatim |
| I3 | **Two channels and the fee**: Israel Post in person (transfer form, 19.30 ₪) or the NII website (valid credit card in the member's own name). | kolzchut, same page |
| I4 | **Immediate-effect registrations outside the six dates**: 18-year-old to 18.5; new oleh on a first registration; newborn to 6 months on a first registration; any resident on a first registration. Do not tell a new oleh to wait for 01.01. | kolzchut, same page |
| I5 | **שב"ן seniority DOES carry across.** The new kupah may not refuse supplementary cover. This corrects the common (and previously published) claim that it is lost. | Leumit switching page, verbatim; kolzchut |
| I6 | **It is not automatic**: the member must obtain an `אישור וותק` from the old kupah and give it to the new one, at the branch-completion step that follows registration. | Leumit switching page, verbatim |
| I7 | **The 90-day clock, and the same-level condition.** The previous שב"ן period is offset against the אכשרה only if the member enrols within 90 days of the switch **in a plan of the same level**. | kolzchut / Leumit, verbatim quote in SKILL.md |
| I8 | **Do not promise a waiting-period length.** A waiver is available `בתנאים מסוימים`, a hedge, not a guarantee; each kupah sets its own periods in its תקנון. | Leumit page; kolzchut |
| I9 | **Registering is not joining.** Basket cover follows registration, but שב"ן and long-term-care enrolment, the magnetic card and the וותק hand-over all happen at the branch step. Skipping it is how people end up uninsured on the supplementary layer. | Leumit / kolzchut |
| I10 | **Tier-name trap**: מכבי זהב is the *entry* tier and מכבי שלי the premium one; only Leumit orders כסף below זהב as expected. Gets switching comparisons backwards. | four kupot's שב"ן pages |
| I11 | Ceilings and copays genuinely differ across the four, so switching is a **real financial comparison**, not only a service one. | sbn01-2025 §§10-14 (differing תקרה למשפחה per plan) |

### J. Cross-cutting output rules

| # | Must cover | Source |
|---|---|---|
| J1 | Attach an "as of" date and a vintage label to every amount; never average two conflicting figures; refuse to estimate a figure the reference files do not carry. | derived from A1/A2 |
| J2 | US insurance vocabulary (deductible, in-network, out-of-network) does not map. Israel has exactly four kupot. | domain framing |
| J3 | The legal notice and the "not a determination of eligibility / not medical advice" framing must lead, given every answer states a figure about the user's own situation. | skills-il legal-review rule for regulated domains |

---

## Should cover (advanced)

| # | Should cover | Source |
|---|---|---|
| S1 | **Dentistry is three separate regimes, each with its own rate table**: children under 18 (§6, in force since 2010, with named sub-items such as prefabricated crowns and GA for under-5s with early childhood caries), preventive/conservative care for 72+ (§7, expanded 1.7.2022), and prosthetic care for 72+ (§8, first in force 1.10.2019, incl. specialist consultation and repair or addition of teeth lines). Adult routine dentistry is outside the basket. | sbn01-2025 §6, §7, §8 |
| S2 | **Chronic (complex nursing) hospitalisation copay**: 85.71 ₪, reduced by order (ק"ת 10236) and indexed only from 2022, an unusual indexation base. | sbn01-2025 §1 item 4 and footnote 3 |
| S3 | **Pregnancy-screening copays are individually priced**: alpha-fetoprotein 73.15 ₪ (§1 item 5) and nuchal translucency 52.81 ₪ (§9). | sbn01-2025 §1 item 5, §9 |
| S4 | **Paramedical and child-development treatments, physiotherapy at non-kupah institutes, and speech therapy outside the kupah** each carry the 36.57 ₪ statutory line; stuttering treatment over age 6 is instead a 50%-of-one-course rule capped at 50% of the Hadassah course tariff, with up to two extra courses for relapse at 12+. | sbn01-2025 §1 items 6, 7, 8, 8(ב) and footnote 4 |
| S5 | **Fertility**: the copay for FSH/LH injectables is capped at 243.82 ₪ per cycle. | sbn01-2025 §1 item 9 |
| S6 | **Entitlements expressed as a refund ceiling rather than a copay**: hearing aid 3,426.85 ₪ per ear every 3.5 years for 18+ (§3); wig after alopecia diagnosis up to 5,569.05 ₪ every two years with **no copay** (§4); medical-food ceiling 854.64 ₪ (§5); Dead Sea psoriasis stay 341.35 ₪/day over 10 consecutive treatment days, Fri/Sat not breaking the run, receipts required (§2). These are the "how much will they give me back" questions, and they are a different shape from a copay. | sbn01-2025 §2, §3, §4, §5 |
| S7 | **Penile prosthesis for impotence is priced in dollars** ($388), the only USD line in the table, a real trap for a calculator. | sbn01-2025 §1 item 10 |
| S8 | **Hybrid insulin pump**: added for 41+ by Knesset Finance Committee on 02.12.2024 across all four kupot, with a 50 ₪ monthly consumables copay, matching the existing 18-40 entitlement. | sbn01-2025 §3 (numbered item 3 of the preamble) |
| S9 | **Mental-health clinic definition (§15.3)** is broad, public hospital, kupah-run, MoH-run incl. a תחנה, or a contracted multidisciplinary team, and it determines which copay line a psychotherapy session falls under; psychotherapy by an independent practitioner outside a mental-health clinic is priced separately. | sbn01-2025 §15.3; §14.7 cross-reference in the Leumit plan |
| S10 | **מוקד / urgent-care and out-of-hours home visits vary by kupah and by day**, roughly 50-108 ₪ for a moked and 51-202 ₪ for a home visit; Leumit is the only kupah publishing a שב"ן tier differential on home visits. | sbn01-2025 §§10-14; Leumit tariff page |
| S11 | **Long-term-care (סיעודי) continuity on a switch is a separate clock from שב"ן**: transfer without new medical underwriting, on documentation presented within **180 days** (kolzchut), against the 90-day שב"ן offset. Two different deadlines, easily merged. | kolzchut, מעבר בין קופות חולים |
| S12 | **Moving to a HIGHER שב"ן tier restarts waiting periods in full**, even where seniority is credited at the same level. | kolzchut, מעבר בין קופות חולים |
| S13 | **Cancelling a transfer**: by the 20th of the month before it takes effect, at the same 19.30 ₪; re-registering within the same window does not restore the original date, it pushes to the next transfer date. | kolzchut / NII switching material |
| S14 | **The ombudsman can move or cancel a transfer date** outside the statutory windows, for a move of more than 60 km with no branch near the new home, or a special medical reason. | נציבות קבילות הציבור לחוק ביטוח בריאות ממלכתי; kolzchut |
| S15 | **The escalation ladder**: inside the kupah (ועדת חריגים → ועדת ערר → פניות הציבור), then נציבות קבילות הציבור לחוק ביטוח בריאות ממלכתי. Meuhedet requires the ER discharge sheet + receipt with a district appeal. State no filing deadline and no commissioner URL (unverified), and do not claim the kupah stage is a precondition. | kupot's פניות הציבור pages; Meuhedet appeals text |
| S16 | **2026 basket expansion** exists as `חוזר מנכ"ל 2/2026` of 08.03.2026 (הרחבת סל שירותי הבריאות לשנת 2026). Cite it by name only, carry no budget figure, technology count or list, none being verifiable from a primary source. | https://www.gov.il/BlobFolder/policy/mk02-2026/he/files_circulars_mk_mk02-2026.pdf |
| S17 | **Chronic-disease definition drifts independently** of the payments circular: it lives in circular 1/2021 "הגדרת מחלה כרונית לצורך תקרה עבור רכישת תרופות לחולים כרוניים", "המתעדכן מעת לעת". A member's ceiling eligibility can change without any change in the amounts. | sbn01-2025 §17.3.1, verbatim |
| S18 | **Contact routing**: the four kupot's numbers (*2700 / *3555 / *3833 / *507), MoH קול הבריאות *5400 with its hours, NII 02-6462000, MDA 101 (widely used but unverifiable against mdais.org, which blocks automated reads, hedge it). | kupot sites; MoH; noted verification gap |
| S19 | **Retrieval gap for Maccabi**: no consolidated tariff page is retrievable (per-item eligibility is client-rendered at maccabi4u.co.il). Maccabi amounts must come from the §11 circular plan, and the skill should say so rather than leaving a blank. | attempted retrieval; sbn01-2025 §11 |
| S20 | **"No slots" / access-to-care** and **"the drug is not covered"** are routing questions, not price questions: הסדר coverage, geography, cancellation lists, the kupah's own published wait target, then פניות הציבור; and for drugs, שב"ן cover, ועדת חריגים, a basket-listed generic, and the right of appeal. Frame as things to check with the kupah, never as asserted fact. | kupot's service charters |

---

## Out of scope (explicit)

Each line states why, as at 2026-09-20.

- **Clinical and diagnostic advice of any kind.** The skill routes and prices; a diagnosis or a treatment recommendation is reserved to a licensed physician and is the single largest legal exposure here.
- **Emergency triage ("should I go to the ER now?").** Answering it is a clinical judgement and a delay risk; the skill directs to 101 / the kupah moked instead.
- **Drug dosing, interactions, contraindications or substitution advice.** The skill may say a generic changes the *copay*; it must never say a generic is *appropriate*.
- **Private (שר"פ) and commercial health insurance pricing.** Outside the public system and outside every source cited here; quoting it would imply a comparison the sources do not support.
- **A shekel ambulance tariff.** The regulations (תקנות מד"א, אגרות הסעת חירום) could not be read from a primary source this cycle; a secondary figure would be unverifiable.
- **A count of the ER waiver list.** The three official renderings bullet the same list differently, so any number is an artefact of the page, not of the law.
- **The 2026 basket's budget, technology count or contents.** Only the circular's name and date are verifiable; the rest would be invention.
- **Named-hospital price lists and תעריפון משרד הבריאות line items.** The MoH publishes the ER *structure* but not the amount in any retrievable circular; only the kupot's own published figures can be quoted.
- **Any determination of an individual's eligibility, exemption status or final bill.** Eligibility is decided by the kupah; the skill explains rules and points at the page that binds.
- **Non-Israeli health systems, tourist and non-resident cover, and foreign-worker insurance.** A different statutory regime (not חוק ביטוח בריאות ממלכתי), so none of the tables above apply.
- **Dental treatment plans and orthodontic pricing beyond the three statutory regimes in S1.** Adult routine dentistry is outside the basket, so there is no public rate table to reason from.
- **NII benefit amounts (נכות, סיעוד, ניידות) themselves.** The skill needs only whether a benefit *triggers* a health exemption; the benefit's own rate table belongs to the NII skills.
- **מד"א membership / דמי חבר subscription products.** A commercial subscription, not a basket entitlement, and not covered by any source above.

---

## Authoritative sources

| Source | URL / identifier | Retrieval status 2026-09-20 |
|---|---|---|
| MoH circular `חוזר סמנכ"ל לפיקוח על קופות החולים ושב"ן 1/2025`, עדכון תשלומים בעד שירותי בריאות ותרופות לשנת 2025 (pub. 12/08/2025, effective 1.4.2025). The statutory table; §§1-9 services, §§10-14 per-kupah plans, §15 definitions, §16 exemptions, §17 ceilings, §18 clarifications, §19 retirement age, §20 index. | https://www.gov.il/BlobFolder/policy/sbn01-2025/he/files_circulars_sbn_sbn01-2025.pdf | **Fetched and full-text extracted.** All §-numbers above read from this file. |
| MoH DG circular 2/2026, הרחבת סל שירותי הבריאות לשנת 2026 (08.03.2026) | https://www.gov.il/BlobFolder/policy/mk02-2026/he/files_circulars_mk_mk02-2026.pdf | BlobFolder PDF; cite by name only |
| `חוזר מנהל הרפואה 21/2016`, the statutory ER `פטור מלא` list | referenced by gov.il and all four kupot; no direct BlobFolder URL confirmed this cycle | **Circular number as published by the citing pages; direct PDF unverified** |
| `חוזר מנכ"ל 06/2024`, psychiatric ER exemption | cited verbatim on the gov.il ER-payment page | cited-on-page; direct PDF unverified |
| Chronic-disease definition circular 1/2021 | named in sbn01-2025 §17.3.1 | **section reference verified in the 1/2025 text; the 1/2021 PDF itself unverified** |
| MoH cross-kupah copayment page | https://call.gov.il/page/GE41 | **ECONNRESET this cycle**; content preserved from earlier capture |
| MoH ER payment service page | https://www.gov.il/he/service/emergency-room-payment | gov.il HTML, Cloudflare-blocked from this machine |
| MoH ambulance evacuation page (updated 26.05.2026) | https://www.gov.il/he/service/ambulance-evacuation | gov.il HTML, Cloudflare-blocked from this machine |
| ER exemptions, per kupah | https://call.gov.il/product-page/1002629 | call.gov.il, unreachable this cycle |
| Kol Zchut, מעבר בין קופות חולים | https://www.kolzchut.org.il/he/מעבר_בין_קופות_חולים | **Fetched.** Source for I1-I4, S11-S12 |
| Kol Zchut, השתתפות עצמית page | title unresolved, the guessed slug returned 404; **page name unverified**, locate before citing | 404 this cycle |
| Clalit tariff page (שירותים בתשלום) | https://www.clalit.co.il/he/info/about_site/Pages/sherutim_betashlum.aspx | kupah-published 2026 vintage |
| Maccabi member site | maccabi4u.co.il | **no consolidated tariff table; client-rendered.** Use sbn01-2025 §11 |
| Meuhedet copayments page | https://www.meuhedet.co.il/מידע-ללקוח/השתתפויות-ופטורים/ | kupah-published 2026 vintage |
| Leumit tariff page (health-basket deductibles) | https://www.leumit.co.il/insurance-policies/health-basket/health-basket-deductables/ | kupah-published, `התעריף נכון ליולי 2026` |
| Leumit switching / שב"ן seniority text | Leumit site, מעבר קופות section | source of the verbatim אישור וותק quote |
| NII switching channel | National Insurance Institute online transfer form | channel, fee and card-in-own-name requirement |
| נציבות קבילות הציבור לחוק ביטוח בריאות ממלכתי | no URL or filing deadline verified this cycle, **do not state one** | negative finding |
| Magen David Adom, 101 | mdais.org blocks automated reads | **number widely used but unconfirmed against a primary source** |

**Not used, deliberately:** nevo.co.il (IP-blocked on this machine today).
