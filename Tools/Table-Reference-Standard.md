---
title: Table Reference Standard and Maintenance
type: documentation
visibility: player-safe
canon_status: operational-record
status: proposed-pilot
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---

# Table Reference Standard and Maintenance

**Proposal, not a completed migration.** Use one versioned `table_reference` YAML mapping in page frontmatter, near the top of the file. Do not maintain a second hand-written machine summary elsewhere. An optional human-facing view should be generated from this mapping. Narrative and dated ledgers remain the supporting record; the summary is a current projection, not new canon.

The current voice reader does not consume this schema. Adding the block alone is not a retrieval fix. A separately approved pilot must test a general class-aware reader/projection, source review and generation binding before activation. Names, filenames and individual section exceptions must not become routing rules.

## Draft v1 contract

- `schema_version: 1`; `entity_kind: pc | npc | asset`; quoted ISO `as_of` review date. Other entity classes need a reviewed extension, not guesses.
- `facts`: `identity`, `role`, `current_status`, `specialties`, `limitations`. Assets also require `class`, `owner`, `operator`. Each fact contains `value`, `assertion_status`, `qualifiers`, `source_refs`.
- Values are text, a list of text, or null. Known facts require `confirmed` or `provisional` plus references. Unknown/unresolved facts require null and an explanatory qualifier. Missing is not zero, false, none, or evidence of absence.
- Preserve complete qualifications, units, lower bounds, historical/current distinctions and paused/abandoned/planned states. Put older conflicting accounts in history; do not silently choose a winner.
- `sections` points to stable existing heading labels for equipment, native stats, history and PC current balances. Do not duplicate Karma/nuyen values or copy an equipment database into this block. Preserve native variant/formula/table semantics.
- References identify reviewed supporting page sections, sessions or rulings. A reference or a `confirmed` label is not authorization or independent verification. Never embed the page's own hash in itself; the external generation binds its exact revision.

See the [draft template](../Templates/Table-Reference.md). The authoring validator checks formatting only, not truth, disclosure rights, freshness or semantic consistency.

## Required update workflow

This applies equally to **player-requested page edits**, between-session changes, and **voice-session closeout**:

1. Identify changed facts and affected pages from reviewed evidence. Apply an event once. Update supporting prose/history/ledger and any existing `table_reference` in the same change; never infer facts from missing fields or prior generated answers.
2. Update values, assertion status, every material qualifier, references and `as_of`. Keep old events in history. For PC money/Karma, update the existing current-balance block and ledger together; the reference block points there rather than keeping another total.
3. Run `python scripts/validate_table_reference.py --require <migrated-pages>`, using an interpreter with PyYAML. Duplicate YAML keys, missing fields and malformed dates are errors. Review source agreement separately: a format pass cannot prove a correct current state.
4. If a page is not migrated, update its canonical facts normally and report **unmigrated**. Do not introduce a new schema during an unrelated player edit or silently omit a broken existing summary. New migrations require the approved template/pilot scope.
5. At closeout, check every changed PC/NPC/asset page, not only the session summary. Report migrated/validated, unmigrated and unresolved pages separately. Do not mark the update complete while summary and record disagree.
6. Stage voice-pinned edits, review exact source ranges, rebuild/rebind and validate the public projection before any separately approved activation. Publication is not voice activation. No permission is granted by frontmatter.

## Pilot and acceptance gate

Recommend a four-page pilot across PC/NPC/asset classes, including a complex status-history case, followed by a reserved set of entities/paraphrases not used in implementation. Retain the ten-page audit as development evidence, not unseen acceptance. Test source agreement, formatting, stale/denied/unknown/ambiguous controls, representative questions, complete text, qualified speech and rollback. Review before bulk conversion; do not require a database-wide rewrite on assumption.
