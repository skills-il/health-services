# Hebrew Exercise & Gym-Slang Map

Israelis log workouts in a mix of Hebrew, transliterated English, and gym slang.
The Logger role must map the user's free text to the canonical English `name` stored
in `log.jsonl`, so the Analyst can group the same exercise across sessions even when
the user phrases it differently each time.

Rule: store the **canonical English name** in the log. Show the user Hebrew back when
you confirm. If a term is ambiguous, ask rather than guess.

## Gym vocabulary (Israeli)

| Hebrew | Meaning |
|---|---|
| מכון / חדר כושר | gym |
| מוט | barbell |
| משקולות / דמבל | dumbbells |
| כבל / פולי | cable / pulley |
| מכונה | machine |
| סט / סדרה | set |
| חזרות / ריפים | reps |
| משקל | load / weight |
| אימון | workout / session |
| חימום | warm-up |
| מתח | pull-up bar / "the bar" (also the pull-up itself) |
| כושר | fitness |

## Common exercises (Hebrew / slang -> canonical name)

| User might say | Canonical `name` |
|---|---|
| לחיצת חזה / בנץ' / פרס חזה | bench press |
| לחיצת חזה בשיפוע / אינקליין | incline bench press |
| לחיצת כתפיים / מיליטרי / פרס כתפיים | overhead press |
| סקוואט / סקוואט מוט | back squat |
| סקוואט גביע / גובלט | goblet squat |
| דדליפט / הרמת מת | deadlift |
| רומנייה / RDL / דדליפט רומני | romanian deadlift |
| חתירה / חתירה במוט / רואו | barbell row |
| חתירת מכונה / חתירה בישיבה / סיטד רואו | seated cable row |
| מתח / פולאפ | pull-up |
| משיכת פולי עליון / לט פולדאון | lat pulldown |
| לחיצת רגליים / לג פרס | leg press |
| כפיפת ברכיים (מכונה) / לג קרל / כפיפת ירך אחורית | leg curl |
| פשיטת ברכיים (מכונה) / לג אקסטנשן | leg extension |
| היפ תראסט / דחיקת אגן | hip thrust |
| לאנג'ים / מספריים / פיתולי מכרעים | lunge |
| מקבילים / דיפס | dip |
| כפיפת מרפקים / בייספס / קרל | barbell curl |
| פשיטת מרפקים / טרייספס / פושדאון | triceps pushdown |
| סקאלקראשר / פשיטת מרפקים בשכיבה | skullcrusher |
| הרחקות כתף / סייד לטרל | lateral raise |
| פרפר / פליי / מקרב חזה | chest fly |
| טרפזים / שראגים | shrug |
| כפיפות בטן / בטן | crunch / ab work |
| פלאנק / קרש | plank |
| הרמות שוקיים / קאף | calf raise |
| פייס פול | face pull |
| הליכון / ריצה | run / treadmill (log under `cardio`) |
| אופניים / ספינינג | cycling (log under `cardio`) |

## Notes

- Do not confuse the knee machines with the squat. "כפיפת ברכיים" (knee flexion) is the
  leg-curl machine (hamstrings) and "פשיטת ברכיים" (knee extension) is the leg-extension
  machine (quads). Neither is a squat. If the user just says "סקוואט" it is the back squat;
  if they say a "מכונה" for the legs, ask which one before mapping.
- "מתח" is context-dependent: alone it usually means the pull-up exercise; "על המתח"
  means on the pull-up bar. If the user writes a number of reps next to it, it's the exercise.
- Transliterated English is common ("בנץ'", "סקוואט", "דדליפט"). Accept both spellings.
- If the user names a variation you do not have a clean canonical for, store the closest
  canonical plus a qualifier in the exercise `name` (e.g. "bench press (close grip)") so the
  Analyst still groups it with the parent movement, and note it in the session `notes`.
- Loads: Israelis train in kilograms. Store `kg`. Only convert if the user explicitly logs pounds.
