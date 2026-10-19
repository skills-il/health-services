#!/usr/bin/env python3
"""Itemize the monthly employer cost of a foreign nursing caregiver in a private home.

Optional helper. The same math is documented in SKILL.md, so any agent can compute it
without this script. All rates are sourced in evidence.json and references/.

Usage:
  python scripts/calc_caregiver_cost.py --help
  python scripts/calc_caregiver_cost.py --wage 6443.85 --completed-years 1 --month 14 --care-level 5
  python scripts/calc_caregiver_cost.py --care-level 6 --insurance 250 --completed-years 4 --month 50
  python scripts/calc_caregiver_cost.py --completed-years 0 --month 3 --care-level 5 \
      --region jerusalem --housing-expense 400

Notes:
  - Amounts are in shekels per month unless stated otherwise.
  - The social-provisions line is money to SET ASIDE for termination, not a monthly transfer.
  - Havraa accrues from month 1 but is not PAYABLE until 12 months are complete, and is
    then paid retroactively from the first day of work.
"""

import sys
import argparse

# Wage floor, effective 01.04.2026 (full-time monthly minimum wage).
MIN_WAGE_MONTHLY = 6443.85

# Employer National Insurance share, from January 2025 (applies to the full wage).
NATIONAL_INSURANCE_RATE = 0.036

# In lieu of pension contributions. A foreign worker cannot be insured in an Israeli
# pension fund, so this is NOT a contribution the employer remits anywhere: it is a sum
# owed to the worker. It accrues only from the SEVENTH month of employment, so charging
# it from month one over-states the first six months.
PENSION_RATE = 0.065
PENSION_FIRST_MONTH = 7

# Severance reserve: one month's salary per year worked = one twelfth of wage accrued monthly.
# A home employer paying directly (no formal pension-fund arrangement) owes full statutory
# severance, which is higher than the 6% the central fund uses. Reserve the full amount.
SEVERANCE_RESERVE_FRACTION = 1.0 / 12.0

# Private-sector recuperation tariff per day, havraa-year 2026 (1.7.2025 to 30.6.2026).
# This resets annually AND can be revised mid-year with retroactive effect: it moved from
# 418.0 to 451.5 on 18.08.2026, reaching back to 1.7.2025, with a duty to pay differentials
# on havraa already paid at the old rate. Re-read the source before relying on it.
HAVRAA_PER_DAY = 451.5
HAVRAA_TARIFF_AS_OF = "2026-08-18"

# Permitted deduction from the worker's wage for medical insurance: at most HALF the premium
# the employer paid, and not more than this monthly cap (nursing worker, from January 2026).
MEDICAL_DEDUCTION_MAX = 168.80
MEDICAL_DEDUCTION_SHARE = 0.5

# All discretionary deductions together may not exceed this share of the wage in one month.
TOTAL_DEDUCTION_CAP_SHARE = 0.25

# Housing deduction ceiling from 1.9.2026, permanent building (the patient's-own-home case),
# NIS per month. Foreign Workers (Rate of Wage Deductions for Suitable Accommodation)
# (Amendment) Regulations 5786-2026, regulation 2(a). The ceiling INCLUDES arnona, water,
# electricity, furniture and appliances, and it caps a reimbursement of expenses the employer
# actually incurred: it is not a flat amount. The old half rate for employer-owned housing and
# the separate 94.34 utilities line were repealed on 1.9.2026. Re-indexed every 1 January.
HOUSING_CAP_PERMANENT = {
    "jerusalem": 1095.0, "tel-aviv": 1257.0, "haifa": 999.0,
    "centre": 1030.0, "south": 999.0, "north": 999.0,
}

# Recuperation days by the YEAR OF EMPLOYMENT being worked (1 = the first year).
#
# Kol Zchut's table is "שנה ראשונה 5, שנה שנייה ושלישית 6, ..." and its worked example pays
# "6 ימי הבראה עבור השנה השנייה", so a worker who has COMPLETED one year accrues at 6 days. An
# earlier version passed completed years straight in, which was one day short at every band edge.
#
# Havraa becomes PAYABLE only after 12 completed months, but it is then paid retroactively to
# the first day of work (kolzchut/דמי_הבראה: "זכאי לתשלום דמי הבראה רטרואקטיבית, החל מיום עבודתו
# הראשון"). So the LIABILITY accrues from month one. An earlier version of this script returned 0
# days for an incomplete first year, which told families to reserve nothing and then landed them
# with five days' worth of havraa falling due in a single month.
def havraa_days(employment_year: int) -> int:
    year = employment_year
    if year <= 1:
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

# Long-term-care monthly cash benefit by level (effective 01.08.2026), used as an offset.
# NOTE: this is the FOREIGN-caregiver column. Bituach Leumi publishes a second, higher column
# for an employer of an ISRAELI caregiver (levels 3-6: 4,223 / 5,217 / 6,458 / 7,452), and
# 6,458 appears in BOTH tables at different levels. Do not mix them.
BENEFIT_BY_LEVEL = {1: 1708, 2: 2484, 3: 3478, 4: 4471, 5: 5465, 6: 6458}
BENEFIT_BY_LEVEL_ISRAELI = {1: 1708, 2: 2484, 3: 4223, 4: 5217, 5: 6458, 6: 7452}


def validate(wage: float, year: int, insurance: float, month: int,
             region: str = None, housing_expense: float = None) -> list:
    """Blocking input problems. Each exists because the tool would otherwise return a
    confident, plausible, wrong number rather than an error."""
    problems = []
    if wage < 0:
        problems.append(f"wage is negative ({wage}).")
    elif wage == 0:
        problems.append("wage is zero. Supply the agreed wage, or omit --wage to use the minimum.")
    if insurance < 0:
        problems.append(f"medical insurance premium is negative ({insurance}).")
    if year < 0:
        problems.append(f"completed years is negative ({year}).")
    if month < 1:
        problems.append(f"month of employment must be 1 or more (got {month}).")
    if housing_expense is not None and housing_expense < 0:
        problems.append(f"housing expense is negative ({housing_expense}).")
    if (region is None) != (housing_expense is None):
        problems.append("--region and --housing-expense go together: the deduction is the actual "
                        "monthly housing expense, capped at the regional ceiling.")
    if wage > 200000:
        problems.append(f"wage of {wage} is implausible for this sector; check the units.")
    # month and completed years describe the same employment and must agree exactly: in month m
    # the worker has completed (m - 1) // 12 full years.
    if month >= 1 and year >= 0 and (month - 1) // 12 != year:
        problems.append(
            f"--month {month} and --completed-years {year} are inconsistent: in month {month} "
            f"the worker has completed {(month - 1) // 12} full year(s), not {year}.")
    return problems


def compute(wage: float, year: int, level: int, insurance: float, month: int = 12,
            region: str = None, housing_expense: float = None) -> dict:
    below_minimum = wage < MIN_WAGE_MONTHLY
    wage = max(wage, MIN_WAGE_MONTHLY)
    national_insurance = round(wage * NATIONAL_INSURANCE_RATE, 2)
    # The in-lieu-of-pension leg accrues only from month 7.
    pension = round(wage * PENSION_RATE, 2) if month >= PENSION_FIRST_MONTH else 0.0
    severance_reserve = round(wage * SEVERANCE_RESERVE_FRACTION, 2)
    # `year` is COMPLETED years, so the year being worked (and accrued) is year + 1.
    havraa_month = round(HAVRAA_PER_DAY * havraa_days(year + 1) / 12, 2)
    havraa_payable = year >= 1
    # The employer may recover part of the medical premium from the wage, subject to a cap.
    medical_deduction = round(min(insurance * MEDICAL_DEDUCTION_SHARE, MEDICAL_DEDUCTION_MAX), 2)
    net_insurance_cost = round(insurance - medical_deduction, 2)
    # Step 4a deductions the employer may recover from the wage, all inside the 25% cap. The
    # housing deduction is the actual expense, never more than the regional ceiling.
    housing_cap = HOUSING_CAP_PERMANENT[region] if region else 0.0
    accommodation_deduction = (round(min(housing_expense, housing_cap), 2)
                               if region else 0.0)
    housing_capped = bool(region) and housing_expense > housing_cap
    # The expense itself is a real employer cost; only the recovered part comes back from the wage.
    housing_cost = round(housing_expense, 2) if region else 0.0
    cap = round(wage * TOTAL_DEDUCTION_CAP_SHARE, 2)
    deductions_requested = round(medical_deduction + accommodation_deduction, 2)
    deductions_allowed = round(min(deductions_requested, cap), 2)
    capped = deductions_requested > cap
    # Only the medical share is already netted off the premium line; the rest reduces cost here.
    other_deductions = round(deductions_allowed - medical_deduction, 2)
    if other_deductions < 0:
        other_deductions = 0.0
    gross = round(wage + national_insurance + pension + severance_reserve
                  + havraa_month + net_insurance_cost + housing_cost - other_deductions, 2)
    offset = BENEFIT_BY_LEVEL.get(level, 0)
    net = round(gross - offset, 2)
    return {
        "wage": wage,
        "below_minimum_supplied": below_minimum,
        "month_of_employment": month,
        "national_insurance": national_insurance,
        "pension": pension,
        "pension_accruing": month >= PENSION_FIRST_MONTH,
        "severance_reserve": severance_reserve,
        "havraa_monthly_equiv": havraa_month,
        "havraa_payable_yet": havraa_payable,
        "accommodation_deduction": accommodation_deduction,
        "housing_cap": housing_cap,
        "housing_cost": housing_cost,
        "housing_capped": housing_capped,
        "deductions_requested": deductions_requested,
        "deductions_allowed": deductions_allowed,
        "deductions_capped": capped,
        "medical_insurance_premium": round(insurance, 2),
        "medical_deduction_from_wage": medical_deduction,
        "medical_insurance_net_cost": net_insurance_cost,
        "deduction_cap_25pct": round(wage * TOTAL_DEDUCTION_CAP_SHARE, 2),
        "gross_monthly_cost": gross,
        "nursing_benefit_offset": offset,
        "net_monthly_cost": net,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Estimate monthly employer cost of a foreign caregiver.")
    ap.add_argument("--wage", type=float, default=MIN_WAGE_MONTHLY, help="Agreed monthly wage (floored at minimum wage).")
    ap.add_argument("--completed-years", "--seniority-year", dest="completed_years",
                    type=int, default=1,
                    help="COMPLETED full years of employment. Use 0 during the first 12 months: "
                         "havraa is NOT yet payable then, but it accrues at the 5-day rate and is "
                         "paid retroactively to day one at the anniversary, so it is still costed. "
                         "1 means one full year completed. --seniority-year is a deprecated alias.")
    ap.add_argument("--month", type=int, default=None,
                    help="Month of employment (1 = the first month). The in-lieu-of-pension "
                         "6.5%% accrues only from month 7, so this changes the answer in the "
                         "first half-year. Must agree with --completed-years. Default: the last "
                         "month of the current year of employment.")
    ap.add_argument("--care-level", type=int, default=0, choices=[0, 1, 2, 3, 4, 5, 6], help="Bituach Leumi long-term-care level (0 = none).")
    ap.add_argument("--insurance", type=float, default=0.0, help="Monthly private medical-insurance premium.")
    ap.add_argument("--region", choices=sorted(HOUSING_CAP_PERMANENT),
                    help="Region for the housing-deduction ceiling in force from 1.9.2026 "
                         "(permanent building, utilities included). Use with --housing-expense.")
    ap.add_argument("--housing-expense", type=float, default=None,
                    help="The housing expense you actually incur or committed to for the worker "
                         "each month. The deduction is this amount, capped at the regional "
                         "ceiling. How this is measured in the family's own flat is unsettled; "
                         "get a labour lawyer's view before deducting above the pre-September "
                         "figures.")
    ap.add_argument("--utilities", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.month is None:
        args.month = 12 * max(args.completed_years, 0) + 12

    problems = validate(args.wage, args.completed_years, args.insurance, args.month,
                        args.region, args.housing_expense)
    if args.utilities:
        problems.append("--utilities was removed: the separate utilities deduction was repealed "
                        "on 1.9.2026 and utilities are now inside the housing ceiling.")
    if problems:
        print("Refusing to compute: the input would produce a confident wrong answer.",
              file=sys.stderr)
        for pr in problems:
            print(f"  - {pr}", file=sys.stderr)
        sys.exit(2)

    r = compute(args.wage, args.completed_years, args.care_level, args.insurance, args.month,
                region=args.region, housing_expense=args.housing_expense)
    print("Monthly employer cost estimate (shekels):")
    print(f"  Wage                         {r['wage']:>10.2f}")
    print(f"  National insurance           {r['national_insurance']:>10.2f}")
    print(f"  In lieu of pension           {r['pension']:>10.2f}"
          + ("" if r['pension_accruing'] else "   (not yet: starts month 7)"))
    print(f"  Severance reserve            {r['severance_reserve']:>10.2f}")
    print(f"  Havraa (monthly equivalent)  {r['havraa_monthly_equiv']:>10.2f}"
          + ("" if r['havraa_payable_yet'] else "   (accrued, not payable until 12 months)"))
    print(f"  Medical insurance premium    {r['medical_insurance_premium']:>10.2f}")
    print(f"    less permitted deduction  -{r['medical_deduction_from_wage']:>10.2f}")
    print(f"    net insurance cost         {r['medical_insurance_net_cost']:>10.2f}")
    if r['housing_cost']:
        print(f"  Housing expense (actual)     {r['housing_cost']:>10.2f}")
    if r['accommodation_deduction']:
        print(f"  less housing deduction       -{r['accommodation_deduction']:>10.2f}"
              + ("   (capped at the regional ceiling)" if r['housing_capped'] else ""))
        print("    WARNING: a ceiling on reimbursing ACTUAL expenses, months from 1.9.2026 only.")
        print("    Needs the worker's signed written consent; above the pre-September amounts get")
        print("    a labour lawyer's view first. Over-deducting is a criminal offence.")
    print(f"  --------------------------------------")
    print(f"  Gross monthly cost           {r['gross_monthly_cost']:>10.2f}")
    print(f"  Nursing-benefit offset      -{r['nursing_benefit_offset']:>10.2f}")
    print(f"  Net monthly cost             {r['net_monthly_cost']:>10.2f}")
    print()
    print(f"Havraa tariff used: {HAVRAA_PER_DAY} NIS/day, as of {HAVRAA_TARIFF_AS_OF}. It resets")
    print("annually and can be revised mid-year with RETROACTIVE effect, so re-read the source.")
    print("The in-lieu-of-pension and severance amounts are owed to the worker at the END of")
    print("employment, not paid monthly, and a foreign worker cannot be insured in an Israeli")
    print("pension fund, so nothing is withheld from the worker for it.")
    print(f"Wage deductions modelled here: {r['deductions_allowed']:.2f} of the 25% cap of "
          f"{r['deduction_cap_25pct']:.2f} NIS/month.")
    if r['deductions_capped']:
        print("  The requested deductions EXCEED the 25% cap and were reduced to it.")
    print("  This tool models only the medical and housing heads. Advances,")
    print("  board, union dues and debts share the SAME 25% cap, so headroom shown here is not")
    print("  clearance to deduct more. Over-deducting is a criminal offence.")
    print("National Insurance may NOT be deducted from a nursing caregiver at all, and a deduction")
    print("not taken in the month cannot be recovered retroactively.")
    if not r['havraa_payable_yet']:
        print("Havraa is ACCRUED above but not yet payable. It falls due once 12 months are")
        print("complete, and is then paid retroactively from the first day of work, so set it aside.")
    if r["below_minimum_supplied"]:
        print()
        print(f"NOTE: the wage supplied was BELOW the minimum wage of {MIN_WAGE_MONTHLY:.2f} and was")
        print("floored to it. Paying below minimum wage is unlawful; this is not a way to lower the cost.")
    print()
    print("Benefit offset uses the FOREIGN-caregiver column. The Israeli-caregiver column is")
    print("higher from level 3 up, and 6,458 appears in both at different levels.")
    if r['accommodation_deduction']:
        print()
        print(f"Housing ceiling used: {r['housing_cap']:.0f} NIS/month, for months from 1.9.2026 only")
        print("(utilities included). It caps a reimbursement of expenses ACTUALLY incurred, not a")
        print("flat sum, and how that is measured in the family's own flat is not settled. For")
        print("January to August 2026 the old half-rate table and 94.34 utilities line applied.")


if __name__ == "__main__":
    main()
