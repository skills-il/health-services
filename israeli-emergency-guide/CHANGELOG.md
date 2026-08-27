# Changelog

## 1.5.0 - 2026-08-27

### Fixed (safety-critical)
- **Removed the "at least 10 minutes" shelter rule for rocket fire.** Home Front Command publishes ONE merged rocket-and-missile guideline whose exit rule is open-ended: stay until an explicit instruction from Home Front Command. There is no separate ballistic-missile regime, and no duration attaches to either. The only current guideline containing "10 minutes" is siren-system disruption, a different scenario, and that is now stated explicitly so an agent does not carry the number across.
- **ER payment rebuilt from the Ministry of Health source.** The referral case is a FULL exemption, not a 269 NIS reduced fee: the previous text told entitled patients to pay. The night window is 01:00 to 06:00 and waives the treatment cost only, leaving the 281 NIS fee; there is no 23:00 boundary. Current tariff is 1,241 NIS (code 5044), effective 1 July 2026.
- **Blood donation booking corrected from 101 to 03-5300400.** The previous text routed donors to the ambulance dispatch line. Donor age band corrected to 18-60 for a first donation.
- **Removed MDA's "average 8 minute response time".** MDA publishes no such figure, and it was being repeated as reassurance inside a worked example about someone collapsing in the street.
- Personnel figure corrected to about 37,500 (was 39,000) and the fleet restated as 206 stations with 2,650+ emergency vehicles, from MDA's own 2024 summary. Removed the unsourced "100% of IDF blood" and "800 donations per day" claims and the EN/HE contradiction over MDA's founding year.
- Sexual-assault line 052-8361202 relabelled from SMS to WhatsApp. Rambam poison control clarified: no separate teratology number, same line, pregnancy questions Sunday to Thursday 09:00 to 14:00 only.

### Fixed (first aid)
- Paediatric and infant CPR now open with 5 rescue breaths, per ERC, which the file already declared Israeli courses follow, and give 15:2 for two rescuers.
- Lone-rescuer guidance no longer tells a parent to withhold the 101 call for 2 minutes; it contradicted a line two rows below in the same file.
- Bleeding control: elevation removed, the "if trained" gate on tourniquets removed, wound packing for junctional bleeding added.
- Burns to 20 minutes of cooling; third-degree burns are cooled with the patient kept warm rather than not cooled; chemical, electrical and inhalation burns added.
- Heatstroke reordered to cold-water immersion first, oral fluids restricted to the fully alert, antipyretics ruled out.
- Snake table corrected: the Palestine viper is Daboia palaestinae, not the אפעה, and the black desert cobra is neurotoxic. Bitten limb at heart level, not below.
- Jellyfish: hot-water immersion leads, with a scald warning; the vinegar step is qualified for the Mediterranean species. Israeli beach flags corrected to white/red/black; there is no purple flag here.

### Added
- `references/oref-scenarios.md`: Home Front Command's full published scenario set quoted verbatim, including terrorist infiltration (with the rule that a rocket alert during an infiltration event does NOT send you outside), hazardous materials, tsunami, prolonged stay, and siren-system disruption.
- `references/er-payment-exemptions.md`: the complete Ministry of Health exemption table, both tiers, plus the entitlements that sit outside it (hostile-action casualties, soldiers, after-hours physician referral) and an explicit list of conditions users wrongly assume are exempt.
- `references/triage-and-red-flags.md`: red flags that override the routing table, the medical rule-out before treating a first panic attack as a mental-health call, ambulance charges, Shabbat and chagim, mass-casualty conduct, patient rights, and the uninsured.
- `references/blood-donation.md`.
- First aid: anaphylaxis with adrenaline, stroke with BE-FAST and last-known-well, hypoglycaemia, seizures and febrile seizures, carbon monoxide, drowning, scorpion sting, and the recovery position.
- Deaf and hard-of-hearing channels now carry real contact details: police 052-2020100 / 08-6525111 / Listen@police.gov.il, welfare silent-call 050-2270118, 105 WhatsApp 052-1210105.
- Psychiatric ER as a free, walk-in, 24/7 rung in the mental-health ladder.
- A legal notice, in both files, immediately after the H1, with the matching clause opening both descriptions.

### Removed
- All stated wait times (ER triage, Terem), replaced with the instruction to return to the triage nurse on deterioration.

## 1.4.3 - 2026-08-19

### Fixed

- Translated section headings that had been left in English in SKILL_HE.md, where they rendered as-is on the Hebrew page. Hebrew is the site's default locale, and the skill validator never checked the Hebrew file, so these went unnoticed.

## 1.4.2 - 2026-08-13

- Corrected the red-alert shelter-timing row. The previous text claimed roughly 1,700 alert zones and entry windows "immediate to 3 minutes" with "Arava and Eilat up to 3 min". The live Home Front Command article on protection time states the entry time runs from immediate up to a minute and a half, most of the country being 90 seconds, and never mentions 1,700 zones or a 3-minute window. Overstating available time in a shelter instruction is a safety defect, so the row now carries the sourced range and adds the "Golan North" / "confrontation line" immediate-entry exception.
- Replaced the placeholder evidence for the 102 (Fire and Rescue) and 104 (Home Front Command) numbers with a verbatim quote from the gov.il national emergency-lines page.
