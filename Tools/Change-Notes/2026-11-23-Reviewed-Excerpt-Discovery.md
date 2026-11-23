---
title: Source-reviewed excerpt partition and discovery — 2026-11-23
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Source-backed discovery — selected offline partition, NOT LIVE

## Reviewed partition
Eight Core excerpts now assemble from exact revision-bound body and governing-heading
spans: action phase, ranged outcome, general Drain, Duration with its table, Control
Pool, Hacking Pool, Detection Factor and a melee-defense contrast. These are selected,
source-informed diagnostic excerpts, not a whole-book reviewed unit index or a claim
that every operation/cross-reference is closed.

Existing exact-source records were revalidated against the current full Core source:
page bytes, book revision, spans and hashes match. Governing parent headings remain
explicit, including those on a different page. Informational cross-references were
not promoted into parents, and no proximity graph was auto-approved.

The formerly partial Duration record now includes its explicitly referenced Permanent
Spell Base Time table as a separate original body block. Sol inspected the rendered
printed page 178: all four table rows and their units, Duration scope, sustained-spell
modifier and normal Damage Resistance exception agree with the source. Logical
body-to-table ordering is explicit; no quote may cross an artificial block join.
This closes that selected excerpt's table dependency, not all spellcasting rules.

Native PDF page witnesses were saved for ordinals 45, 46, 106, 111, 115, 164, 180 and
209, with individually observed printed folios 43, 44, 104, 109, 113, 162, 178 and 207.
No global page offset was assumed. Native extraction interleaves columns on the table
page, so a visual page check—not native text alone—verified its row relationships.
An initial render command had a syntax error; the corrected render completed before
review. Corpus/PDF source text was not rewritten.

Maximum serialized view is **2,991 characters**, below the 5,700 cap. Adept Boost's
unreviewed associated dependency and Quick Start's unresolved OCR order remain held.
All other proposal edges remain unreviewed/held. This offline partition is not a new
live source grant, discovered-handle registry or activated serving generation.

## Generic discovery measurement
Qwen-low authored the pure lexical ranker in isolated b4aeb35. Sol reviewed it, wrote
six tests and ran the frozen diagnostic questions without changing the ranking after
seeing results. Ranking uses general word matching, IDF and frequency/title weighting;
it contains no rule names, expected-answer map, source-specific boosts or facts.
Token cleanup affects ranking only, never quoted source bytes. The call reports
247 prompt / 887 completion tokens; no paid-token savings are quantified.

Six tests pass: match/no mutation, no-overlap empty result, limit validation, empty
input, deterministic ranking and unchanged hyphenated source text. Compilation passes.
The earlier bounded assembler and source hash/span checks were reused separately.

Across the eight known answerable questions:
- Applicable excerpt in top five: **8/8**.
- Applicable excerpt ranked first: **7/8**.
- The ranged-staging question still ranks melee defense first; the correct ranged
  excerpt ranks second. Keep this failure visible. The same numerical value from
  the wrong mechanic remains unsafe support.

This is a small, closed-world, source-informed partition. It measures **candidate
availability**, not unseen recall, full-mechanic completeness, final answers or voice
acceptance. No claim that the full discovery/serving gate has passed is made. All four
boundary questions were also ranked for inspection, but ranking is not admission:
missing-input/private controls must still clarify, and an invented pool can retrieve
related pool text without becoming a real mechanic.

## Status and next step
No full-handler, model-answer, STT or playback replay was run. The last actual full
rules handler result remains 0/8 useful answers. Existing live features were untouched.

Next recommendation: a default-off isolated unit search/get adapter with pinned
manifest/source checks, request-local discovery handles, exact block quotes, coverage
metadata and existing read/time limits. Preserve the ranged-versus-melee contrast and
freeze held-out cases before assessing ranking or applicability. Then test the generic
action-output schema and the complete handler; do not silently force the top hit into
an answer. No individual passage patches, broader grants or activation.

The dependency-review milestone is complete only for these selected excerpts. Broad
relationship validation, unknown dependency closure, held-out coverage and human
acceptance remain open. Re-estimate the project after those discovery/handler gates,
not from this 8/8 top-five result alone.

## Evidence
Private runtime/unit-partition-20261123: frozen inputs, native witnesses and rendered
page, reviewed records/views, exact partition digest, test log and all discovery
rankings. Workfiles/unit-partition-20261123 contains the Sol build/review harness and
Qwen ranker. Source is under tools/rules_unit_prototype/search.py in the isolated branch.
[Relationship and completion checklist](2026-11-23-Unit-Relationships) and
[unit contract](2026-11-22-Rules-Unit-Design).
