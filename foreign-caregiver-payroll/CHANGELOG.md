# Changelog

## 1.2.0 (2026-10-19)

### Corrected

- **Housing deductions follow the regulations in force from 1.9.2026.** The amendment published on
  16.7.2026 replaced the employer-owned half rate and the separate 94.34 NIS utilities line with one
  regional ceiling per building type (Jerusalem 1,095, Tel Aviv 1,257, Haifa 999, Centre 1,030,
  South 999, North 999 NIS for a permanent building), utilities included. The ceiling caps a
  reimbursement of expenses actually incurred; the skill now says that how this is measured in the
  family's own flat is unsettled and routes a larger deduction to a labour lawyer. The old table is
  kept for back-pay only.
- **Havraa days are read by the year of employment being worked, not by completed years.** A worker
  with one completed year accrues 6 days, not 5. The old keying under-reserved one day at every
  band edge, in the prose, the calculator and the checker.
- **Nursing-benefit amounts updated to 01.08.2026** in both columns (foreign caregiver 1,708 to
  6,458; Israeli caregiver 1,708 to 7,452). The 6,448 collision is now 6,458.
- **Annual leave is counted by calendar year**, as the Annual Leave Law's work year starts on 1
  January: a mid-year starter moves up a row every January, ahead of her anniversary.
- Housing guidance now says a higher deduction needs the worker's fresh written consent to the new
  amount, that a rented flat has a measurable expense, and that the actual expense must be
  documented at any amount.
- The income-tax bullet no longer calls National Insurance "the main statutory deduction"; it is
  the employer's own cost and is never deducted from a nursing caregiver.
- The description no longer opens with a "legal advice" clause; it opens with "Not a binding
  payroll calculation".

### Calculator

- `--region` now takes the 1.9.2026 ceiling and requires `--housing-expense`, the actual monthly
  expense; the deduction is that expense capped at the ceiling. `--utilities` was removed and now
  refuses with an explanation. The stated housing expense is now counted as a cost before the
  recovered deduction, so the total can no longer fall below the wage. Havraa uses the days of the
  year being worked. `--month` must now agree exactly with `--completed-years` (the old check let a
  full year of mismatch through, and the defaults contradicted each other); it defaults to the last
  month of the current year.

### Checker (foreign-caregiver-cost)

- Havraa no longer zero in year one and no longer one day short at band edges; benefit levels
  updated; a "past the sixth month" input applies the 6.5% leg only from month 7 (always once a
  year is complete); the leave lines were removed (leave runs on calendar years, which the tool
  cannot see) and are now a caveat; stale goldens that failed the tool's own verify gate replaced.

## 1.1.0 (2026-08-27)

### Corrected

- **Recuperation pay (havraa) is no longer treated as a zero-cost item in year one.** It becomes
  payable only after 12 completed months, but is then paid retroactively from the worker's first
  day, so the liability accrues from month one and must be reserved monthly. The bundled
  calculator accrues it too, labelled "accrued, not payable until 12 months".
- **Dismissal shortly before the first anniversary no longer reads as a way to cap exposure at
  12.5%.** The Severance Pay Law presumes such a dismissal was made to avoid severance, so the
  family should reserve on the severance row.
- **Annual leave now shows the NET column beside the gross one** (14 days against 16 for years
  1-5). Leave redemption runs on the net figure.
- The permitted-deduction table's income-tax row no longer asserts that tax is generally nil.

### Added

- A **legal notice** section in both languages, immediately after the title, and a short legal
  clause opening every description. The skill reaches a shekel conclusion about the reader's own
  household, so it carries the labour-law notice.
- **Four further deduction heads** (advances, board, union dues and disciplinary fines) and the
  debts row's quarter-of-wage sub-cap and undisputed-balance rule on the final salary.
- The **two-week deadline** to register as an employer with Bituach Leumi.
- The duty to provide accommodation for **at least seven days after employment ends**.
- What happens on the **patient's death**: the worker is treated as dismissed, and the money comes
  out of the estate, whose bank account may be frozen pending a probate or inheritance order.
- The published figure for a **worked weekly rest day or holiday** (439.73 NIS at minimum wage),
  which previously the reader was told to go and look up.
- Leave redemption's three-year reach-back.

### Removed

- An uncited claim that labour-court global supplements run **higher** than the 20% figure people
  quote. No primary source supports a band, so the skill now states that a court may award one on
  the facts and that no percentage can be quoted in advance.

### Calculator

- New `--region` and `--utilities` flags apply the accommodation and utility deductions against
  the 25% cap, and the output names the heads it does not model so headroom is not read as
  clearance to deduct more.
- Refuses an implausible wage, and refuses a month and seniority that contradict each other in
  either direction.

## 1.0.1 (2026-07-21)

- Evidence-integrity pass: all cited figures re-verified against live sources.
