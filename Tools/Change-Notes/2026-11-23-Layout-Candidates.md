---
title: Layout-aware candidate inventory — 2026-11-23
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Layout candidates — structural improvement, NOT a serving generation

## Built
Isolated f4b79d0 adds a generic, pure candidate extractor. It recognizes exact source
page markers, mixed-case/uppercase heading cues and table cues, and groups intervening
body lines without crossing a page marker. All character offsets, indentation and
source text remain exact. Every span remains unknown/unreviewed; none becomes a
complete rule unit because of a typography heuristic. No source rewrite, live bridge
change, new source permission, integration or activation occurred.

Before drafting, Sol inspected the actual 1,437,881-character Core source: 31,151 lines
and 346 page markers. Source identity and controls were frozen. Qwen-low then returned
one tool-free source draft; Sol inspected it, authored independent verification and
measured the real-source inventory. No Qwen repair or Sol source correction was
needed for this extractor. It exceeded the requested source-line ceiling (110 lines
versus 85 requested), so instruction-following is not claimed perfect. The call reports
354 prompt / 1,255 completion tokens, including 255 reasoning tokens; paid Sol savings
remain unmeasured. Code-drafting output limits are not voice response limits.

## Measured
- Five verification methods pass: exact partition/determinism, mixed-case and table
  cues/page resets, bad revision, bad input type, and original-slice hash fidelity.
  Python compilation passes.
- The complete source is partitioned into **4,381 candidates**: 346 marker spans,
  1,967 body spans, 1,960 heading candidates and 108 table candidates. Reconstruction
  equals the original text exactly, with no gaps or overlaps. Every source marker is
  preserved and no candidate crosses one. Source SHA remains unchanged.
- Maximum span: 6,357 characters; nine spans exceed 5,700 characters. They are not
  silently shortened or declared valid bounded units. This is an inventory, not a
  serving response.
- Of 17 previously reviewed Core heading witnesses, 16 appear as heading candidates;
  the remaining table title appears as a table candidate, as intended by cue priority.
  These are known witnesses, not an unseen recall benchmark or proof of scope.
- A deterministic 12-candidate sample revealed a clear false heading cue: a table
  cell was classified as heading-like. Its source context was inspected. Candidate
  typography therefore cannot authorize governing-heading relationships. No heading
  precision score or table-layout accuracy claim is made.

The prior blank-line extractor made five blocks including one of 1.35 million
characters. This replacement fixes that gross segmentation defect without changing
source bytes. It does not yet recover verified paragraph boundaries, table row/column
relationships, section hierarchy or cross-page dependency closure.

## Acceptance and next objective
**Span-inventory structural checks pass. Rules-unit retrieval acceptance is untested.**
Zero new units were promoted, and no searchable reviewed generation exists. The
8/8 discovery gate, held-out/full-handler gates and voice tests were not run. The last
actual full-handler result remains 0/8 useful answers. No speed improvement is claimed.

Next bounded objective: use these candidate spans to propose explicit heading/body,
continuation and table-header/row relationships, then independently source-review a
representative partition. Governing scope, qualifiers and reading order must be
verified before completeness is asserted. Unknown relationships remain held, not
inferred from a nearby heading or next page. Only after that can host-authorized unit
search/get and question-level coverage be tested. Keep this class-wide and generic;
no individual rule/page branches, manual answer facts in the parser, or bulk OCR rewrite.

The existing bounded assembler may be reused, but its nine earlier reviewed Core
witnesses are not new extractor coverage. No live change is proposed at this checkpoint.

## Evidence
Private artifacts: runtime/layout-candidates-20261123 on the data tier: source freeze,
raw Qwen draft, exact candidate inventory, verification log, heading-witness results,
deterministic sample and summary. Source/harness: workfiles/layout-candidates-20261123;
committed extractor: tools/rules_unit_prototype/layout_candidates.py.
[Previous prototype](2026-11-23-Rules-Unit-Prototype) and
[unit contract](2026-11-22-Rules-Unit-Design).

Follow-up: [Relationship proposals and completion checklist](2026-11-23-Unit-Relationships). Still not serving coverage.
