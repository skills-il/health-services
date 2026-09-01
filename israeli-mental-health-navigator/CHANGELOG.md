# Changelog

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

