#!/usr/bin/env python3
"""
Israeli Therapy Cost Estimator

Estimates monthly and annual therapy costs based on treatment setting
(kupat cholim vs. private), therapy type, session frequency, and city.

Usage:
    python scripts/therapy-cost-estimator.py --sessions-per-month 4 --type private --city tel-aviv
    python scripts/therapy-cost-estimator.py --sessions-per-month 4 --type kupat-cholim
    python scripts/therapy-cost-estimator.py --sessions-per-month 2 --type private --city haifa --therapist social-worker
    python scripts/therapy-cost-estimator.py --help
"""

import argparse
import sys


# Private therapy cost ranges by therapist type and city (NIS per session)
PRIVATE_COSTS = {
    "psychologist": {
        "tel-aviv": {"low": 400, "high": 600},
        "jerusalem": {"low": 350, "high": 550},
        "haifa": {"low": 300, "high": 500},
        "beer-sheva": {"low": 280, "high": 450},
        "herzliya": {"low": 400, "high": 600},
        "other": {"low": 300, "high": 500},
    },
    "psychiatrist": {
        "tel-aviv": {"low": 600, "high": 900},
        "jerusalem": {"low": 550, "high": 800},
        "haifa": {"low": 500, "high": 750},
        "beer-sheva": {"low": 450, "high": 700},
        "herzliya": {"low": 600, "high": 900},
        "other": {"low": 500, "high": 750},
    },
    "social-worker": {
        "tel-aviv": {"low": 250, "high": 450},
        "jerusalem": {"low": 220, "high": 400},
        "haifa": {"low": 200, "high": 380},
        "beer-sheva": {"low": 180, "high": 350},
        "herzliya": {"low": 250, "high": 450},
        "other": {"low": 200, "high": 380},
    },
    "art-therapist": {
        "tel-aviv": {"low": 300, "high": 500},
        "jerusalem": {"low": 280, "high": 450},
        "haifa": {"low": 250, "high": 420},
        "beer-sheva": {"low": 230, "high": 400},
        "herzliya": {"low": 300, "high": 500},
        "other": {"low": 250, "high": 420},
    },
}

# Kupat cholim subsidized therapy costs
KUPAT_CHOLIM_COSTS = {
    "quarterly_copay": 34,       # Approximate quarterly copay in NIS
    "sessions_per_quarter": 4,   # Typical sessions covered per quarter
    "sessions_per_year": 16,     # Typical maximum sessions per year
}

# University training clinic costs (reduced rates)
UNIVERSITY_CLINIC_COSTS = {
    "low": 150,
    "high": 250,
    "label": "University Training Clinic",
}

# Sliding scale options
SLIDING_SCALE = {
    "description": "Some therapists offer reduced fees based on financial need",
    "typical_discount": 0.30,  # 30% typical discount
}

VALID_CITIES = ["tel-aviv", "jerusalem", "haifa", "beer-sheva", "herzliya", "other"]
VALID_THERAPISTS = list(PRIVATE_COSTS.keys())
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
                f"Kupat cholim typically covers {sessions_per_year} sessions per year",
                f"Quarterly copay: approximately {quarterly_copay} NIS",
                "Wait times may be 2-8 weeks for initial appointment",
                "SHABAN (supplementary insurance) may provide additional sessions",
            ],
        })

        if excess_sessions > 0:
            result["notes"].append(
                f"You requested {requested_annual} sessions/year, but kupat cholim covers ~{sessions_per_year}. "
                f"The remaining {excess_sessions} sessions would need to be private or through SHABAN."
            )

    elif treatment_type == "university-clinic":
        low = UNIVERSITY_CLINIC_COSTS["low"]
        high = UNIVERSITY_CLINIC_COSTS["high"]

        result.update({
            "monthly_low": low * sessions_per_month,
            "monthly_high": high * sessions_per_month,
            "annual_low": low * sessions_per_month * 12,
            "annual_high": high * sessions_per_month * 12,
            "per_session_low": low,
            "per_session_high": high,
            "notes": [
                "University training clinics offer reduced rates (150-250 NIS/session)",
                "Therapists are graduate students supervised by licensed professionals",
                "Quality is generally good; supervisors review all cases",
                "Availability may be limited to academic year (October-June)",
                "Examples: TAU Psychological Services, Hebrew U clinic, BGU clinic",
            ],
        })

    elif treatment_type == "sliding-scale":
        # Use private rates with discount
        costs = PRIVATE_COSTS[therapist_type][city]
        discount = SLIDING_SCALE["typical_discount"]
        low = costs["low"] * (1 - discount)
        high = costs["high"] * (1 - discount)

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
                f"Sliding scale assumes ~{int(discount * 100)}% reduction from standard rates",
                "Not all therapists offer sliding scale; ask when scheduling",
                "Some therapists reserve sliding-scale slots for students and low-income clients",
                "Be upfront about financial constraints when first contacting the therapist",
            ],
        })

    else:  # private
        costs = PRIVATE_COSTS[therapist_type][city]
        low = costs["low"]
        high = costs["high"]

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
        lines.append(f"  City:                {result['city']}")
    lines.append(f"  Sessions/Month:      {result['sessions_per_month']}")
    lines.append("")

    lines.append("-" * 60)
    lines.append("  COST BREAKDOWN")
    lines.append("-" * 60)
    lines.append("")

    if result["per_session_low"] == result["per_session_high"]:
        lines.append(f"  Per session:         {result['per_session_low']:>8,.0f} NIS")
    else:
        lines.append(f"  Per session:         {result['per_session_low']:>8,.0f} - {result['per_session_high']:>8,.0f} NIS")

    if "regular_low" in result:
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
            lines.append(f"  Sessions NOT covered:  {result['excess_sessions']} (would need private/SHABAN)")

    lines.append("")
    lines.append("-" * 60)
    lines.append("  NOTES")
    lines.append("-" * 60)
    for note in result.get("notes", []):
        lines.append(f"  * {note}")

    lines.append("")
    lines.append("  COST-SAVING OPTIONS:")
    lines.append("  * Start with kupat cholim (subsidized, ~34 NIS/quarter)")
    lines.append("  * Check SHABAN for additional covered sessions")
    lines.append("  * University training clinics: 150-250 NIS/session")
    lines.append("  * Ask private therapists about sliding scale fees")
    lines.append("  * EAP through employer: 3-6 free sessions")
    lines.append("")
    lines.append("  Disclaimer: Costs are estimates based on 2025-2026 data.")
    lines.append("  Actual prices vary by individual therapist and situation.")
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
