---
title: Unit relationship proposals and completion map — 2026-11-23
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Unit relationships — proposal scaffold, NOT serving coverage

## Built and checked
Isolated ccfc729 adds a generic relationship proposer over the frozen layout spans.
It offers the last two same-page heading candidates as alternative body/table links,
and a table-to-body hypothesis until the next heading. A page boundary produces a
held cross-page dependency, never automatic continuation or a governing assertion.
Markers are never evidence parents. No rule/page names or answer facts are encoded.

Qwen-low drafted it and made one bounded repair. Sol caught marker-reset and
continuation-state problems; the repair still had a stray closing brace and treated
all numbered-page rows as markers. Sol corrected those two defects, then independently
verified the result. Failed syntax evidence and original drafts remain private.
The two calls report 1,034 prompt and 1,784 completion tokens combined; no paid Sol
savings or untouched-Qwen-success claim is made.

Six verification methods pass: alternative same-page links without mutation, marker
reset and cross-page holds, repeated-marker reset, table/heading reset, malformed and
overlapping input rejection, and empty input. Compilation passes.

Across the existing inventory: **3,554 edges**, consisting of 2,995 heading/body,
184 heading/table, 30 table/body and 345 cross-page hypotheses. Statuses are 3,209
unreviewed and 345 held. No candidate was promoted by proximity.

Independent comparison against the prior exact-source annotations found a same-page
heading/body proposal in seven of 24 annotation comparisons. Sol inspected the source
heading/body excerpts for those matches (defense, action phase, Drain, Duration,
Control Pool, Hacking Pool and Detection Factor). These are known source witnesses,
not unseen evaluation. The comparison also includes cross-page parents, tables and
span-granularity mismatches, so 7/24 is **not** heading recall, precision or question
coverage. Unmatched relationships are not declared absent from the book.

No new complete unit generation exists. Table header/column/row relationships and
cross-page dependency closure are still unresolved. This scaffold is suitable for
review, not search/get integration. Source grants, corpus files and the live bridge
were not changed. The last full-handler result remains 0/8 useful rules answers; no
new voice, STT, playback or full-handler improvement is claimed.

## Estimated completion checklist — current rules-reader diversion
These are planning ranges, not measured completion percentages or promises.
- Done: diagnose page/context failures and preserve evidence provenance.
- Done: exact layout-span candidate inventory and structural checks.
- Done in this pass: generic relationship proposals and bounded source-witness checks.
- Open: verify heading/body, continuation and table dependencies; build a bounded,
  reviewed Core unit partition and prove discovery coverage.
- Open: isolated unit search/get integration plus a shared action-output schema.
- Open: known and held-out full-handler acceptance, then voice acceptance and separate
  activation approval. Refusing all answerable questions is a failure, not a safety win.

At the start of this pass: approximately **4–6 focused work passes including this one**,
provisionally **1–3 working days for a bounded Core pilot**, conditional on no new layout
blocker. This does not estimate all-book coverage. The dependency-review and discovery
results are the next re-estimation gates; elapsed time cannot substitute for acceptance.
The current proposal scaffold does not close the dependency-review milestone.

Proposed gates remain: reviewed discovery coverage for all eight known answerables;
known and held-out sets each at least 7/8 correct/useful with applicable citations,
zero wrong factual answers and all four boundary controls appropriate. These are
pilot-advancement gates, not proof the general system is solved. Speed and human
playback acceptance stay separate.

## Larger voice project checklist
- Live within tested scope: wake/playback and telemetry foundations; structured SR3
  equipment lookup; public campaign reader; PC current balances; four-summary pilot.
- Open: complete the general-rules diversion above, currently 0/8 full-handler utility.
- Open: broaden campaign source standardization and cross-entity coverage tests.
- Open: establish rules coverage beyond the Core pilot, retaining honest out-of-coverage
  refusals instead of implying the entire ingested library is answer-ready.
- Open: mixed conversation/STT, latency, refusal and monitor-precision acceptance;
  resolve or explicitly disposition the known baseline broad-suite failures.
- Open: representative human voice acceptance and a published supported-coverage /
  remaining-limit checklist, followed by separately approved activation.

**No defensible whole-project completion date yet.** Re-estimate after discoverable
unit coverage passes. The goal remains casual, quick and correct campaign/SR3 answers
or a short honest refusal—not ever more tests of a system that answers nothing.

## Next bounded objective
Review a representative relationship partition and explicitly close or hold its
heading, table and continuation dependencies. Use class-wide metadata, not individual
passage exceptions. Do not wire an unreviewed proximity graph into voice. Search/get
and coverage tests follow only after a source-reviewed generation exists.

## Evidence
Private runtime/unit-relations-20261123: source/inventory/witness freeze, raw Qwen
responses, tests, proposal graph, exact-source witness comparison and summary.
Source/harness: workfiles/unit-relations-20261123. Committed helper:
tools/rules_unit_prototype/relations.py.
[Layout inventory](2026-11-23-Layout-Candidates) and
[approved unit contract](2026-11-22-Rules-Unit-Design).
