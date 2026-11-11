# Changelog

## 1.5.0 - 2026-11-11

### Fixed

- Frozen eggs were said to be limited by the age-45 own-egg ceiling when thawed. The Ministry of Health lets women use frozen eggs until 54; age 45 limits new retrievals. Embryos made before 45 can be transferred later (Maccabi funds this until the 54th birthday), so a 46-year-old with stored embryos is no longer sent straight to egg donation.
- Reserve duty: a reservist whose partner is in treatment has the same 5 or 10-day release as an entitlement, not case by case; the surgical-retrieval period is for the man undergoing it; a female reservist has a separate route through her unit doctor.
- Costs: "small copays" and "all hormonal medications covered" are replaced by the 3-stage copay structure and the pharmacy copay on fertility drugs, with Maccabi's published figures as an example.
- Surrogacy: the eligibility anchor is now HCJ 781/15 and Director General Circular 7/2021 instead of an unsourced "January 2022 reform"; the intended parents' IVF stages are basket-funded.
- Sick pay restarts each treatment series for women but runs per year for men.
- references/ivf-process-detailed.md no longer says embryo storage carries an annual fee from the start (5 free years, then 5 paid) or that retrieval gives one sick day.
- The description no longer opens with "legal advice" wording.
- Coverage checker: children from a previous relationship can be counted separately (`--previous-children`); age is now applied to the third-child SHABAN row, sperm donation, PGT and surrogacy rows; a woman aged 45 to 53 sees the frozen-embryo route; elective freezing at 41+ mentions continuing a process started before 41; errors go to stderr.

### Added

- references/work-and-service-rights.md: absence and pay, dismissal-protection conditions, career soldiers (keva), the three reserve-duty tracks, and Bituach Leumi funding for bereaved families of hostile-act victims (28,562 NIS in 2026).
- Imported donor sperm (identity-release donors) and donated eggs from abroad.
- Shared parenting and PGD for carrier couples as eligible groups.
- SHABAN seniority carries over only within 90 days of a kupah switch; Meuhedet Si and Leumit Zahav credits; Leumit Zahav freezing from 1 July 2026.
- Embryos fertilized abroad for surrogacy (temporary order for contracts signed by 1.8.2027) and the intended-parent rules.

## 1.4.0 - 2026-09-13

### Added

- A legal notice at the top of both skill files, and a short clause opening the description, stating the output is general information on published rules, not medical or legal advice and not an eligibility determination.
- Reserve-duty (miluim) release during fertility treatment: minimum release periods, Form 58, and the emergency call-up exception.
- How switching kupah works for a fertility benefit: 6 fixed switch dates a year, SHABAN seniority, and qualification periods.
- A single age-40 timeline, so the own-egg ceiling, the age-42 cycle rule, the elective-freezing window and the SHABAN bands are given together.

### Fixed

- The posthumous sperm bill was described as having passed a preliminary reading. It did not pass in the 25th Knesset, so nothing is pending.
- The coverage checker treated a woman aged exactly 45 as still inside the own-egg track. Funding runs until the 45th birthday.
- The checker and the troubleshooting text no longer state a conclusion about the user's own entitlement; they describe the published rules and leave eligibility to the kupah.
- Two evidence snippets that no longer matched their Kol Zchut pages.
- The donated-egg track ends at the 54th birthday ("not yet 54"); the checker and text treated 54 as still inside it.
- Removed the Meuhedet Si 30-41 age band, which Meuhedet's public page does not state; users are told to confirm the age with Meuhedet.
- The previous-relationship rule now matches the source: a couple's children from earlier marriages do not count, and a single woman who already has children is told to confirm with her kupah.
- Checker status labels no longer overstate coverage: medical egg freezing reads "depends on indication", and elective freezing with an unknown kupah or Meuhedet reads "depends on kupah".
- references/surrogacy-law-guide.md contradicted the skill (a 5-member committee, "genetically related" instead of "relative", unsourced cost totals and timelines). It is rewritten to the sourced rules only.

## 1.3.2 - 2026-08-19

### Fixed

- Translated section headings that had been left in English in SKILL_HE.md, where they rendered as-is on the Hebrew page. Hebrew is the site's default locale, and the skill validator never checked the Hebrew file, so these went unnoticed.

