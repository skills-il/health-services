#!/usr/bin/env python3
"""Offline tests for build_calendar.py (standard library only).

Run: python3 test_build_calendar.py
Checks the schedule rules (cohort switch, 6-week visit, RSV by birth month,
HPV regional exception) and that the .ics output is structurally valid
RFC 5545: CRLF line endings, lines folded at 75 octets, balanced
BEGIN/END blocks, and the required VEVENT properties.
"""

import datetime as dt
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_calendar as bc  # noqa: E402

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)


def unfold(text):
    lines = text.split("\r\n")
    out = []
    for ln in lines:
        if ln.startswith(" ") and out:
            out[-1] += ln[1:]
        else:
            out.append(ln)
    return [ln for ln in out if ln]


def validate_ics(text):
    check(text.endswith("\r\n"), "ics must end with CRLF")
    check("\n" not in text.replace("\r\n", ""), "bare LF found in ics")
    for raw in text.split("\r\n"):
        check(len(raw.encode("utf-8")) <= 75, f"line longer than 75 octets: {raw[:40]}")
    lines = unfold(text)
    check(lines[0] == "BEGIN:VCALENDAR" and lines[-1] == "END:VCALENDAR", "calendar wrapper")
    stack = []
    events = []
    cur = None
    for ln in lines:
        if ln.startswith("BEGIN:"):
            stack.append(ln[6:])
            if ln == "BEGIN:VEVENT":
                cur = {}
        elif ln.startswith("END:"):
            check(stack and stack[-1] == ln[4:], f"unbalanced {ln}")
            if stack:
                stack.pop()
            if ln == "END:VEVENT":
                events.append(cur)
                cur = None
        elif cur is not None and stack[-1] == "VEVENT":
            name = ln.split(":", 1)[0].split(";", 1)[0]
            cur[name] = ln.split(":", 1)[1]
    check(not stack, "unclosed blocks")
    for need in ("VERSION:2.0", "PRODID:-//skills-il//israeli-parenting-companion//EN"):
        check(need in lines, f"missing {need}")
    uids = set()
    for ev in events:
        for prop in ("UID", "DTSTAMP", "DTSTART", "DTEND", "SUMMARY"):
            check(prop in ev, f"VEVENT missing {prop}")
        uids.add(ev.get("UID"))
        start = dt.datetime.strptime(ev["DTSTART"], "%Y%m%d").date()
        end = dt.datetime.strptime(ev["DTEND"], "%Y%m%d").date()
        check(end > start, "DTEND must be after DTSTART")
    check(len(uids) == len(events), "UIDs must be unique")
    return events


def items_for(birth, today="2026-11-17", **kw):
    return bc.build_items(dt.date.fromisoformat(birth), dt.date.fromisoformat(today), "en", **kw)


def find(items, key):
    return next(i for i in items if i["key"] == key)


def main():
    # Cohort born on/after 1.1.2025: MMRV 2 at 18 months, HepA 2 in grade 1.
    new = items_for("2025-01-01")
    check(("mmrv", "2/2") in find(new, "18m")["vaccines"], "new cohort MMRV2 at 18m")
    check(find(new, "24m")["vaccines"] == [], "new cohort no vaccine at 24m")
    check(find(new, "grade1")["vaccines"] == [("hepa", "2/2")], "new cohort HepA2 in grade 1")
    # Cohort born on/before 31.12.2024: HepA 2 at 24 months, MMRV 2 in grade 1.
    old = items_for("2024-12-31")
    check(("mmrv", "2/2") not in find(old, "18m")["vaccines"], "old cohort no MMRV2 at 18m")
    check(find(old, "24m")["vaccines"] == [("hepa", "2/2")], "old cohort HepA2 at 24m")
    check(find(old, "grade1")["vaccines"] == [("mmrv", "2/2")], "old cohort MMRV2 in grade 1")
    # 2-month visit is held at 6 weeks.
    check(find(new, "2m")["date"] == dt.date(2025, 2, 12), "2-month visit at 6 weeks")
    # Month arithmetic clamps to month end.
    check(bc.add_months(dt.date(2026, 1, 31), 1) == dt.date(2026, 2, 28), "month clamp")
    # RSV: born 1.9-31.3 in hospital (note on the birth row).
    winter = items_for("2026-03-14")
    check(any("in hospital" in n for n in find(winter, "birth")["notes"]), "RSV hospital note")
    # --current-grade derives the grade-1 year (school year starting September).
    with tempfile.TemporaryDirectory() as d2:
        rc = bc.main(["--birth-date", "2018-06-20", "--current-grade", "3", "--today", "2026-11-17",
                      "--format", "md", "--out-dir", d2])
        check(rc == 0 and "01/09/2027" in (Path(d2) / "checklist.md").read_text(encoding="utf-8"),
              "current grade 3 in 2026-27 puts grade 4 in September 2027")
    check(("rsv_hosp", "") in find(winter, "birth")["vaccines"], "RSV listed on the birth row")
    # RSV: born 1.4-31.8, rule text only, no computed season row or status.
    summer = items_for("2026-05-10")
    check(not any(i["key"] in ("rsv", "rota-deadline") for i in summer), "no computed RSV row")
    check(any("not in hospital" in n for n in find(summer, "birth")["notes"]), "RSV Tipat Halav rule on birth row")
    check(not any("until" in n.lower() or "ask now" in n.lower() for n in find(summer, "birth")["notes"]),
          "no RSV catch-up wording")
    check(not any(any("RSV" in n for n in i["notes"]) for i in items_for("2023-05-10")), "no RSV note before the program")
    # Items are sorted by date (dated items first).
    dated = [i["date"] for i in summer if i["date"]]
    check(dated == sorted(dated), "items sorted by date")
    # HPV regional exception.
    reg = items_for("2015-03-01", hpv_both_grade8=True, grade1_year=2021)
    check(not any(i["key"] == "grade7" for i in reg), "region: no grade 7 HPV")
    check(find(reg, "grade8")["vaccines"] == [("tdap", "1/1"), ("hpv", "1/2"), ("hpv", "2/2")],
          "region: both HPV in grade 8")
    # South/North districts: booster in grade 1, grade 2 keeps flu only.
    sn = items_for("2020-03-01", booster_grade1=True, grade1_year=2026)
    check(("tdap_ipv", "1/1") in find(sn, "grade1")["vaccines"], "south/north: booster in grade 1")
    check(find(sn, "grade2")["vaccines"] == [("flu", "1/1")], "south/north: grade 2 flu only")
    # Special education: flu in grades 1 to 6.
    se = items_for("2020-03-01", special_ed=True)
    check(all(("flu", "1/1") in find(se, f"grade{g}")["vaccines"] for g in range(1, 7)), "special-ed flu 1-6")
    # Preterm: hepatitis B dates are not fixed; iron note replaces the 4-month guide.
    pt = items_for("2026-09-20", preterm=True, due_date=dt.date(2026, 11, 25),
                   discharge_date=dt.date(2026, 11, 10))
    check(find(pt, "1m")["hepb_preterm"], "preterm: HepB rows flagged for the under-2-kg rule")
    check(find(pt, "1m")["in_hospital"] and find(pt, "2m")["in_hospital"], "preterm: in-hospital visits")
    check(any("discharge letter" in n for n in find(pt, "2m")["notes"]), "in-hospital vaccines: check letter")
    check(all(v[0] != "rota" for k in ("2m", "4m", "6m") for v in find(pt, k)["vaccines"])
          and all(find(pt, k)["rota_nurse"] for k in ("2m", "4m", "6m")), "preterm: rotavirus left to NICU team or nurse")
    check(not any(i["key"] == "rota-deadline" for i in pt), "preterm: no computed rotavirus deadline")
    early_home = items_for("2026-10-30", preterm=True, discharge_date=dt.date(2026, 11, 12))
    check(("rota", "1/3") in find(early_home, "2m")["vaccines"], "preterm home before 6 weeks: routine rotavirus")
    check(not any("call" in n.lower() and "rotavirus" in n.lower() for i in pt for n in i["notes"]),
          "preterm: no 'call right after discharge' instruction")
    # South/North booster exception applies only to the pre-2025 cohort (MoH page).
    sn_new = items_for("2025-02-01", booster_grade1=True)
    check(("tdap_ipv", "1/1") in find(sn_new, "grade2")["vaccines"], "booster exception not for 2025 cohort")
    check(any("iron" in n for n in find(pt, "4m")["notes"]) and find(pt, "4m")["guide"] is None,
          "preterm: iron note")
    # Olim: past items are labelled as before arrival.
    ol = items_for("2023-06-10", olim=True)
    check(all(i.get("olim") for i in ol if i["past"]), "olim: past items flagged")
    # Older child: past items before April 2025 do not list current-schedule doses.
    older = items_for("2019-05-10")
    check(find(older, "2m")["title"] == "2-month visit" and find(older, "2m")["old_schedule"],
          "pre-2022 2-month visit and old-schedule flag")
    # Past items are flagged and excluded from the .ics by default.
    check(find(winter, "birth")["past"] and not find(winter, "12m")["past"], "past flags")
    ics = bc.to_ics(winter, dt.date(2026, 3, 14), dt.date(2026, 11, 17), "he", "נועה")
    events = validate_ics(ics)
    check(len(events) == 6, f"expected 6 upcoming visit events, got {len(events)}")
    ics_all = bc.to_ics(winter, dt.date(2026, 3, 14), dt.date(2026, 11, 17), "en", None,
                        include_past=True)
    check(len(validate_ics(ics_all)) == 12, "include-past gives birth, first visit and 10 visits")
    # Twins: different names give different UIDs.
    a = bc.to_ics(winter, dt.date(2026, 3, 14), dt.date(2026, 11, 17), "en", "Noa")
    b = bc.to_ics(winter, dt.date(2026, 3, 14), dt.date(2026, 11, 17), "en", "Lior")
    uids = lambda t: {l for l in t.split("\r\n") if l.startswith("UID:")}
    check(not (uids(a) & uids(b)), "twins get distinct UIDs")
    # The notice comes first in every event description and in the table.
    check("DESCRIPTION:This calendar shows" in "".join(l.lstrip(" ") if l.startswith(" ") else "\n" + l
                                                      for l in a.split("\r\n")), "notice first in ics")
    check(bc.to_table(winter, "en").startswith("> This calendar shows"), "notice first in table")
    # Escaping of commas and semicolons.
    check(bc.ics_escape("a,b;c\\d\ne") == "a\\,b\\;c\\\\d\\ne", "text escaping")
    # CLI: invalid and future dates exit 2, valid run writes three files.
    check(bc.main(["--birth-date", "31/02/2026"]) == 2, "invalid date exits 2")
    check(bc.main(["--birth-date", "2030-01-01", "--today", "2026-11-17"]) == 2, "future exits 2")
    check(bc.main(["--birth-date", "2000-01-01", "--today", "2026-11-17"]) == 2, "18+ exits 2")
    with tempfile.TemporaryDirectory() as d:
        rc = bc.main(["--birth-date", "14.03.2026", "--today", "2026-11-17", "--out-dir", d])
        check(rc == 0, "valid run exits 0")
        for f in ("calendar.ics", "checklist.md", "table.md"):
            check((Path(d) / f).exists(), f"{f} written")
        validate_ics((Path(d) / "calendar.ics").read_bytes().decode("utf-8"))

    if FAILS:
        print("FAIL")
        for f in FAILS:
            print(" -", f)
        return 1
    print("PASS: all calendar checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
