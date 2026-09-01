#!/usr/bin/env python3
"""
Israeli Therapy Cost Estimator

Estimates monthly and annual therapy costs based on treatment setting
(kupat cholim vs. private), therapy type and session frequency.

Note: --city is accepted for backwards compatibility but does NOT change any figure.
The private rates are the national HebPsy survey averages.

Usage:
    python scripts/therapy-cost-estimator.py --sessions-per-month 4 --type private --city tel-aviv
    python scripts/therapy-cost-estimator.py --sessions-per-month 4 --type kupat-cholim
    python scripts/therapy-cost-estimator.py --sessions-per-month 2 --type private --city haifa --therapist social-worker
    python scripts/therapy-cost-estimator.py --help
"""

import argparse
import sys


# Private therapy rates, NIS per session.
#
# These are the published averages from the HebPsy (Psychologia Ivrit) 2025 rate
# survey, which is the only methodologically grounded price source for this market.
# They are NOT invented ranges, and no per-city figure is quoted here: the survey
# reports regional variation of a few tens of shekels, which is smaller than the
# spread between individual therapists, so a per-city number would imply a
# precision the source does not support.
#
# Psychiatrists are deliberately absent. The survey did not sample them, so this
# script refuses to quote a psychiatrist rate rather than inventing one. That
# matches SKILL.md Step 5, which tells the user to ask the practice directly.
PRIVATE_COSTS = {
    "psychologist": {"average": 421},
    "social-worker": {"average": 371},
    "art-therapist": {"average": 366},
    "psychiatrist": None,  # no sourced rate exists; handled explicitly below
}

# Kupat cholim subsidized therapy costs
KUPAT_CHOLIM_COSTS = {
    # Copay depends on the SETTING, not on the kupah. Maccabi's published figures
    # (page last updated 29.7.2026): 41 NIS quarterly at a public-hospital outpatient
    # clinic, free at a psychiatric hospital, free at public and agreement clinics.
    # 41 is used here as the worst-case (highest) published figure.
    # Clalit / Meuhedet / Leumit publish their secondary-physician tariffs separately
    # and have NOT been read; do not assume they match.
    "quarterly_copay": 41,
    # Published entitlement: 2 assessment sessions + a 15-session kartisiya within
    # one year = 17 sessions. Agreement clinics have no session cap.
    "sessions_per_quarter": 4,
    "sessions_per_year": 17,
}

# University training clinics publish their own rates and they differ widely
# between institutions, so no figure is hard-coded here. The script reports the
# route and tells the user to ask the specific clinic, which is what SKILL.md says.
UNIVERSITY_CLINIC_COSTS = {"average": None, "label": "University Training Clinic"}

# Sliding scale options
SLIDING_SCALE = {
    "description": "Some therapists offer reduced fees based on financial need",
    "typical_discount": 0.30,  # ILLUSTRATIVE ONLY. No survey publishes a sliding-scale
    # discount, so this is a worked example, not a rate anyone is entitled to.
}

VALID_CITIES = ["tel-aviv", "jerusalem", "haifa", "beer-sheva", "herzliya", "other"]
VALID_THERAPISTS = list(PRIVATE_COSTS.keys())
PRICED_THERAPISTS = [k for k, v in PRIVATE_COSTS.items() if v]
VALID_TYPES = ["private", "kupat-cholim", "university-clinic", "sliding-scale"]

CITY_DISPLAY = {
    "tel-aviv": "Tel Aviv",
    "jerusalem": "Jerusalem",
    "haifa": "Haifa",
    "beer-sheva": "Be'er Sheva",
    "herzliya": "Herzliya",
    "other": "Other city",
}

THERAPIST_DISPLAY = {
    "psychologist": "Clinical Psychologist (Psikholog Klini)",
    "psychiatrist": "Psychiatrist (Psikh'iater)",
    "social-worker": "Clinical Social Worker (Oveid Sotsiali Klini)",
    "art-therapist": "Art Therapist (Metapel B'Omanut)",
}


def survey_rate(therapist_type):
    """Return the sourced average rate, or None where no source exists."""
    entry = PRIVATE_COSTS.get(therapist_type)
    return entry["average"] if entry else None


def estimate_costs(sessions_per_month, treatment_type, city, therapist_type):
    """Calculate estimated therapy costs."""
    result = {
        "sessions_per_month": sessions_per_month,
        "treatment_type": treatment_type,
    }

    if treatment_type == "kupat-cholim":
        quarterly_copay = KUPAT_CHOLIM_COSTS["quarterly_copay"]
        sessions_per_quarter = KUPAT_CHOLIM_COSTS["sessions_per_quarter"]
        sessions_per_year = KUPAT_CHOLIM_COSTS["sessions_per_year"]

        # Monthly cost is quarterly copay divided by 3
        monthly_cost = quarterly_copay / 3
        annual_cost = quarterly_copay * 4  # 4 quarters

        # Check if requested sessions exceed what kupat cholim provides
        requested_annual = sessions_per_month * 12
        excess_sessions = max(0, requested_annual - sessions_per_year)

        result.update({
            "monthly_low": monthly_cost,
            "monthly_high": monthly_cost,
            "annual_low": annual_cost,
            "annual_high": annual_cost,
            "per_session_low": quarterly_copay / sessions_per_quarter if sessions_per_quarter > 0 else 0,
            "per_session_high": quarterly_copay / sessions_per_quarter if sessions_per_quarter > 0 else 0,
            "sessions_covered": sessions_per_year,
            "excess_sessions": excess_sessions,
            "notes": [
                f"Published entitlement: {sessions_per_year} sessions per year "
                "(2 assessment + a 15-session kartisiya within one year)",
                f"Quarterly copay used here: {quarterly_copay} NIS. This is Maccabi's "
                "published public-hospital outpatient figure (29.7.2026) and is the "
                "worst case. At a public Ministry of Health clinic, at an agreement "
                "clinic, or at a psychiatric hospital the cost may be zero. Check "
                "your own kupah's copay booklet",
                "At a private clinic UNDER AGREEMENT with your kupah there is no "
                "session cap and no cost",
                "Wait times run to weeks or months in many regions. There is no binding "
                "national maximum waiting time, so do not treat one as an entitlement.",
                "Whether supplementary insurance (shaban) adds anything here is a question "
                "for your own kupah's shaban terms; this script does not assume it does.",
            ],
        })

        if excess_sessions > 0:
            result["notes"].append(
                f"You requested {requested_annual} sessions/year, but kupat cholim covers ~{sessions_per_year}. "
                f"The remaining {excess_sessions} sessions would need another route, for example a clinic under agreement with your kupah, which has no session cap."
            )

    elif treatment_type == "university-clinic":
        result.update({
            "unpriced": True,
            "label": UNIVERSITY_CLINIC_COSTS["label"],
            "notes": [
                "University training clinics offer reduced rates, but each clinic sets and "
                "publishes its own, so this script does not quote one. Ask the specific clinic.",
                "Therapists are graduate students supervised by licensed professionals",
                "Availability may be limited to the academic year (October-June)",
                "Examples: TAU Psychological Services, Hebrew U clinic, BGU clinic",
            ],
        })

    elif treatment_type == "sliding-scale":
        # Use private rates with discount
        rate = survey_rate(therapist_type)
        if rate is None:
            result.update({
                "unpriced": True,
                "therapist": THERAPIST_DISPLAY[therapist_type],
                "notes": [
                    "No sourced rate exists for this profession, so no figure is estimated. "
                    "The HebPsy survey does not sample psychiatrists. Ask the practice directly.",
                ],
            })
            return result
        discount = SLIDING_SCALE["typical_discount"]
        low = rate * (1 - discount)
        high = rate * (1 - discount)
        costs = {"low": rate, "high": rate}  # single sourced average, so no range

        result.update({
            "therapist": THERAPIST_DISPLAY[therapist_type],
            "city": CITY_DISPLAY[city],
            "monthly_low": low * sessions_per_month,
            "monthly_high": high * sessions_per_month,
            "annual_low": low * sessions_per_month * 12,
            "annual_high": high * sessions_per_month * 12,
            "per_session_low": low,
            "per_session_high": high,
            "regular_low": costs["low"],
            "regular_high": costs["high"],
            "notes": [
                f"ILLUSTRATIVE: assumes a ~{int(discount * 100)}% reduction. No source publishes a "
                "standard sliding-scale discount; ask the individual therapist what they offer",
                "Not all therapists offer sliding scale; ask when scheduling",
                "Some therapists reserve sliding-scale slots for students and low-income clients",
                "Be upfront about financial constraints when first contacting the therapist",
            ],
        })

    else:  # private
        rate = survey_rate(therapist_type)
        if rate is None:
            result.update({
                "unpriced": True,
                "therapist": THERAPIST_DISPLAY[therapist_type],
                "notes": [
                    "No sourced rate exists for this profession, so no figure is estimated. "
                    "The HebPsy survey does not sample psychiatrists. Ask the practice directly.",
                ],
            })
            return result
        low = rate
        high = rate

        result.update({
            "therapist": THERAPIST_DISPLAY[therapist_type],
            "city": CITY_DISPLAY[city],
            "monthly_low": low * sessions_per_month,
            "monthly_high": high * sessions_per_month,
            "annual_low": low * sessions_per_month * 12,
            "annual_high": high * sessions_per_month * 12,
            "per_session_low": low,
            "per_session_high": high,
            "notes": [
                "Private therapy costs vary by therapist experience and specialization",
                "First session may cost more (intake assessment)",
                "Some expenses may be tax-deductible if prescribed as medical treatment",
                "Keep all receipts (kabbalot) for potential tax benefits",
            ],
        })

    return result


def format_result(result):
    """Format the estimation result for display."""
    lines = []
    lines.append("")
    lines.append("=" * 60)
    lines.append("  ISRAELI THERAPY COST ESTIMATE")
    lines.append("=" * 60)
    lines.append("")

    type_labels = {
        "private": "Private Therapy",
        "kupat-cholim": "Kupat Cholim (Subsidized)",
        "university-clinic": "University Training Clinic",
        "sliding-scale": "Private (Sliding Scale)",
    }

    lines.append(f"  Treatment Setting:   {type_labels[result['treatment_type']]}")
    if "therapist" in result:
        lines.append(f"  Therapist Type:      {result['therapist']}")
    if "city" in result:
        lines.append(f"  City:                {result['city']} (does not affect the figure; the survey rate is national)")
    lines.append(f"  Sessions/Month:      {result['sessions_per_month']}")
    lines.append("")

    lines.append("-" * 60)
    lines.append("  COST BREAKDOWN")
    lines.append("-" * 60)
    lines.append("")

    if result.get("unpriced"):
        lines.append("  No figure is estimated for this option, because no sourced rate exists.")
        lines.append("")
        for note in result.get("notes", []):
            lines.append(f"  - {note}")
        lines.append("")
        lines.append("-" * 60)
        lines.append("  Rates are the published HebPsy 2025 survey averages. This is an")
        lines.append("  estimate, not a quote and not a bill. Confirm with the provider and")
        lines.append("  with your own kupah's copay booklet.")
        lines.append("-" * 60)
        lines.append("")
        return "\n".join(lines)

    if result["per_session_low"] == result["per_session_high"]:
        lines.append(f"  Per session:         {result['per_session_low']:>8,.0f} NIS")
    else:
        lines.append(f"  Per session:         {result['per_session_low']:>8,.0f} - {result['per_session_high']:>8,.0f} NIS")

    if "regular_low" in result:
        if result['regular_low'] == result['regular_high']:
            lines.append(f"  (Regular rate:       {result['regular_low']:>8,} NIS)")
        else:
            lines.append(f"  (Regular rate:       {result['regular_low']:>8,} - {result['regular_high']:>8,} NIS)")

    lines.append("")

    if result["monthly_low"] == result["monthly_high"]:
        lines.append(f"  Monthly cost:        {result['monthly_low']:>8,.0f} NIS")
    else:
        lines.append(f"  Monthly cost:        {result['monthly_low']:>8,.0f} - {result['monthly_high']:>8,.0f} NIS")

    if result["annual_low"] == result["annual_high"]:
        lines.append(f"  Annual cost:         {result['annual_low']:>8,.0f} NIS")
    else:
        lines.append(f"  Annual cost:         {result['annual_low']:>8,.0f} - {result['annual_high']:>8,.0f} NIS")

    if "sessions_covered" in result:
        lines.append("")
        lines.append(f"  Sessions covered/year: {result['sessions_covered']}")
        if result["excess_sessions"] > 0:
            lines.append(f"  Sessions NOT covered:  {result['excess_sessions']} (see notes for other routes)")

    lines.append("")
    lines.append("-" * 60)
    lines.append("  NOTES")
    lines.append("-" * 60)
    for note in result.get("notes", []):
        lines.append(f"  * {note}")

    lines.append("")
    lines.append("  COST-SAVING OPTIONS:")
    lines.append("  * Start with kupat cholim (often free; up to 41 NIS/quarter)")
    lines.append("  * Ask your kupah what, if anything, your shaban adds here. Do not assume it")
    lines.append("    adds sessions: it may not sell what is already inside the health basket")
    lines.append("  * University training clinics offer reduced rates")
    lines.append("  * Ask private therapists about sliding scale fees")
    lines.append("  * An employer EAP may cover some sessions; the number is set by the employer's")
    lines.append("    contract, so ask HR rather than assuming one")
    lines.append("")
    lines.append("  Disclaimer: Costs are estimates based on 2025-2026 data.")
    lines.append("  Actual prices vary by individual therapist and situation.")
    lines.append("")

    lines.append("-" * 60)
    lines.append("  Private rates are the published HebPsy 2025 survey averages, and kupah")
    lines.append("  copays depend on the SETTING. This is an estimate, not a quote and not a")
    lines.append("  bill. Confirm with the provider and with your own kupah's copay booklet.")
    lines.append("-" * 60)
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Estimate therapy costs in Israel.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sessions-per-month 4 --type private --city tel-aviv
  %(prog)s --sessions-per-month 4 --type kupat-cholim
  %(prog)s --sessions-per-month 2 --type private --city haifa --therapist social-worker
  %(prog)s --sessions-per-month 4 --type university-clinic
  %(prog)s --sessions-per-month 4 --type sliding-scale --city tel-aviv --therapist psychologist

Treatment types: private, kupat-cholim, university-clinic, sliding-scale
Therapist types: psychologist, psychiatrist, social-worker, art-therapist
Cities: tel-aviv, jerusalem, haifa, beer-sheva, herzliya, other
        """,
    )

    parser.add_argument(
        "--sessions-per-month",
        type=int,
        required=True,
        help="Number of therapy sessions per month (typically 1-4)",
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=VALID_TYPES,
        help="Treatment setting (private, kupat-cholim, university-clinic, sliding-scale)",
    )
    parser.add_argument(
        "--city",
        choices=VALID_CITIES,
        default="other",
        help="City for private therapy pricing (default: other)",
    )
    parser.add_argument(
        "--therapist",
        choices=VALID_THERAPISTS,
        default="psychologist",
        help="Type of therapist for private therapy (default: psychologist)",
    )

    args = parser.parse_args()

    # Validate sessions
    if args.sessions_per_month < 1 or args.sessions_per_month > 12:
        print("Error: Sessions per month must be between 1 and 12.")
        sys.exit(1)

    # City and therapist are only relevant for private and sliding-scale
    if args.type in ("kupat-cholim", "university-clinic") and args.city != "other":
        pass  # Silently ignore city for non-private types

    result = estimate_costs(
        sessions_per_month=args.sessions_per_month,
        treatment_type=args.type,
        city=args.city,
        therapist_type=args.therapist,
    )

    print(format_result(result))


if __name__ == "__main__":
    main()
