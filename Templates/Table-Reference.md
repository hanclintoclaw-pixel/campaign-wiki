---
title: Draft Table Reference Template
type: template
visibility: player-safe
canon_status: operational-record
status: proposed-pilot
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---

# Draft Table Reference Template

Not installed on campaign pages. Add this mapping inside existing frontmatter only during an approved migration. Replace unknowns solely from reviewed evidence; do not paste invented example facts. See [maintenance and acceptance rules](../Tools/Table-Reference-Standard.md).

```yaml
table_reference:
  schema_version: 1
  entity_kind: pc
  as_of: "2026-11-22"
  facts:
    identity: {value: null, assertion_status: unknown, qualifiers: ["Not reviewed."], source_refs: []}
    role: {value: null, assertion_status: unknown, qualifiers: ["Not reviewed."], source_refs: []}
    current_status: {value: null, assertion_status: unresolved, qualifiers: ["Reconcile history first."], source_refs: []}
    specialties: {value: null, assertion_status: unknown, qualifiers: ["Not reviewed."], source_refs: []}
    limitations: {value: null, assertion_status: unknown, qualifiers: ["Not reviewed."], source_refs: []}
  sections:
    current_balances: "Current Karma and Nuyen"
```

For an asset, use `entity_kind: asset` and add `class`, `owner`, `operator` fact objects with the same fields. Do not infer these from a directory name. NPCs use `npc` and omit PC balance references unless an approved schema extension is needed.

Formatting check: `python scripts/validate_table_reference.py --require path/to/page.md` (PyYAML required). It does not check truth or source permissions. Without `--require`, absent blocks are reported as **unmigrated**, never as validated.
