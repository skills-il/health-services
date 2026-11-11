#!/usr/bin/env python3
"""
Israeli Fertility Treatment Coverage Checker

Summarises the published fertility coverage rules that may apply given
age, number of existing children (from the current relationship),
relationship status, kupat cholim and insurance type. General rules only,
not an eligibility determination: the kupah decides eligibility.

Sources for the rules encoded here:
  - Kol Zchut, IVF: ages 18 to 45 with own eggs, until 54 with a donated egg;
    twins exhaust the entitlement; MoH Circular 6/2014 cycle rules.
  - Kol Zchut, egg freezing: elective from 30 until the 41st birthday,
    MoH Circular 1/2011 caps of 6 retrievals, 25 eggs (30-35), 35 eggs (36-40).
  - Kol Zchut, receiving donor sperm: the kupah funds the procedure, the
    woman buys the sperm vial herself.
  - Kol Zchut, receiving a donated egg: statutory recipient fee of 10,000 NIS
    (7,000 NIS on income support).
  - Maccabi eligibility 2565: frozen-embryo transfer (stage C) funded until the
    54th birthday when stages A and B were done before the 45th; fertility drugs
    carry a pharmacy copay.
  - gov.il oocyte cryopreservation: frozen eggs may be used until age 54; a woman
    who started elective freezing before 41 may continue while it is continuous.

Usage:
    python scripts/fertility-coverage-checker.py --age 38 --children 1 --insurance basic
    python scripts/fertility-coverage-checker.py --age 46 --children 0
    python scripts/fertility-coverage-checker.py --age 40 --children 0 --kupah meuhedet --insurance shaban
    python scripts/fertility-coverage-checker.py --age 36 --children 0 --status married --male-factor
    python scripts/fertility-coverage-checker.py --age 41 --children 2 --previous-children 1 --kupah meuhedet
    python scripts/fertility-coverage-checker.py --help
"""

import argparse
import sys

OWN_EGG_AGE_LIMIT = 45      # until the 45th birthday
DONOR_EGG_AGE_LIMIT = 54    # funded treatment with a donated egg
CYCLE_RULE_AGE = 42         # MoH Circular 6/2014
ELECTIVE_MIN_AGE = 30       # turned 30
ELECTIVE_MAX_AGE = 40       # not yet 41
MEDICAL_FREEZE_RISK_AGE = 39

# Elective egg-freezing SHABAN subsidies, all at a 3,500 NIS copay per cycle.
ELECTIVE_SHABAN = {
    "clalit": (30, 37, "Clalit Mushlam Platinum, ages 30 to 37 (until the 38th "
                       "birthday): 2 retrievals / 25 eggs at 30-35, 3 retrievals / "
                       "35 eggs at 36-37, 12-month qualification, not for women "
                       "who already used a preservation entitlement."),
    "maccabi": (31, 38, "Maccabi Sheli, ages 31 to 38 inclusive: up to 3 treatments "
                        "or 25 eggs, 12-month qualification."),
    "meuhedet": (30, 40, "Meuhedet Si (shia): 3,500 NIS copay, but Meuhedet's public "
                          "page gives no age band, so confirm your age with Meuhedet."),
    "leumit": (30, 37, "Leumit Zahav, ages 30 to 37 inclusive: up to 4 rounds, "
                       "12-month qualification."),
}

KUPAH_LABELS = {
    "clalit": "Clalit",
    "maccabi": "Maccabi",
    "meuhedet": "Meuhedet",
    "leumit": "Leumit",
    "unknown": "Not specified",
}


def _entitlement_children(children, previous_children, new_relationship):
    """Living children counted against the 2-child entitlement.

    Entitlement attaches to common children of the CURRENT relationship, so
    children from a previous relationship are not counted.
    """
    if new_relationship:
        return 0
    return max(0, children - previous_children)


def check_coverage(age, children, status, insurance, kupah, male_factor,
                   new_relationship, income_support, previous_children=0):
    """Determine fertility treatment coverage based on input parameters."""
    result = {
        "age": age,
        "children": children,
        "counted_children": (children if status == "single" else
                             _entitlement_children(children, previous_children,
                                                   new_relationship)),
        "status": status,
        "insurance": insurance,
        "kupah": kupah,
        "treatments": [],
        "notes": [],
        "warnings": [],
    }

    counted = result["counted_children"]
    remaining = max(0, 2 - counted)
    # "until the 45th birthday": a woman who has turned 45 is past the ceiling.
    own_egg_ok = age < OWN_EGG_AGE_LIMIT
    # Egg donation: "turned 18 and not yet 54", so a woman who has turned 54 is past it.
    donor_egg_ok = age < DONOR_EGG_AGE_LIMIT
    # Some funded IVF track (own eggs, donated egg or stored embryos) remains open.
    funded_track = remaining > 0 and donor_egg_ok
    copay_text = ("Per-stage kupah copays (stages A, B, C); fertility drugs carry a "
                  "pharmacy copay; a donor sperm vial is NOT included")

    treatments = []

    # ---------------------------------------------------------------- IVF
    # Every combination of age and children must produce exactly one IVF row.
    if remaining > 0 and own_egg_ok:
        details = (
            f"Covered under the published rules. Counting {counted} living child(ren) "
            f"from the current relationship, the rules fund treatment toward up to "
            f"{remaining} more living child(ren); your kupah decides eligibility. The funded ceiling with your own eggs is age "
            f"{OWN_EGG_AGE_LIMIT} (until your 45th birthday)."
        )
        if age >= CYCLE_RULE_AGE:
            details += (
                " NOTE, age 42+ cycle rule (MoH Circular 6/2014): you may not "
                "perform more than 3 CONSECUTIVE cycles that did not reach embryo "
                "transfer. Any transfer, even in the third cycle, restarts the "
                "count. After 4 consecutive cycles with no transfer, or 8 cycles "
                "with no clinical pregnancy, the treating team must convene a "
                "review before continuing."
            )
        treatments.append({
            "name": "IVF (In Vitro Fertilization), own eggs",
            "hebrew": "הפריה חוץ גופית מביציות עצמיות",
            "covered": True,
            "source": "Health Basket (Sal Briut)",
            "details": details,
            "cost": copay_text,
        })
    elif remaining > 0 and not own_egg_ok and donor_egg_ok:
        treatments.append({
            "name": "IVF, own eggs",
            "hebrew": "הפריה חוץ גופית מביציות עצמיות",
            "covered": False,
            "source": "N/A",
            "details": (
                f"At age {age} the funded own-egg track has ended: the basket funds "
                f"IVF with the woman's own eggs only until her 45th birthday. This "
                f"does NOT mean your fertility coverage ended, see the egg-donation "
                f"row below."
            ),
            "cost": "Self-pay if a unit agrees to treat",
        })
        treatments.append({
            "name": "Frozen embryo transfer (stage C) of embryos made before 45",
            "hebrew": "החזרת עובר מוקפא",
            "covered": "If embryos are stored",
            "source": "Health Basket",
            "details": (
                "Age 45 limits new retrievals, not transfers. Maccabi's published "
                "terms fund thawing and transferring an embryo until the 54th "
                "birthday when stimulation and retrieval were done before the 45th; "
                "confirm your kupah's terms. The Ministry of Health also lets women "
                "use their own frozen eggs until 54, but whether the kupah funds "
                "thawing and fertilizing them after 45 is not stated, so ask."
            ),
            "cost": "Stage C copay",
        })
    elif remaining > 0 and not donor_egg_ok:
        treatments.append({
            "name": "IVF (any egg source)",
            "hebrew": "הפריה חוץ גופית",
            "covered": False,
            "source": "N/A",
            "details": (
                f"At age {age} both funded tracks have ended: own eggs are funded "
                f"until the 45th birthday, and treatment with a donated egg is "
                f"funded until the {DONOR_EGG_AGE_LIMIT}th birthday."
            ),
            "cost": "Not funded",
        })
    elif insurance == "shaban" and donor_egg_ok:
        treatments.append({
            "name": "IVF (third child or beyond)",
            "hebrew": "הפריה חוץ גופית לילד שלישי ומעלה",
            "covered": "Partial",
            "source": "SHABAN (Supplementary Insurance)",
            "details": (
                "Basic basket coverage is exhausted (2 living children from the "
                "current relationship). Some SHABAN plans fund additional cycles, "
                "with their own age limits and qualification periods. Contact your "
                "kupah to verify the plan terms for your age."
            ),
            "cost": "Varies by SHABAN plan",
        })
    elif not donor_egg_ok:
        treatments.append({
            "name": "IVF (third child or beyond)",
            "hebrew": "הפריה חוץ גופית לילד שלישי ומעלה",
            "covered": False,
            "source": "N/A",
            "details": (
                f"Basic basket coverage is exhausted (2 living children from the "
                f"current relationship), and at age {age} even the donated-egg track "
                f"of the basket has ended (54th birthday). Ask any SHABAN plan for "
                f"its own age limit before assuming it pays."
            ),
            "cost": "Self-pay",
        })
    else:
        treatments.append({
            "name": "IVF (third child or beyond)",
            "hebrew": "הפריה חוץ גופית לילד שלישי ומעלה",
            "covered": False,
            "source": "N/A",
            "details": (
                "Basic basket coverage ends after 2 living children from the current "
                "relationship. Note that twins from one funded birth already exhaust "
                "the entitlement. Without SHABAN, a further cycle is self-paid; get a "
                "written quote from the unit. SHABAN fertility benefits carry a "
                "qualification period, so check the plan's terms before relying on it."
            ),
            "cost": "Self-pay; ask the unit for a written quote",
        })

    # -------------------------------------------------- Egg donation track
    if remaining > 0 and donor_egg_ok:
        fee = "7,000 NIS (income support)" if income_support else "10,000 NIS"
        highlight = (
            "This is the funded route from age 45. "
            if not own_egg_ok else ""
        )
        treatments.append({
            "name": "IVF with a donated egg (recipient)",
            "hebrew": "הפריה חוץ גופית מתרומת ביצית",
            "covered": "With a medical opinion",
            "source": "Health Basket (Egg Donation Law 2010)",
            "details": (
                f"{highlight}Funded for Israeli-resident women from 18 until their "
                f"{DONOR_EGG_AGE_LIMIT}th birthday with a medical opinion that they cannot "
                f"conceive from their own eggs, within the same 2-living-children "
                f"entitlement. The recipient pays a statutory fee to the hospital; "
                f"the kupah funds the rest."
            ),
            "cost": f"Statutory recipient fee: {fee}",
        })

    # ---------------------------------------------------------------- IUI
    if remaining > 0 and own_egg_ok:
        treatments.append({
            "name": "IUI (Intrauterine Insemination)",
            "hebrew": "הזרעה תוך רחמית",
            "covered": True,
            "source": "Health Basket",
            "details": "Covered. Often tried before IVF as a less invasive option.",
            "cost": "Kupah copays; a donor vial, if used, is self-purchased",
        })

    # ------------------------------------------- Elective egg freezing
    band = ELECTIVE_SHABAN.get(kupah)
    in_moh_window = ELECTIVE_MIN_AGE <= age <= ELECTIVE_MAX_AGE
    if in_moh_window:
        if band and band[0] <= age <= band[1]:
            covered = ("Depends on kupah" if kupah == "meuhedet" else "Partial") if insurance == "shaban" else False
            band_text = (
                f"Your kupah's band covers you: {band[2]} "
                if insurance == "shaban"
                else f"Your kupah offers it through SHABAN, which you do not hold: {band[2]} "
            )
        elif band:
            covered = False
            band_text = (
                f"Your kupah's SHABAN band does NOT cover age {age}: {band[2]} "
                f"Other kupot use different bands, so compare before assuming. "
            )
        else:
            covered = "Depends on kupah" if insurance == "shaban" else False
            band_text = "Pass --kupah to see whether your kupah's band includes your age. "
        treatments.append({
            "name": "Egg Freezing, elective (social)",
            "hebrew": "הקפאת ביציות אלקטיבית",
            "covered": covered,
            "source": "SHABAN only (never the basic basket)",
            "details": (
                f"Elective freezing is NEVER funded by the basic basket, but the "
                f"Ministry of Health permits it from age {ELECTIVE_MIN_AGE} until the "
                f"41st birthday and caps it (Circular 1/2011) at 6 retrievals, a "
                f"maximum of 25 eggs at ages 30 to 35 and 35 eggs at ages 36 to 40. "
                f"All four kupot now subsidize it through SHABAN at a 3,500 NIS copay "
                f"per cycle, on different age bands: Clalit 30-37, Maccabi 31-38, "
                f"Leumit 30-37; Meuhedet publishes no age band. {band_text}"
                f"Eggs are stored for up to 5 years and renewal requires advance "
                f"written notice."
            ),
            "cost": "3,500 NIS per cycle with a subsidizing SHABAN plan, otherwise "
                    "self-pay plus an annual storage fee",
        })
    else:
        continuation = (
            " A woman who STARTED before her 41st birthday may continue to the "
            "retrieval or egg cap while the process stays continuous."
            if age > ELECTIVE_MAX_AGE else ""
        )
        treatments.append({
            "name": "Egg Freezing, elective (social)",
            "hebrew": "הקפאת ביציות אלקטיבית",
            "covered": False,
            "source": "N/A",
            "details": (
                f"Elective freezing may start only from age {ELECTIVE_MIN_AGE} "
                f"until the 41st birthday, so at age {age} a new process cannot "
                f"start, and it is never in the basic basket.{continuation} Medical "
                f"egg freezing may still apply if you have a documented indication."
            ),
            "cost": "A new elective process cannot start at this age",
        })

    # --------------------------------------------- Medical egg freezing
    medical_details = (
        "Funded (eggs, embryos or ovarian tissue) for girls and women facing "
        "chemotherapy, radiation or ovary removal, and up to age "
        f"{MEDICAL_FREEZE_RISK_AGE} for women at increased risk of premature "
        "ovarian failure: diminished ovarian reserve, fragile-X premutation, a "
        "disease proven to raise that risk, gonadotoxic treatment not due to "
        "malignancy, planned removal of more than one ovary, or an ovarian "
        "endometrioma of at least 4 cm before surgery; also within gender "
        "transition. Toward a first and second child; the increased-risk and "
        "gender-transition tracks are capped at 4 cycles or 20 eggs (6 or 40 for "
        "fragile-X). Storage is funded until 2 children are born or "
        "the 42nd birthday, whichever comes first. Raise it BEFORE gonadotoxic "
        "treatment starts."
    )
    if counted >= 2:
        medical_covered = False
        medical_details = ("Medical preservation is funded toward a first and second "
                           "child, and 2 children are counted here. " + medical_details)
    elif age > MEDICAL_FREEZE_RISK_AGE:
        medical_covered = "Ask your kupah"
        medical_details = (f"At age {age} the increased-risk track (to 39) has ended; "
                           "Clalit states its oncology track runs to the 41st birthday, "
                           "so ask your kupah and the oncology unit. " + medical_details)
    else:
        medical_covered = "Depends on indication"
    treatments.append({
        "name": "Egg Freezing, medical indication",
        "hebrew": "הקפאת ביציות מסיבה רפואית",
        "covered": medical_covered,
        "source": "Health Basket",
        "details": medical_details,
        "cost": "No copay at a public hospital at Maccabi; storage beyond the "
                "funded period is self-paid",
    })

    # ------------------------------------------------------ Donor sperm
    # Married couples are eligible too when the infertility is male-factor,
    # which the previous version of this script silently excluded.
    show_sperm = status in ("single", "female-couple") or male_factor
    if show_sperm and not funded_track:
        treatments.append({
            "name": "Sperm Donation",
            "hebrew": "תרומת זרע",
            "covered": False,
            "source": "N/A",
            "details": (
                "No basket-funded treatment track remains open for these inputs "
                "(age or children), so the insemination itself is not funded either. "
                "The sperm vial is never funded."
            ),
            "cost": "Self-pay",
        })
    elif show_sperm:
        why = {
            "single": "as a single woman",
            "female-couple": "as a partner in a female couple",
            "married": "for a couple with male-factor infertility",
        }.get(status, "")
        treatments.append({
            "name": "Sperm Donation",
            "hebrew": "תרומת זרע",
            "covered": "Partial",
            "source": "Health Basket funds the procedure only",
            "details": (
                f"The published rules include applicants {why} in the eligible group. The kupah funds the "
                f"medical treatment (insemination, monitoring, lab work), but NOT the "
                f"sperm itself: `את מנת הזרע האישה רוכשת על חשבונה`. Donors are "
                f"anonymous, and donor insemination may not be performed in a private "
                f"clinic."
            ),
            "cost": "Vial NOT funded: several hundred NIS domestic, up to thousands "
                    "imported, and several vials are often needed",
        })

    # ------------------------------------------------------------- ICSI
    if remaining > 0 and (own_egg_ok or donor_egg_ok):
        icsi_details = (
            "Covered when medically indicated (low sperm count or motility, previous "
            "fertilization failure)."
        )
        if male_factor:
            icsi_details += (
                " With male-factor infertility, remember that the WOMAN's kupah funds "
                "the couple's treatment, but treatment of the man's sperm is funded by "
                "HIS kupah. Azoospermia is worked up at the fertility unit, and "
                "surgical retrieval (TESE, micro-TESE) belongs to that pathway; ask "
                "the unit and the kupah what is covered before scheduling."
            )
        treatments.append({
            "name": "ICSI (Intracytoplasmic Sperm Injection)",
            "hebrew": "הזרקת זרע תוך ביצית",
            "covered": True,
            "source": "Health Basket",
            "details": icsi_details,
            "cost": "Covered",
        })

    # -------------------------------------------------------------- PGT
    if funded_track:
        treatments.append({
            "name": "PGT (Preimplantation Genetic Testing)",
            "hebrew": "אבחון גנטי טרום השרשה",
            "covered": "Partial",
            "source": "Health Basket / SHABAN",
            "details": (
                "Funded for defined indications, including couples at high risk of a "
                "chromosomal defect or genetic disease. The 2026 basket (Director General "
                "Circular 02/2026) added PGT for carriers of high-cancer-risk mutations "
                "(BRCA1/BRCA2, Lynch syndrome) as part of IVF, and that entitlement is "
                "capped: `תוגבל לשני הריונות בלבד, שהסתיימו בלידה`. Eligibility is set on "
                "a genetic counselor's recommendation. Indications outside the list are "
                "self-pay or case-by-case."
            ),
            "cost": "Covered for listed indications; otherwise self-pay",
        })

    # --------------------------------------------------------- Surrogacy
    treatments.append({
        "name": "Surrogacy",
        "hebrew": "פונדקאות",
        "covered": (("Own eggs retrieved by 43 only"
                     if status == "single" and age > 43 else "IVF stages only")
                    if funded_track else False),
        "source": ("Health Basket for the IVF; surrogacy costs out-of-pocket"
                   if funded_track else "Out-of-pocket for these inputs"),
        "details": (
            "Legal under the Embryo Carrying Agreements Law 1996 for couples and "
            "single intended parents, subject to an approval committee. Intended "
            "parents must be Israeli residents, at least one under 54, with no more "
            "than 2 common children. The surrogate must be an Israeli resident, at "
            "least 22 and not yet 39, who has given birth before and is not a "
            "relative, and she can never be the egg donor. The committee will not "
            "approve eggs retrieved after age 43, and a single intended mother may "
            "not use a donated egg, so she needs her own eggs retrieved by 43. An "
            "intended mother also needs a medical opinion that she cannot carry a "
            "pregnancy or that it would seriously endanger her health. The intended "
            "parents' IVF stages are basket-funded; the surrogacy costs are not."
        ),
        "cost": "Large and highly variable; there is no official tariff, so get "
                "written quotes rather than trusting a headline figure",
    })

    # ------------------------------------------------------------ Notes
    if not own_egg_ok and donor_egg_ok:
        result["warnings"].append(
            f"Age {age} has reached the own-egg ceiling (until the 45th birthday), but NOT "
            f"past the funded egg-donation ceiling of {DONOR_EGG_AGE_LIMIT}. Under the "
            f"published rules, turning 45 ends the own-egg track, not fertility "
            f"coverage as a whole; ask the unit about the egg-donation track."
        )
    if age >= DONOR_EGG_AGE_LIMIT:
        result["warnings"].append(
            f"Age {age} is past both funded ceilings ({OWN_EGG_AGE_LIMIT} own eggs, "
            f"{DONOR_EGG_AGE_LIMIT} with a donated egg)."
        )
    if own_egg_ok and CYCLE_RULE_AGE - 2 <= age < CYCLE_RULE_AGE:
        result["notes"].append(
            "From your 42nd birthday the Circular 6/2014 cycle rule applies: no more "
            "than 3 consecutive cycles that did not reach embryo transfer. Own-egg "
            "retrievals are funded until the 45th birthday; Maccabi funds transferring "
            "embryos made before then until the 54th birthday (confirm your kupah)."
        )
    if own_egg_ok and age >= CYCLE_RULE_AGE:
        result["notes"].append(
            "Age 42+ cycle rule (MoH Circular 6/2014): no more than 3 consecutive "
            "cycles that did not reach embryo transfer, with any transfer resetting "
            "the count, plus a mandatory treating-team review after 4 consecutive "
            "no-transfer cycles or 8 cycles without clinical pregnancy."
        )
    result["notes"].append(
        "Twins from one funded birth exhaust the entitlement: the statute counts "
        "children, not pregnancies."
    )
    if children >= 1 and status == "single":
        result["warnings"].append(
            "You reported existing children and no partner. The single-parent track "
            "is published for a woman without children, so the rows above may not "
            "reflect your case: confirm your entitlement with your kupah in writing."
        )
    elif previous_children and not new_relationship:
        result["notes"].append(
            f"{previous_children} of the {children} child(ren) you reported are from a "
            f"previous relationship and are not counted: the entitlement is to a "
            f"common child of the current relationship. Confirm with your kupah."
        )
    elif new_relationship and children > 0:
        result["notes"].append(
            f"You reported {children} child(ren) from a previous relationship, so "
            f"they are not counted here. Entitlement attaches to children of the "
            f"CURRENT relationship. Confirm this with your kupah in writing."
        )
    elif children >= 1:
        result["notes"].append(
            "All reported children were counted as common children of the current "
            "relationship. If any are from a previous marriage, pass "
            "--previous-children N (or --new-relationship if all are): for a couple "
            "the entitlement is to a common child."
        )
    if status == "female-couple":
        result["notes"].append(
            "Reciprocal IVF is not permitted in Israel: one partner's egg may be "
            "fertilized here, but not transferred into her partner's uterus in Israel."
        )
    if insurance == "basic":
        result["notes"].append(
            "SHABAN fertility benefits have a qualification period (12 months on the "
            "Clalit, Maccabi and Leumit elective egg-freezing benefits), so enroll "
            "before you need it."
        )
    result["notes"].append(
        "If a kupah refuses something you believe you are entitled to, the statutory "
        "route is the Public Complaints Commissioner for the National Health "
        "Insurance Law at the Ministry of Health, not the kupah's own ombudsman."
    )

    if status == "single" and children >= 1:
        # The single-parent track is published for a woman WITHOUT children, so
        # do not label any funded row as covered for a single woman with children.
        for tr in treatments:
            if tr["covered"] is True or tr["covered"] == "With a medical opinion":
                tr["covered"] = "Confirm with your kupah"
    result["treatments"] = treatments
    return result


def _wrap(text, indent, width=78):
    lines = []
    current = indent
    for word in text.split():
        if len(current) + len(word) + 1 > width and current.strip():
            lines.append(current)
            current = indent + word
        else:
            current += (" " if current.strip() else "") + word
    if current.strip():
        lines.append(current)
    return lines


def format_result(result):
    """Format the coverage check result for display."""
    lines = ["", "=" * 78, "  ISRAELI FERTILITY COVERAGE CHECK", "=" * 78, ""]

    status_labels = {
        "single": "Single woman",
        "married": "Married or partnered",
        "female-couple": "Female same-sex couple",
    }
    insurance_labels = {
        "basic": "Basic health basket only",
        "shaban": "Basic + SHABAN (supplementary)",
    }

    lines.append(f"  Age:                {result['age']}")
    lines.append(f"  Children (current): {result['counted_children']}"
                 + (f"   (reported {result['children']}, previous relationship "
                    f"not counted)" if result['counted_children'] != result['children'] else ""))
    lines.append(f"  Status:             {status_labels.get(result['status'], result['status'])}")
    lines.append(f"  Kupat cholim:       {KUPAH_LABELS.get(result['kupah'], result['kupah'])}")
    lines.append(f"  Insurance:          {insurance_labels.get(result['insurance'], result['insurance'])}")
    lines.append("")

    for warning in result.get("warnings", []):
        lines.append("  *** WARNING:")
        lines.extend(_wrap(warning, "      "))
        lines.append("")

    lines.append("-" * 78)
    lines.append("  TREATMENT COVERAGE")
    lines.append("-" * 78)

    for treatment in result["treatments"]:
        lines.append("")
        covered = treatment["covered"]
        if covered is True:
            status_str = "COVERED UNDER PUBLISHED RULES"
        elif covered == "Partial":
            status_str = "PARTIAL"
        elif isinstance(covered, str):
            status_str = covered.upper()
        else:
            status_str = "NOT COVERED UNDER PUBLISHED RULES"

        lines.append(f"  [{status_str}] {treatment['name']}")
        # Hebrew label is printed on its own line, without wrapping punctuation
        # around it, so bidirectional reordering cannot mangle brackets.
        lines.append(f"           {treatment['hebrew']}")
        lines.append(f"           Source: {treatment['source']}")
        lines.extend(_wrap("Cost: " + treatment["cost"], "           "))
        lines.extend(_wrap(treatment["details"], "           "))

    if result.get("notes"):
        lines.append("")
        lines.append("-" * 78)
        lines.append("  ADDITIONAL NOTES")
        lines.append("-" * 78)
        for note in result["notes"]:
            wrapped = _wrap(note, "    ")
            wrapped[0] = "  * " + wrapped[0].strip()
            lines.extend(wrapped)

    lines.append("")
    lines.append("-" * 78)
    lines.append("  General rules only, not an eligibility determination and not")
    lines.append("  medical or legal advice. Confirm with your kupat cholim.")
    lines.append("  The health basket and SHABAN plans are updated annually.")
    lines.append("-" * 78)
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description=("Summarise the published Israeli fertility coverage rules for given "
                     "inputs. Not an eligibility determination."),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --age 38 --children 1 --insurance basic
  %(prog)s --age 46 --children 0
  %(prog)s --age 43 --children 0
  %(prog)s --age 40 --children 0 --kupah meuhedet --insurance shaban
  %(prog)s --age 36 --children 0 --status married --male-factor
  %(prog)s --age 41 --children 2 --previous-children 1 --kupah meuhedet

Statuses:  married (default), single, female-couple
Kupot:     unknown (default), clalit, maccabi, meuhedet, leumit
Insurance: basic (default), shaban
        """,
    )

    parser.add_argument("--age", type=int, required=True,
                        help="Age of the woman seeking treatment")
    parser.add_argument("--children", type=int, required=True,
                        help="Number of living children (see --new-relationship)")
    parser.add_argument("--status", choices=["married", "single", "female-couple"],
                        default="married", help="Relationship status (default: married)")
    parser.add_argument("--kupah", choices=["unknown", "clalit", "maccabi",
                                            "meuhedet", "leumit"],
                        default="unknown",
                        help="Kupat cholim, used for the elective egg-freezing band")
    parser.add_argument("--insurance", choices=["basic", "shaban"], default="basic",
                        help="basic (health basket only) or shaban (with supplementary)")
    parser.add_argument("--male-factor", action="store_true",
                        help="Male-factor infertility is involved")
    parser.add_argument("--new-relationship", action="store_true",
                        help="ALL existing children are from a previous relationship")
    parser.add_argument("--previous-children", type=int, default=0,
                        help="How many of --children are from a previous relationship")
    parser.add_argument("--income-support", action="store_true",
                        help="Recipient receives havtachat hachnasa (reduced egg-donation fee)")

    args = parser.parse_args()

    if args.age < 18 or args.age > 60:
        print("Error: Age must be between 18 and 60.", file=sys.stderr)
        sys.exit(1)
    if args.children < 0 or args.children > 10:
        print("Error: Number of children must be between 0 and 10.", file=sys.stderr)
        sys.exit(1)
    if args.previous_children < 0 or args.previous_children > args.children:
        print("Error: --previous-children must be between 0 and --children.",
              file=sys.stderr)
        sys.exit(1)

    result = check_coverage(
        age=args.age,
        children=args.children,
        status=args.status,
        insurance=args.insurance,
        kupah=args.kupah,
        male_factor=args.male_factor,
        new_relationship=args.new_relationship,
        income_support=args.income_support,
        previous_children=args.previous_children,
    )

    print(format_result(result))


if __name__ == "__main__":
    main()
