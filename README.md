# Nashville Shadowrun Campaign Wiki

Git-backed Markdown campaign memory for the Nashville Shadowrun game.

## Structure

- `index.md` — front page / dashboard
- `Current-State.md` — live campaign posture
- `Sessions/` — per-session notes and summaries
- `NPCs/` — character dossiers
- `Factions/` — corps, crews, and organizations
- `Locations/` — apartments, clubs, offices, neighborhoods
- `Clues/` — loose threads, unpulled leads, and archived clue evidence
- `Arcs/` — major plot arcs
- `Timeline/` — campaign chronology
- `Templates/` — copyable starter pages for common wiki categories
- `meta/` — schemas, templates, conventions

## Editing model

- Human-readable Markdown pages
- YAML frontmatter for structured metadata
- Git history as audit trail
- Cindy maintains pages primarily; humans can review and correct canon
- Post-session closeout can patch `index.md` and `Current-State.md` with `scripts/update_current_campaign_state.py`
