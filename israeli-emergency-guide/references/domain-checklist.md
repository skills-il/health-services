# Coverage Contract: Israeli Emergency Guide

This file is the coverage contract for the skill. It exists so that a future review can diff the skill's contents against the authoritative scenario taxonomies rather than spot-checking. It was created on 2026-08-01, when the review found that four of the seven official Home Front Command scenario categories were absent and nobody had noticed.

Rule for using this file: a row marked NOT COVERED is a known, deliberate gap, not an oversight. A row that becomes wrong is a defect. Never delete a row to make the table look complete.

## Home Front Command life-saving guideline categories

These are the seven official categories, taken from the route table of the live oref.org.il single-page application (extracted 2026-08-01 from its JavaScript bundle, since the site blocks automated fetch of the rendered pages). Each exists in Hebrew, English and Arabic.

| Category | Route | Coverage |
|----------|-------|----------|
| Rocket and missile attacks | `life-saving-guidelines/rocket-and-missile-attacks` | COVERED, Step 8, including the two shelter-exit regimes |
| Earthquake | `life-saving-guidelines/earthquake` | PARTIAL, in `references/first-aid-basics.md` only, not in SKILL.md |
| Infiltration of a hostile aerial vehicle | `life-saving-guidelines/infiltration-of-a-hostile-aerial-vehicle` | PARTIAL, one row in Step 8 |
| Terrorist infiltration | `life-saving-guidelines/terrorist-infiltration` | NOT COVERED. Highest-priority gap. This is the defining civilian scenario of 7 October and the skill invokes 7 October as its framing |
| Hazardous materials event | `life-saving-guidelines/hazardous-materials-event` | NOT COVERED. Shelter-in-place versus evacuate is the inverse of the rocket decision, so getting them backwards is fatal |
| Radiological event | `life-saving-guidelines/radiological-event` | NOT COVERED |
| Fear of a tsunami | `life-saving-guidelines/fear-of-a-tsunami` | NOT COVERED. The correct action after a felt coastal earthquake, moving inland and uphill without waiting for an alert, is counter-intuitive |

## Emergency numbers

| Number | Service | In Step 1 table | Verified at the operator's own site |
|--------|---------|-----------------|--------------------------------------|
| 101 | MDA | Yes | Pending, mdais.org blocks automated fetch |
| 100 | Police | Yes | Yes |
| 102 | Fire and Rescue | Yes | No, pending |
| 104 | Home Front Command | Yes | No, pending, oref.org.il blocks automated fetch |
| 105 | Child online protection | Yes | Pending, gov.il blocks automated fetch |
| 110 | Police information, accessible text position | Yes | Yes |
| 112 | Police, from a locked or SIM-less phone | Yes, with the "not unified" warning | Yes, by absence from the police emergency-lines page plus corroboration |
| 118 | Welfare | Yes | Pending |
| 119 | National Cyber Directorate | NOT COVERED, could not be verified this cycle |
| 1201 | ERAN | Yes | Via the Ministry of Health, not ERAN's own site |
| 1202 / 1203 | Sexual assault crisis lines | Yes | Yes |
| 04-7771900 | National Poison Information Center | Yes | Yes |
| 1-800-220-000 | National domestic violence hotline | NOT COVERED, could not be verified at a government source this cycle |
| *3362 | NATAL | Yes, in Step 7 | Pending |
| 103 | Israel Electric, downed lines | NOT COVERED |

## Non-voice access channels

Required because a voice-only emergency guide is unusable for deaf and hard-of-hearing users.

| Service | Channel | Coverage |
|---------|---------|----------|
| MDA | SMS and WhatsApp 052-7000101, fax 1-800-500101, app chat | COVERED, Step 1b |
| Police | The accessible position at the 110 centre | COVERED, Step 1b |
| ERAN | WhatsApp and SMS | COVERED, Step 1b |
| SAHAR | Chat, WhatsApp, Talkit app | COVERED, Step 1b |
| Sexual assault lines | SMS | COVERED, Step 1b |
| Home Front Command | SMS alerting and Cell Broadcast | PARTIAL, mentioned in the shelter-exit rule, not in Step 1b |

## Care-routing and cost

| Topic | Coverage |
|-------|----------|
| When to call 101 versus Terem versus ER versus clinic | COVERED, Step 2 |
| ER copay, self-referral, referral, and night tiers | COVERED, Step 4 |
| ER copay exemption categories | COVERED, Step 4 |
| HMO after-hours lines | NOT COVERED. The Ministry of Health lists 24/7 mental-health lines for all four HMOs |
| Psychiatric ER, 24/7, no referral, no charge | NOT COVERED |
| Level-1 trauma centers | COVERED, Step 3 and the hospital directory |
| Patient rights in an emergency | COVERED, Step 6 |

## First aid

| Topic | Coverage | Guideline currency |
|-------|----------|--------------------|
| Adult CPR | COVERED | Consistent with current guidance |
| Child CPR | COVERED | Consistent |
| Infant CPR | COVERED | Updated to the 2025 AHA and AAP technique, with a note that Israeli course material may differ |
| AED | COVERED | Consistent |
| Choking, adult and infant | COVERED | Matches the 2025 reinstatement of back blows, plus the pregnancy and large-body variant |
| Severe bleeding, tourniquets | COVERED | Not re-verified against a guideline source |
| Burns, heatstroke, snake bite, jellyfish | COVERED | Not re-verified against a guideline source |
| Drowning | NOT COVERED |
| Opioid overdose | NOT COVERED. The 2025 guidelines added dedicated guidance |
