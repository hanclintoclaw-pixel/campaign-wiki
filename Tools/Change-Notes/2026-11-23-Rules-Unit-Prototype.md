---
title: Offline rules-unit prototype — 2026-11-23
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Offline rules-unit prototype — builder acceptance FAILED

## Built
Isolated code 2824788 saves two pure helpers: an unreviewed candidate-span inventory
and a bounded assembler over exact reviewed source spans. Neither is wired to search,
the bridge or production. No corpus rewrite, permission change, service restart or
live activation occurred. This is a partial prototype, not the proposed rules-unit
retrieval system or a reviewed new serving generation.

Qwen-low authored each helper in a separate small tool-free job, then one repair
per helper. Sol inspected the drafts and independently tested them. The first builder
dropped indentation. The assembler initially had an invalid import and omitted
heading admission; its repair still misunderstood the heading-list schema. Sol
corrected that list validation and tightened whitespace-only boundary handling.
Original drafts and failed test evidence are retained; these are not untouched-Qwen
or first-attempt-success claims. All code drafting stayed on low effort. The larger
code-output budget was separate from unchanged voice limits. No paid-token savings
are quantified.

## Measured
Seven verification methods pass: exact indented/Unicode slices and deterministic IDs,
revision refusal, valid assembly without mutation, stale/digest refusal, unread-heading
refusal, incomplete/bounds refusal and whole-unit overflow refusal. Compilation passes.
Source SHA remained unchanged across the inventory measurement.

The admitted Core source has 1,437,881 characters. Blank-line inventory emitted only
five candidate blocks, of sizes 18, 104, 1,349,585, 158 and 88,007 characters. Exact
non-whitespace coverage and nonoverlap checks pass, but this is plainly not usable
rules-unit segmentation. Every candidate remains unknown/unreviewed; zero candidates
were promoted. The failure is Sol's unvalidated blank-line planning assumption, not
proof that the underlying rules facts are wrong or that Qwen alone caused the miss.

Separately, of eleven existing Core records in the earlier reviewed sidecar, nine
complete units assemble intact under the 5,700-character serialized limit; two partial
sections are withheld. These are old reviewed witnesses, not nine newly extracted
units or question-level successes. The caller supplies the host admission map; these
helpers are not a remote security boundary or a grant.

## Open / next work
Builder acceptance fails. No searchable unit generation was produced, so the proposed
8/8 retrieval-coverage gate and held-out/full-handler gates were not run or claimed.
The last actual full-handler result remains 0/8 useful answers. No new STT, TTS,
Discord playback or human voice acceptance was tested.

The next implementation problem is generic layout-aware candidate extraction using
source page structure and heading/paragraph/table evidence, not blank-line splitting
or individual rule patches. Preserve exact source spans and unknown status until
scope/layout/dependency review. Do not convert arbitrary page chunks into complete
rules units just to populate an index. The assembler can be reused; it does not solve
heading inference or dependency closure. No bulk OCR rewrite is justified by this
failed splitter alone.

## Evidence
Private data: runtime/rules-unit-prototype-20261123 on the data tier: source/witness
freeze, Qwen drafts/repairs, candidate spans, tests and summary. Code/harness:
workfiles/rules-unit-prototype-20261123; committed helpers under tools/rules_unit_prototype.
[Approved design](2026-11-22-Rules-Unit-Design).

Follow-up: [Layout-aware replacement inventory](2026-11-23-Layout-Candidates). No serving generation or activation.
