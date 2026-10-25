# Changelog

## 1.6.0 - 2026-10-25

Safety cycle: every crisis number and hours window was re-read on the operator's own page or the Ministry of Health index (page dated 21.10.2026), and the coverage gaps carried from 1.5.1 were closed.

### Fixed

- Ministry of Welfare 118 was listed with "hours unconfirmed". gov.il states 24 hours a day, 7 days a week except Yom Kippur, with a silent text channel on 050-227-0118 and a landline alternative 077-9208560.
- Sexual assault lines: the association's WhatsApp 052-836-1202 is restored (it is on the association's own contact page), but with its real hours, Sunday-Thursday and Saturday 17:00-23:00 and nothing on Friday; the anonymous chat runs to 24:00. Only the 1202/1203 phone lines are 24/7. Religious women: *2511, with the Tahel centre's 02-6730002 also listed. 1202/1203 are labelled by the responder's gender, as the association does.
- Sahar was shown as 24/7. Its own page also posts hours of Sunday-Thursday 16:00-03:00 and Friday, Saturday and holiday eves 18:00-00:00; the skill now relies on the posted hours and routes Arabic speakers to 118 first outside the ERAN Arabic window.
- Elem: Sunday-Wednesday 20:00-24:00. The WhatsApp number is no longer given, because Elem's page links two numbers without saying which is the counselling line.
- Natal: its own page publishes *3362, but the Ministry of Health index still prints 1-800-363-363; the gotcha now says so instead of calling the old number dead. Unsourced language and staffing claims for Natal, ERAN, AMCHA and *5400 were removed, and the crisis-line tip no longer promises that nothing is ever recorded or passed on.
- The compulsory-examination conditions (s.6 urgent, s.7 non-urgent) are stated in the body again, with the rule that refusal and deterioration alone are not enough.

### Added

- Minors: consent from 14 covers routine care only and mental health treatment is non-routine, with the Youth Law social-worker exception when contacting the parents could harm the minor; voluntary admission from 15 (s.4B); the municipal educational-psychology service (shefach). Previously recorded as out of scope because no source could be read.
- Day treatment and day hospitalization (adults 18+, by referral, free).
- Confidentiality and reporting duties: Patient's Rights Law ss.19-20, Treatment of Mental Patients Law s.42, Traffic Ordinance s.12B, Firearms Law s.11A, Penal Law s.368D. The skill does not assert that a "psychiatric register" exists.
- Bituach Leumi pays a general disability pension retroactively for at most 12 months before the filing date.
- Reservists: the 2024 benefit and the 120-day combat-array track, both expiring 31.12.2026; the 2026 track is described as decided but not yet operating.
- A January 2025 proposal for a 35 NIS psychotherapy copay is recorded as not approved, so it is not quoted as a current charge.
- Metivta *2837 (Ministry of Health culturally adapted line) in the directory.

### Changed

- The frontmatter description no longer carries "not legal advice" wording, per catalog policy.

## 1.5.1 - 2026-09-02

Follow-up to 1.5.0, closing what a post-release review found. Nothing here is a fact correction; all of it is propagation and honesty about limits.

### Fixed

- `references/patient-rights.md` carried two of the three general-hospital ER limbs while the body carried all three. The reference is the file the body delegates to, so the shorter version was the one an agent would quote.
- The cost estimator still accepted `--city`, still echoed "City: Tel Aviv", and the value no longer changed any figure after the per-city rates were removed in 1.5.0. A user could read a national survey average as a city-specific quote. The flag now says plainly that it does not affect the figure.
- The sliding-scale mode printed a degenerate "421 - 421 NIS" range, and its 30% discount is now labelled ILLUSTRATIVE in the output as well as in the code, because no source publishes a standard sliding-scale discount.
- The four kupah mental-health lines were sourced on the Ministry of Health index but appeared in neither reference file, so the skill's own instruction to verify every hotline number against the reference directory could not be satisfied for them. They are now in the directory with that source.

### Changed

- The children-and-adolescents bullet asserted coverage the skill does not route. It now says what is true (minors go through the same assessment-plus-kartisiya structure and often get priority placement) and says explicitly that routes outside the kupah for minors, such as school-based educational-psychology services, are NOT covered here, pointing the parent at the school or municipality. Naming those services properly needs a source that could not be read this cycle, and `references/domain-checklist.md` now records that as an explicit out-of-scope with the reason and a re-open date rather than as silence.
- Two evidence entries gained a `source_note` recording HOW they were attributed, not merely that they were: the 10-day examination-order quote is word-for-word identical in section 8 and section 9(c), so the quote alone cannot establish which section it came from, and the resilience-centre figure sits behind bidi control characters in the PDF text layer, which makes a naive substring check report it missing when it is present.

## 1.5.0 - 2026-09-02

### Fixed
- A reviewer found that the shaban promise, the invented 3-6 EAP session figure, an unverified expedited-PTSD-recognition claim and a medication row keyed to four named diagnoses had been repaired in English and left standing in Hebrew, which is the site's default locale. All four are now fixed in both languages, along with two repairs that an aborted edit had silently dropped from the Hebrew file.
- The Elem youth line was published as Sunday to Thursday; the operator publishes a narrower window. Since the hours appear only on the site's front page, which the evidence gate cannot cite, the row now warns that it is evening-only and not every weeknight rather than asserting a window that cannot be sourced.
- 118 was asserted as 24/7 in three places while the reference file's own note declined to confirm any window. No hours are claimed for it now.
- The therapy-types guide recommended combining therapy with medication for "moderate-to-severe" depression twenty-four lines after declaring severity-keyed treatment selection out of scope, and told users to arrive asking for a named modality. Both are gone.

- Form 571 was presented as the way into the hostility-victims track. It is not. Bituach Leumi's own form page states it is for someone who has ALREADY been recognized, to request a medical-treatment benefit (tatar) or a disability grade, so an agent following the old text sent claimants to a form they cannot use. Recognition starts with the injury-notification and recognition claim, which Bituach Leumi forwards to the determining authority at the Ministry of Defense.
- The 2026 drug-basket entry named a medication that does not exist ("Riagility"). The drug is Reagila (ריאגילה, cariprazine). The line-of-therapy positioning that was attached to Auvelity is a prescribing question and has been removed rather than restated, and the entry now says plainly that post-trauma treatments were considered for the 2026 basket and left out of it, so nobody tells a PTSD patient their coverage was expanded.
- The reservist therapy benefit was cited to a Bituach Leumi reserve-pay page that contains none of that text. Re-sourced, and the terms it omitted are now stated: the reimbursement is one-time and capped at 2,500 NIS for combat-array reservists and 1,000 for others, 2025 service is claimable until 31.12.2027, and by government decision the 2026 assistance also covers routine orders and not only tzav 8.
- Removed a claimed late-2025 Bituach Leumi policy clarification about PTSD not being time-limited. A browser read of the cited page found none of it.
- Removed the caseload figures (82,400 wounded and the rest) and the 366/175 million basket additions. Their only source is a publication that is Cloudflare-walled to any automated read, so nothing could confirm them. The skill now routes to shikum.mod.gov.il instead of quoting a number it cannot stand behind.
- Removed the OneFamily number from both skill files. The bundled hotline directory had already deleted it as unconfirmable, and the deletion had never propagated to the body, which is exactly the failure the directory's own verification note warns about.
- The general-hospital ER fee now states both limbs the Ministry of Health page gives: Form 17 reduces it, a specific referral to that medical centre plus Form 17 avoids it, and admission waives it.
- The bundled cost estimator was printing invented per-city rates, including psychiatrist rates that the skill body expressly refuses to quote because no survey samples them. It now uses the published HebPsy 2025 averages, refuses to produce a figure for psychiatrists and for university clinics rather than inventing one, and prints a not-a-quote footer.

### Added
- The way IN to compulsory care, which the previous cycle's involuntary-admission block silently assumed had already happened. A family whose relative refuses to be seen now gets the actual route: the district psychiatrist is the addressee, anyone including a family member may bring the case, section 6 covers the urgent limb with its three cumulative conditions, section 7 the non-urgent, an examination order runs 10 days, and only then can a hospitalization order follow. Immediate danger still means 101 or 100 first.
- Section 4A of the Sick Pay Law, with its two statutory exceptions. The skill previously told employees flatly that they cannot be dismissed during sick leave, which is over-broad: the protection runs on the accrued balance and does not apply where notice preceded the absence or the workplace shut down.
- An external escalation route. A refused patient was being sent to the kupah's own ombudsman and then to an information line with no authority over a kupah; the Ministry of Health commissioner for National Health Insurance complaints, who can direct a kupah to provide a service, is now named.
- The sexual-assault sector lines (Arab women, religious women, religious men) that the association publishes and the skill omitted, while an unsourced secondary number was removed.

- Psychiatric emergency rooms, which are the one route the skill's referral rules do not apply to: open 24 hours a day all year, no referral, no charge. The skill previously carried the referral requirement everywhere and never carved out the emergency route, so an agent could tell someone in acute distress to go and obtain a referral first.
- Rights on involuntary admission under the Treatment of Mental Patients Law, 1991: the 7-day hospitalization period and who may extend it, the 5-day psychiatric-committee appeal, the 45-day District Court appeal, and the right to a lawyer under the Legal Aid Law. The crisis example already reached involuntary admission and attached no rights to it.
- `references/patient-rights.md` with the emergency-route table, the full extension ladder with section numbers, and the sal shikum basket.
- `references/domain-checklist.md`, the coverage contract this domain was missing, so future reviews have something to audit against.
- A legal notice in both languages after the H1, and a short legal clause opening both descriptions, as the regulated-profession gate requires.

## 1.4.2 - 2026-08-19

### Fixed

- Translated section headings that had been left in English in SKILL_HE.md, where they rendered as-is on the Hebrew page. Hebrew is the site's default locale, and the skill validator never checked the Hebrew file, so these went unnoticed.

