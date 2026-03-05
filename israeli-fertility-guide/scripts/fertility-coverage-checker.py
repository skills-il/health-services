#!/usr/bin/env python3
"""
Israeli Fertility Treatment Coverage Checker

Determines what fertility treatment coverage a person is entitled to based
on age, number of existing children (from current relationship), marital
status, and insurance type.

Usage:
    python scripts/fertility-coverage-checker.py --age 38 --children 1 --insurance basic
    python scripts/fertility-coverage-checker.py --age 33 --children 0 --status single --insurance basic
    python scripts/fertility-coverage-checker.py --age 42 --children 2 --insurance shaban
    python scripts/fertility-coverage-checker.py --help
"""

import argparse
import sys


def check_coverage(age, children, status, insurance):
    """Determine fertility treatment coverage based on input parameters."""
    result = {
        "age": age,
        "children": children,
        "status": status,
        "insurance": insurance,
        "treatments": [],
        "notes": [],
        "warnings": [],
    }

    # Age-based eligibility
    if age > 45:
        result["warnings"].append(
            "Age exceeds 45. Health basket IVF coverage ends at age 45. "
            "Some SHABAN plans may extend coverage slightly. "
            "Consult your kupat cholim for specific options."
        )
        basic_ivf_eligible = False
    elif age >= 42:
        basic_ivf_eligible = children < 2
        result["notes"].append(
            f"At age {age}, IVF success rates are lower but you remain legally "
            "entitled to coverage until age 45."
        )
    else:
        basic_ivf_eligible = children < 2

    # Children-based eligibility
    has_basic_ivf = basic_ivf_eligible and children < 2

    # Build treatment list
    treatments = []

    # IVF coverage
    if has_basic_ivf:
        treatments.append({
            "name": "IVF (In Vitro Fertilization)",
            "hebrew": "הפריה חוץ גופית",
            "covered": True,
            "source": "Health Basket (Sal Briut)",
            "details": (
                f"Fully covered. You have {children} children from your current "
                f"relationship, so you are entitled to coverage for "
                f"{2 - children} more live birth(s)."
            ),
            "cost": "Minimal copays (parking, some medications)",
        })
    elif children >= 2 and insurance == "shaban":
        treatments.append({
            "name": "IVF (In Vitro Fertilization)",
            "hebrew": "הפריה חוץ גופית",
            "covered": True,
            "source": "SHABAN (Supplementary Insurance)",
            "details": (
                "Basic health basket coverage is exhausted (2 live births reached). "
                "SHABAN may cover additional IVF cycles depending on your specific plan. "
                "Contact your kupat cholim to verify your SHABAN fertility benefits."
            ),
            "cost": "Varies by SHABAN plan; may have higher copays",
        })
    elif children >= 2:
        treatments.append({
            "name": "IVF (In Vitro Fertilization)",
            "hebrew": "הפריה חוץ גופית",
            "covered": False,
            "source": "N/A",
            "details": (
                "Basic health basket coverage ends after 2 live births. "
                "Without SHABAN, IVF costs are fully out-of-pocket "
                "(approximately 15,000-25,000 NIS per cycle). "
                "Consider upgrading to SHABAN with fertility benefits "
                "(note: 6-12 month waiting period)."
            ),
            "cost": "15,000-25,000 NIS per cycle (out-of-pocket)",
        })

    # IUI coverage
    if children < 2 and age <= 45:
        treatments.append({
            "name": "IUI (Intrauterine Insemination)",
            "hebrew": "הזרעה תוך רחמית",
            "covered": True,
            "source": "Health Basket",
            "details": "Fully covered. Often tried before IVF as a less invasive option.",
            "cost": "Minimal copays",
        })

    # Egg freezing
    if status == "single" and 30 <= age <= 41:
        treatments.append({
            "name": "Egg Freezing (Elective)",
            "hebrew": "הקפאת ביציות (אלקטיבית)",
            "covered": True,
            "source": "Health Basket",
            "details": (
                f"As a single woman age {age}, you are eligible for funded "
                "elective egg freezing (up to 4 cycles). Annual storage fees "
                "(1,000-2,000 NIS/year) are out-of-pocket."
            ),
            "cost": "Cycles covered; storage: 1,000-2,000 NIS/year",
        })
    elif status == "single" and age < 30:
        treatments.append({
            "name": "Egg Freezing (Elective)",
            "hebrew": "הקפאת ביציות (אלקטיבית)",
            "covered": False,
            "source": "N/A",
            "details": (
                f"Elective egg freezing is covered for single women ages 30-41. "
                f"At age {age}, you are not yet eligible. You will become eligible at age 30."
            ),
            "cost": "10,000-15,000 NIS per cycle if done privately before age 30",
        })
    elif status == "single" and age > 41:
        treatments.append({
            "name": "Egg Freezing (Elective)",
            "hebrew": "הקפאת ביציות (אלקטיבית)",
            "covered": False,
            "source": "N/A",
            "details": (
                f"Elective egg freezing coverage is for ages 30-41. "
                f"At age {age}, the funded window has passed. "
                "Medical egg freezing (for health reasons) may still be covered."
            ),
            "cost": "10,000-15,000 NIS per cycle (out-of-pocket)",
        })

    # Medical egg freezing (always mention for cancer patients, etc.)
    treatments.append({
        "name": "Egg Freezing (Medical)",
        "hebrew": "הקפאת ביציות (רפואית)",
        "covered": True,
        "source": "Health Basket",
        "details": (
            "Egg freezing for medical reasons (cancer treatment, surgery, medical "
            "conditions that threaten fertility) is covered regardless of age "
            "or marital status."
        ),
        "cost": "Covered; storage fees may apply",
    })

    # Sperm donation
    if status in ("single", "single-female-couple"):
        treatments.append({
            "name": "Sperm Donation",
            "hebrew": "תרומת זרע",
            "covered": True,
            "source": "Health Basket",
            "details": (
                "Sperm donation through licensed sperm banks is covered. "
                "Donors are anonymous. Selection available by general characteristics."
            ),
            "cost": "Covered",
        })

    # ICSI
    if has_basic_ivf:
        treatments.append({
            "name": "ICSI (Intracytoplasmic Sperm Injection)",
            "hebrew": "הזרקת זרע תוך ביצית",
            "covered": True,
            "source": "Health Basket",
            "details": (
                "Covered when medically indicated (low sperm count/motility, "
                "previous fertilization failure)."
            ),
            "cost": "Covered",
        })

    # Genetic testing
    treatments.append({
        "name": "PGT (Preimplantation Genetic Testing)",
        "hebrew": "בדיקה גנטית טרום השתלה",
        "covered": "Partial",
        "source": "Health Basket / SHABAN",
        "details": (
            "PGT-M (for known genetic conditions) is usually covered. "
            "PGT-A (aneuploidy screening) coverage varies; some SHABAN plans cover it. "
            "If not covered, cost is approximately 5,000-10,000 NIS."
        ),
        "cost": "Varies; 5,000-10,000 NIS if not covered",
    })

    # Surrogacy
    treatments.append({
        "name": "Surrogacy",
        "hebrew": "פונדקאות",
        "covered": False,
        "source": "Mostly out-of-pocket",
        "details": (
            "Legal in Israel. Medical costs (IVF) may be partially covered by "
            "the health basket. Surrogate compensation, legal fees, and other costs "
            "are out-of-pocket (total: 150,000-250,000 NIS). "
            "Requires approval from a special committee."
        ),
        "cost": "150,000-250,000 NIS total",
    })

    result["treatments"] = treatments

    # SHABAN recommendation
    if children >= 1 and insurance == "basic":
        result["notes"].append(
            "Consider enrolling in SHABAN (supplementary insurance) before "
            "needing additional fertility treatment. SHABAN plans have a "
            "6-12 month waiting period for fertility benefits."
        )

    # Relationship change note
    if children >= 2:
        result["notes"].append(
            "If you have started a new relationship since your previous children, "
            "the 2-live-birth count may reset. Consult your kupat cholim to clarify."
        )

    return result


def format_result(result):
    """Format the coverage check result for display."""
    lines = []
    lines.append("")
    lines.append("=" * 65)
    lines.append("  ISRAELI FERTILITY COVERAGE CHECK")
    lines.append("=" * 65)
    lines.append("")

    status_labels = {
        "single": "Single",
        "married": "Married/Partnered",
        "single-female-couple": "Same-Sex Female Couple",
    }

    insurance_labels = {
        "basic": "Basic Health Basket Only",
        "shaban": "Basic + SHABAN (Supplementary)",
    }

    lines.append(f"  Age:                {result['age']}")
    lines.append(f"  Children (current): {result['children']}")
    lines.append(f"  Status:             {status_labels.get(result['status'], result['status'])}")
    lines.append(f"  Insurance:          {insurance_labels.get(result['insurance'], result['insurance'])}")
    lines.append("")

    # Warnings first
    for warning in result.get("warnings", []):
        lines.append(f"  *** WARNING: {warning}")
        lines.append("")

    lines.append("-" * 65)
    lines.append("  TREATMENT COVERAGE")
    lines.append("-" * 65)

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
        lines.append(f"           ({treatment['hebrew']})")
        lines.append(f"           Source: {treatment['source']}")
        lines.append(f"           Cost: {treatment['cost']}")

        # Wrap details text
        detail_text = treatment["details"]
        words = detail_text.split()
        current_line = "           "
        for word in words:
            if len(current_line) + len(word) + 1 > 65:
                lines.append(current_line)
                current_line = "           " + word
            else:
                current_line += (" " if current_line.strip() else "") + word
        if current_line.strip():
            lines.append(current_line)

    # Notes
    if result.get("notes"):
        lines.append("")
        lines.append("-" * 65)
        lines.append("  ADDITIONAL NOTES")
        lines.append("-" * 65)
        for note in result["notes"]:
            lines.append(f"  * {note}")

    lines.append("")
    lines.append("-" * 65)
    lines.append("  Disclaimer: This is an estimate based on current regulations.")
    lines.append("  Contact your kupat cholim for exact coverage details.")
    lines.append("  Regulations and health basket contents are updated annually.")
    lines.append("-" * 65)
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Check fertility treatment coverage eligibility in Israel.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --age 38 --children 1 --insurance basic
  %(prog)s --age 33 --children 0 --status single --insurance basic
  %(prog)s --age 42 --children 2 --insurance shaban
  %(prog)s --age 28 --children 0 --status single --insurance basic

Statuses: married (default), single, single-female-couple
Insurance: basic (default), shaban
        """,
    )

    parser.add_argument(
        "--age",
        type=int,
        required=True,
        help="Age of the woman seeking treatment",
    )
    parser.add_argument(
        "--children",
        type=int,
        required=True,
        help="Number of living children from current relationship",
    )
    parser.add_argument(
        "--status",
        choices=["married", "single", "single-female-couple"],
        default="married",
        help="Relationship status (default: married)",
    )
    parser.add_argument(
        "--insurance",
        choices=["basic", "shaban"],
        default="basic",
        help="Insurance type: basic (health basket only) or shaban (with supplementary)",
    )

    args = parser.parse_args()

    # Validate age
    if args.age < 18 or args.age > 55:
        print("Error: Age must be between 18 and 55.")
        sys.exit(1)

    # Validate children
    if args.children < 0 or args.children > 10:
        print("Error: Number of children must be between 0 and 10.")
        sys.exit(1)

    result = check_coverage(
        age=args.age,
        children=args.children,
        status=args.status,
        insurance=args.insurance,
    )

    print(format_result(result))


if __name__ == "__main__":
    main()
