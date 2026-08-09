#!/usr/bin/env python3
"""
Israeli Fertility Treatment Coverage Checker

Determines what fertility treatment coverage a person is entitled to based
on age, number of existing children (from the current relationship),
relationship status, kupat cholim and insurance type.

Sources for the rules encoded here:
  - Kol Zchut, IVF: ages 18 to 45 with own eggs, to 54 with a donated egg;
    twins exhaust the entitlement; MoH Circular 6/2014 cycle rules.
  - Kol Zchut, egg freezing: elective from 30 until the 41st birthday,
    MoH Circular 1/2011 caps of 6 retrievals, 25 eggs (30-35), 35 eggs (36-40).
  - Kol Zchut, receiving donor sperm: the kupah funds the procedure, the
    woman buys the sperm vial herself.
  - Kol Zchut, receiving a donated egg: statutory recipient fee of 10,000 NIS
    (7,000 NIS on income support).

Usage:
    python scripts/fertility-coverage-checker.py --age 38 --children 1 --insurance basic
    python scripts/fertility-coverage-checker.py --age 46 --children 0
    python scripts/fertility-coverage-checker.py --age 40 --children 0 --kupah meuhedet --insurance shaban
    python scripts/fertility-coverage-checker.py --age 36 --children 0 --status married --male-factor
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
                       "35 eggs at 36-37, 5 years of storage included."),
    "maccabi": (31, 38, "Maccabi Sheli, ages 31 to 38 inclusive: up to 3 treatments "
                        "or 25 eggs, available from 15.03.2026, 12-month qualification."),
    "meuhedet": (30, 41, "Meuhedet Si (shia), ages 30 to 41."),
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


def _entitlement_children(children, status, new_relationship):
    """Living children counted against the 2-child entitlement."""
    if new_relationship:
        # Entitlement attaches to children of the CURRENT relationship.
        return 0
    return children


def check_coverage(age, children, status, insurance, kupah, male_factor,
                   new_relationship, income_support):
    """Determine fertility treatment coverage based on input parameters."""
    result = {
        "age": age,
        "children": children,
        "counted_children": _entitlement_children(children, status, new_relationship),
        "status": status,
        "insurance": insurance,
        "kupah": kupah,
        "treatments": [],
        "notes": [],
        "warnings": [],
    }

    counted = result["counted_children"]
    remaining = max(0, 2 - counted)
    own_egg_ok = age <= OWN_EGG_AGE_LIMIT
    donor_egg_ok = age <= DONOR_EGG_AGE_LIMIT

    treatments = []

    # ---------------------------------------------------------------- IVF
    # Every combination of age and children must produce exactly one IVF row.
    if remaining > 0 and own_egg_ok:
        details = (
            f"Fully covered. Counting {counted} living child(ren) from the current "
            f"relationship, you are entitled to funding toward {remaining} more "
            f"living child(ren). The funded ceiling with your own eggs is age "
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
            "cost": "Small copays; the donor sperm vial is NOT included",
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
    elif remaining > 0 and not donor_egg_ok:
        treatments.append({
            "name": "IVF (any egg source)",
            "hebrew": "הפריה חוץ גופית",
            "covered": False,
            "source": "N/A",
            "details": (
                f"At age {age} both funded tracks have ended: own eggs are funded "
                f"until the 45th birthday, and treatment with a donated egg is "
                f"funded until age {DONOR_EGG_AGE_LIMIT}."
            ),
            "cost": "Not funded",
        })
    elif insurance == "shaban":
        treatments.append({
            "name": "IVF (third child or beyond)",
            "hebrew": "הפריה חוץ גופית לילד שלישי ומעלה",
            "covered": "Partial",
            "source": "SHABAN (Supplementary Insurance)",
            "details": (
                "Basic basket coverage is exhausted (2 living children from the "
                "current relationship). Some SHABAN plans fund additional cycles. "
                "Contact your kupah to verify the plan terms and qualification period."
            ),
            "cost": "Varies by SHABAN plan",
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
                "written quote from the unit (market estimates run roughly 15,000 to "
                "25,000 NIS per cycle). SHABAN fertility benefits carry a "
                "qualification period of up to 12 months."
            ),
            "cost": "Self-pay; ask the unit for a written quote",
        })

    # -------------------------------------------------- Egg donation track
    if remaining > 0 and donor_egg_ok:
        fee = "7,000 NIS (income support)" if income_support else "10,000 NIS"
        highlight = (
            "This is the funded route above age 45. "
            if not own_egg_ok else ""
        )
        treatments.append({
            "name": "IVF with a donated egg (recipient)",
            "hebrew": "הפריה חוץ גופית מתרומת ביצית",
            "covered": True,
            "source": "Health Basket (Egg Donation Law 2010)",
            "details": (
                f"{highlight}Funded for Israeli-resident women aged 18 to "
                f"{DONOR_EGG_AGE_LIMIT} with a medical opinion that they cannot "
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
            "cost": "Small copays; a donor vial, if used, is self-purchased",
        })

    # ------------------------------------------- Elective egg freezing
    band = ELECTIVE_SHABAN.get(kupah)
    in_moh_window = ELECTIVE_MIN_AGE <= age <= ELECTIVE_MAX_AGE
    if in_moh_window:
        if band and band[0] <= age <= band[1]:
            covered = "Partial" if insurance == "shaban" else False
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
            covered = "Partial" if insurance == "shaban" else False
            band_text = ""
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
                f"Meuhedet 30-41, Leumit 30-37. {band_text}"
                f"Eggs are stored for up to 5 years and renewal requires advance "
                f"written notice."
            ),
            "cost": "3,500 NIS per cycle with a subsidizing SHABAN plan, otherwise "
                    "self-pay plus an annual storage fee",
        })
    else:
        treatments.append({
            "name": "Egg Freezing, elective (social)",
            "hebrew": "הקפאת ביציות אלקטיבית",
            "covered": False,
            "source": "N/A",
            "details": (
                f"Elective freezing is permitted only from age {ELECTIVE_MIN_AGE} "
                f"until the 41st birthday, so at age {age} it is outside the window "
                f"entirely, and it is never in the basic basket. Medical egg freezing "
                f"may still apply if you have a documented indication."
            ),
            "cost": "Not available electively at this age",
        })

    # --------------------------------------------- Medical egg freezing
    treatments.append({
        "name": "Egg Freezing, medical indication",
        "hebrew": "הקפאת ביציות מסיבה רפואית",
        "covered": True,
        "source": "Health Basket",
        "details": (
            "Funded for girls and women facing chemotherapy or radiation that may "
            f"harm fertility, and up to age {MEDICAL_FREEZE_RISK_AGE} for women at "
            "increased risk of premature ovarian failure (fragile-X premutation "
            "carriers, a disease proven to raise that risk, gonadotoxic treatment "
            "not due to malignancy, or prophylactic ovarian surgery). Ovarian "
            "tissue freezing is a listed basket "
            "method too. Raise it BEFORE gonadotoxic treatment starts."
        ),
        "cost": "Covered; annual storage fees usually apply",
    })

    # ------------------------------------------------------ Donor sperm
    # Married couples are eligible too when the infertility is male-factor,
    # which the previous version of this script silently excluded.
    show_sperm = status in ("single", "female-couple") or male_factor
    if show_sperm:
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
                f"You are within the eligible group {why}. The kupah funds the "
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
    treatments.append({
        "name": "PGT (Preimplantation Genetic Testing)",
        "hebrew": "אבחון גנטי טרום השרשה",
        "covered": "Partial",
        "source": "Health Basket / SHABAN",
        "details": (
            "Funded for defined indications. The 2026 basket (Director General "
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
        "covered": False,
        "source": "Mostly out-of-pocket",
        "details": (
            "Legal under the Embryo Carrying Agreements Law 1996 for couples and "
            "single individuals, subject to an approval committee. The surrogate must "
            "be an Israeli resident, at least 22 and not yet 39, who has given birth "
            "before and is not a relative, and she can never be the egg donor. Medical "
            "IVF costs may be partly covered."
        ),
        "cost": "Large and highly variable; there is no official tariff, so get "
                "written quotes rather than trusting a headline figure",
    })

    # ------------------------------------------------------------ Notes
    if not own_egg_ok and donor_egg_ok:
        result["warnings"].append(
            f"Age {age} is past the own-egg ceiling of {OWN_EGG_AGE_LIMIT}, but NOT "
            f"past the funded egg-donation ceiling of {DONOR_EGG_AGE_LIMIT}. Anyone "
            f"telling you your fertility coverage has ended is wrong."
        )
    if age > DONOR_EGG_AGE_LIMIT:
        result["warnings"].append(
            f"Age {age} is past both funded ceilings ({OWN_EGG_AGE_LIMIT} own eggs, "
            f"{DONOR_EGG_AGE_LIMIT} with a donated egg)."
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
    if new_relationship and children > 0:
        result["notes"].append(
            f"You reported {children} child(ren) from a previous relationship, so "
            f"they are not counted here. Entitlement attaches to children of the "
            f"CURRENT relationship. Confirm this with your kupah in writing."
        )
    elif children >= 1:
        result["notes"].append(
            "If your existing children are from a previous relationship, pass "
            "--new-relationship: the count attaches to the current relationship."
        )
    if status == "female-couple":
        result["notes"].append(
            "Reciprocal IVF is not permitted in Israel: one partner's egg may be "
            "fertilized here, but not transferred into her partner's uterus in Israel."
        )
    if insurance == "basic":
        result["notes"].append(
            "SHABAN fertility benefits have a qualification period (up to 12 months "
            "on the elective egg-freezing benefits), so enroll before you need it."
        )
    result["notes"].append(
        "If a kupah refuses something you believe you are entitled to, the statutory "
        "route is the Public Complaints Commissioner for the National Health "
        "Insurance Law at the Ministry of Health, not the kupah's own ombudsman."
    )

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
            status_str = "COVERED"
        elif covered == "Partial":
            status_str = "PARTIAL"
        else:
            status_str = "NOT COVERED"

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
    lines.append("  Disclaimer: this is an estimate based on published rules.")
    lines.append("  Contact your kupat cholim for a binding answer in your case.")
    lines.append("  The health basket and SHABAN plans are updated annually.")
    lines.append("-" * 78)
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Check fertility treatment coverage eligibility in Israel.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --age 38 --children 1 --insurance basic
  %(prog)s --age 46 --children 0
  %(prog)s --age 43 --children 0
  %(prog)s --age 40 --children 0 --kupah meuhedet --insurance shaban
  %(prog)s --age 36 --children 0 --status married --male-factor

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
                        help="Existing children are from a previous relationship")
    parser.add_argument("--income-support", action="store_true",
                        help="Recipient receives havtachat hachnasa (reduced egg-donation fee)")

    args = parser.parse_args()

    if args.age < 18 or args.age > 60:
        print("Error: Age must be between 18 and 60.")
        sys.exit(1)
    if args.children < 0 or args.children > 10:
        print("Error: Number of children must be between 0 and 10.")
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
    )

    print(format_result(result))


if __name__ == "__main__":
    main()
