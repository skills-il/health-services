---
name: israeli-food-allergy-navigator
description: "Not medical advice and not a diagnosis. Bureaucracy navigator for life-threatening (IgE) food allergy in Israel, focused on children. Covers what ganim, schools and tzaharonim owe under Ministry of Education standing instruction 0042: allergen-free zones and signage, menus planned ahead for holidays and trips, catering approval, non-discrimination. Builds the parent packet (annual health declaration, allergist letter, two in-date EpiPens, medication forms) and the accommodation-request letter. Covers the personal medical assistant criterion and the five prohibitions schools most often breach, plus the Bituach Leumi disabled-child claim for allergy at 50% (1,943 NIS), ages 9 months to 10 years, with its five qualifying alternatives. Use when a parent or allergic adult needs entitlements, school arrangements, or a claim. Do NOT use for celiac or gluten (use israeli-celiac-navigator), meal planning (use israeli-nutrition-planner), clinical diagnosis, drug dosing, or non-Israeli systems."
license: MIT
---

# Israeli Food Allergy Navigator

## Legal notice

This is a free information tool operated by an artificial-intelligence model. It explains the bureaucratic entitlements of children and adults with food allergy in Israel, quotes the Ministry of Education standing instruction and the Bituach Leumi criterion, and drafts request letters to educational institutions. All of its output is produced automatically, without the involvement, review or approval of a physician, an allergy specialist, or any licensed medical professional.

The tool's output is not a medical diagnosis, not a medical opinion, not a prescription and not treatment. It is bureaucratic information about entitlements and documents only. Where the tool helps lay out an allergy action-plan card, that card is a transcription aid for the plan the treating physician wrote, it is not itself a medical instruction, and it must be reviewed and signed by the treating physician before use. The tool does not examine the child, does not interpret allergy test results, does not determine which allergens are involved, does not assess the degree of risk, does not decide whether an adrenaline auto-injector is required, and does not determine any dose. Those acts require the tools and experience of a physician specialising in allergy. An artificial-intelligence model may err, omit data, or present a wrong conclusion.

Do not rely on this tool for any medical decision, and do not use it to decide whether a reaction requires treatment. Where an anaphylactic reaction is suspected, inject adrenaline per the treating physician's instructions and call 101 immediately. Any text the tool drafts is an automatic draft for personal organisation only. It explains appeal routes and deadlines published by Bituach Leumi but does not draft or file an appeal, and is prepared without the involvement of a lawyer. This tool is not a substitute for advice that takes account of the particular data and needs of each person, and before any medical decision, the filing of a claim or an appeal you should consult the treating physician and the competent authority. Any use of the output is the sole responsibility of the user.

## Critical Disclaimer

**Read this before using the skill. Every response based on this skill must repeat the relevant disclaimer.**

1. **This is a bureaucracy navigator, not medical advice.** Never diagnose an allergy, never recommend or adjust a dose, never tell anyone whether they need an EpiPen. Those are decisions for a physician specialising in allergy (רופא/ה מומחה/ית לאלרגיה).
2. **In a suspected anaphylactic reaction, the answer is always adrenaline then 101.** Never help a user reason about whether a reaction is "bad enough". If a user is describing a reaction happening right now, tell them to inject the EpiPen and call 101 (Magen David Adom) immediately, and stop giving bureaucracy guidance.
3. **The 1,943 NIS figure is the current published amount and Bituach Leumi rates update every January.** Always cite the effective year and point the user at the BTL source before they budget around it.
4. **Do not promise an outcome on a claim or a סייעת application.** Eligibility criteria are published, but the decision belongs to the committee. Describe the criteria and the evidence needed, not the verdict.
5. **Do not fabricate a circular number, section number, or form number.** Every one used in this skill is sourced in the Reference Links or the reference files. If a user asks about something not sourced there, say so and point them at the source.

## Problem

A child with a life-threatening food allergy in Israel has written, binding rights that almost no parent knows. The Ministry of Education obliges the gan, school and tzaharon to declare allergen-free zones, plan menus around the allergen and avoid exclusion. Bituach Leumi pays a disabled-child allowance from 9 months to 10 years on any one of five conditions, one needing no documented episode. Schools still say a סייעת is a precondition for a trip, which the instruction forbids. This skill turns the written rules into the documents a parent sends.

## Instructions

### Step 0: Triage the request before anything else

Classify what the user is asking:

| Situation | Response |
|---|---|
| A reaction is happening NOW | Stop. Tell them: give first aid without delay following the child's own written action plan from their doctor, inject the EpiPen into the outer thigh, call 101 immediately, and note the time of injection. Tell them the 101 dispatcher will talk them through what to do until help arrives, so stay on the line and follow the dispatcher. **If no injector is available, do not stall: call 101 immediately, say "תגובה אנפילקטית ואין מזרק", stay on the line, and ask whether another injector is on site.** While on the line to 101, and without leaving the child without an adult, ask another person to fetch the institution's own injector: a school, gan, tzaharon or licensed maon of ten or more toddlers must keep one by law, behind a sign reading "מזרק אפינפרין". A mishpachton or small home daycare may have none, so never delay 101 to look. Do not continue with any other content, and do not give any further clinical guidance yourself. |
| No diagnosis yet, suspects allergy | Route to a kupat cholim allergist referral first. The skill's entitlements almost all require an allergist's written document. Do not help them self-diagnose. |
| Diagnosed, needs school arrangements | Go to Step 2 and Step 3. This is the most common case. |
| Child aged 0-3 in a maon or mishpachton | Go to Step 2e. Instruction 0042 does not apply there. |
| Diagnosed, asking about money | Go to Step 5 (Bituach Leumi). Check the age window first, it disqualifies many. |
| Adult with allergy | Go to Step 6. Most child-specific entitlements do not apply. |

### Step 1: Understand what kind of allergy this is

The obligations differ by allergen behaviour, so establish this early. Reactions develop from eating the allergenic food **even in a minimal quantity**, and in rare cases contact alone causes a significant reaction.

Epidemiology and the main Israeli allergens are in `references/moe-standing-instruction-0042.md`.

**The distinction that drives everything downstream:**

| Allergen type | Example | What the institution must do |
|---|---|---|
| Airborne dispersal | Peanuts, nuts in natural form, snacks containing peanuts | Define the **whole institution or activity area** as a zone clean of the allergen, with prominent signage visible to all, inside and outside, stating the allergen may not be brought in |
| Contact or ingestion only | Most milk, egg, sesame cases | Declare the **classroom, activity area and further agreed spaces** a safe environment, announced by prominent signs identifiable during all activity hours |

Ask the user which their child's allergist has documented. If they do not know, that is the first thing to get in writing.

### Step 2: Build the pre-school-year parent packet

This is the highest-value deliverable in the skill. Produce it as a checklist the parent can work through, and offer to draft each document.

**2a. The annual health declaration plus allergist letter**

Parents must sign a health declaration (הצהרת בריאות) **every year** and attach a medical document from the treating allergist detailing the foods the child is allergic to and the actions to take on exposure. The declaration is governed today by standing instruction **0382**, which also says the school **may not demand any further declaration or medical document** beyond the declaration and the physician's signed document, so a separate per-trip medical form is not required. Draft a request to the allergist listing exactly what the letter must contain, so the family does not need a second appointment, and ask it to state explicitly whether the allergen has airborne-dispersal property, since that determines the institution's obligation under Step 1.

**2b. Two EpiPens, not one**

This trips up most families. The instruction requires:
- One **in-date** injector deposited in the emergency medicine box at the school, gan, or the facility where the tzaharon runs, marked with the student's name and details, **plus a photocopy of the HMO card**
- A **second** injector bearing the name, kept in the student's own bag
- Parents are responsible for replacing each injector when it expires

**On paying for them.** The places one is needed (school box, the child's bag, tzaharon, home) are often three or four. EpiPen and EpiPen Jr are **in the health basket** with a registry restriction (specialist prescription or another restriction), and the Mylan generic auto-injectors are in the basket too; Jext is registered but **not** in the basket, and nasal adrenaline (neffy) is not registered in Israel. Maccabi publishes a 15% co-pay subject to a minimum fee, final cost set at dispensing. **No kupah publishes how many injectors it funds per year, so never state a number.** Tell the family to ask their kupah how many are funded, the co-pay, and what the allergist must write for additional injectors. Detail in `references/injectors-and-oit.md`.

Offer a tracking note with both expiry dates. **Track the device, not only the date:** a growing child can outgrow the junior device while the expiry still looks fine, so ask the allergist at every renewal which strength suits the child now. Never state a strength, a weight band or a dose yourself.

**2c. Medication-administration forms**

Parents must sign the forms permitting medication to be administered to the student. 0042 still cites these as section 2.2-74 of עב/1(ב), but that instruction was **cancelled and replaced by standing instruction 0384**, "הנחיות למתן טיפול תרופתי במוסד החינוך" (29.12.2022). It needs two documents, a specialist's form and the parents' authorisation, and the physician's request is valid for one school year at most. Ask the secretary for the forms under instruction 0384 by its title; quoting the old section number sends the office looking for a cancelled text.

**2d. Tzaharon registration disclosure**

Parents must report **at the registration stage** for the tzaharon that the child has a food allergy. Flag this because tzaharon registration often happens months before the school year and parents forget it is a separate disclosure.

**2e. Ages 0-3: maon and mishpachton**

Instruction 0042 covers schools, ganim and tzaharonim, not daycare. A licensed maon is supervised by the Ministry of Education under the Daycare Supervision Law and its operating booklet, which says a toddler with allergy may not be refused or removed during the year, may not be excluded from any activity or separated from the group, and requires signage. Parents supply the medication at their own cost and authorise staff in writing; after any adrenaline or antihistamine the toddler goes to hospital by ambulance. A meal-time allergy aide is applied for through the Ministry of Labor and funded by the Welfare Ministry; the 2025-26 circular expired on 31.8.2026 and no successor was published as of October 2026, so send the family to the gov.il service page rather than stating terms. Also ask the maon to confirm all staff completed the mandatory first-aid course with its allergy content, and that the action plan is posted in the toddler's room. Detail in `references/maon-ages-0-3.md`.

### Step 3: The accommodations letter to the gan or school

Draft a letter that cites the instruction rather than asking as a favour. The institution's obligations, all of which can be requested by name:

| Obligation | What to ask for concretely |
|---|---|
| Zone definition and signage | Written confirmation which zone is declared allergen-clean, and that signs are identifiable during all activity hours |
| Awareness | That the principal or delegate raise awareness among the team, staff, parents and students |
| Timetable | That most lessons be in the home classroom, and eating take place after the long break where possible |
| Cleaning | A named duty student to wipe the child's desk before lessons in other spaces. In gan and tzaharon this is staff, not children |
| Tzaharon merging | That tzaharon groups not be merged before the meal, only after it |
| Menus planned in advance | Holidays (including mishloach manot), health meals, food sales and trips planned to exclude the allergen, with the parents' committee enlisted |
| Emotional support | Accompaniment by the institution's counsellor or psychologist, and guidance to the tzaharon manager on the emotional support required |
| No exclusion | Explicit acknowledgement that discrimination or exclusion on grounds of the allergy is prohibited |
| Class-parent notification | Notification to all class and tzaharon parents before the year starts and at the first parents' meeting, with the family |
| Catering | The caterer's contact details before any trip or activity with food, so parents can approve the composition or supply their own |
| The child's own voice | The option for the child to present their allergy themselves at the start of the year, per their age and willingness |
| Staff training with hands-on injector practice | Confirmation the start-of-year training covered **practical use of the injector**, not just awareness, and that every substitute, instructor and temporary worker is briefed. This decides whether an adult in the room can actually act |
| Protocol posted, not filed | The attack protocol and family phone numbers displayed in the office **and** one further prominent place |
| Pre-year meeting and a named contact | The meeting the principal must hold before the year starts with the management team and the health-service nurse (a dietitian and the parents are recommended invitees), which sets **a named person responsible for contact with the parents** |
| Vending machines | If the institution is declared allergen-clean, products containing the allergen may not be sold in its vending machines or cafeteria |
| Bring your own food, and pay less for it | The right to supply the child's meal independently **and have the proportional part of the payment deducted** |
| Overnight and multi-day trips | Per the Ministry's 2019 health-supervision trip guidance: the trip medic is told about the child and where the injector is kept and rides the child's bus, and on an overnight trip the children sleeping in the same space are told to keep the allergen out of it |

Write the letter in Hebrew, short and non-adversarial: cite the instruction, list the requests, offer to meet. If it is ignored, escalate to the school's מפקח/ת and the district office (for a tzaharon, the local authority's education department), not to a legal threat.

### Step 4: The personal medical assistant (סייעת רפואית)

Life-threatening food allergy **is** included in the criteria for a personal escort (medical assistant) from the inter-ministerial committee, per **section 2.2-91 of עז/4(א)**, "סייעות רפואיות בחינוך הרגיל", today standing instruction **0011**. Read its criterion before promising anything: it names allergy to milk, peanuts, nuts, almonds, sesame, eggs or fish "עם תיעוד ברור של חומרת התגובה ובשילוב של אסטמה אלרגית", on a document from a paediatric allergist dated within the six months before the application. Assistance starts at age 3 in a municipal gan, is decided separately from the Bituach Leumi allowance, and only the local authority can apply or appeal. Quote the criterion and ask the allergist to address each element; never tell a family they will qualify.

**Two rights schools most often get wrong, and the most useful thing in this skill:**

The first two are in 0042 section 5.14, alongside the cross-reference to עז/4(א):

1. **Parents may not be compelled** to submit an application for assistance via the local authority. If a school presents the application as mandatory, that is contrary to the instruction.
2. **A student may not be prevented** from taking part in an educational activity at, or on behalf of, the institution in the absence of an assistant, **even where the student is found eligible**. A school cannot make a trip conditional on a סייעת being present.

**Three further prohibitions, all in instruction 0042 itself rather than in עז/4(א), which parents are rarely told about:**

3. **Attendance may not be conditioned on the allergy at all.** Section 5.15: "אין להתנות השתתפות תלמיד במסגרת המוסד החינוכי או בצהרון בשל היותו אלרגי למזון או בעל לקות בריאות אחרת". Quote this when a gan or tzaharon says it cannot take the child.
4. **Parents may not be made to sign a waiver.** The institution may not have parents sign documents that place responsibility for caring for the child on one party or another, or that release it from responsibility. If a school presents a waiver as a condition of attendance, it is acting contrary to the instruction.
5. **Parents may not be compelled to come along as escorts on a trip, and a trip may not be conditioned on their doing so.** Parents must be *allowed* to accompany, including with a car for evacuation, but "come with him or he stays home" is prohibited. In practice this demand is more common than the סייעת version, so check which one the family is actually facing.

When told a child cannot attend without a סייעת or a parent, quote the point back and offer a short reply citing the instruction, not a legal threat.

Applications go through the local authority. Windows vary by municipality and school year, so tell the user to check their own municipality rather than relying on a date from this skill.

### Step 5: The Bituach Leumi disabled-child claim (גמלת ילד נכה)

Allergy is a named qualifying condition on the Bituach Leumi list of impairments for the disabled-child allowance.

**Check the gate first, in this order.** Most families fail on age, so ask that before anything else:

| Requirement | Exact criterion |
|---|---|
| Age | From age **9 months to age 10 years** |
| Rate | **50%**, amounting to **1,943 NIS** |
| Qualifying event | The general eligibility conditions **plus one of five alternatives**, listed below |
| Diagnostic tests | Confirmation of allergy test criteria: skin prick test (SPT), blood test, or challenge test (מבחן תגר) |
| Allergist recommendation | A recommendation from a physician specialising in allergy to be permanently equipped with an EpiPen, **or a reasoned justification for refraining** from carrying one. This is both a required document **and**, on its own, qualifying alternative 5 below |
| Episode documentation | **Real-time** medical documentation of the treatment given during an attack that included a respiratory component or anaphylactic shock |
| Retroactivity | Paid up to **one year retroactively** from the date the claim was filed |

**The five alternative qualifying conditions. Only one is needed, and agents routinely present just the first.** Bituach Leumi lists them under "ועל אחד מהתנאים האלה". The child underwent a food allergy event that:

1. was characterised by **anaphylactic shock**; or
2. was expressed as an **anaphylactic reaction**, meaning a clinical response of **two different body systems**; or
3. was expressed as **shortness of breath characterised by a drop in oxygen saturation**; or
4. **required treatment with injected adrenaline** (EpiPen); **or**
5. **there is a standing recommendation from an allergy specialist to be permanently equipped with an EpiPen** (or a reasoned justification for refraining from carrying one).

**Alternative 5 is not an event at all, and it is the one that changes answers.** A child who has never had a documented reaction still qualifies on this route if their allergist has recommended carrying an EpiPen, which for a diagnosed life-threatening allergy is common. Never tell a family they fail the criterion for want of a documented episode: check 5 first, since it is the only one obtainable on demand at a routine appointment.

Route 2 is broader than families assume: a reaction involving two body systems may qualify even if nobody called it anaphylaxis. Ask what happened; the characterisation is the physician's and the committee's, not the skill's.

**On the real-time documentation.** It cannot be reconstructed later, so tell every newly diagnosed family to take the ER or clinic documentation **at the visit** whenever the child is treated for a reaction with breathing difficulty or anaphylaxis. A second contemporaneous record exists: a school reaction that needed evacuation or the injector must be filed as an exceptional incident (0042 section 6.11), so families should request a copy. It corroborates, it does not replace.

**But missing documentation is not automatically fatal.** First, qualifying alternative 5 above does not require an episode at all. Second, where the required documentation does not exist, current documentation from a **pulmonologist or allergist confirming active asthma** should be brought instead. Never tell a family their claim is hopeless purely because they did not collect paperwork at the time; check the asthma route first.

**Committee and duration.** Comprehensive documents let BTL decide **without summoning the child**; include documents from the last year. If decided on documents alone, the family may request within **45 days** a committee with the child present. A first determination runs **two years**, then **three** per the child's condition, then to age 10.

**If a committee is convened**, recommend the free preparation at **Yad Machvana (יד מכוונת)** by name, and tell the family they may ask that daily-living activities the child does unaided not be examined. Both, plus the one-page summary to bring, are in `references/bituach-leumi-allergy-claim.md`. The allowance also unlocks benefits elsewhere (for example a local arnona discount), so the claim is worth more than the monthly figure.

If the child is over 10, say so plainly, then send the family to the impairment list (for example **"קצבה לילד עם מספר ליקויים"**) rather than closing the door. Do not suggest the respiratory criterion on asthma grounds: it covers oxygen most of the day, a tracheostomy or CF.

### Step 6: Adults with food allergy

Most of the above is child-specific. For adults:
- The educational-institution obligations do not apply. Workplace arrangements are negotiated with the employer, not granted by this instruction.
- The disabled-child allowance does not apply by definition.
- Allergen labelling on packaged food is the main systematic protection. Since 02.01.2025 allergens are emphasised **inside the ingredient list** (EU Regulation 1169/2011, adopted under section 3א of the Public Health Protection (Food) Law), but until **1.1.2028** either format is lawful, so absent emphasis is not evidence of an absent allergen. "עלול להכיל" is unregulated and voluntary. Detail in `references/allergen-labelling.md`.
- Restaurants and airline meals: a request confirmed in writing in advance, not an entitlement.

### Step 7: OIT, and being honest about it

Oral immunotherapy (OIT) is the treatment families ask about most. Answer with visible uncertainty:
- **Do not state the waiting time, the minimum age or the cost as fact.** The treating centres do not publish them; give the centre's contact details, not a number.
- **Basket status, stated narrowly.** Shamir's own programme page says its OIT is private, not in the health basket and not funded by supplementary insurance, and the 2026 basket expansion contains no food-allergy item. Other centres' funding is unverified here, so send the family to their kupah before they budget.
- Do not quote success rates as a promise, and never imply OIT removes the need for an EpiPen.

The food-allergy treatment unit at Shamir Medical Center (formerly Assaf Harofeh) is on **08-9779820** or **foodallergyait@gmail.com**; the institute office is **08-9779817**.


## Examples

### Example 1: Newly diagnosed 4-year-old, peanut allergy, gan starts in September

Peanut is airborne-dispersal, so the **whole gan** must be declared allergen-clean with visible signage. Produce the packet: allergist request with airborne-property language, annual health declaration, two EpiPens with the emergency-box HMO card copy, and the medication-administration forms. Draft the accommodations letter. Flag the BTL claim as open (age 4 is inside the window) and note that the allergist's EpiPen recommendation alone qualifies under alternative 5, so the claim does not wait on an episode.

### Example 2: School says the trip requires a סייעת or the child stays home

First establish which demand is being made, a סייעת or a parent escort, since the instruction prohibits both separately. Quote the relevant rights from Step 4. Draft a short, non-adversarial reply citing 0042 section 5.14, noting that a student may not be prevented from participating in the absence of an assistant even when eligible, and that parents may not be compelled to apply via the local authority. Offer to attend a meeting.

### Example 3: Parent of an 11-year-old asks about the allowance

Answer plainly that the allergy criterion runs to age 10, so a claim on it will not succeed now. Redirect to the school accommodations, which have no age limit, and to the impairment list if another condition is present.

## Bundled Resources

### References

| File | Contents |
|---|---|
| `references/moe-standing-instruction-0042.md` | The institution and parent obligations, quoted, with section references |
| `references/bituach-leumi-allergy-claim.md` | The claim gate, the five qualifying alternatives, and how to prepare in advance |
| `references/document-templates.md` | Letter and form skeletons: allergist request, accommodations letter, action-plan card, סייעת response |
| `references/maon-ages-0-3.md` | Daycare rules for ages 0-3, the allergy aide, the epinephrine stock duty |
| `references/injectors-and-oit.md` | Basket status of each injector, kupah pages, the school stock-injector law, OIT funding |

## Recommended MCP Servers

| MCP | Why |
|---|---|
| `kolzchut` | Live All-Rights pages for entitlements that change between school years |
| `israel-drugs` | Registration status and availability of adrenaline auto-injectors |
| `israel-clinical-trials` | Open Israeli trials, relevant when a family asks about OIT research |

## Gotchas

These are agent failure modes, not user errors.

1. **Do not answer a live reaction with bureaucracy.** If the message describes symptoms happening now, the only correct output is adrenaline plus 101. An agent that starts explaining entitlements while a child is reacting has failed completely.
2. **Do not assume the 50% rate generalises.** 50% / 1,943 NIS is the allergy criterion's rate only; never transfer a rate across criteria.
3. **Do not silently drop the age gate.** Agents tend to describe the claim enthusiastically and mention the 9-month-to-10-year window as an afterthought, or not at all. Lead with it. It is the single most common reason a claim fails.
4. **Do not treat the instruction's prohibitions as soft guidance.** "May not be compelled" and "may not be prevented" (5.14), "may not be conditioned on the allergy" (5.15), "may not be made to sign a waiver" (5.16) and "may not be compelled to escort" (6.14(ג)) are the five most actionable sentences in the instruction, and agents routinely paraphrase them into vague encouragement. Quote them.
5. **Do not conflate this with celiac.** Celiac is autoimmune, has no EpiPen, no anaphylaxis pathway, and an entirely different entitlement set. Route to `israeli-celiac-navigator`.
6. **Do not present the BTL criterion as requiring a documented episode.** There are five qualifying alternatives and the fifth is a standing allergist EpiPen recommendation with no event at all. Treating the allergist letter purely as supporting evidence, rather than as a qualifying route in its own right, wrongly turns families away.
7. **Do not cite the cancelled instruction numbers as live.** 0042 still points to 2.2-74 and 2.2-84, but the current texts are instructions 0384 (medication) and 0382 (health declaration). Do not apply 0042 to a maon either; Step 2e.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Bituach Leumi, allergy criterion | https://www.btl.gov.il/benefits/Disabled_Child/likuilist/Pages/allergy.aspx | Age window, rate, required evidence |
| Bituach Leumi, disabled-child impairment list | https://www.btl.gov.il/benefits/Disabled_Child/likuilist/Pages/default.aspx | Whether another criterion fits better |
| Bituach Leumi, disabled child | https://www.btl.gov.il/benefits/Disabled_Child/Pages/default.aspx | Claim filing route and current amounts |
| Ministry of Health allergen guidance | https://www.gov.il/he/pages/allergens-guidance | Current allergen labelling requirements |
| Ministry of Health food reform, allergen marking | https://www.gov.il/he/pages/02012025-01 | Changes to how allergens are marked |
| Ministry of Education instruction 0042 | https://apps.education.gov.il/Mankal/Horaa.aspx?siduri=51 | Whether 0042 is still in force and its full section text |
| Instruction 0384, medication in school | https://apps.education.gov.il/Mankal/Horaa.aspx?siduri=483 | The current medication forms |
| Instruction 0011, medical assistants | https://apps.education.gov.il/Mankal/Horaa.aspx?siduri=41 | The allergy criterion for a סייעת |
| Bituach Leumi, disabled-child rates | https://www.btl.gov.il/benefits/Disabled_Child/Pages/%D7%A9%D7%99%D7%A2%D7%95%D7%A8%D7%99%20%D7%94%D7%92%D7%9E%D7%9C%D7%94.aspx | The 50% amount and its effective date, updated every January |
| Shamir food allergy clinic | https://www.shamir.org/clinic/foodallergyclinic/ | OIT programme contact details, ask them for wait and age |

## Troubleshooting

### Problem: "The gan says it cannot be nut-free because other parents object"

The obligation for an airborne-dispersal allergen is to define the institution or activity area as clean of the allergen with prominent signage, and to enlist the parents' leadership in planning menus. Parental objection does not remove it. Draft a letter citing the instruction and requesting written confirmation of the declared zone.

### Problem: "Bituach Leumi rejected the claim"

**First check whether the claim was assessed against qualifying alternative 5**, the standing allergist recommendation to carry an EpiPen, which requires no documented episode. Families are commonly refused for want of episode documentation when alternative 5 was open to them, so establish which route was actually considered before accepting the refusal. Otherwise identify the missing document: the test confirmation, the allergist recommendation, or the real-time episode documentation (with the active-asthma fallback). Before the family decides whether to appeal, check the age window is still open. A medical-committee decision is appealed to the **ועדה רפואית לעררים** with a reasoned request to the branch's disabled-child department: the law allows 60 days, and BTL says it accepts 90, so aim for 60. A rejection on non-medical grounds goes to the Labour Court within 12 months. A new claim may be filed after 6 months, or at once on deterioration. Always check the deadline printed on the decision letter; the skill explains routes but does not draft the appeal, and free legal aid exists. Detail in `references/bituach-leumi-allergy-claim.md`.

### Problem: "The school lost the EpiPen or it expired"

Replacement is the parents' responsibility under the instruction. Rebuild the emergency box deposit: in-date injector, name and details, HMO card photocopy, and confirm the second injector in the child's bag. Use this as the trigger to set an expiry reminder for both.
