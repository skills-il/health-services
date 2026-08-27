# Changelog

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
