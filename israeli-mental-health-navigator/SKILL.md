---
name: israeli-mental-health-navigator
description: Not a clinical diagnosis and not treatment. Guide to mental health services in Israel including therapy through kupot cholim, crisis hotlines, PTSD resources, and workplace mental health rights. Use when a user needs information about accessing psychiatric or psychological care, finding subsidized therapy, understanding the 2015 mental health reform, using crisis lines like ERAN (1201) or Natal, or navigating PTSD recognition through Bituach Leumi. Covers CBT, EMDR, private therapy costs, and employee mental health days. Also covers psychiatric emergency rooms and the rights that apply to compulsory hospitalization. Do NOT use for clinical diagnosis or medication recommendations.
license: MIT
compatibility: Works with all major AI coding agents
---


# Israeli Mental Health Navigator

## Legal notice

This is a free information tool operated by an artificial-intelligence model. It explains how the Israeli mental health system is structured: entitlements under the National Health Insurance Law, the referral routes into the kupot cholim, crisis lines, and what the Treatment of Mental Patients Law, 1991 provides. All of its output is produced automatically, without the involvement, review or approval of a physician, psychiatrist, psychologist, social worker or lawyer. The output is not a diagnosis, not a severity assessment, not treatment, not a professional opinion and not legal advice, but general information about existing arrangements only: it involves no examination of and no meeting with a patient, does not consider your personal circumstances, and does not determine a disability percentage or an entitlement. An artificial-intelligence model may err, omit data or present a wrong conclusion, so verify every figure with your kupat cholim, with Bituach Leumi or with the competent authority.

Do not rely on the output to decide on treatment or medication, to appeal a hospitalization order or in any other legal proceeding, or to file a claim with Bituach Leumi. This tool is not a substitute for advice that takes into account the particular data and needs of each person. If you are in immediate distress call ERAN at 1201, and if anyone is in immediate danger call 101 or 100.

## Instructions

### Step 1: Mental Health Rights Under National Health Insurance

Since July 2015, mental health care in Israel has been covered under the National Health Insurance Law (chok bituach briut mamlachti, חוק ביטוח בריאות ממלכתי). This landmark reform transferred psychiatric and psychological services from the Ministry of Health to the kupot cholim (health funds).

| Aspect | Details |
|--------|---------|
| Year of reform | July 2015 |
| Current system | Kupot cholim (Clalit, Maccabi, Meuhedet, Leumit) |
| What is covered | Psychiatric consultation, psychotherapy, psychological assessment, medication |
| Who is eligible | All Israeli residents registered with a kupat cholim |
| Cost to patient (2026) | Depends on the setting, not a single national number. See Step 2 |

Key rights:
- Every Israeli resident has the right to mental health treatment through their kupah, for children, adolescents and adults, covering individual and group therapy, with psychiatric medications under the health basket (sal briut, סל בריאות)
- A referral IS required for the community route, and some kupot add a pre-authorization step (Step 2). Only Maccabi's procedure was read, so do not generalize it to the other three. None of this applies to a psychiatric ER, see Step 3

2025-2026 system status: kupat cholim mental health budgets rose from around 347 million NIS in 2024 to around 591 million NIS in 2025, with further additions budgeted for 2026. Demand still outpaces supply and waiting lists remain a known bottleneck. A January 2025 Ministry of Health proposal to charge 35 NIS per public psychotherapy session (capped at 210 NIS per family per quarter) was not approved at its Knesset hearing and no later approval was found, so do not quote it as a current copay.

### Step 2: Accessing Therapy Through Kupat Cholim

The process for starting therapy through any of the four kupot:

| Step | Action | Details |
|------|--------|---------|
| 1 | Get a referral | From your family doctor or a mental health clinician. Ask whether Form 17 is also required |
| 2 | Submit a pre-authorization request | Kupah-dependent. Maccabi requires bakashat hitchayvut with the referral attached |
| 3 | Contact the mental health department | Call the machleket briut hanefesh (מחלקת בריאות הנפש) and book at the clinic |
| 4 | Initial assessment | A defined entitlement, not an informal screening. See the session table below |
| 5 | Begin treatment | Typically weekly, reviewed periodically |

Copay depends on the SETTING, not on which kupah you belong to. The National Health Insurance service catalogue defines it by reference:

| Setting | Copay rule |
|---------|-----------|
| Community mental health clinic (מרפאה בקהילה) | Charged at the secondary-physician (rofeh shniyoni) quarterly tariff |
| Outpatient clinic in a general hospital (מרפאת חוץ בבית חולים כללי) | Charged at the standard hospital outpatient tariff |
| Outpatient clinic in a psychiatric hospital (מרפאת חוץ בבית חולים פסיכיאטרי) | Charged at the secondary-physician quarterly tariff |

The only per-kupah figures we could read directly are Maccabi's (page updated 29.7.2026): **41 NIS quarterly** at a public-hospital outpatient clinic, and **free** at a psychiatric hospital, at public Ministry of Health clinics, and at private clinics under agreement with Maccabi.

VERIFY BEFORE QUOTING: Clalit, Meuhedet and Leumit publish their secondary-physician tariffs in separate copay booklets we have not read. Do not assume they match Maccabi's 41 NIS. Send the user to their own kupah's booklet or service line.

Session entitlement (Maccabi's published structure, at Ministry of Health public clinics and hospital outpatient clinics):

| Stage | Entitlement |
|-------|-------------|
| Assessment (adults or children) | 2 sessions: one diagnostic meeting plus one treatment meeting |
| Treatment card (kartisiya, כרטיסייה) | 15 therapeutic sessions from a defined list, up to one year from the first treatment, whichever comes first |
| At private clinics under agreement with the kupah | Assessment plus a course of treatment at the therapist's clinical discretion. No fixed session cap |

The agreement-clinic route has no session cap and no cost, and is usually the best answer for someone who cannot afford private therapy.

Important notes:
- Waits run to weeks or months in many regions, and there is no binding national maximum, so do not quote one as an entitlement.
- If the therapist is not a good fit, you may request a different one
- Do not promise anything from supplementary insurance (shaban, שב"ן). A shaban may not sell a service already inside the health basket, and adult psychotherapy has been inside it since 2015, so what it adds is a question for the user's own kupah
- Children and adolescents go through the same assessment-plus-kartisiya structure. A minor of 14 may consent alone only to routine care, and mental health treatment is not routine, so the caregiver involves the parents, unless the minor objects or contacting them could harm the minor or the treatment, in which case a social worker under the Youth Law is brought in instead; from 15 a minor may ask to be admitted voluntarily (s.4B). Outside the kupah, the municipal educational-psychology service (shefach, שפ"ח), reached through the child's school, also assesses and treats pupils and advises parents. Details in `references/patient-rights.md`
- Do NOT expect reimbursement for a therapist you find yourself (Maccabi states none is given). When the public clinic is full, ask for a private clinic UNDER AGREEMENT with your kupah (מרפאה פרטית שבהסכם), see Troubleshooting.
- Once treatment starts, a kupah may not cut it off over a contract dispute with the provider (Deputy DG circular 01/2017).
- Between weekly therapy and admission sits day treatment or day hospitalization (ashpuz yom, אשפוז יום): adults 18+ in an acute state, five days a week, 6-7 hours a day, by referral from a mental health professional, free of charge. For minors, Kol Zchut points to separate children's frameworks; ask the kupah.
- Fear of a record keeps people from care. Caregivers owe confidentiality (Patient's Rights Law ss.19-20, Treatment of Mental Patients Law s.42), with statutory exceptions that include reporting duties for driving (Traffic Ordinance s.12B), firearms (Firearms Law s.11A) and a suspected offence against a minor or helpless person by someone responsible for them (Penal Law s.368D). Details, and what not to promise, in `references/patient-rights.md`.

### Step 3: Crisis Hotlines and Emergency Support

| Hotline | Number | Hebrew Name | Availability | Focus |
|---------|--------|-------------|-------------|-------|
| ERAN | 1201; WhatsApp 052-845-1201; SMS 052-999-3544 | ער"ן | Phone 24/7; chat and WhatsApp 08:00-02:00; SMS 08:00 to midnight; email within 48h. Arabic is extension 7 and runs ONLY 10:00-12:00 and 19:00-21:00 | General emotional support, suicidal ideation, crisis intervention |
| Sahar | Chat at sahar.org.il, WhatsApp 055-957-1399 | סה"ר | Says 24/7, but its own page also posts hours of Sun-Thu 16:00-03:00 and Fri, Sat and holiday eves 18:00-00:00; rely on those | Online emotional support in Hebrew and Arabic for those who prefer text |
| Natal | *3362 | נט"ל | Phone 24/7; chat Sun-Thu 16:00-24:00 | Trauma and PTSD, war and terror-related distress |
| Nefesh Achat | *8944 | נפש אחת | 24/7, 7 days a week including holidays | Post-trauma support line run by MoD Rehabilitation with Natal, for IDF disabled, discharged soldiers and their families |
| Sexual assault support centers | 1202 (answered by women), 1203 (answered by men). WhatsApp and sector lines in the reference directory | מרכזי הסיוע לנפגעות ולנפגעי תקיפה מינית | Phone 24/7, free. Text channels are NOT 24/7 | Sexual assault support, accompaniment through medical and legal proceedings |
| Ministry of Welfare | 118; silent text channel 050-227-0118 | משרד הרווחה | 24/7 except Yom Kippur | Welfare emergencies and domestic violence |

Kupat cholim mental health hotlines (for intake and scheduling; a referral is still required for treatment):

| Kupat Cholim | Mental Health Hotline |
|-------------|---------------------|
| Clalit | *8703 |
| Maccabi | *3555 |
| Meuhedet | *3833 |
| Leumit | *507 |

When to use which: immediate emotional distress or suicidal thoughts, ERAN 1201. Trauma after a security incident, Natal *3362. Post-trauma distress as an IDF disabled person, discharged soldier or family member, Nefesh Achat *8944. After a sexual assault, 1202 for a woman responder or 1203 for a man. Prefer not to call, Sahar chat at sahar.org.il or WhatsApp 055-957-1399 within its posted hours, or ERAN chat 08:00-02:00. If someone is in immediate danger of harming themselves or others, call 101 (MDA) or 100 (police).

Psychiatric emergency rooms (cheder miyun psikh'iatri, חדר מיון פסיכיאטרי) are the one route this skill's referral rules do NOT apply to. The Ministry of Health states they are open 24 hours a day all year, need no referral, and are not charged for. A general hospital ER is different: the visit carries a fee. The Ministry of Health page states three things about it, so give all three: a Form 17 commitment from your kupah reduces it, a specific referral to that medical centre from an authorized party together with a Form 17 commitment avoids it, and admission waives it entirely. When someone must be seen tonight, this is the answer, and there is nothing to arrange first.

If there is immediate danger, call 101 or 100 first. When someone deteriorating REFUSES to be seen, the route is a district psychiatrist (psikh'iater mechozi, פסיכיאטר מחוזי), to whom anyone, including a family member, can bring the case, and who may order a compulsory examination in writing. The urgent route (s.6) needs all three of: illness substantially impairing judgment or reality-testing, IMMEDIATE physical danger to self or others, and refusal. The non-urgent route (s.7) needs the same impairment, refusal, and one listed harm (non-immediate physical danger, severely impaired ability to meet basic needs, severe mental suffering caused to another, or serious property damage). Refusal and deterioration alone are not enough. The order is valid for 10 days (s.8). Only after the examination can a hospitalization order follow. That order authorizes up to 7 days, extendable by 7 more by the district psychiatrist and beyond that only by a psychiatric committee. Any person may appeal to the committee, which hears an appeal against a hospitalization order within 5 days, and a further appeal lies to the District Court within 45 days, with a right to a lawyer under the Legal Aid Law. The conditions in full and the extension ladder are in `references/patient-rights.md`.

### Step 4: Types of Treatment Available

| Treatment | Hebrew Name | Best For |
|-----------|-------------|----------|
| CBT (Cognitive Behavioral Therapy) | טיפול קוגניטיבי-התנהגותי | Anxiety, depression, OCD, phobias |
| EMDR (Eye Movement Desensitization and Reprocessing) | EMDR | PTSD, trauma, distressing memories |
| Psychodynamic therapy | טיפול פסיכודינמי | Long-term personality issues, recurring relationship problems |
| Psychiatric medication | טיפול תרופתי | Prescribed by a psychiatrist (psych'iater, פסיכיאטר) |
| Group therapy | טיפול קבוצתי | Social anxiety, grief, addiction, support |
| Play therapy | טיפול במשחק | Children ages 3-12 with emotional difficulties |

What each modality involves, how long it typically runs, and its availability through the kupot are in `references/therapy-types-guide.md`.

Post-October 7 expansion (active 2025-2026):
- EMDR was significantly expanded across all kupot, more trauma-focused therapists were deployed, and group programs were established for affected communities
- Resilience centers (merkazei chosen, מרכזי חוסן) operated by the Ministry of Health in the south, north, Judea and Samaria, plus a national resilience center created after October 7. Together they serve roughly 1.3 million residents (per State Comptroller 2025 report)
- Sal briut 2026 added two medications for adults with major depression: Auvelity and Reagila (ריאגילה, cariprazine). Post-trauma treatments were considered for the 2026 basket and left out of it, so do not tell a user that PTSD coverage was expanded in it. Verify current coverage with your kupah pharmacist.

### Step 5: Private Therapy Options and Costs

The 2025 HebPsy rate survey put the national average at around 395 NIS per session (about 2% higher than 2024), with the Tel Aviv / Shfela area roughly 40 NIS above the periphery.

| Option | Cost per session (2025-2026) |
|--------|------------------------------|
| Private psychologist (psikholog, פסיכולוג) | HebPsy 2025 survey average 421 NIS |
| Private psychiatrist (psikh'iater, פסיכיאטר) | Not covered by the HebPsy survey. Ask the practice directly |
| Private social worker (oveid sotsiali, עובד סוציאלי) | HebPsy 2025 survey average 371 NIS |
| Online therapy platforms | Not covered by the HebPsy survey. Varies widely by platform |
| Art therapy (tipul be'omanut, טיפול באומנות) | HebPsy 2025 survey average 366 NIS |

Finding a private therapist:
Directories: BeTipulNet (betipulnet.co.il); HebPsy (hebpsy.net), which also lists kupah agreement (hesder) therapists; Get Help Israel (gethelpisrael.com) in English.
- University training clinics offer reduced rates. Ask the clinic for its current rate

### Step 6: Workplace Mental Health

Israeli labor law provides protections for employees dealing with mental health challenges.

| Right | Details |
|-------|---------|
| Sick days (yemei machala, ימי מחלה) | Mental health conditions qualify for sick leave, same as physical illness |
| Sick day accrual | 1.5 days per month of employment (18 per year), capped at 90 accumulated days under the Sick Pay Law (chok dmei machala) |
| First day payment | Unpaid; days 2-3 at 50%; day 4+ at 100% of salary |
| Confidentiality | Employer receives a sick note (ishur machala, אישור מחלה) without diagnosis details |
| Dismissal during sick leave | Section 4A of the Sick Pay Law bars dismissing an employee absent through illness, for the sick-day balance they have accrued and up to the statutory maximum. It does NOT apply if notice was given before the absence began, or if the workplace ceased operating or the employer became insolvent |
| Discrimination protection | Illegal to discriminate based on a mental health condition (Equal Rights for People with Disabilities Law, 1998) |
| Workplace accommodations | Employer may be required to provide reasonable accommodations |

Employee assistance programs (EAP, תוכנית סיוע לעובדים): the number of free confidential sessions is set by the employer's contract, so ask HR rather than assuming a figure.

### Step 7: PTSD-Specific Resources

PTSD (post-traumatic stress disorder, הפרעת דחק פוסט-טראומטית) is widespread in Israel. Caseload figures circulate in the press but are not published in a form we could verify, so cite shikum.mod.gov.il rather than a number.

| Resource | Description | Contact |
|----------|-------------|---------|
| Bituach Leumi general disability claim | Form 7801 for mental health disability recognition | btl.gov.il or local branch |
| Bituach Leumi hostility victims (nifgaei eiva, נפגעי איבה) | Recognition path for civilian terror and war victims. Recognition starts with the injury-notification and recognition claim, NOT with Form 571 | btl.gov.il |
| Resilience centers (merkazei chosen, מרכזי חוסן) | Community-based trauma support, MoH-operated | Municipalities, mostly south, north, and Judea and Samaria |

Lines for this track: Natal *3362 and Nefesh Achat *8944 (both 24/7); BeYadayim Tovot *3757 for free help filing an IDF-disability claim, Sun-Thu 08:00-17:00; the Combat Reaction Unit 03-6401400, Sun-Thu 09:00-17:00, free with no recognition needed and no time limit; MoD Rehabilitation *8150 and the Iron Swords desk *6500, Sun-Thu 08:00-18:00, both information desks and NOT crisis lines. Holocaust-survivor support is through AMCHA (amcha.org), and the Ministry of Health information line is *5400, also not a crisis line.

File promptly in either track. A general disability pension is paid retroactively for at most 12 months before the filing date, so a late claim loses the months before that.

Bituach Leumi general disability recognition (mental health track):
1. Complete Form 7801 (tviya le'kitzbat nechut klalit, תביעה לקצבת נכות כללית) online or at a local branch
2. Attach a psychiatric or psychological opinion plus relevant medical documentation
3. Attend a medical committee evaluation (vaada refuit, ועדה רפואית)
4. Eligibility requires medical disability of at least 60%, or at least 40% if there are multiple impairments and one of them reaches 25%
5. As of 01.01.2026 Bituach Leumi publishes a full monthly pension of 4,711 NIS at a full incapacity grade (100% or 75%), 3,211 NIS at 74%, 2,894 NIS at 65% and 2,718 NIS at 60%, plus 1,214 NIS per child and 1,518 NIS for a spouse at the full grade (spouse income ceiling 7,848 NIS gross per month). Eligibility is also income-tested; the current earnings threshold is published on the Bituach Leumi eligibility page and should be read there rather than quoted from memory
6. The mental health rehabilitation basket (sal shikum, סל שיקום) is a SEPARATE Ministry of Health entitlement at a lower bar. It does not require a pension or an earning-capacity finding: Israeli residents aged 18 and over with at least 40% psychiatric disability qualify, determined either by Bituach Leumi or by a psychiatrist authorized by the Ministry of Health, and application is to a regional rehabilitation committee. A person refused the disability pension entirely can still qualify. The covered services and the application route are listed in `references/patient-rights.md`.

For terror or war-related trauma, the hostility-victims track at Bituach Leumi is usually faster and more generous than the general disability track. The order of steps matters: first file the injury-notification and recognition claim (todaa al pgia ve'hakara ke'nifga peulot eiva), which Bituach Leumi forwards to the determining authority (harashut hama'ashera) at the Ministry of Defense to decide whether the event was a hostile act. Form 571 comes AFTER recognition: it requests a medical-treatment benefit (tatar) or a disability grade, and is open only to someone already recognized. Recognized victims also get a rehabilitation basket that includes psychological treatment. Assistance line: 02-6269999.

Post-October 7 programs (still active 2025-2026):
- Reservists, 2025 service: 30+ days under tzav 8 since January 1, 2025 gives a one-time reimbursement for emotional, psychological, psychotherapeutic and complementary treatment, for themselves and for spouses and children up to age 14, capped at 2,500 NIS for combat-array reservists and 1,000 NIS for others, claimable until 31.12.2027
- Reservists, deadline 31.12.2026: the 2024 benefit (30+ days under tzav 8 in the Iron Swords war: up to 1,500 NIS for emotional treatment plus 1,500 NIS for couples therapy) and the combat-array track (120+ days under tzav 8 since 07.10.2023: 80% of each session up to 240 NIS, for the reservist, spouse and children up to 18, at most 22 sessions or 5,280 NIS with children and 15 sessions or 3,600 NIS without) both expire at the end of 2026. Raise them first
- Reservists, 2026 service: a separate 2026 track under Government Decision 3812 also covers service under routine orders, not only tzav 8, but per Kol Zchut it starts only once the reservists' aid fund publishes its policy, and its terms were not confirmable on an official page. Have the user confirm the current terms with the reservists' centre before paying

## Examples

### Example 1: Starting Therapy for Anxiety
User says: "I've been having panic attacks and want to start therapy. How do I do this through my kupat cholim?"

Actions:
1. Get a referral from your family doctor first, and ask whether your kupah also needs Form 17 or a pre-authorization request
2. Call the kupah's mental health department (machleket briut hanefesh) for an intake appointment and describe the symptoms
3. Cost depends on the setting: typically no charge at a Ministry of Health public clinic or an agreement clinic, and Maccabi publishes 41 NIS per quarter at a public-hospital outpatient clinic. Check your own kupah's booklet
4. If the wait is long, ask for a referral to a private clinic UNDER AGREEMENT with your kupah, where the therapist sets the course with no session cap. Do not expect reimbursement for a therapist you find yourself

Result: weekly treatment through the kupah, with reassignment available if the fit is poor.

### Example 2: Crisis Support After a Difficult Event
User says: "My friend just told me they're having suicidal thoughts. What do I do right now?"

Actions:
1. Stay with your friend; do not leave them alone
2. Call ERAN at 1201 together, or call on their behalf
3. If there is immediate danger, call 101 (MDA) or 100 (police)
4. Encourage your friend to go to a psychiatric ER (cheder miyun psikh'iatri). It is open 24/7, needs no referral and is not charged for, so there is nothing to arrange in advance
5. After the immediate crisis, help them schedule an appointment with their kupat cholim

Result: ERAN provides immediate crisis intervention and guidance. If hospitalization is needed the ER psychiatric team evaluates and can arrange voluntary or involuntary admission; the rights that attach to an involuntary admission are in Step 3 and in `references/patient-rights.md`.

### Example 3: Navigating Workplace Mental Health Leave
User says: "I need to take time off work for depression but I'm worried about my job. What are my rights?"

Actions:
1. Get a sick note (ishur machala) from your doctor. It does not name a diagnosis
2. Submit it to HR. You accrue 1.5 sick days per month (18 per year)
3. Section 4A of the Sick Pay Law bars dismissal while you are absent through illness, for as long as your accrued balance lasts. It does not apply if notice was given before the absence, or if the workplace shut down
4. For extended leave, ask your doctor for a longer ishur machala

Result: sick leave on a note with no diagnosis, with dismissal protection under section 4A.

### Example 4: Seeking PTSD Treatment
User says: "I've been having flashbacks and nightmares since a traumatic event. Where do I get help?"

Actions:
1. For immediate support, call Natal at *3362, or Nefesh Achat *8944 if you are an IDF disabled person, a discharged soldier or a family member
2. Contact your kupah for a referral for PTSD-specific treatment, and ask what trauma-focused options the clinic offers
3. If symptoms are severe, request an urgent psychiatric evaluation
4. If the trauma is related to a recognized event (military service, terror attack, war), file with the appropriate track: for nifgaei eiva start with the injury-notification and recognition claim at Bituach Leumi (Form 571 is the post-recognition benefit request, not the way in), Form 7801 for general mental health disability, or contact MoD Rehabilitation at *8150 (Iron Swords casualties: *6500). Free help preparing an IDF-disability claim is available from BeYadayim Tovot at *3757

Result: trauma-focused treatment through the kupah, plus recognition where it applies.

## Bundled Resources

### References
- `references/crisis-hotlines-directory.md`. Full directory of Israeli crisis lines with hours, languages and the population each serves, including lines for Arabic, Russian and Amharic speakers, LGBTQ+, youth, women, elderly and veterans. It also records which numbers were REMOVED for being unconfirmable, so a stale number cannot quietly return. Consult whenever a user needs a contact right now.
- `references/therapy-types-guide.md`. What each therapy type treats, how long it runs, kupah availability and private cost. Consult when choosing between modalities.
- `references/patient-rights.md`. Emergency-route rules, rights under the Treatment of Mental Patients Law, 1991, the sal shikum basket, minors, day hospitalization, and confidentiality and reporting duties. Consult on compulsory admission, appeals, or where to go tonight.
- `references/domain-checklist.md`. The coverage contract for this domain: what a complete answer must include, and what is deliberately out of scope. Internal, for reviewers.

### Scripts
- `scripts/therapy-cost-estimator.py`. Estimates therapy costs by treatment setting (kupat cholim, private, university clinic, sliding scale), therapist type, and city. Run: `python scripts/therapy-cost-estimator.py --sessions-per-month 4 --type private --city tel-aviv`

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [Israel Mental Health Services](https://agentskills.co.il/en/mcp/israel-mental-health) | Community mental health clinics by city, HMO and therapy type, from Ministry of Health data |
| [Kolzchut (All-Rights)](https://agentskills.co.il/en/mcp/kolzchut) | Rights and entitlements, including disability and Bituach Leumi |
| [Israel Drugs](https://agentskills.co.il/en/mcp/israel-drugs) | Psychiatric medication details and health basket status |

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Ministry of Health, official helpline index | https://me.health.gov.il/mental-health/therapy-rehabilitation/crisis-support/first-aid/ | Official crisis line numbers, service listings, policy updates |
| ERAN | https://www.eran.org.il/online-emotional-help/ | ERAN hotline details, languages, operating hours |
| Natal | https://www.natal.org.il/קו-הסיוע-של-נטל/ | Natal contact number, trauma services, operating hours |
| Sahar | https://sahar.org.il/help/ | Online chat availability, WhatsApp contact, hours |
| BeTipulNet | https://betipulnet.co.il/ | Therapist directory, crisis line listings, therapy type guides |
| Get Help Israel | https://gethelpisrael.com/ | English-language hotline directory, therapist finder |
| Bituach Leumi, hostility victims | https://www.btl.gov.il/benefits/Victims_of_Hostilities/Pages/default.aspx | Order of steps for recognition, which form applies at which stage |
| Treatment of Mental Patients Law, 1991 | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%98%D7%99%D7%A4%D7%95%D7%9C_%D7%91%D7%97%D7%95%D7%9C%D7%99_%D7%A0%D7%A4%D7%A9 | Involuntary admission periods, appeal windows, committee composition |

## Gotchas

- A psychiatric ER needs no referral and is free, while the community route needs a referral and often a pre-authorization. Agents apply the clinic's rules to the emergency route and tell a user in acute distress to get a referral first, which is exactly the wrong instruction at that moment.
- ERAN is 1201, not a toll-free format. Agents generate plausible but wrong crisis numbers. Verify every hotline number against the reference directory.
- Natal's own page publishes *3362. The Ministry of Health helpline index still prints the older 1-800-363-363, so agents find both; give *3362, the number Natal itself publishes.
- The kupah session entitlement is two-stage (2 assessment sessions plus a 15-session kartisiya within a year), not a vague "12-16 per year", and at a clinic under agreement there is no cap at all. Agents state one number for both settings.
- Copay for a psychiatrist is set by SETTING, not by kupah. There is no single national number. Agents commonly invent one and apply it to all four kupot.
- Sal shikum requires 40% psychiatric disability at age 18+, and is separate from the general disability pension (which needs 60% medical disability). Agents commonly merge the two thresholds.
- MoD Rehabilitation runs three numbers and agents mix them up: *8150 general call center, *6500 Iron Swords casualties desk, and *8944 (Nefesh Achat), the only 24/7 emotional-support line of the three. *3104 is not an MoD number. If in doubt route to shikum.mod.gov.il.
- The national sexual assault lines are 1202 (answered by women) and 1203 (answered by men), and the association also publishes sector lines for Arab society, religious women and religious men. For domestic violence the route is 118. Agents frequently swap the two services.
- Form 571 is NOT the way into the hostility-victims track. It is open only to someone ALREADY recognized, for a medical-treatment benefit or a disability grade, so agents that present it as the recognition form send claimants to a form they cannot use. Recognition begins with the injury-notification and recognition claim. Form 7801 is the general-disability claim. Cite a btl.gov.il URL rather than guessing any other number.

## Troubleshooting

### Error: "My kupat cholim says there's a 2-month wait for therapy"
Cause: High demand for mental health services, especially since 2023, has created long wait times in many kupot cholim.
Solution: Ask for a referral to a private clinic UNDER AGREEMENT with your kupah (מרפאה פרטית שבהסכם): the official alternative route, free, with the course set by the therapist. A self-found private therapist is not reimbursed, and do not promise that shaban gets anyone in faster. Meanwhile, ERAN (1201) for immediate support.

### Error: "I was told therapy through kupat cholim is only for severe conditions"
Cause: Intake gatekeeping. The 2015 reform covers all mental health needs, not only severe conditions.
Solution: Insist on your right to treatment under the National Health Insurance Law. If refused, file a complaint with the kupah's own ombudsman (netziv kvilot hatzibur, נציב קבילות הציבור), and if that fails go OUTSIDE the kupah to the Ministry of Health commissioner for National Health Insurance complaints, who can direct a kupah to provide a service. The kupah's internal ombudsman is not the end of the road, and *5400 is an information line with no authority over a kupah.

### Error: "My employer asked me why I'm taking sick days"
Cause: Some employers improperly request medical details beyond what is legally required. An employer is entitled to receive a sick note confirming the employee cannot work, but not the diagnosis or reason.
Solution: Provide only the standard sick note (ishur machala) from your doctor. Politely inform HR that you are not required to disclose your diagnosis. If pressured, contact the Ministry of Labor public-inquiries service at gov.il, or the Kav LaOved organization at kavlaoved.org.il, for guidance on your rights.
