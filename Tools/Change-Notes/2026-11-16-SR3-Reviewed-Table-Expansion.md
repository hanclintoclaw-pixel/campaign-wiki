---
title: "2026-11-16 — HE grenades and the numbered Ares Predators in the reviewed tables"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-16
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-16
---

# HE grenades and the numbered Ares Predators in the reviewed tables

## Shipped

Bridge commits `04406e2`, `a916f2a` and `d1f370a` are pushed on the bridge's main branch. The reviewed reference now covers HE grenade damage and the numbered Ares Predators. “What are the stats for X” reads the whole reviewed row with unit-tagged cells rather than declining. Spoken currency is rendered as “nuyen”; the evidence cell retains the printed currency glyph.

The core Grenades table, printed p.283, contributes Offensive (HE or AP), Defensive (HE or AP), Concussion, Smoke and Smoke (Infra-Red). The Grenade Damage Table, printed p.119, contributes grenade and mini-grenade damage rows. HE replies identify Damage 10S, Power 10 and base Damage Level Serious, explicitly not damage points or dice. Offensive blast is –1/m and defensive blast is –1/0.5m; the printed price is 30¥ and availability is 4/4 days. These are printed source values, not performance measurements.

HE aliases both HE rows deliberately: the printed identity does not select a delivery variant. Shared damage can be answered; differing blast values are both stated. AP-specific asks still decline because printed p.119 sends their damage interpretation to unreviewed flechette rules. Mini-grenade asks still decline because only their damage code is reviewed.

Ares Predator II and III come from The Cannon Companion, printed p.19, not from suffixing the base Ares Predator in core printed p.278. The Cannon Companion's printed p.6 identifies the book as for Shadowrun Third Edition. Explicit aliases handle Arabic-numeral asks without naive Roman-numeral suffix replacement.

### Why it broke that way

The earlier bounded reference did not contain grenades or the numbered Predators. Lookup declined rather than borrowing a nearby row.

The core grenade pages were transcribed from rendered page images and checked against their native PDF text. The Cannon Companion scan has no PDF text layer. Its reviewed page therefore binds the rendered PNG's SHA-256 and render resolution instead of a native-text proof. The gun row was read at distinct render resolutions and agreed across both reads; every cell also independently matched the item-cache row before acceptance. The cache supplies a locating lead, never a citation: it has no book or page. Reviewed evidence lives in `~/.openclaw/cindylou-table-evidence/`.

The reference now uses `schema: 2`, with pages keyed by book and PDF page under `sources`. Each citation names its source book. Any missing or changed binding for any bound book makes the whole reference stale, rather than answering from whichever books remain available.

`sr3_tables/audit_reference.py` checks each page's `text_sha256` against the named book and verifies book/page provenance against declared row locations. Wrong-book binding fails. Audit self-tests reject an adjacent wrong-row Ammo token, a swapped reviewed image and an invented semantic quote.

Range asks remain restricted to the core reviewed Weapon Range Table. A Cannon Companion row has no reviewed `range_row`, so its range ask declines rather than borrowing core ranges.

## Measured

- The real-handler grader was exercised through `test_sr3_tables.py`. The evidence pack gives its case count without an explicit evidence-type label, so no numerical coverage claim is made here.
- Changing Predator II damage to “Damage 10S” failed the grader, as intended; citing core printed p.278 for a Cannon Companion row also failed (ad-hoc probe with mutated cases). The page number and damage expression identify the mutations, not measured outcomes.
- The pack records decline controls for AP grenade, mini-grenade, unknown Predator suffixes, another edition and armor-ignoring interpretations, alongside positive controls intended to detect blanket declining.
- After the final restart, the bridge's boot source hash matched committed `voice_chat.py`, and Discord `on_ready` was present (ad-hoc probe over `voice_bridge.log`).

## Still open

Received Discord voice wake, TTS playback and the new rows in the current registry generation were not tested. Bridge readiness and source-hash agreement do not establish end-to-end audio acceptance.

The reference remains bounded. Unreviewed flechette interpretation, fuller mini-grenade statistics, unsupported Predator identities and Cannon Companion range answers remain declines. The evidence pack does not explicitly classify the reference inventory or graded-case totals by the hub's required evidence types; those totals are omitted rather than assigned a provenance label.

## Corrections

No corrections to the shipped implementation are recorded in this entry.

[Back to change notes](../Change-Notes.md)
