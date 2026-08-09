---
name: israeli-nutrition-planner
description: >-
  Plan meals and make dietary decisions based on Israeli Ministry of Health guidelines,
  the Nutritional Rainbow diet, and front-of-package red/green labeling. Use when user asks
  about "healthy eating Israel", "meal plan", "tochnit tazona", "keshet tazonit", "red label
  food", "tiyug adom", "kosher meal plan", "halal meal plan", "Pesach menu", "weekly menu",
  "what to eat", or "tazona briut". Covers the rainbow food groups, red-label thresholds
  (sugar, sodium, saturated fat), the annually updated green label, kosher and halal
  planning, Pesach kitniyot, fasting days (Yom Kippur, Ramadan, minor fasts), Israeli
  nutrient gaps with supplement upper limits and drug interactions, pregnancy food safety,
  allergen and gluten label reading, HMO dietitian entitlements, and GLP-1 context. This
  skill refuses to set calorie or deficit targets and routes any sign of disordered eating
  to care. Do NOT use for clinical nutrition therapy, eating disorder treatment, sports
  nutrition, or medical dietary prescriptions.
license: MIT
---

# Israeli Nutrition Planner

## Problem

Planning balanced meals in Israel means navigating the Ministry of Health's Nutritional Rainbow, reading the front-of-package red and green labels on every product, and working within kosher, halal, and holiday constraints that shape both what goes in a meal and when it can be eaten. Most people either ignore the labels or cannot translate the rainbow's frequency-based recommendations into an actual weekly menu, and default to convenience foods carrying red labels for sugar, sodium, or saturated fat.

## Instructions

### Step 1: Assess Needs and Clear the Medical Gates

Ask the user about their dietary context before planning:

| Question | Why it matters |
|----------|---------------|
| How many people are you planning for? | Portion scaling |
| Any food allergies or intolerances? | Exclusion list |
| Do you keep kosher or halal? At what level? | Meat-dairy separation, permitted foods |
| Budget preference (economy, moderate, flexible)? | Ingredient selection |
| Any health conditions? Ask by name: diabetes, kidney disease, high blood pressure, celiac, pregnancy or breastfeeding, a past or present eating disorder | Blocking gate, see below |
| Any regular medication? | Food and drug interactions, see Step 8.5 |
| Cooking skill level? | Recipe complexity |

**This is a blocking gate, not a disclaimer.** If any of the following is present, you constrain or withhold the plan. Do not generate a full menu and then attach a warning at the end.

| Condition | What you do |
|-----------|-------------|
| **Diabetes** (any type, including gestational) | Do not set carbohydrate targets or exchange counts. Give the rainbow framework only, and route to the kupat cholim dietitian under the National Diabetes Program (Step 8). |
| **Kidney disease** | **Withhold the meal plan.** Renal diets restrict protein, potassium, phosphorus and sodium in combinations only a renal dietitian can set, and this skill's defaults (legumes at every meal, dark leafy greens, tahini, salt substitutes) are actively harmful here. Route to the nephrologist and renal dietitian. |
| **Pregnancy or breastfeeding** | You may plan, but you must apply Step 8.7 (pregnancy food safety) to every menu item, and never set a weight target. |
| **Celiac** | Plan with the Step 8.6 gluten exclusions, and route to the kupat cholim dietitian, covered for celiac with a doctor referral. |
| **Eating disorder, past or present** | **Stop. Do not plan.** Go to Step 1.5. |
| **Chronic medication** | Apply Step 8.5 before recommending any supplement or any food in quantity. |

For any diagnosed condition needing a therapeutic diet, route to a registered clinical dietitian (diyetanit klinit). This skill gives general healthy-eating guidance per MoH guidelines, not clinical nutrition therapy.

### Step 1.5: Eating-Disorder and Calorie-Target Gate

This skill does not set numeric intake targets, and it does not help anyone eat less.

**Hard refusal rule.** If the user asks for a calorie target, a calorie deficit, a goal weight, a rate of weight loss, or a macro split for weight loss, refuse the number. Say plainly that this skill does not set calorie or deficit targets, that a personalised target is a clinical decision, and route the user to a clinical dietitian (diyetanit klinit) through their kupat cholim. Do not offer an estimate, a range, a formula, or a "rough idea" instead. An estimate presented with a caveat is still a number, and it is the number that does the harm.

**Screening trigger.** Stop planning and route, on any of these signals, whether stated directly or implied:

- restriction: "how little can I eat", deliberate meal skipping, fasting to lose weight, cutting a food group for weight reasons
- purging or compensation: vomiting, laxatives, diuretics, exercising to cancel out food
- body-image distress: calling foods "bad" or "safe", disgust at their own body, fear of specific foods or of gaining weight
- rapid-loss goals: a target date, a target number on the scale, a large loss in a short window
- loss of control: bingeing, eating in secret, guilt after eating
- a stated history of anorexia, bulimia, or binge eating

**What to do instead.** Say clearly that this is outside what the skill will do, and that it is raised because these patterns are common and treatable, not as an accusation. Route to:

- their kupat cholim family doctor, who can refer to an eating-disorder service
- the specialised eating-disorder clinics at Sheba, Ichilov and Soroka, which require a referral
- ER"N (Emotional First Aid), a free anonymous national support line on 1201, also by online chat, in several languages. ER"N is general emotional first aid, not an eating-disorder clinic and not a substitute for treatment.

If the user is in immediate danger, direct them to emergency services (101) or a hospital emergency room, not to a meal plan. Do not continue to Steps 2 through 9 until the topic has changed to something this skill can safely do, such as explaining what a red label means.

### Step 2: Apply the Nutritional Rainbow

The Israeli Ministry of Health replaced the food pyramid with the **Nutritional Rainbow** (Keshet Tazonit). It organizes foods by recommended consumption frequency, not traditional food groups.

| Rainbow Band | Frequency | Foods | Key Guidance |
|-------------|-----------|-------|--------------|
| **Green** | Multiple times daily, at every meal | Vegetables, fruits, whole grains | Eat a variety of colors. Prefer whole fruits over juice. Choose whole grains (lechem maleh, orez maleh) over refined. |
| **Yellow** | At least once daily (choose from each sub-group) | (1) Legumes: lentils, chickpeas, beans, broad beans, peas. (2) Healthy fats: olive oil, tahini, nuts, avocado. (3) Unsweetened dairy or alternatives. | Legumes are the protein backbone of the rainbow. Use olive oil as the primary cooking fat. |
| **Orange** | Several times per week | Fish, poultry, eggs | Vary throughout the week. Purchase raw and cook at home. Prefer baking, grilling, or steaming over frying. |
| **Pink** | Infrequent, limited | Red meat (beef, lamb) | Maximum 300g per week of home-cooked red meat. Excludes processed meat (naknikiot, hamburgers, pastrami). |
| **Below the rainbow** | Minimize or avoid | Ultra-processed foods: candy, sweetened drinks, processed meats, packaged snacks with industrial additives | These are not part of the rainbow. Read labels for red markings. |

**Core principles:** most of the plate is vegetables, fruits, whole grains and legumes; home cooking over packaged or restaurant meals; herbs and spices (za'atar, cumin, turmeric) instead of salt and sugar; water as the main drink; and eating together with family where possible.

### Step 3: Read Front-of-Package Labels

Since January 2021 (Phase 2), Israeli food products carry mandatory red warning labels if they exceed these thresholds:

| Nutrient | Per 100g (solid food) | Per 100ml (liquid food) |
|----------|----------------------|------------------------|
| **Sodium** | greater than 400 mg | greater than 300 mg |
| **Total Sugars** | greater than 10 g | greater than 5 g |
| **Saturated Fat** | greater than 4 g | greater than 3 g |

**Red label (tiyug adom):** A red circle with the nutrient name appears on the front of the package. A product can have 1, 2, or 3 red labels. Products with any red label should be consumed sparingly.

**Green label (tiyug yarok):** Voluntary positive marking. Two rules matter. First, a food carrying any red label can never carry a green label. Second, eligibility is limited to an enumerated list of food groups: milk, yogurts, cheeses, tofu, soy beverages, certain vegetable oils, seeds and nuts, grains, legumes, tahini, tahini salad, fish, eggs, poultry, fruits and vegetables. Within those groups the food must be unprocessed or minimally processed, with no additives beyond salt and spices under a per-group sodium cap.

**The green label is not frozen.** An independent scientific committee at the Ministry of Health updates the green-label criteria annually. In February 2026 it added a new eligible category, "Prepared Dishes and Salads", covering ready-to-eat legume salads, vegetable- and whole-grain-based dishes, hearty soups, and combined meals whose every ingredient meets the criteria. **Before telling a user that a food is or is not green-label eligible, check the current criteria on the Ministry page.** The red thresholds are stable, the green criteria are not.

**Exemptions.** Fresh unpackaged produce, single-ingredient raw meat, fish and eggs, restaurant and food-service meals, multipacks, packages with a front area under 25 cm2, and specific products such as tea, coffee, yeast and food extracts carry no red label even above threshold. They must still show the standard nutrition panel on the back. The full list is in `references/red-green-labels.md`.

**Shopping rule:** prefer zero red labels, and between similar products pick the one with fewer. A green label is a strong daily choice. A red label is not "forbidden", it means the product should not be a daily staple. Phase 2 thresholds (January 2021) are the current red-label standard, and there is no Phase 3 in the regulation.

### Step 4: Build a Weekly Meal Plan

Structure the week by rainbow frequency, not by calories. A worked daily template (three meals plus one or two snacks, each mapped to its rainbow bands) and a seven-day protein rotation are in `references/nutritional-rainbow.md`. Load it when building the plan.

The shape to hold on to: vegetables and whole grains at every meal, something from each yellow sub-group daily, fish twice a week, poultry and eggs across the week, and red meat capped at 300g of home-cooked unprocessed meat per week and usually landing on Friday night. In pregnancy, filter every fish choice through Step 8.7 first.

### Step 5: Handle Kosher Constraints

For users who keep kosher, every meal is planned as meat (basari), dairy (halavi), or neutral (pareve), and dairy meals must be spaced from meat meals. The waiting-time rules, the pareve list, and the utensil implications are in `references/kosher-halal-planning.md`.

**Planning strategies:**
- Morning meals are naturally dairy-friendly (yogurt, cheese, milk) since no meat was eaten overnight
- If lunch is meat-based, dinner can be dairy only if there are 6 hours between them
- Friday night dinner is typically meat; Saturday lunch can be meat (cholent) or dairy, depending on family tradition
- Pareve meals (legume-based, fish, egg-based) give maximum flexibility and avoid timing constraints entirely

### Step 5.5: Halal and Arab-Israeli Households

This is the segment with the largest nutrition-related health gap in the country. The Ministry of Health's own regulatory impact report records overweight and obesity rates in Arab society reaching **38%** among children and **70%** among women of low socioeconomic status, and the Ministry's Arab-community campaign records diabetes prevalence 2.5 times higher and heart disease 2.3 times higher than in Jewish society. Plan for these households properly rather than treating kosher as the default.

The constraints, in short: ask which halal certification the household accepts rather than assuming a kosher hechsher covers it; exclude pork in every form plus cooking wine, alcohol-containing sauces and vanilla extract; check gelatin in yogurts and desserts and rennet in cheese for animal source; and note that there is no meat-dairy separation, so combined dishes are open and the menu is wider than a kosher one. Details are in `references/kosher-halal-planning.md`.

**Build on what the kitchen already does well.** Arab-Israeli home cooking is already close to the rainbow: mujaddara, freekeh and burghul, molokhia and other cooked greens, ful and hummus, labneh, olive oil, zaatar, fresh salads, baked and grilled fish and poultry. Anchor the plan in those dishes rather than substituting an unfamiliar menu. The realistic levers are sweetened drinks, portions of white rice and refined bread, frying, and the sodium load of commercial spice mixes and pickles. Offer the plan in Arabic where preferred, and route to the kupat cholim dietitian, which has Arabic-speaking staff in most regions.

### Step 6: Adapt for Israeli Supermarket Products

Use products available at the major Israeli chains (Shufersal, Rami Levy, Yeinot Bitan, Victory, Osher Ad). The full staples table, filtered to items that typically carry zero red labels, is in `references/staples-and-nutrient-gaps.md`. Load it when producing a shopping list.

Two habits matter more than the list: check front-of-package labels on anything canned, packaged, or sauced, and prefer the fresh produce and bulk legume aisles, which are exempt from labeling because they are unprocessed rather than because they slipped a threshold.

### Step 7: Handle Religious Fasts and Special Days

Israeli nutrition planning runs into religious fasts. On these days hydration and electrolytes matter more than caloric balance.

| Fast | Duration | Pre-fast meal (seuda mafseket / suhur) | Break-fast | Notes |
|------|----------|---------------------------------------|-----------|-------|
| Yom Kippur | ~25 hours, no food or water | Complex carbs (whole grains, legumes), low salt, plenty of water hours before. Taper caffeine 1-2 days prior to avoid withdrawal headaches. | Slow rehydration, light dairy or fruit before a heavier meal. | Pregnant, nursing, ill, children under 9: consult rabbi and doctor. **Diabetics on insulin or sulfonylureas (e.g., glibenclamide, glimepiride) are at high risk of hypoglycemia and should generally not fast without an endocrinologist's plan.** |
| Ramadan (suhur to iftar) | ~14-16 hours daily, no food or water during daylight | Suhur: oatmeal, eggs, dates, vegetables, plenty of water. | Iftar: dates and water first, then a balanced meal with protein, vegetables, complex carbs. | Avoid heavily salted or fried foods at iftar. **Diabetics on insulin or sulfonylureas should consult kupat cholim before fasting**: international guidance (IDF/DAR) classifies them as high risk and recommends pre-Ramadan medication adjustment and weekly monitoring. |
| Tisha B'Av, 17 Tammuz, Tzom Gedalia, Asara b'Tevet, Ta'anit Esther | Sunrise to sunset (or full day for Tisha B'Av) | Light meal beforehand, hydrate well | Light food first | Pregnant and nursing women are exempt from minor fasts; check with a rabbi. |

For diabetic, hypertensive, pregnant, or chronically ill users planning to fast, the standard advice is to consult their kupat cholim primary doctor or endocrinologist (covered by sal briut), not to provide a meal plan for the fast.

**Pesach: the week that breaks the rainbow.** For eight days (seven in some practice), chametz removal strips the whole-grain column out of the green band, and for Ashkenazi households kitniyot removal also strips the legume sub-group out of the yellow band, which is the protein backbone of the rainbow. Losing both at once is the biggest structural gap in the Israeli food year.

**Always ask which custom the household follows. Never assume.** Sephardi and Mizrahi communities generally eat kitniyot, so rice, chickpeas, lentils, beans, and peas stay available and the plan barely changes. Ashkenazi communities generally do not.

For an Ashkenazi household, plan the eight days around eggs, fish, poultry, and dairy carrying more of the protein load, spread across the day rather than concentrated in one meal; quinoa where the household's rabbinic authority permits it, so ask; nuts, almonds, seeds, and nut flours in place of legume flours; potato, sweet potato, and matzah meal for starch, with vegetables raised to replace the lost fibre; and a deliberate fibre and fluid plan, because constipation over Pesach is the predictable consequence of losing whole grains and legumes together.

### Step 8: Connect Users to Kupat Cholim Resources

When users have specific health goals, route them to the appropriate kupat cholim service rather than providing clinical advice:

| Need | Where to refer |
|------|---------------|
| Weight management, BMI counseling | Kupat cholim dietitian (diyetanit) - included in sal briut for adults with BMI greater than or equal to 30 or a chronic condition. Premium tiers (Clalit Platinum, Maccabi Sheli, Meuhedet Adif, Leumit Gold) add broader dietitian access. |
| Diabetes prevention or management | National Diabetes Program (Tochnit Sukeret Leumit) - all four HMOs cover **14 dietitian visits per year** for people with diabetes, with a referral from the family doctor. Directly confirmed for Clalit, Maccabi, Leumit, and Meuhedet. No referral needed at Maccabi for diabetes, prediabetes, or gestational diabetes. |
| Pediatric nutrition | Tipat Halav for children under 6, school nurse for school-age |
| Eating disorders | Specialized clinics at Sheba, Ichilov, Soroka (referral required). See Step 1.5 before routing. |
| Pregnancy nutrition | OB-GYN and kupat cholim dietitian (covered without separate referral), folic acid recommended pre-conception and through the first trimester |
| Weight-loss medication (GLP-1) | Wegovy (semaglutide) is the drug approved in Israel for chronic weight management, and adults buy it privately at high ongoing monthly cost. Since the Health Ministry's letter of April 2024, Ozempic is no longer prescribed off-label for weight loss. **Age-based basket coverage and prices move with every sal briut cycle, so do not quote an age band, a price, or an eligibility count. Send the user to their family doctor, endocrinologist, or the current sal briut listing.** |

### Step 8.5: Nutrient Gaps and Supplement Safety

Israel has documented population-level gaps in iodine, vitamin D, iron, B12 among vegans, and folate around pregnancy. The detail is in `references/staples-and-nutrient-gaps.md`.

**What belongs in the plan is the safety rule, not the dose.** Supplements are drugs with ceilings and interactions, and this skill names neither a starting dose nor a stacking plan.

| Nutrient | Ceiling and cautions |
|----------|----------------------|
| **Vitamin D** | Adult upper intake level is 100 micrograms per day, which is 4,000 IU. High-dose loading regimens are a medical decision. |
| **Iodine** | Adult upper level is 1,100 micrograms per day. **Iodine is not for everyone.** Excess iodine harms the thyroid as surely as deficiency does, so anyone with thyroid disease, on thyroid medication, or with a nodular goitre must not start iodine or switch to iodized salt without their doctor. |
| **Folate** | Upper level from supplements is 1,000 micrograms per day; the routine pre-conception dose is 400 micrograms. **The 5 milligram dose is prescription strength, for specific higher-risk pregnancies only. Never self-selected, and never presented as over the counter.** |
| **Iron** | Adult upper level is 45 milligrams per day. Iron is supplemented for a blood-test-confirmed deficiency, not on suspicion. |
| **B12** | No upper level is set, but a vegan who feels unwell needs a blood test, not a bigger pill. Long-term metformin lowers B12 absorption, so a metformin user going plant-based needs their doctor to check levels. |

**Food and drug interactions this skill actively creates.** Check these before finalising any plan for a user on chronic medication:

- **Levothyroxine (Eltroxin, Euthyrox) with calcium or iron.** Levothyroxine is taken on an empty stomach 30 to 60 minutes before breakfast or 3 to 4 hours after dinner, and must not be taken within 4 hours of anything containing iron or calcium. This skill recommends tahini for both, so a tahini breakfast and a morning levothyroxine tablet collide directly. Move the tahini to lunch, or move the tablet.
- **Warfarin (Coumadin) with vitamin K.** The green band puts dark leafy greens at every meal, and warfarin dosing is calibrated to habitual vitamin K intake, so a sudden jump in spinach or kale changes the INR. Do not tell a warfarin user to increase greens. Tell them to keep intake consistent and to speak to their anticoagulation clinic first.
- **General gate.** If the user takes any chronic medication, say explicitly that supplements and large dietary shifts must be cleared with their doctor or pharmacist first.

### Step 8.6: Allergen and Gluten Label Reading

Step 1 collected the allergy list. Teach the user to read the package rather than only handing them an exclusion list.

**Reading the ingredient list.** Every packaged food sold in Israel must list all ingredients in descending order by weight, so the first item is the largest component. Additives such as tartrazine and sulphites are named explicitly as well as by functional group.

**Hebrew label vocabulary.** רכיבים is the ingredient list, מכיל is "contains", and עלול להכיל is the precautionary "may contain". The full Hebrew-to-English allergen glossary, covering milk, egg, gluten-grain, peanut, tree-nut, sesame, soy, fish and the minor allergen names, is in `references/red-green-labels.md`. Give the user the Hebrew words for their own allergens so they can scan a package themselves.

**The precautionary line is not a guarantee.** "עלול להכיל" flags possible cross-contact, but its absence does not prove a product is allergen-free: lines change and importers relabel. For a severe or anaphylactic allergy, have the user confirm with the manufacturer's consumer line and work with their allergist. A generated menu is never the last check.

**Gluten and celiac.** A "ללא גלוטן" claim follows the international Codex threshold of under 20 mg/kg gluten. Naturally gluten-free Israeli staples include rice, legumes, fresh produce, tahini, olive oil, plain dairy, eggs, and fresh meat, fish and poultry. The usual traps are soy sauce (most contain wheat), seitan, bourekas, malt-flavoured cereals, beer, and commercial soups and sauces. Kupat cholim dietitians are covered for celiac with a doctor referral.

### Step 8.7: Pregnancy Food Safety

If the user is pregnant, this step overrides menu preferences. Two of this skill's own defaults, brined and soft cheeses and twice-weekly fish, need editing. Per Ministry of Health guidance:

**Avoid for infection risk (listeria, toxoplasma, salmonella):** unpasteurised dairy or dairy of unknown origin; mould-ripened cheeses (brie, camembert, gorgonzola, roquefort); brined cheeses stored in water (feta, tzfatit, bulgarit), which are fine once thoroughly cooked, for example baked into a pashtida; raw or undercooked meat, poultry, fish and eggs, including sushi with raw fish, carpaccio, seafood, runny eggs, home-made mayonnaise, aioli, hollandaise, tiramisu, home-made ice cream and egg-white foams; uncooked smoked fish (lox, smoked salmon, herring, lakerda, ceviche) and creamy fish spreads such as ikra; pate and cold cured meats such as pastrami unless cooked through; soft-serve ice cream; unwashed produce, and hummus spread kept beyond about two days.

**Avoid for mercury:** large predatory fish, specifically large mackerel, swordfish, bluefin tuna, albacore tuna, and shark. Light canned tuna and the ordinary range of Israeli sea and pond fish stay in.

**On this skill's own staples:** labaneh and gvina levana are fine in pregnancy when made from pasteurised milk from a licensed producer, which covers the standard supermarket product. It is the brined and mould-ripened cheeses that come out. Wash produce under running water even when peeling, scrub hard-skinned produce, cook eggs and poultry through, and route anything uncertain to the kupat cholim pregnancy-monitoring team.

### Step 9: Generate Output

Provide the user with:

1. **Weekly meal plan table** with all 7 days, 3 meals + snacks per day
2. **Shopping list** organized by supermarket sections (produce, grains, dairy, proteins, pantry)
3. **Red label check** for any packaged products in the shopping list
4. **Kosher or halal designation** for each meal if relevant
5. **A note of which gates in Step 1, 1.5, 8.5 and 8.7 were applied**, so the user can see what was constrained and why

**Do not output a calorie count, a macro target, or a nutrition breakdown framed as a target.** If the user wants to know what is in a food, use the Israeli national nutrition database (Tzameret), which holds over 4,500 Israeli food items with 74 nutrient components, roughly 1,400 Israeli recipes and portion weights, rather than a foreign table that mis-describes Israeli staples. Present values as descriptive facts about a food, never as a target to hit or stay under and never as a daily total.

Format the meal plan as a clear table the user can print or save.

## Examples

### Example 1: Basic Weekly Meal Plan

User says: "Plan a healthy weekly menu for my family of 4"

Actions:
1. Ask the Step 1 questions, including the named health conditions and any medication
2. Build a 7-day plan on the rainbow frequencies with a protein rotation
3. Generate a shopping list with quantities for 4 people
4. Flag packaged products that typically carry red labels

Result: A weekly menu plus an organized shopping list.

### Example 2: A Calorie Target Request

User says: "I want to lose weight fast before a wedding, how few calories can I eat?"

Actions:
1. Do not answer with a number, a range, or a formula
2. Name the refusal plainly: this skill does not set calorie or deficit targets
3. Read the request against the Step 1.5 screening list. "How few calories" plus a rapid-loss deadline hits two triggers, so route rather than plan
4. Offer the routes: family doctor for a dietitian referral under the health basket, ER"N on 1201 for anonymous emotional support, and the specialised clinics if relevant
5. Offer only what is safe: what the rainbow bands are, how to read a red label

Result: No number given, a clear explanation of why, and a concrete route to real help.

### Example 3: Kosher Shabbat Menu

User says: "Plan Friday night dinner and Saturday meals, we keep kosher glatt"

Actions:
1. Friday dinner: meat-based (chicken soup, main, sides)
2. Saturday lunch: meat (cholent) or dairy, if 6+ hours from the Friday meat meal
3. Seuda shlishit: lighter, dairy or pareve
4. Mark every meal basari/halavi/pareve and note the waiting times

Result: A Shabbat plan with kosher designations.

## Bundled Resources

### References

- `references/nutritional-rainbow.md` -- Complete Nutritional Rainbow food groups, frequencies, and portion guidance. Consult when building meal plans or answering questions about Israeli dietary guidelines.
- `references/red-green-labels.md` -- Red-label thresholds (Phase 1 and Phase 2) plus the green-label rules and the annual-update history. Consult when evaluating food products or answering a green-label question.
- `references/staples-and-nutrient-gaps.md` -- Israeli supermarket staples by category, and the population nutrient gaps behind the supplement questions. Consult when producing a shopping list or explaining a deficiency.
- `references/kosher-halal-planning.md` -- Kosher meat-dairy rules and waiting times, and halal constraints. Consult when the household keeps either.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Efsharibari (MoH portal) | https://efsharibari.health.gov.il/en/ | Rainbow guidance, recipes, campaigns |
| MoH labeling regulations | https://efsharibari.health.gov.il/en/governance/legislation/unhealthy-food-labeling-law/ | Red-label thresholds and regulation text |
| MoH green-label criteria | https://efsharibari.health.gov.il/eat-healthy/buy-healthy-food/food-labeling/green-labeling/ | Current eligible groups. Check before any green-label claim |
| MoH green-label update, Feb 2026 | https://www.gov.il/en/pages/23022026-01 | Annual review, Prepared Dishes and Salads |
| Tzameret national nutrition database | https://data.gov.il/api/3/action/package_show?id=nutrition-database | Nutrient values for Israeli foods |
| MoH food safety in pregnancy | https://me.health.gov.il/parenting/family-planning/healthy-pregnancy/healthy-lifestyle/food-safety/ | Listeria, mercury, cheese exclusions |
| MoH National Diabetes Program | https://www.gov.il/he/pages/diabetesnationalproject | Program scope and patient resources |
| ER"N, Emotional First Aid | https://www.eran.org.il/ | Free anonymous support line 1201 and chat |
| Maccabi dietitian eligibility | https://www.maccabi4u.co.il/eligibilites/3856/ | Referral rules for dietitian visits |

## Gotchas

1. **Red label thresholds changed in January 2021.** Phase 1 (2020) thresholds were higher: 500mg sodium, 13.5g sugar, 5g saturated fat per 100g solid. Always use Phase 2: 400mg sodium, 10g sugar, 4g saturated fat per 100g. Phase 1 numbers give users false confidence about unhealthy products.

2. **The red thresholds are frozen but the green criteria are not.** There is no Phase 3 for red labels, but it is wrong to call the whole system static: green-label criteria are set by an independent MoH scientific committee that updates them annually, and February 2026 added the Prepared Dishes and Salads category. Never assert green-label eligibility from memory.

3. **The Nutritional Rainbow is not the food pyramid.** Israel officially replaced the pyramid with the Nutritional Rainbow (Keshet Tazonit). Do not generate content based on the pyramid model. The rainbow organizes by consumption frequency, not by traditional food groups.

4. **Kosher waiting times vary by community.** The 6-hour wait after meat is the most common Israeli practice (Shulchan Aruch), but Yemenite Jews traditionally wait 3 hours. Never state one waiting time as universal. Ask which custom the user follows, or default to 6 hours with a note about variation.

5. **Red meat limit is 300g per week of home-cooked meat, excluding processed meat.** Processed meats (naknikiot, pastrami, frozen patties) are "below the rainbow" and should be minimised entirely, not counted toward the 300g.

7. **Israeli table salt is not iodized by default,** and desalinated drinking water removes another baseline source. But do not turn that into a blanket "buy iodized salt" instruction: excess iodine harms the thyroid too, and thyroid patients need their doctor's word first. See Step 8.5.

8. **Never assume kitniyot on Pesach, and never assume kosher over halal.** Sephardi and Mizrahi households eat kitniyot, Ashkenazi households generally do not, and the difference decides whether the yellow band survives the holiday. Likewise, do not offer a kosher plan to a household that keeps halal. Ask in Step 1.

9. **Wegovy and Ozempic are not interchangeable, and basket details move every cycle.** Wegovy (semaglutide) is the drug approved for chronic weight management in Israel, and adults buy it privately. Since the Health Ministry's April 2024 letter, Ozempic is no longer prescribed off-label for weight loss. Do not quote age bands, prices, or eligibility counts from memory, they change with every basket cycle. GLP-1 users have reduced appetite and early satiety, so plans should emphasise protein and nutrient density per bite rather than volume.

## Troubleshooting

### FAQ: The user asks for a calorie target or a weight-loss number
Answer: Refuse the number, and do not substitute an estimated range. Explain the rainbow's frequency-based approach, route to a clinical dietitian (diyetanit klinit) via the kupat cholim, and check the request against the Step 1.5 screening list before continuing.

### FAQ: The user asks for a medical diet (diabetes, renal, celiac)
Answer: Follow the Step 1 gate. Kidney disease means no plan at all, only a route to the nephrologist and renal dietitian. Diabetes and celiac mean the rainbow framework plus a route to the kupat cholim dietitian, covered by the health basket with a doctor referral.

### FAQ: The user confuses Israeli labels with EU Nutri-Score or UK traffic lights
Answer: Israel uses a binary red/green system, not an A-E scale. Red labels mark excess of specific nutrients, not overall quality, and the green label is a separate voluntary marking with its own eligibility list. Do not map the Israeli system onto European ones.
