#!/usr/bin/env python3
"""Build a personal Tipat Halav + routine-vaccine calendar for an Israeli child.

Offline only: standard library, no network, no subprocess. Works in a sandbox
with no internet access.

Every age, vaccine and visit below is taken from the Israeli Ministry of Health
(MoH) pages listed in SOURCES. Nothing here is medical advice: the script
places the PUBLISHED routine schedule on a calendar. It never decides whether a
child should be vaccinated, never gives a dose, and never computes catch-up
intervals. Those decisions belong to the Tipat Halav nurse or the doctor.

Usage:
  python3 build_calendar.py --birth-date 2026-03-14 --name "Noa" --lang he --out-dir ./noa
  python3 build_calendar.py --birth-date 14/03/2026 --format table
  python3 build_calendar.py --birth-date 2026-09-20 --preterm --due-date 2026-11-25 \
      --discharge-date 2026-11-10
  python3 build_calendar.py --birth-date 2020-03-01 --grade1-year 2026 --booster-grade1

Outputs (--format all, the default): calendar.ics, checklist.md, table.md
Exit codes: 0 ok, 2 invalid input.
"""

import argparse
import calendar as _cal
import datetime as dt
import hashlib
import sys
from pathlib import Path

SCHEDULE_VERSION = {"he": "לוח חיסוני השגרה של משרד הבריאות, ספטמבר 2026 (נבדק 17/11/2026)",
                    "en": "MoH routine schedule, September 2026 (checked 17/11/2026)"}

# Birth-cohort switch (MoH table footnotes 2 and 3, measles page):
# born 1.1.2025 or later: MMRV dose 2 at 18 months, hepatitis A dose 2 in grade 1.
# born 31.12.2024 or earlier: hepatitis A dose 2 at 24 months, MMRV dose 2 in grade 1.
COHORT_SWITCH = dt.date(2025, 1, 1)
# Since 3.4.22 the 2-month vaccines are given at 6 weeks ("until further notice").
SIX_WEEK_FROM = dt.date(2022, 4, 3)
# Past items before this date may follow an older schedule (oral polio stopped
# March 2025), so the checklist does not list current-schedule doses for them.
CURRENT_SCHEDULE_FROM = dt.date(2025, 4, 1)

SOURCES = [
    ("Tipat Halav visit plan (MoH)",
     "https://me.health.gov.il/parenting/raising-children/infant-and-child-development/tipat-halav/tipat-halav-schedule/"),
    ("Routine vaccine schedule (MoH)",
     "https://me.health.gov.il/parenting/raising-children/immunization-schedule/babies-immunization-schedule/"),
    ("Routine schedule table, September 2026 (MoH PDF)",
     "https://www.gov.il/BlobFolder/policy/luah/he/files_publications_units_epidemiology_vaccine_guidelines_120_LUAH.pdf"),
    ("RSV immunization by birth month (MoH)",
     "https://me.health.gov.il/parenting/raising-children/immunization-schedule/children-vaccines/rsv-vaccine-beyfortus/"),
    ("School vaccines (MoH)",
     "https://me.health.gov.il/parenting/raising-children/immunization-schedule/vaccine-schedule-6-to-18-years/"),
    ("Preterm infant vaccination (MoH)",
     "https://me.health.gov.il/parenting/raising-children/infant-and-child-development/prematurity/preterm-infant-vaccination/"),
    ("Measles: second dose brought forward (MoH)",
     "https://me.health.gov.il/parenting/raising-children/common-childhood-diseases-and-symptoms/viral-diseases/measles/"),
]

VAX = {
    "hepb": {"he": "צהבת B (דלקת כבד B)", "en": "Hepatitis B"},
    "penta": {"he": "מחומש (DTaP-Hib-IPV)", "en": "5-in-1 (DTaP-Hib-IPV)"},
    "rota": {"he": "רוטה", "en": "Rotavirus"},
    "pcv": {"he": "פנאומוקוקוס", "en": "Pneumococcal"},
    "mmrv": {"he": "החיסון המרובע (MMRV)", "en": "MMRV (measles, mumps, rubella, varicella)"},
    "hepa": {"he": "צהבת A", "en": "Hepatitis A"},
    "tdap_ipv": {"he": "דחף דיפתריה, טטנוס, שעלת ופוליו",
                 "en": "Diphtheria, tetanus, pertussis and polio booster"},
    "tdap": {"he": "דחף דיפתריה, טטנוס ושעלת", "en": "Diphtheria, tetanus and pertussis booster"},
    "flu": {"he": "שפעת", "en": "Influenza (flu)"},
    "hpv": {"he": "פפילומה (HPV)", "en": "HPV (papilloma)"},
    "rsv_hosp": {"he": "RSV (בבית החולים, לנולדים 1.9 עד 31.3)", "en": "RSV (in hospital, for births 1.9 to 31.3)"},
}

# Development items: verbatim MoH Hebrew; English is a translation.
DEV = {
    "2m": {"he": "מעקב במבט אחרי עצם נע, השמעת קולות בתגובה לקולות שנשמיע, חיוך כתגובה לחיוך שלנו והרמת ראש בשכיבה על הבטן.",
           "en": "Follows a moving object with the eyes, makes sounds in response to sounds, smiles back, lifts the head when lying on the tummy."},
    "4m": {"he": "מעקב במבט בקו אנכי, תגובה לקולות ולצלילים, תגובה בהנאה לקול ולדמות אדם, השמעת קולות מגוונים (כולל עיצורים), הבאת ידיים לקו האמצע, אחיזה והושטה של חפץ, הרמת ראש ובית חזה בשכיבה על הבטן.",
           "en": "Follows vertically with the eyes, reacts to voices and sounds, reacts with pleasure to a voice and a face, makes varied sounds (including consonants), brings hands to the midline, reaches for and grasps an object, lifts head and chest on the tummy."},
    "6m": {"he": "העברת חפץ מיד ליד, השמעת הברות חוזרות, רתיעה מזרים והתהפכות מהגב לבטן ומהבטן לגב.",
           "en": "Passes an object from hand to hand, repeats syllables, is wary of strangers, rolls back to tummy and tummy to back."},
    "9m": {"he": "הקשת חפצים זה בזה כמשחק, זחילה, השמעת קולות בדו-שיח, תגובה לקריאה בשם, חיקוי מחוות, אכילה עצמאית, תפיסת צבת, הבנת הוראות פשוטות, מעבר עצמאי לישיבה, אמירת מילה אחת או השמעת קול עם משמעות.",
           "en": "Bangs objects together in play, crawling, back-and-forth babbling, responds to own name, imitates gestures, self-feeding, pincer grasp, understands simple instructions, gets to sitting alone, says one word or a meaningful sound."},
    "12m": {"he": "הבעת רצון במחוות או במילים, יצירת קשר עין והדדיות במשחק משותף, קימה לעמידה בתמיכה, הליכה בתמיכה, הצבעה על חפצים מוכרים לפי בקשה, אמירת 3-2 מילים, הנחת קובייה בתוך כוס.",
            "en": "Shows wants with gestures or words, eye contact and turn-taking in shared play, pulls to stand with support, walks with support, points to familiar objects on request, says 2 to 3 words, puts a block in a cup."},
    "18m": {"he": "הכרה של איבר אחד בגוף, הליכה ללא עזרה, עלייה במדרגות עם עזרה, אכילה עצמאית בכפית, בניית מגדל קוביות, כיווץ והבלטת שפתיים כדי לתת נשיקה, אוצר מילים של יותר מ-10 מילים, משחק פונקציונלי (כמו הסעת מכונית), יוזמה לאינטראקציה או למשחק הדדי.",
            "en": "Knows one body part, walks without help, climbs stairs with help, eats with a spoon, builds a block tower, puckers lips to kiss, more than 10 words, functional play (like pushing a car), starts interaction or shared play."},
    "24m": {"he": "דיבור המכוון למטרות תקשורת, הבנת פעולות ללא מחווה מלווה, כינוי חפצים בשם, צירוף של 2 מילים לפחות למשפט, ריצה ללא נפילות, עלייה וירידה במדרגות בתמיכת מעקה, השתתפות בפעילויות יומיום, חיקוי ציור של קווים אופקיים, מאונכים ומעוגלים, משחק סימבולי (למשל, השכבת בובה לישון).",
            "en": "Talks to communicate, understands actions without a gesture, names objects, joins at least 2 words, runs without falling, up and down stairs holding a rail, joins daily routines, copies horizontal, vertical and round lines, pretend play (for example putting a doll to sleep)."},
    "4y": {"he": "עמידה על רגל אחת, העתקת ריבוע, ספירה עד 3, הכרה של לפחות 3 מילות יחס, דיבור מובן, משחק עם חברים באותו הגיל, התלבשות עצמאית, אכילה בעזרת כף ומזלג.",
           "en": "Stands on one foot, copies a square, counts to 3, knows at least 3 prepositions, speech others understand, plays with peers, dresses alone, eats with spoon and fork."},
    "5y": {"he": "תיאור תמונה תוך שימוש בפעלים בזמנים נכונים, מענה על שאלות התמצאות, קפיצה על רגל אחת, הליכה עקב בצד אגודל, ציור דמות אדם, העתקת צורות גאומטריות ומשחק עם חברים באותו הגיל.",
           "en": "Describes a picture using correct verb tenses, answers orientation questions, hops on one foot, heel-to-toe walk, draws a person, copies geometric shapes, plays with peers."},
}

# Guidance reminders per visit (no doses, ever).
GUIDE = {
    "first": {"he": "האחות עוברת על מכתב השחרור ומדריכה על האכלה, שינה, בטיחות, התמודדות עם בכי ומתן ויטמין D. אפשר לשאול כאן גם על משכב הלידה.",
              "en": "The nurse goes over the discharge letter and covers feeding, sleep, safety, crying and vitamin D. You can ask about your own postpartum recovery too."},
    "1m": {"he": "ויטמין D ניתן מלידה ועד גיל שנה. את הכמות נותנת האחות.",
           "en": "Vitamin D is given from birth to age 1. The nurse gives the amount."},
    "2m": {"he": "שאלו על שפה ומשחק, על בכי ועל המשך ויטמין D.",
           "en": "Ask about language and play, crying, and continuing vitamin D."},
    "4m": {"he": "תוסף ברזל מתחיל בגיל 4 חודשים מלא וממשיך עד גיל שנה וחצי. את הכמות נותנת האחות.",
           "en": "An iron supplement starts at 4 completed months and continues to 18 months. The nurse gives the amount."},
    "6m": {"he": "במפגש הזה מעלים את המינון של תוסף הברזל (האחות מסבירה). סביב חצי שנה מתחילים מזון משלים לפי סימני מוכנות.",
           "en": "The iron dose goes up at this visit (the nurse explains). Solid foods start around 6 months, by readiness signs."},
    "9m": {"he": "מקבלים הפניה לספירת דם לקראת המפגש של גיל שנה.",
           "en": "You get a referral for a blood count before the 12-month visit."},
    "12m": {"he": "מפסיקים ויטמין D וממשיכים תוסף ברזל עד גיל שנה וחצי.",
            "en": "Vitamin D stops; the iron supplement continues to 18 months."},
    "18m": {"he": "מפסיקים תוסף ברזל. שאלו על גמילה מחיתולים.",
            "en": "The iron supplement stops. Ask about toilet training."},
    "24m": {"he": "שאלו על תזונה, שינה, בטיחות וגמילה מחיתולים.",
            "en": "Ask about nutrition, sleep, safety and toilet training."},
    "4y": {"he": "במפגש נערכת בדיקת חדות ראייה.",
           "en": "A visual acuity check is done at this visit."},
    "5y": {"he": "לקראת כיתה א' בודקים מיומנויות מוטוריות, בשלות קוגניטיבית ובשלות רגשית וחברתית.",
           "en": "Before grade 1 the nurse checks motor skills, cognitive readiness and emotional and social readiness."},
}

VISIT_LABEL = {
    "birth": {"he": "לידה (בבית החולים)", "en": "Birth (in hospital)"},
    "first": {"he": "מפגש ראשון בטיפת חלב", "en": "First Tipat Halav visit"},
    "first_book": {"he": "לקבוע מפגש ראשון בטיפת חלב (כיומיים אחרי השחרור)",
                   "en": "Book the first Tipat Halav visit (about 2 days after discharge)"},
    "1m": {"he": "מפגש גיל חודש", "en": "1-month visit"},
    "2m": {"he": "מפגש גיל חודשיים (מתקיים בגיל 6 שבועות)", "en": "2-month visit (held at 6 weeks)"},
    "2m_old": {"he": "מפגש גיל חודשיים", "en": "2-month visit"},
    "4m": {"he": "מפגש גיל 4 חודשים", "en": "4-month visit"},
    "6m": {"he": "מפגש גיל חצי שנה", "en": "6-month visit"},
    "9m": {"he": "מפגש גיל 9 חודשים", "en": "9-month visit"},
    "12m": {"he": "מפגש גיל שנה", "en": "12-month visit"},
    "18m": {"he": "מפגש גיל שנה וחצי", "en": "18-month visit"},
    "24m": {"he": "מפגש גיל שנתיים", "en": "24-month visit"},
    "4y": {"he": "מפגש גיל 4 שנים", "en": "4-year visit"},
    "5y": {"he": "מפגש גיל 5 שנים", "en": "5-year visit"},
}

# (key, offset kind, offset value, physician exam?)
VISITS = [
    ("1m", "months", 1, False),
    ("2m", "days", 42, True),
    ("4m", "months", 4, False),
    ("6m", "months", 6, False),
    ("9m", "months", 9, True),
    ("12m", "months", 12, False),
    ("18m", "months", 18, True),
    ("24m", "months", 24, True),
    ("4y", "months", 48, False),
    ("5y", "months", 60, False),
]

T = {
    "title": {"he": "לוח טיפת חלב וחיסוני שגרה", "en": "Tipat Halav and routine vaccine calendar"},
    "child": {"he": "הילד/ה", "en": "Child"},
    "born": {"he": "תאריך לידה", "en": "Birth date"},
    "cohort_new": {"he": "תאריך הלידה הוא 1.1.2025 או אחריו: מנה שנייה של המרובע בגיל שנה וחצי, מנה שנייה של צהבת A בכיתה א'.",
                   "en": "Born on or after 1.1.2025: MMRV dose 2 at 18 months, hepatitis A dose 2 in grade 1."},
    "cohort_old": {"he": "תאריך הלידה הוא עד 31.12.2024: מנה שנייה של צהבת A בגיל שנתיים, מנה שנייה של המרובע בכיתה א'.",
                   "en": "Born on or before 31.12.2024: hepatitis A dose 2 at 24 months, MMRV dose 2 in grade 1."},
    "date": {"he": "תאריך", "en": "Date"},
    "what": {"he": "מה", "en": "What"},
    "vaccines": {"he": "חיסונים", "en": "Vaccines"},
    "no_vax": {"he": "אין חיסון שגרה במפגש הזה", "en": "No routine vaccine at this visit"},
    "old_schedule": {"he": "לבדוק בפנקס (הלוח שהיה אז בתוקף יכול להיות שונה)",
                     "en": "Check the booklet (the schedule in force then may have differed)"},
    "doctor": {"he": "כולל בדיקת רופא", "en": "Includes a physician's examination"},
    "dev": {"he": "מה האחות בודקת בהתפתחות (לפי משרד הבריאות)", "en": "What the nurse checks in development (per the Ministry of Health)"},
    "ask": {"he": "מה לשאול / להכין", "en": "What to ask / prepare"},
    "status": {"he": "סטטוס", "en": "Status"},
    "past": {"he": "עבר: בודקים בפנקס החיסונים. אם משהו חסר, פונים לאחות טיפת חלב לגבי השלמה.",
             "en": "Past: check the vaccine booklet. If something is missing, ask the Tipat Halav nurse about catching up."},
    "past_olim": {"he": "לפני העלייה: לא יופיע בפנקס ישראלי. מביאים את התיעוד מחו\"ל לאחות, והיא קובעת מה להשלים.",
                  "en": "Before arrival: not in an Israeli booklet. Bring the foreign record to the nurse, who decides what to complete."},
    "in_hospital": {"he": "בתאריך הזה התינוק עדיין באשפוז לפי תאריך השחרור. ההנחיות במכתב השחרור קובעות את ההמשך.",
                    "en": "The baby is still in hospital on this date, per the discharge date. The discharge letter sets what happens next."},
    "around": {"he": "בסביבות התאריך. קובעים תור בתחנה.", "en": "Around this date. Book with your station."},
    "first_visit": {"he": "קובעים תור לטיפת חלב עוד בזמן האשפוז, ליומיים אחרי השחרור מבית החולים. מביאים את מכתב השחרור, פנקס חיסונים, חיתול בד, חיתולים ובגדים להחלפה, ותמ\"ל ובקבוק אם לא מניקים. המפגש הראשון נמשך כשעה.",
                    "en": "Book the Tipat Halav visit while still in hospital, for about 2 days after discharge. Bring the discharge letter, vaccine booklet, a cloth diaper, spare diapers and clothes, and formula and a bottle if not breastfeeding. The first visit takes about an hour."},
    "hepb_birth": {"he": "המנה הראשונה של צהבת B ניתנת אחרי הלידה, בבית החולים.",
                   "en": "The first hepatitis B dose is given after birth, in hospital."},
    "rsv_hospital": {"he": "RSV: לפי משרד הבריאות, מי שנולדו בין 1.9 ל-31.3 מקבלים את החיסון בבית החולים לפני השחרור. בודקים בפנקס או במכתב השחרור. לפי משרד הבריאות, תינוקות שהיו אמורים לקבל את החיסון בבית החולים ולא חוסנו יכולים להתחסן בטיפת חלב במסגרת הביקורים השגרתיים; על כל שאלה שואלים את אחות טיפת חלב.",
                     "en": "RSV: per the Ministry of Health, babies born between 1.9 and 31.3 get it in hospital before discharge. Check the booklet or the discharge letter. Per the Ministry of Health, babies who should have had it in hospital and did not can get it at Tipat Halav during the routine visits; ask the Tipat Halav nurse about anything else."},
    "rsv_tipat_rule": {"he": "RSV: לפי משרד הבריאות, מי שנולדו בין 1.4 ל-31.8 מקבלים את החיסון בטיפת חלב, בסוף הקיץ ובתחילת הסתיו, לפני עונת ה-RSV, ולא בבית החולים. בטבלת משרד הבריאות חודשי החיסון בטיפת חלב הם ספטמבר עד 31 במרץ. בודקים בפנקס, ועל המועד שואלים את אחות טיפת חלב.",
                       "en": "RSV: per the Ministry of Health, babies born between 1.4 and 31.8 get it at Tipat Halav at the end of summer or start of autumn, before the RSV season, not in hospital. The MoH table gives the Tipat Halav months as September to 31 March. Check the booklet and ask the Tipat Halav nurse about timing."},
    "school": {"he": "חיסוני בית ספר (אחות בית הספר)", "en": "School vaccines (school nurse)"},
    "school_note": {"he": "בית הספר קובע את התאריך ומבקש את פנקס החיסונים כשבועיים לפני. הסתייגות כותבים בהצהרת הבריאות.",
                    "en": "The school sets the date and asks for the vaccine booklet about two weeks before. Any reservation goes in the health declaration."},
    "school_undated": {"he": "כדי להכניס את חיסוני בית הספר ללוח, מריצים שוב עם --grade1-year (השנה שבה הילד עולה לכיתה א').",
                       "en": "To put school vaccines on the calendar, run again with --grade1-year (the year the child starts grade 1)."},
    "grade": {"he": "כיתה", "en": "Grade"},
    "school_reminder": {"he": "תזכורת לתחילת שנת הלימודים", "en": "Reminder at the start of the school year"},
    "hpv_region": {"he": "במחוז אשקלון ובנפת צפת שתי מנות הפפילומה ניתנות בכיתה ח', כחצי שנה זו מזו.",
                   "en": "In the Ashkelon district and the Tzfat sub-district both HPV doses are given in grade 8, about half a year apart."},
    "booster_region": {"he": "במחוזות דרום וצפון של משרד הבריאות חיסון הדחף נגד דיפתריה, טטנוס, שעלת ופוליו ניתן בכיתה א' ולא בכיתה ב' (לפי אתר המשרד, לילדים שנולדו לפני 1.1.2025).",
                       "en": "In the MoH South and North districts the diphtheria, tetanus, pertussis and polio booster is given in grade 1, not grade 2 (per the MoH site, for children born before 1.1.2025)."},
    "booster_new_cohort": {"he": "באתר משרד הבריאות החריג של מחוזות דרום וצפון מופיע רק לילדים שנולדו לפני 1.1.2025, ולכן הלוח משאיר את הדחף בכיתה ב'. כדאי לוודא מול אחות בית הספר.",
                           "en": "On the MoH site the South and North district exception appears only for children born before 1.1.2025, so this calendar keeps the booster in grade 2. Confirm with the school nurse."},
    "region_hint": {"he": "במחוזות דרום וצפון חיסון הדחף של כיתה ב' ניתן כבר בכיתה א'. אם לא ברור באיזה מחוז אתם, שאלו את אחות בית הספר.",
                    "en": "In the South and North districts the grade-2 booster is given in grade 1. If you are not sure of your district, ask the school nurse."},
    "school_screen": {"he": "שירותי הבריאות בבית הספר לכיתות א' עד ט' כוללים גם בדיקות סינון (ראייה, שמיעה והערכת גדילה) ושירותי בריאות השן. התוצאות מגיעות להורים.",
                      "en": "The school health service for grades 1 to 9 also includes screening (vision, hearing and growth assessment) and dental services. Results go to the parents."},
    "sped_flu": {"he": "בחינוך המיוחד השפעת ניתנת בכיתות א' עד ו'.", "en": "In special education, flu is given in grades 1 to 6."},
    "flu_note": {"he": "שפעת: משרד הבריאות ממליץ על חיסון שנתי מגיל 6 חודשים. הוא ניתן בקופת החולים לקראת החורף, ובכיתות ב' עד ד' גם בבית הספר.",
                 "en": "Flu: the Ministry of Health recommends a yearly shot from 6 months. It is given at the kupah before winter, and in grades 2 to 4 also at school."},
    "measles_early": {"he": "חצבת: למי שגר ביישוב עם התפרצות פעילה, מבקר בו או נוסע לחו\"ל, משרד הבריאות ממליץ על מנה מוקדמת נוספת בגיל 6 עד 11 חודשים, בנוסף ל-2 מנות השגרה. בודקים מול טיפת חלב מה בתוקף.",
                      "en": "Measles: for anyone living in or visiting a locality with an active outbreak, or travelling abroad, the Ministry of Health recommends an extra early dose at 6 to 11 months, on top of the 2 routine doses. Check with Tipat Halav what currently applies."},
    "measles_dose2": {"he": "חצבת: ילדים מעל גיל שנה שקיבלו מנה אחת בלבד, וגרים ביישוב עם התפרצות, מבקרים בו או נוסעים לחו\"ל, מקדימים את המנה השנייה (משרד הבריאות, עדכון נובמבר 2026).",
                      "en": "Measles: children over age 1 with only one dose who live in or visit an outbreak locality, or travel abroad, bring the second dose forward (Ministry of Health, November 2026 update)."},
    "preterm_head": {"he": "פג (נולד לפני שבוע 37)", "en": "Preterm (born before week 37)"},
    "preterm_vax": {"he": "חיסונים ניתנים לפי הגיל הכרונולוגי (מתאריך הלידה), עם חריגים. רוטה: לפי משרד הבריאות, תינוק שעדיין מאושפז בגיל חודשיים מקבל את המנה הראשונה אחרי השחרור, ואת המנה הראשונה אפשר לקבל רק עד גיל 14 שבועות ו-6 ימים. את המועד קובעים צוות הפגייה או האחות. צהבת B: לפג במשקל מתחת ל-2 ק\"ג הסדרה מתחילה בשחרור, במשקל 2 ק\"ג או בגיל חודש, המוקדם מביניהם; המנה השנייה חודש אחרי הראשונה, ומנת הדחף 5 חודשים אחרי השנייה. אם האם נשאית של צהבת B, מנה שניתנה בלידה לתינוק מתחת ל-2 ק\"ג לא נספרת. את התאריכים האלה קובעת האחות.",
                    "en": "Vaccines go by chronological age (from the birth date), with exceptions. Rotavirus: per the Ministry of Health, a baby still in hospital at 2 months gets dose 1 after discharge, and dose 1 can be given only up to age 14 weeks and 6 days. The NICU team or the nurse sets the timing. Hepatitis B: for a preterm baby under 2 kg the series starts at discharge, 2 kg or 1 month of age, whichever comes first; dose 2 one month after dose 1, the booster 5 months after dose 2. If the mother is a hepatitis B carrier, a birth dose given to a baby under 2 kg does not count. The nurse sets these dates."},
    "preterm_iron": {"he": "לפי משרד הבריאות, רוב הפגים מתחילים תוסף ברזל כבר מגיל שבועיים, והכמות נקבעת לפי משקל הגוף על ידי אחות טיפת חלב. מכתב השחרור מהפגייה קובע את התזונה ואת תדירות המעקב.",
                     "en": "Per the Ministry of Health, most preterm babies start an iron supplement from 2 weeks of age, with the amount set by body weight by the Tipat Halav nurse. The NICU discharge letter sets feeding and follow-up frequency."},
    "preterm_dev": {"he": "בבדיקות ההתפתחות מתחשבים בגיל המתוקן, בעיקר בשנה הראשונה (ואצל פגים קטנים מאוד עד גיל 3, לפי מכבי). עקומות הגדילה נקראות לפי הגיל המתוקן (משרד הבריאות). האחות מחליטה איך לקרוא את הבדיקה.",
                    "en": "Developmental checks take corrected age into account, mainly in the first year (up to age 3 for very small preemies, per Maccabi). Growth curves are read by corrected age (Ministry of Health). The nurse decides how to read each check."},
    "hosp_vax": {"he": "בודקים במכתב השחרור אם החיסונים של המפגש הזה ניתנו באשפוז, ועל כל מה שלא מופיע שם שואלים את צוות הפגייה או את אחות טיפת חלב.",
                 "en": "Check the discharge letter for this visit's vaccines, and ask the NICU team or the Tipat Halav nurse about anything not listed."},
    "rota_preterm_label": {"he": "רוטה (פג: המנה והמועד נקבעים על ידי צוות הפגייה או האחות)", "en": "Rotavirus (preterm: dose and timing set by the NICU team or the nurse)"},
    "hepb_preterm": {"he": "פג מתחת ל-2 ק\"ג: מועדי צהבת B נקבעים על ידי האחות", "en": "Preterm under 2 kg: hepatitis B dates are set by the nurse"},
    "corrected": {"he": "גיל מתוקן בתאריך הזה", "en": "Corrected age on this date"},
    "olim_head": {"he": "ילד שעלה מחו\"ל", "en": "Child who arrived from abroad"},
    "olim_notes": {"he": [
        "לא מחכים למפגש הבא לפי הגיל: עד גיל 6 נרשמים עכשיו לתחנת טיפת חלב. תחנות של משרד הבריאות נותנות שירות לכולם, בלי תלות בקופת החולים.",
        "מביאים את התיעוד מחו\"ל. מצב החיסונים נקבע לפי תיעוד רפואי או מידע מהימן, ובלי תיעוד או כשיש ספק מתייחסים לילד כמי שלא חוסן.",
        "גיל בית ספר: עד כיתה ט' ההשלמה דרך שירותי הבריאות בבית הספר, ללא תשלום. מכיתה י' ועד גיל 18 בלשכות הבריאות, תור דרך 5400*.",
        "האחות, לא הלוח הזה, קובעת אילו מנות מחו\"ל נחשבות ומה להשלים.",
    ], "en": [
        "Do not wait for the next age-based visit: under 6, register with a Tipat Halav station now. MoH stations serve everyone, regardless of kupah.",
        "Bring the foreign record. Vaccine status is set from medical records or reliable information; with no record, or a doubtful one, the child is treated as unvaccinated.",
        "School age: up to grade 9 catch-up is through the school health service, free. From grade 10 to age 18 at the health bureaus, booked via *5400.",
        "The nurse, not this calendar, decides which foreign doses count and what to complete.",
    ]},
    "redflags_head": {"he": "מתי לא לחכות למפגש הבא", "en": "When not to wait for the next visit"},
    "redflags": {"he": [
        "קושי להעיר, חוסר תגובה, בלבול משמעותי, פרכוסים, פריחה אדומה או סגולה שלא נעלמת בלחיצה, קשיי נשימה או עור חיוור ומנומר: מיד למיון או 101.",
        "עד גיל חודשיים: חום של 38 ומעלה מחייב פנייה מיידית לחדר מיון, גם בלי תסמינים נוספים.",
        "מגיל חודשיים עד 3 חודשים: חום של 38 ומעלה מחייב בדיקה רפואית דחופה. עם רפיון, ישנוניות חריגה או ירידה בערנות: מיד למיון.",
        "חום מתחת ל-36 אצל תינוק: מחממים (בגד נוסף, שמיכה, קרוב לגוף). אם זה לא עוזר והתינוק נראה חולה, פונים לבדיקה.",
        "צהבת בולטת, למשל בלובן העיניים: לא מחכים למועד המעקב, מגיעים מיד לבדיקה.",
        "מתחת לגיל שנה: יותר מ-60 נשימות בדקה, שקיעה של העור בין הצלעות או נשימה בעזרת כנפי האף: בדיקה מיידית או מיון.",
        "הקאות דמיות או ירוקות: מיד למיון. סימני התייבשות (מעט שתן, שתן כהה, יובש בפה, חוסר תגובה, מרפס שקוע): פונים לטיפול.",
        "שלשול: אצל תינוקות ופעוטות יותר מ-48 שעות, אצל ילדים יותר מ-72 שעות, דם או ריר בצואה, או חום מעל 39: פונים לטיפול. בכל גיל: אין שיפור אחרי 48 שעות: בדיקה.",
        "פרכוס: משכיבים על הצד ולא פותחים את הפה. מתקשרים למד\"א אם לא נפסק תוך 5 דקות או יש קשיי נשימה, חנק או הכחלה.",
        "שבוע אחרי מנת רוטה ראשונה או שנייה: כאב בטן ובכי קיצוני, הקאות, דם בצואה, קירוב הרגליים לחזה או חולשה: מיד למיון.",
        "מגע עם חולה בחצבת: מתקשרים בהקדם לקול הבריאות 5400* או ללשכת הבריאות. הם מחליטים אם צריך חיסון.",
        "מנת יתר של תרופה: המרכז הארצי למידע בהרעלות 04-7771900, בכל שעה.",
        "בכי לא הורג, טלטול כן. מניחים את התינוק בעריסה, יוצאים לרגע לחדר אחר ומבקשים עזרה.",
        "שאלות שאינן דחופות: מוקד אחיות טיפת חלב בקול הבריאות 5400* (שלוחה 1 ואז 9).",
    ], "en": [
        "Hard to wake, not responding, marked confusion, a seizure, a red or purple rash that does not fade when pressed, breathing difficulty, or pale mottled skin: ER now or call 101.",
        "Up to 2 months: a temperature of 38 or higher means going to the ER immediately, even with no other symptoms.",
        "2 to 3 months: 38 or higher needs an urgent medical check. With floppiness, unusual sleepiness or reduced alertness: ER now.",
        "Below 36 in a baby: warm them (extra layer, blanket, held close). If that does not help and the baby looks ill, get a medical check.",
        "Marked jaundice, for example in the whites of the eyes: do not wait for the follow-up date, go for a check now.",
        "Under age 1: more than 60 breaths a minute, skin sinking between the ribs, or nasal flaring: immediate check or ER.",
        "Bloody or green vomit: ER now. Dehydration signs (little or dark urine, dry mouth, no response, sunken fontanelle): get care.",
        "Diarrhea: infants and toddlers over 48 hours, children over 72 hours, blood or mucus in the stool, or fever above 39: get care. Any age: no improvement after 48 hours: get a check.",
        "Seizure: lay on the side, do not open the mouth. Call MDA if it does not stop within 5 minutes or with breathing difficulty, choking or blue skin.",
        "In the week after rotavirus dose 1 or 2: abdominal pain with extreme crying, vomiting, blood in the stool, legs drawn to the chest, or weakness: ER now.",
        "Contact with someone who has measles: call Kol HaBriut *5400 or the district health bureau as soon as possible. They decide whether a vaccine is needed.",
        "Too much of a medicine: National Poison Information Center 04-7771900, any hour.",
        "Crying does not kill, shaking does. Put the baby in the crib, step into another room, and ask for help.",
        "Non-urgent questions: the Tipat Halav nurse line at Kol HaBriut *5400 (extension 1, then 9).",
    ]},
    "disclaimer": {"he": "לוח זה מציג את תוכנית חיסוני השגרה ואת מפגשי טיפת חלב כפי שפרסם משרד הבריאות. הוא אינו ייעוץ רפואי, אינו אבחון, אינו הערכה התפתחותית ואינו קובע אם לחסן. החלטות על חיסון, השלמה או דחייה מקבלים עם אחות טיפת חלב או הרופא.",
                   "en": "This calendar shows the routine vaccine plan and Tipat Halav visits as published by the Ministry of Health. It is not medical advice, not a diagnosis, not a developmental assessment, and does not decide whether to vaccinate. Decisions on vaccinating, catching up or postponing are made with the Tipat Halav nurse or the doctor."},
    "sources": {"he": "מקורות", "en": "Sources"},
    "generated": {"he": "הופק", "en": "Generated"},
    "schedule_version": {"he": "גרסת הלוח", "en": "Schedule version"},
    "past_short": {"he": "עבר, לבדוק בפנקס", "en": "Past, check booklet"},
    "olim_short": {"he": "לפני העלייה", "en": "Before arrival"},
    "hosp_short": {"he": "באשפוז", "en": "In hospital"},
    "old_booklet": {"he": "בפנקסים ישנים יכולים להופיע גם חיסונים שכבר לא ניתנים, למשל פוליו בטיפות לפה (bOPV), שהופסק במרץ 2025. הוא לא ברשימת החיסונים להשלמה של משרד הבריאות.",
                    "en": "Older booklets may also list vaccines no longer given, for example oral polio drops (bOPV), stopped in March 2025. It is not on the Ministry of Health catch-up list."},
}

HE_GRADE = {1: "א'", 2: "ב'", 3: "ג'", 4: "ד'", 5: "ה'", 6: "ו'", 7: "ז'", 8: "ח'"}


def grade_name(g, lang):
    return HE_GRADE[g] if lang == "he" else str(g)


def tr(key, lang):
    return T[key][lang]


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def parse_date(text, what):
    text = (text or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y"):
        try:
            return dt.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"{what}: '{text}' is not a valid date. Use YYYY-MM-DD, DD/MM/YYYY or DD.MM.YYYY.")


def add_months(d, months):
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    day = min(d.day, _cal.monthrange(y, m)[1])
    return dt.date(y, m, day)


def age_text(born, on, lang):
    """Whole months and remaining days between two dates."""
    if on < born:
        return "עדיין לפני תאריך הלידה המשוער" if lang == "he" else "still before the due date"
    months = (on.year - born.year) * 12 + (on.month - born.month)
    if add_months(born, months) > on:
        months -= 1
    days = (on - add_months(born, months)).days
    if lang == "he":
        return f"{months} חודשים ו-{days} ימים"
    m = "month" if months == 1 else "months"
    d = "day" if days == 1 else "days"
    return f"{months} {m} {days} {d}"


# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------

def visit_vaccines(key, born):
    new_cohort = born >= COHORT_SWITCH
    table = {
        "birth": [("hepb", "1/3")],
        "first": [],
        "1m": [("hepb", "2/3")],
        "2m": [("penta", "1/4"), ("rota", "1/3"), ("pcv", "1/3")],
        "4m": [("penta", "2/4"), ("rota", "2/3"), ("pcv", "2/3")],
        "6m": [("penta", "3/4"), ("rota", "3/3"), ("hepb", "3/3")],
        "9m": [],
        "12m": [("penta", "4/4"), ("pcv", "3/3"), ("mmrv", "1/2")],
        "18m": [("hepa", "1/2")] + ([("mmrv", "2/2")] if new_cohort else []),
        "24m": [] if new_cohort else [("hepa", "2/2")],
        "4y": [],
        "5y": [],
    }
    return table[key]


def school_vaccines(grade, born, hpv_both_grade8=False, booster_grade1=False, special_ed=False):
    new_cohort = born >= COHORT_SWITCH
    # The MoH schedule page shows the South/North grade-1 booster exception only
    # in the panel for children born before 1.1.2025.
    booster_grade1 = booster_grade1 and not new_cohort
    out = []
    if grade == 1:
        out += [("hepa", "2/2")] if new_cohort else [("mmrv", "2/2")]
        if booster_grade1:
            out.append(("tdap_ipv", "1/1"))
        if special_ed:
            out.append(("flu", "1/1"))
    elif grade == 2:
        if not booster_grade1:
            out.append(("tdap_ipv", "1/1"))
        out.append(("flu", "1/1"))
    elif grade in (3, 4):
        out.append(("flu", "1/1"))
    elif grade in (5, 6):
        if special_ed:
            out.append(("flu", "1/1"))
    elif grade == 7:
        if not hpv_both_grade8:
            out.append(("hpv", "1/2"))
    elif grade == 8:
        out.append(("tdap", "1/1"))
        out += [("hpv", "1/2"), ("hpv", "2/2")] if hpv_both_grade8 else [("hpv", "2/2")]
    return out


SCHOOL_GRADES = (1, 2, 3, 4, 5, 6, 7, 8)


def build_items(born, today, lang, due_date=None, grade1_year=None, hpv_both_grade8=False,
                discharge_date=None, preterm=False, booster_grade1=False, special_ed=False,
                olim=False):
    items = []
    rsv_in_hospital = born.month >= 9 or born.month <= 3
    hosp_until = discharge_date
    rota_to_nurse = preterm and (discharge_date is None or discharge_date > born + dt.timedelta(days=42))

    def visit_item(key, date, title, vaccines, physician, notes):
        past = date < today
        in_hosp = bool(hosp_until and date < hosp_until and key not in ("birth",))
        old = past and date < CURRENT_SCHEDULE_FROM
        # Preterm baby still in hospital at the 6-week visit (or discharge date
        # unknown): MoH moves rotavirus dose 1 to after discharge, so the timing
        # is left to the NICU team or the nurse. No deadline is computed.
        rota_nurse = rota_to_nurse and any(v[0] == "rota" for v in vaccines)
        if rota_nurse:
            vaccines = [v for v in vaccines if v[0] != "rota"]
        if in_hosp and vaccines:
            notes = notes + [tr("hosp_vax", lang)]
        return {"kind": "visit", "key": key, "date": date, "title": title,
                "vaccines": vaccines, "old_schedule": old, "physician": physician,
                "dev": DEV.get(key, {}).get(lang), "guide": GUIDE.get(key, {}).get(lang),
                "notes": notes, "past": past, "in_hospital": in_hosp,
                "hepb_preterm": preterm and any(v[0] == "hepb" for v in vaccines),
                "rota_nurse": rota_nurse}

    # Birth (in hospital)
    birth_notes = [] if preterm else [tr("hepb_birth", lang)]
    if not born < CURRENT_SCHEDULE_FROM:
        birth_notes.append(tr("rsv_hospital" if rsv_in_hospital else "rsv_tipat_rule", lang))
    birth_vax = visit_vaccines("birth", born)
    if rsv_in_hospital and not born < CURRENT_SCHEDULE_FROM:
        birth_vax = birth_vax + [("rsv_hosp", "")]
    items.append(visit_item("birth", born, VISIT_LABEL["birth"][lang], birth_vax, False, birth_notes))

    # First Tipat Halav visit
    if discharge_date:
        first_date = discharge_date + dt.timedelta(days=2)
        first_title = VISIT_LABEL["first"][lang]
    else:
        first_date = born
        first_title = VISIT_LABEL["first_book"][lang]
    first_notes = [tr("first_visit", lang)]
    items.append(visit_item("first", first_date, first_title, [], False, first_notes))

    for key, kind, val, physician in VISITS:
        if key == "2m":
            date = born + dt.timedelta(days=42)
            title = VISIT_LABEL["2m"][lang]
            if date < SIX_WEEK_FROM:
                date = add_months(born, 2)
                title = VISIT_LABEL["2m_old"][lang]
        else:
            date = add_months(born, val)
            title = VISIT_LABEL[key][lang]
        notes = []
        if key in ("6m", "9m"):
            notes.append(tr("measles_early", lang))
        if key == "12m":
            notes.append(tr("measles_dose2", lang))
        if key == "4m" and preterm:
            notes.append(tr("preterm_iron", lang))
        if due_date and due_date > born and key not in ("4y", "5y"):
            notes.append(f"{tr('corrected', lang)}: {age_text(due_date, date, lang)}")
        it = visit_item(key, date, title, visit_vaccines(key, born), physician, notes)
        if key == "4m" and preterm:
            it["guide"] = None
        items.append(it)

    items.sort(key=lambda i: (i["date"], 0 if i["key"] == "birth" else 1))

    for g in SCHOOL_GRADES:
        vax = school_vaccines(g, born, hpv_both_grade8, booster_grade1, special_ed)
        if not vax:
            continue
        notes = [tr("school_note", lang)]
        if g in (7, 8) and hpv_both_grade8:
            notes.append(tr("hpv_region", lang))
        old_cohort = born < COHORT_SWITCH
        if g in (1, 2) and booster_grade1 and old_cohort:
            notes.append(tr("booster_region", lang))
        elif g in (1, 2) and old_cohort:
            notes.append(tr("region_hint", lang))
        elif g in (1, 2) and booster_grade1:
            notes.append(tr("booster_new_cohort", lang))
        if special_ed and g in (1, 5, 6):
            notes.append(tr("sped_flu", lang))
        date = None
        year_label = None
        if grade1_year:
            start_year = grade1_year + g - 1
            date = dt.date(start_year, 9, 1)
            year_label = f"{start_year}-{start_year + 1}"
        past = bool(date and add_months(date, 10) < today)
        items.append({
            "kind": "school", "key": f"grade{g}", "date": date, "grade": g,
            "title": tr("school", lang),
            "vaccines": vax, "old_schedule": bool(past and date < CURRENT_SCHEDULE_FROM),
            "physician": False, "dev": None, "guide": None, "notes": notes,
            "year_label": year_label, "past": past, "in_hospital": False, "hepb_preterm": False,
        })

    if olim:
        for it in items:
            if it["past"]:
                it["olim"] = True
    return items


def vax_text(it, lang):
    if it.get("olim"):
        return tr("past_olim", lang)
    if it.get("old_schedule"):
        return tr("old_schedule", lang)
    parts = [VAX[k][lang] if dose in ("1/1", "") else f"{VAX[k][lang]} {dose}" for k, dose in it["vaccines"]]
    if it.get("hepb_preterm"):
        parts.append(tr("hepb_preterm", lang))
    if it.get("rota_nurse"):
        parts.append(tr("rota_preterm_label", lang))
    if not parts:
        return tr("no_vax", lang)
    return ", ".join(parts)


def status_text(it, lang):
    if it.get("in_hospital"):
        return tr("hosp_short", lang)
    if it.get("olim"):
        return tr("olim_short", lang)
    if it["past"]:
        return tr("past_short", lang)
    return "[ ]"


# ---------------------------------------------------------------------------
# iCalendar (RFC 5545)
# ---------------------------------------------------------------------------

def ics_escape(text):
    return (text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,")
            .replace("\r\n", "\\n").replace("\n", "\\n"))


def fold(line):
    """Fold a content line at 75 octets without splitting a UTF-8 character."""
    if len(line.encode("utf-8")) <= 75:
        return [line]
    out, cur = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(cur) + len(b) > 75:
            out.append(cur.decode("utf-8"))
            cur = b" " + b
        else:
            cur += b
    if cur:
        out.append(cur.decode("utf-8"))
    return out


def to_ics(items, born, today, lang, name=None, include_past=False):
    stamp = today.strftime("%Y%m%dT000000Z")
    who = name or tr("child", lang)
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             "PRODID:-//skills-il//israeli-parenting-companion//EN",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
             f"X-WR-CALNAME:{ics_escape(who + ' - ' + tr('title', lang))}"]
    for it in items:
        if it["date"] is None or it.get("in_hospital"):
            continue
        if it["past"] and not include_past:
            continue
        seed = f"{born.isoformat()}|{name or ''}|{it['key']}"
        uid = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:24]
        start = it["date"]
        end = start + dt.timedelta(days=1)
        desc = [tr("disclaimer", lang)]
        vt = vax_text(it, lang)
        if vt:
            desc.append(f"{tr('vaccines', lang)}: {vt}")
        if it.get("physician"):
            desc.append(tr("doctor", lang))
        if it.get("dev"):
            desc.append(f"{tr('dev', lang)}: {it['dev']}")
        if it.get("guide"):
            desc.append(f"{tr('ask', lang)}: {it['guide']}")
        desc.extend(it["notes"])
        if it["kind"] == "visit" and it["key"] not in ("birth", "first"):
            desc.append(tr("around", lang))
        if it["kind"] == "school":
            desc.append(f"{tr('school_reminder', lang)} {it['year_label']}")
        label = it["title"] if it["kind"] != "school" else f"{tr('grade', lang)} {grade_name(it['grade'], lang)}: {it['title']}"
        summary = f"{who}: {label}"
        lines += ["BEGIN:VEVENT", f"UID:{uid}@israeli-parenting-companion",
                  f"DTSTAMP:{stamp}", f"DTSTART;VALUE=DATE:{start.strftime('%Y%m%d')}",
                  f"DTEND;VALUE=DATE:{end.strftime('%Y%m%d')}",
                  f"SUMMARY:{ics_escape(summary)}",
                  f"DESCRIPTION:{ics_escape(chr(10).join(desc))}",
                  "TRANSP:TRANSPARENT",
                  "BEGIN:VALARM", "ACTION:DISPLAY", "TRIGGER:-P3D",
                  f"DESCRIPTION:{ics_escape(summary)}", "END:VALARM",
                  "END:VEVENT"]
    lines.append("END:VCALENDAR")
    folded = []
    for ln in lines:
        folded.extend(fold(ln))
    return "\r\n".join(folded) + "\r\n"


# ---------------------------------------------------------------------------
# Markdown outputs
# ---------------------------------------------------------------------------

def fmt_date(d):
    return d.strftime("%d/%m/%Y") if d else ""


def date_cell(it, lang):
    if it["date"]:
        return fmt_date(it["date"])
    return f"{tr('grade', lang)} {grade_name(it['grade'], lang)}"


def to_table(items, lang, with_notice=True):
    rows = []
    if with_notice:
        rows += [f"> {tr('disclaimer', lang)}", ""]
    rows += [f"| {tr('date', lang)} | {tr('what', lang)} | {tr('vaccines', lang)} | {tr('status', lang)} |",
             "|---|---|---|---|"]
    for it in items:
        what = it["title"] + (f" ({tr('doctor', lang)})" if it.get("physician") else "")
        rows.append(f"| {date_cell(it, lang)} | {what} | {vax_text(it, lang) or '-'} | {status_text(it, lang)} |")
    return "\n".join(rows) + "\n"


def to_checklist(items, born, today, lang, name=None, due_date=None, grade1_year=None,
                 preterm=False, olim=False):
    who = name or tr("child", lang)
    new_cohort = born >= COHORT_SWITCH
    out = [f"# {who}: {tr('title', lang)}", "",
           f"> {tr('disclaimer', lang)}", "",
           f"- {tr('born', lang)}: {fmt_date(born)}",
           f"- {tr('cohort_new' if new_cohort else 'cohort_old', lang)}",
           f"- {tr('schedule_version', lang)}: {SCHEDULE_VERSION[lang]}",
           f"- {tr('generated', lang)}: {fmt_date(today)}", ""]
    if preterm or (due_date and due_date > born):
        out += [f"## {tr('preterm_head', lang)}", ""]
        if preterm:
            out += [f"- {tr('preterm_vax', lang)}", f"- {tr('preterm_iron', lang)}"]
        out += [f"- {tr('preterm_dev', lang)}", ""]
    if olim:
        out += [f"## {tr('olim_head', lang)}", ""] + [f"- {n}" for n in T["olim_notes"][lang]] + [""]
    out += [f"## {tr('redflags_head', lang)}", ""]
    out += [f"- {r}" for r in T["redflags"][lang]]
    out += ["", to_table(items, lang, with_notice=False), ""]
    if any(it["past"] for it in items) and not olim:
        out += [f"> {tr('old_booklet', lang)}", ""]
    if not grade1_year:
        out += [f"> {tr('school_undated', lang)}", ""]
    for it in items:
        out.append(f"## [ ] {date_cell(it, lang)}: {it['title']}")
        out.append("")
        if it.get("in_hospital"):
            out.append(f"- {tr('in_hospital', lang)}")
        elif it.get("olim"):
            out.append(f"- {tr('past_olim', lang)}")
        elif it["past"]:
            out.append(f"- {tr('past', lang)}")
        vt = vax_text(it, lang)
        if vt:
            out.append(f"- {tr('vaccines', lang)}: {vt}")
        if it.get("physician"):
            out.append(f"- {tr('doctor', lang)}")
        if it.get("dev"):
            out.append(f"- {tr('dev', lang)}: {it['dev']}")
        if it.get("guide"):
            out.append(f"- {tr('ask', lang)}: {it['guide']}")
        for n in it["notes"]:
            out.append(f"- {n}")
        out.append("")
    out += [f"- {tr('flu_note', lang)}", f"- {tr('school_screen', lang)}", "", f"## {tr('sources', lang)}", ""]
    out += [f"- {label}: {url}" for label, url in SOURCES]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    p = argparse.ArgumentParser(description="Tipat Halav + routine vaccine calendar (offline).")
    p.add_argument("--birth-date", required=True, help="YYYY-MM-DD, DD/MM/YYYY or DD.MM.YYYY")
    p.add_argument("--name", default=None, help="Child's first name or nickname (optional)")
    p.add_argument("--lang", choices=["he", "en"], default="he")
    p.add_argument("--preterm", action="store_true", help="Born before week 37 (MoH definition)")
    p.add_argument("--due-date", default=None, help="Expected due date, to show corrected age (optional)")
    p.add_argument("--discharge-date", default=None, help="Hospital discharge date (optional)")
    p.add_argument("--grade1-year", type=int, default=None,
                   help="Calendar year in which the child starts grade 1 (September). Optional.")
    p.add_argument("--current-grade", type=int, default=None,
                   help="Child's grade in the current school year (1-12); used to derive --grade1-year")
    p.add_argument("--booster-grade1", action="store_true",
                   help="MoH South or North district: the grade-2 booster is given in grade 1")
    p.add_argument("--hpv-both-grade8", action="store_true",
                   help="Ashkelon district or Tzfat sub-district: both HPV doses in grade 8")
    p.add_argument("--special-education", action="store_true", help="Special education: flu in grades 1 to 6")
    p.add_argument("--olim", action="store_true", help="Child arrived from abroad: past items were not given in Israel")
    p.add_argument("--include-past", action="store_true", help="Also put past items in the .ics")
    p.add_argument("--today", default=None, help="Override today's date (testing)")
    p.add_argument("--format", choices=["all", "ics", "md", "table"], default="all")
    p.add_argument("--out-dir", default=".", help="Where to write files (format all/ics/md)")
    a = p.parse_args(argv)

    try:
        today = parse_date(a.today, "--today") if a.today else dt.date.today()
        born = parse_date(a.birth_date, "--birth-date")
        due = parse_date(a.due_date, "--due-date") if a.due_date else None
        discharge = parse_date(a.discharge_date, "--discharge-date") if a.discharge_date else None
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if born > today:
        print("error: the birth date is in the future. This calendar starts from an actual birth date.",
              file=sys.stderr)
        return 2
    if add_months(born, 18 * 12) <= today:
        print("error: the child is 18 or older; the routine childhood schedule no longer applies.",
              file=sys.stderr)
        return 2
    if discharge and discharge < born:
        print("error: --discharge-date is before the birth date.", file=sys.stderr)
        return 2
    if due and abs((due - born).days) > 150:
        print("error: --due-date is more than about 5 months from the birth date; check it.",
              file=sys.stderr)
        return 2
    if a.current_grade is not None:
        if not 1 <= a.current_grade <= 12:
            print("error: --current-grade must be between 1 and 12.", file=sys.stderr)
            return 2
        school_year_start = today.year if today.month >= 9 else today.year - 1
        a.grade1_year = school_year_start - (a.current_grade - 1)
    if a.grade1_year is not None and not (born.year + 4 <= a.grade1_year <= born.year + 8):
        print("error: --grade1-year should be the year grade 1 starts, a few years after birth.",
              file=sys.stderr)
        return 2

    items = build_items(born, today, a.lang, due_date=due, grade1_year=a.grade1_year,
                        hpv_both_grade8=a.hpv_both_grade8, discharge_date=discharge,
                        preterm=a.preterm, booster_grade1=a.booster_grade1,
                        special_ed=a.special_education, olim=a.olim)

    if a.format == "table":
        sys.stdout.write(to_table(items, a.lang))
        return 0
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    if a.format in ("all", "ics"):
        (out / "calendar.ics").write_bytes(
            to_ics(items, born, today, a.lang, a.name, a.include_past).encode("utf-8"))
        written.append(out / "calendar.ics")
    if a.format in ("all", "md"):
        (out / "checklist.md").write_text(
            to_checklist(items, born, today, a.lang, a.name, due, a.grade1_year, a.preterm, a.olim),
            encoding="utf-8")
        written.append(out / "checklist.md")
    if a.format == "all":
        (out / "table.md").write_text(to_table(items, a.lang), encoding="utf-8")
        written.append(out / "table.md")
    for w in written:
        print(f"wrote {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
