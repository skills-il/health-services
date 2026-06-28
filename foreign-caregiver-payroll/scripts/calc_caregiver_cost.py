#!/usr/bin/env python3
"""Itemize the monthly employer cost of a foreign nursing caregiver in a private home.

Optional helper. The same math is documented in SKILL.md, so any agent can compute it
without this script. All rates are sourced in evidence.json and references/.

Usage:
  python scripts/calc_caregiver_cost.py --help
  python scripts/calc_caregiver_cost.py --wage 6443.85 --seniority-year 1 --care-level 5
  python scripts/calc_caregiver_cost.py --care-level 6 --insurance 250 --seniority-year 4

Notes:
  - Amounts are in shekels per month unless stated otherwise.
  - The social-provisions line is money to SET ASIDE for termination, not a monthly transfer.
  - Havraa is zero until the worker completes 12 months.
"""

import argparse

# Wage floor, effective 01.04.2026 (full-time monthly minimum wage).
MIN_WAGE_MONTHLY = 6443.85

# Employer National Insurance share, from January 2025 (applies to the full wage).
NATIONAL_INSURANCE_RATE = 0.036

# Employer pension contribution.
PENSION_RATE = 0.065

# Severance reserve: one month's salary per year worked = one twelfth of wage accrued monthly.
# A home employer paying directly (no formal pension-fund arrangement) owes full statutory
# severance, which is higher than the 6% the central fund uses. Reserve the full amount.
SEVERANCE_RESERVE_FRACTION = 1.0 / 12.0

# Private-sector recuperation tariff per day.
HAVRAA_PER_DAY = 418.0

# Recuperation days by seniority year.
def havraa_days(year: int) -> int:
    if year < 1:
        return 0  # not entitled until 12 months completed
    if year == 1:
        return 5
    if year <= 3:
        return 6
    if year <= 10:
        return 7
    if year <= 15:
        return 8
    if year <= 19:
        return 9
    return 10

# Long-term-care monthly cash benefit by level (effective 01.04.2026), used as an offset.
BENEFIT_BY_LEVEL = {1: 1705, 2: 2480, 3: 3472, 4: 4464, 5: 5456, 6: 6448}


def compute(wage: float, year: int, level: int, insurance: float) -> dict:
    wage = max(wage, MIN_WAGE_MONTHLY)
    national_insurance = round(wage * NATIONAL_INSURANCE_RATE, 2)
    pension = round(wage * PENSION_RATE, 2)
    severance_reserve = round(wage * SEVERANCE_RESERVE_FRACTION, 2)
    havraa_month = round(HAVRAA_PER_DAY * havraa_days(year) / 12, 2)
    gross = round(wage + national_insurance + pension + severance_reserve + havraa_month + insurance, 2)
    offset = BENEFIT_BY_LEVEL.get(level, 0)
    net = round(gross - offset, 2)
    return {
        "wage": wage,
        "national_insurance": national_insurance,
        "pension": pension,
        "severance_reserve": severance_reserve,
        "havraa_monthly_equiv": havraa_month,
        "medical_insurance": round(insurance, 2),
        "gross_monthly_cost": gross,
        "nursing_benefit_offset": offset,
        "net_monthly_cost": net,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Estimate monthly employer cost of a foreign caregiver.")
    ap.add_argument("--wage", type=float, default=MIN_WAGE_MONTHLY, help="Agreed monthly wage (floored at minimum wage).")
    ap.add_argument("--seniority-year", type=int, default=1, help="Completed full years of employment (use 0 during the first year; havraa starts only after 12 months).")
    ap.add_argument("--care-level", type=int, default=0, choices=[0, 1, 2, 3, 4, 5, 6], help="Bituach Leumi long-term-care level (0 = none).")
    ap.add_argument("--insurance", type=float, default=0.0, help="Monthly private medical-insurance premium.")
    args = ap.parse_args()

    r = compute(args.wage, args.seniority_year, args.care_level, args.insurance)
    print("Monthly employer cost estimate (shekels):")
    print(f"  Wage                         {r['wage']:>10.2f}")
    print(f"  National insurance           {r['national_insurance']:>10.2f}")
    print(f"  Pension (set aside)          {r['pension']:>10.2f}")
    print(f"  Severance reserve (set aside){r['severance_reserve']:>10.2f}")
    print(f"  Havraa (monthly equivalent)  {r['havraa_monthly_equiv']:>10.2f}")
    print(f"  Medical insurance            {r['medical_insurance']:>10.2f}")
    print(f"  --------------------------------------")
    print(f"  Gross monthly cost           {r['gross_monthly_cost']:>10.2f}")
    print(f"  Nursing-benefit offset      -{r['nursing_benefit_offset']:>10.2f}")
    print(f"  Net monthly cost             {r['net_monthly_cost']:>10.2f}")
    print()
    print("Reminder: pension and severance are accrued for termination, not paid monthly.")
    print("Havraa is zero until 12 months are completed. Verify rates against references/ before relying on them.")


if __name__ == "__main__":
    main()
