# CLAUDE.md

This is a Skills IL category repository for healthcare skills tailored for the Israeli market, including HMO navigation, patient rights, and health insurance guidance. Each subdirectory is a self-contained skill following the open Agent Skills standard.

## Skill Structure

Each skill folder must contain:
- `SKILL.md` - Required skill definition with YAML frontmatter (English)
- `SKILL_HE.md` - Required Hebrew content (no frontmatter)

## SKILL.md Requirements

- `name`: kebab-case, matches folder name
- `description`: What it does + When to use it, <1024 chars
- `license: MIT`
- `metadata.display_name`: bilingual `{he, en}`
- `metadata.display_description`: bilingual `{he, en}`
- `metadata.tags`: bilingual `{he, en}` arrays
