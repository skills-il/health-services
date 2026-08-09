---
name: israeli-hmo-navigator
description: Navigate Israel's four HMOs (kupot cholim) and healthcare system for costs, referrals, emergency-room fees and coverage decisions. Use when user asks about Clalit, Maccabi, Meuhedet, Leumit, "kupat cholim", health basket (sal briut), copayments (hishtatfut atzmit), emergency room (miyun) fees and exemptions, Form 17 (tofes 17), ambulance refunds, prescription copays, supplementary insurance (bituach mashlim), or switching HMOs. Do NOT use for emergency medical advice or for clinical drug information.
license: MIT
compatibility: Static reference, no network required. Amounts carry an "as of" date and are re-indexed by the Ministry of Health and by each kupah. Verify any amount against the member's own kupah page before quoting it to them.
---

# Israeli HMO Navigator

## How to use this skill, and its dating rule

Israel's National Health Insurance Law of 1995 guarantees universal coverage through four kupot cholim. This skill routes a member to the right cost, the right exemption and the right form.

Two vintages of amounts are in circulation right now: the Ministry of Health circular `חוזר סמנכ"ל לפיקוח על קופות החולים ושב"ן 1/2025` (published 12.08.2025, effective 1 April 2025), which is the statutory table, and each kupah's own tariff page, which carries 2026-indexed values roughly three percent higher. No 2026 payments circular exists yet.

**Rules for any answer you give from this skill:**

1. Always attach the "as of" date to an amount.
2. Always say which of the two vintages the amount came from.
3. Never average two conflicting figures, and never silently pick one. State both.
4. Tell the user to confirm the amount on their own kupah's page before relying on it. The reference data here is exactly the thing that drifts.
5. If a figure is not in this skill's reference files, say you do not have it rather than estimating.

The bulk tables live in `references/`. Load the one you need:

| File | Contents |
|---|---|
| `references/copay-tables.md` | statutory table, all four kupot's own 2026 tables, urgent care and home visits, prescription schemes, the six open conflicts |
| `references/er-waiver-list.md` | the full statutory `פטור מלא` list, the two agra-only triggers, the retro-claim procedure, each kupah's own extensions |
| `references/exemptions-and-ceilings.md` | the section 16 population table, the ceilings, the stacking rules, the retirement-age trap |

## The four kupot and how to reach them

| Kupah | Hebrew | Phone | Supplementary tiers, entry then premium |
|---|---|---|---|
| Clalit Health Services | כללית שירותי בריאות | `*2700` | כללית מושלם, then כללית מושלם פלטינום |
| Maccabi Healthcare Services | מכבי שירותי בריאות | `*3555` (`מכבי ללא הפסקה`) | מכבי זהב, then מכבי שלי |
| Meuhedet | מאוחדת | `*3833` | מאוחדת עדיף, then מאוחדת עדיף Plus |
| Leumit Health Fund | לאומית שירותי בריאות | `*507`, also 1700-507507 | לאומית כסף, then לאומית זהב |

Leumit's `*507` line runs `פעיל בימים א'-ה' 7:00-20:00, שישי וערבי חג 7:00-12:00`.

Other numbers: Ministry of Health `קול הבריאות` on `*5400` or 08-6241010, open `ראשון עד חמישי 8:00-18:00; שישי וערבי חג 8:00-13:00`. National Insurance Institute entitlement updates on 02-6462000. For a medical emergency, Magen David Adom is 101; that number is universally used but could not be confirmed against mdais.org in this cycle, which blocks automated reads.

Tier-name trap: **מכבי זהב is the entry tier despite the "gold" name, and מכבי שלי is the premium tier above it.** Only Leumit puts כסף below זהב the way most countries would expect.

## What will this actually cost me

This is the single highest-value decision in the whole skill, and it is a ladder, not a lookup. Walk it downward and stop at the first rung that fits the clinical situation.

| Route | Typical cost | Note |
|---|---|---|
| Clinic, primary doctor | 0 | a GP, family doctor, paediatrician, internist or gynaecologist is free |
| Evening, night or weekend moked | 50 to 108 | varies by kupah and by day, see `references/copay-tables.md` |
| Doctor's home visit | 51 to 202 | Leumit is the only kupah publishing a שב"ן tier differential here |
| Emergency room, agra only | 259 to 269 | the agra alone, before any treatment charge |
| Emergency room, full unreferred daytime visit | up to 1,199 | at Clalit; Leumit caps its non-exempt visit at 600 |
| Emergency room, reason on the statutory waiver list | 0 | see `references/er-waiver-list.md` first, before anyone pays |

Two things fall out of that ladder. Getting a referral or a Form 17 before going, where the situation allows it, is worth several hundred shekels. And checking the waiver list first is worth the whole amount, because people routinely pay for visits that are free by law.

## The billing model is a floating quarter, not a per-visit fee

The most common mistake made about Israeli copays is billing a specialist "per visit". It is not per visit. The circular defines it in section 15.6, verbatim:

`"רבעון" – בעבור שירות של ביקור אצל רופא, מכון או מרפאת חוץ שנקבע לגביו תשלום אחת לרבעון, יהיה החבר פטור מתשלום בעבור אותו שירות במשך שלושה חודשים מיום הביקור (גם אם התקופה האמורה חלה לאחר תום הרבעון הקלנדרי שבו היה אותו ביקור), ואולם התקרה בעד ביקורים כאמור תחושב על בסיס רבעון קלנדרי.`

`לעניין שירותים אחרים ותרופות – "רבעון" משמעו רבעון קלנדרי.`

**Both halves matter and they use different clocks.** The exemption runs three months **from the date of the visit**, so it floats and can cross a calendar boundary. But the family **ceiling** for those same visits is computed on the **calendar** quarter. For all other services and for drugs, "quarter" simply means the calendar quarter. Leumit's own heading says the same thing: `שיעורי ההשתתפויות הרבעוניות עבור שירותי הסל (תשלום עבור רבעון צף)`.

Who is free and who is paid, from sections 15.7 and 15.8:

- `רופא ראשוני`, verbatim `רופאים כלליים (שאינם מומחים), ורופאים מומחים בענפי הרפואה הבאים: רפואת המשפחה, רפואת ילדים, רפואה פנימית וגניקולוגיה`. **Free.**
- `רופא שניוני`, verbatim `רופא מומחה בקהילה, שאינו נכלל בהגדרת רופא ראשוני (כולל פסיכיאטר), ולעניין חוזר זה – גם דיאטנית ופודיאטריה.` **Paid**, once per floating quarter.
- `מכונים` are imaging and diagnostic institutes outside general hospitals (15.2). `מרפאות חוץ` are `מרפאות הפועלות במסגרת בתי חולים כלליים (כולל מרפאות בריאות הנפש בבתי חולים כלליים)` (15.4).

So a gynaecologist is free while a dermatologist is paid, and a dietitian and a podiatrist bill like a specialist even though neither is a physician.

## The emergency room is always two numbers, never one

The Ministry of Health does **not** publish the emergency-room amount. Its own service page, updated 14.07.2026, says under `עלות השירות` only: `תעריפי השירות מפורטים בתעריפון משרד הבריאות.`

What it does publish is the structure, verbatim:

`הטיפול הרפואי במלר"ד (חדר מיון) כרוך בתשלום על-פי תעריף משרד הבריאות. התשלום הוא בעד שירותים שונים והוא כולל שני מרכיבים: אגרת מיון. תשלום על הטיפול הניתן בחדר המיון. בחלק מהמקרים יינתן פטור מלא מתשלום, או פטור מתשלום על הטיפול ללא פטור מאגרת מיון.`

**So an emergency-room bill is an agra plus a treatment charge, and you must quote both.** Quoting the agra alone understates the bill by a factor of four or more, which is precisely how earlier versions of this skill told people an emergency room costs "about a hundred shekels".

The two components, as the kupot publish them:

| Situation | Amount | Source and date |
|---|---|---|
| Clalit, 06:00-01:00, no referral, reason not on the statutory list | 1,199 ₪, being agra plus treatment | Clalit, `לפי תעריף משרד הבריאות, צמוד למחיר יום אשפוז` |
| Clalit, 01:00-06:00, reason not on the statutory list | 269 ₪, agra only | Clalit |
| Clalit, found retrospectively to have been medically justified | 269 ₪, agra only | Clalit |
| Clalit, reason on the statutory exempt list | 0 | Clalit |
| Leumit, reduced agra | 259 ₪ | Leumit, `התעריף נכון ליולי 2026` |
| Leumit, non-exempt visit, capped | 600 ₪ | Leumit, `במקום התעריף המלא המפורסם במחירון משרד הבריאות` |
| Meuhedet, agra, non-exempt, at any hour of the day | 269.00 ₪ | Meuhedet |
| Maccabi | not published in retrievable form | see `references/copay-tables.md` |

Three consequences worth stating out loud to a member:

1. The agra is roughly 259 to 269 depending on kupah, and all three kupot that publish it claim to be following `מחירון משרד הבריאות`, so the divergence is unexplained.
2. The treatment charge is what makes the difference between an agra-only night visit and a 1,199 daytime one. Leumit caps its non-exempt visit at 600 while Clalit charges up to 1,199 for what may be the same presentation.
3. **A psychiatric emergency room is free.** gov.il, verbatim: `הפונים למחלקה לרפואה דחופה – מלר"ד (חדר מיון) במרכז רפואי לבריאות הנפש פטורים מתשלום.` (per `חוזר מנכ"ל 06/2024`)

Before anyone pays an emergency-room bill, check `references/er-waiver-list.md`.

## The emergency-room waiver list

The statutory list comes from `חוזר מנהל הרפואה 21/2016` and is shared by all four kupot. The full quoted list, the two separate agra-only triggers, the retro-claim procedure and each kupah's own non-uniform extensions are in `references/er-waiver-list.md`.

Four things to carry in your head:

- **Do not state a count** for the list. gov.il, Leumit and call.gov.il bullet the same statutory list into different numbers of items.
- The **hour rule** (01:00-06:00) and the **retrospective-justification rule** are two different triggers. The second applies `ללא קשר לשעת הביקור`. They get conflated constantly.
- If you already paid, you can still claim it back: bring the discharge summary and the receipt to the kupah's secretariat, and if the visit is found medically justified the kupah issues the commitment form to the hospital.
- The kupot's extensions are **not uniform**. Clalit has a blanket 19:00 to 07:00 exemption, Maccabi has an all-hours list plus a separate partial-payment list, Meuhedet gates on referral validity windows and road-accident time bands, and Leumit grants exemptions retrospectively via a moked doctor. Check the member's own kupah, never another one's.

## Copayments, ceilings and exemptions

The basic basket of **services** is identical across the four kupot by law. **The ceilings and the copayment amounts are not.** They are the one place the four legally differ, and the spread is wide: the quarterly family ceiling runs from 242.71 to 303.39 under the circular, and from 250 to 313.40 on the kupot's own 2026 pages. Never tell a member "it costs the same everywhere".

Full tables are in `references/copay-tables.md` and `references/exemptions-and-ceilings.md`. The load-bearing points:

- Which visits count toward the family ceiling, verbatim: `תקרת תשלום למשפחה (ילדים - עד גיל 18) - תקרה רבעונית המתייחסת להשתתפויות בגין ביקור אצל: רופא ראשוני, רופא שניוני, מרפאות חוץ ומכונים.` Dental copays are excluded.
- **Stacking**: reductions of the same kind do not compound, so an oleh who is also above retirement age gets the ceiling halved once, not quartered. Reductions of different kinds do apply on top of one another, and a discount never costs you the ceiling.
- **The retirement-age trap**: the family ceiling uses **mandatory** retirement age, while the exemptions in 16.1 and the drug discount in 16.8.2 use **optional** retirement age. A member can qualify for one and not the other.
- **The senior drug discount starts at 72, not 75.** Age 75 was superseded on 1.1.2016 and is the most common stale figure in circulation on this topic.
- The mobility-allowance exemption runs to 18 years **and 3 months**, not to 18.
- Organ donors, `טיפות חלב`, occupational medicine, child development for young children, and the named disease list `חולי דיאליזה, אונקולוגיה, איידס, גושה, CF, תלסמיה, המופיליה ושחפת` all carry their own exemptions. Holocaust survivors receiving a listed payment have a full prescription exemption.

## Prescription copayments are four different schemes

Do not give one generic prescription rule. **Clalit's scheme is structurally different from the other three.** Clalit charges 15 percent of the maximum consumer price or a low floor, whichever is the **higher**, from a threshold of 20.64. Maccabi, Meuhedet and Leumit charge a flat minimum up to a threshold of roughly 151.70 to 161.81 and only then switch to 15 percent.

Two further rules people miss: Maccabi charges `תרופות להן יש תחליפים זולים או שאינן חלק מספר התרופות (לפי הרשימה) – 50% מהמחיר לצרכן.` And a drug available only under a שב"ן, sold to someone not in that שב"ן, gets neither discount nor ceiling: `לא ייכלל בתקרת התשלום לחולים כרוניים, ולא יחולו עליו כל הנחה ופטור`.

Full per-kupah thresholds, floors and generic rates are in `references/copay-tables.md`.

## Ambulance refunds, and the trap

gov.il, updated 26.05.2026, verbatim:

- Full refund: `מי שפונו באמבולנס רגיל של מגן דוד אדום (מד"א) או ניידת טיפול נמרץ ואושפזו בבית חולים – זכאים להחזר מלא`
- Half refund: `מי שפונו בניידת טיפול נמרץ ולא אושפזו בבית חולים – זכאים להחזר בגובה 50%`
- **No refund at all**: `מי שפונו באמבולנס רגיל ולא אושפזו – אינם זכאים להחזר בעבור הוצאות ההעברה.`

The third line is the trap, and it is the one most people get wrong: a **regular** ambulance that does **not** end in admission is not refunded. Only the intensive-care ambulance carries a partial refund without admission.

Routing matters too. A **work accident** or a **terror-victim** case routes to the National Insurance Institute, not the kupah. A **road accident** routes to the **motor insurer**. Oncology and dialysis transport is refunded at `50% מתעריף מגן דוד אדום או ממחיר הנסיעה בפועל באמבולנס (הנמוך מביניהם)`.

**There is a 60-day deadline**, verbatim: `מי שלא יסדירו את התשלום באמצעות קופת חולים תוך 60 יום מיום הפינוי או ההעברה, יחויבו לשלם את מלוא הסכום לחברת האמבולנס.` Miss it and the full amount falls on the member.

No shekel ambulance tariff is given in this skill. The tariff lives in `תקנות מגן דוד אדום (אגרות הסעת חירום באמבולנס)` and could not be read from a primary source, so do not state one.

## Form 17

gov.il calls it `"טופס 17" (טופס התחייבות מהקופה המבטחת)`. It is the kupah's **financial commitment** to a provider, issued **in advance**, and it is what converts a chargeable visit into a covered one. All four kupot issue it digitally through their app or site.

The kupah does not have to issue one where the member attended without a prior commitment, where the reason is outside the exempt list, where the visit was not urgent, or where the treatment was elective. Those four cases are the usual reason a Form 17 request is refused.

## Switching kupot, and שב"ן seniority

A switch takes effect on one of six fixed dates a year, and a member may make `עד 2 מעברים בלבד, במהלך פרק זמן של 12 חודשים.`

| Apply between | Effective |
|---|---|
| 16.09-15.11 | 01.01 |
| 16.11-15.01 | 01.03 |
| 16.01-15.03 | 01.05 |
| 16.03-15.05 | 01.07 |
| 16.05-15.07 | 01.09 |
| 16.07-15.09 | 01.11 |

Two channels: in person at an Israel Post branch, `יש להתייצב באופן אישי ... ולרכוש טופס מעבר`, where the transfer form must be **purchased** (the fee amount is not published, so do not state one); or on the National Insurance Institute website, where `יש להצטייד בכרטיס אשראי בתוקף, על שמכם`.

**Supplementary-insurance seniority does carry across.** This corrects a false claim in earlier versions of this skill. Leumit, verbatim:

`עם מעברך לקופה חדשה מסתיים הביטוח המשלים (שב"ן) בקופה הישנה ... הקופה החדשה אינה רשאית להגביל או למנוע את הצטרפותך לביטוח המשלים, ובתנאים מסוימים אף תהיה זכאי לפטור מתקופת המתנה בקופה החדשה. על מנת לשמור על רצף זכויות עליך להעביר לקופה אליה עברת אישור וותק מהקופה הקודמת.`

Read that carefully before advising anyone. The new kupah may not refuse you supplementary cover. A waiver of the waiting period is available `בתנאים מסוימים`, which is a hedge, not a guarantee. And it is **not automatic**: the member must obtain an `אישור וותק` from the old kupah and hand it to the new one. Long-term-care continuity since 1.1.17 works the same way. Do not promise a specific waiting-period length or an "equivalent tier" rule; neither is established from a primary source.

## Examples

### Example 1: "I went to the ER on Tuesday afternoon and got a bill"
Ask three things before anything else: which kupah, what the reason for the visit was, and whether they were admitted. If admitted, it is free even without a referral or Form 17. If the reason is on the statutory `פטור מלא` list, it is free. If neither, quote the agra and the treatment charge as two components, give the kupah's published figure with its date, and walk them through the retro-claim route with the discharge summary and the receipt.

### Example 2: "How much is a dermatologist?"
Do not answer per visit. Explain the floating quarter: one charge covers that service for three months from the visit date, while the family ceiling is counted on the calendar quarter. Give the member's own kupah's figure from `references/copay-tables.md` with both vintages where they conflict, and check whether the family ceiling or an exemption already applies.

### Example 3: "Is it worth switching kupot?"
Cover the six effective dates, the two-per-12-months limit, and both channels. Correct the common belief that supplementary seniority is lost: it carries, but only if they get an `אישור וותק` from the old kupah. Point out that ceilings and copay amounts genuinely differ between the four, so it is a real financial comparison and not only a service one.

### Example 4: "My mother is 73 and pays a lot for prescriptions"
Check the 72-and-over drug discount, which uses optional retirement age. Check whether she is also in an exempt population under section 16. Check the chronic-drug monthly or quarterly ceiling for her kupah, noting that Meuhedet reckons it on a different period. Then give the per-kupah prescription scheme, because Clalit's works differently from the other three.

## Recommended MCP Servers

| MCP Server | What it provides | Install |
|---|---|---|
| **il-health** | Ministry of Health data: hospital quality of service, patient surveys, child health checkups, kupat cholim information | [Install](https://agentskills.co.il/en/mcp/il-health) |
| **kolzchut** | Israel's rights and entitlements knowledge base | [Install](https://agentskills.co.il/en/mcp/kolzchut) |
| **israel-drugs** | Israeli pharmaceutical database: medication profiles, health basket status, pricing, generic alternatives | [Install](https://agentskills.co.il/en/mcp/israel-drugs) |
| **israel-mental-health** | Community mental health clinics and psychiatric services by city, kupah and therapy type | [Install](https://agentskills.co.il/en/mcp/israel-mental-health) |
| **israel-clinical-trials** | Active and completed clinical trials at Israeli hospitals | [Install](https://agentskills.co.il/en/mcp/israel-clinical-trials) |

When these are available, prefer them over the static tables here for anything time-sensitive.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| MoH circular 1/2025, the statutory table | https://www.gov.il/BlobFolder/policy/sbn01-2025/he/files_circulars_sbn_sbn01-2025.pdf | definitions, ceilings, exemptions, all four kupot |
| MoH cross-kupah copayment page | https://call.gov.il/page/GE41 | family ceilings, what counts toward them |
| MoH emergency-room payment page | https://www.gov.il/he/service/emergency-room-payment | the two-component structure and the waiver list |
| MoH ambulance evacuation page | https://www.gov.il/he/service/ambulance-evacuation | refund rules and the 60-day deadline |
| ER exemptions, per kupah | https://call.gov.il/product-page/1002629 | each kupah's own non-uniform extensions |
| Clalit tariff page | https://www.clalit.co.il/he/info/about_site/Pages/sherutim_betashlum.aspx | Clalit's current amounts and update date |
| Leumit tariff page | https://www.leumit.co.il/insurance-policies/health-basket/health-basket-deductables/ | Leumit's current amounts and update date |
| Meuhedet copayments page | https://www.meuhedet.co.il/מידע-ללקוח/השתתפויות-ופטורים/ | Meuhedet's current amounts |
| Maccabi member site | https://www.maccabi4u.co.il | per-item eligibility, no consolidated tariff table |
| Ministry of Health | https://www.gov.il/he/departments/ministry_of_health | circulars, complaints, service pages |

## Gotchas

- Israel has exactly four kupot cholim. US insurance vocabulary such as "deductible", "in-network" and "out-of-network" does not map onto this system.
- **The basic basket of services is identical by law; the copays and ceilings are not.** Saying "it costs the same at every kupah" is wrong and is a real financial error for a member choosing between them.
- Specialist copays are **not per visit**. They are a floating quarter, and the ceiling that caps them is a calendar quarter. Two different clocks.
- A gynaecologist, paediatrician, internist and family doctor are **primary** and therefore free. A community specialist, a psychiatrist, a dietitian and a podiatrist are **secondary** and are charged.
- An emergency-room answer with a single number is always wrong. Agra plus treatment, with the waiver list checked first.
- **מכבי זהב is the entry supplementary tier, not the premium one.** מכבי שלי sits above it.
- The senior drug discount threshold is **72**. The figure 75 was superseded on 1.1.2016 and is still widely repeated.
- A regular ambulance that does not end in hospital admission is **not** refunded at all. Only the intensive-care ambulance is partly refunded without admission, and the claim has a 60-day deadline.
- Supplementary-insurance seniority **does** carry when switching kupot, subject to conditions, but only against an `אישור וותק` from the old kupah. It is not automatic and it is not impossible.
- Adult dental care is not in the basic basket; children are covered to 18. Dental copays are also excluded from the family ceiling.
- The 2026 health basket was issued as `חוזר מנכ"ל 1/2026 מיום 08.03.2026 – הרחבת סל שירותי הבריאות לשנת 2026`. **This skill deliberately carries no budget figure, technology count or list of additions for it**, because none could be verified from a primary source. Cite the circular by name and send the user to the Ministry of Health announcement.
- Amounts here are dated snapshots and are re-indexed. Treat every figure as needing confirmation against the kupah's own page, especially since no 2026 payments circular has been issued yet.

## Troubleshooting

### "I cannot get an appointment, there are no slots"
Possible causes to check with the kupah, not assumptions to state as fact: whether the specialty is covered by a `הסדר` with a nearby provider at all, whether the shortage is geographic rather than system-wide, and whether the member is looking only at one clinic. Ask the kupah directly, ask about cancellation lists, try other clinics in the same kupah, and check whether a supplementary tier opens a faster lane. If the wait exceeds the kupah's own published target, go to the kupah's `פניות הציבור`.

### "The medication is not covered"
The drug is probably outside the national basket. Check whether the supplementary plan covers it, whether a special approval from the kupah's medical committee is possible, and whether a basket-listed generic exists. A refusal can be appealed. Note that a drug available only under a שב"ן, sold to a non-member of it, carries neither discount nor ceiling.

### "My supplementary insurance says there is a waiting period"
Possible causes to check with the kupah: whether an `אישור וותק` from the previous kupah was ever submitted, and which specific benefit the waiting period attaches to. Do **not** tell the member that waiting periods cannot be waived; that is false. The new kupah may not refuse supplementary cover, and a waiver is available `בתנאים מסוימים`. This skill does not state a waiting-period length, because no primary source establishes one. Basic-basket coverage is immediate either way.

### Escalation ladder for any unresolved dispute
Inside the kupah first: `ועדת חריגים`, `ועדת ערר`, and `פניות הציבור`. All four publish these routes. Leumit's are by fax to 03-6949614, by post to `פניות הציבור, שפרינצק 23 תל אביב`, in person at the member's medical centre, or through the site form. Meuhedet adds `ניתן להגיש ערעור לוועדת ערעורים מחוזית בצרוף גיליון המיון וקבלה על התשלום של המיון.` Above the kupah sits the Ministry of Health's `נציבות קבילות הציבור לחוק ביטוח בריאות ממלכתי`. This skill deliberately gives no URL or online-form address for the commissioner and states no filing deadline, because none could be verified. Do not claim that a kupah-level complaint is a precondition for going to the commissioner.
