---
title: Isolated rule-review integration — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Rule-review integration — release acceptance FAILED, NOT LIVE

## Shipped
Isolated candidate `336d706` (base `d656991`) adds default-off
`LIVE_WAKE_RULE_REVIEW_V2_ENABLED`. It requires the existing rules-provenance mode
and does not change campaign/equipment behavior. Rules action generation and compact
semantic review use low effort, 128 thinking tokens, 512 total tokens and the existing
12-second transport / 13-second child / 25-second owner deadlines. The new rules
path refuses truncated/empty generations instead of invoking the legacy none retry;
gate-off behavior is retained. No live configuration, model or source grant changed.

Transport accepts only the host-owned compact verdict schema and the fixed positive
cap. Source/revision/quote validation, canonical claim rendering and qualified speech
remain in place. Whole-answer responsiveness cannot override unsupported claim labels.

The section projector uses the independently pinned reviewed sidecar, never as an
access grant. Every referenced heading/continuation page must already have been read
this turn, at the same revision; every selected span must occur in that actual read
window. Unknown, ambiguous, unread or over-budget context refuses. It performs no
extra reads and does not bypass the existing read/discovery budgets. No page/rule
exceptions were coded.

## Measured
- 76 focused tests pass, including new compact-decoder, scope, gate-off/on and actual
  fixed-subprocess transport checks. Python compilation, Node syntax and diff checks pass.
- Corrected decoder acceptance agrees on all 36 saved results from the prior cap trial.
  This is response replay, not 36 new integrated model calls.
- Four real campaign/equipment handler pairs (Curtis identity, Dolly status, Curtis
  balance, Predator damage) have exact gate-off/on reply, speech and display-page parity.
  Discord delivery was mocked; no operator CLI calls were allowed.
- The unchanged frozen 12-question full-handler rules replay produced **0/8 useful
  answers to answerable questions**. All four ambiguous/private/unsupported controls
  remained appropriate. Refusing all answerable questions fails the project goal.
- Positive-case handler wall time was 6.32–19.52 seconds, before TTS/playback. No new
  audio, STT or human voice acceptance is claimed. The known broad suite was not rerun;
  focused passes do not erase its previously recorded baseline issues.

Failure breakdown across the eight answerable questions:
1. Three eligible proposals could not obtain an authorized reviewed view: an alternate
   source page outside the small annotation pilot, the held Quick Start OCR-order unit,
   and a pool section whose governing heading had not been read this turn.
2. One wrong bonus-for-formula proposal reached the completed reviewer and was withheld.
   That prevented a wrong answer; it did not produce the requested formula.
3. One proposal failed the exact-quote contract; one abstained after lookup.
4. One generated action was malformed JSON; one lacked a valid bounded claim envelope.

The prior full-handler result was 1/8. This is not a fresh paired causal comparison,
but the current candidate is plainly not release-ready. Reviewer completion improved
in the controlled trial; that did not solve retrieval coverage or generation contracts.

## Corrections / authorship
Qwen-low drafted the compact decoder and one bounded repair. Sol caught response
normalization and claim-count defects; the repair still assigned a list rather than
an encoded claims object. Sol corrected that final adapter assignment, authored the
read-scope projector, wiring, tests and harness, and independently verified behavior.
The first Qwen draft was not correct, and this is not untouched Qwen implementation.
The two code-drafting calls report 565 prompt and 1,711 completion tokens combined;
paid Sol incremental usage and a comparable baseline are unavailable, so no numerical
savings claim is made. Drafting limits were separate from voice limits.

## Still open / next recommendation
Do not activate or keep tuning thinking settings. The next general objective should
be a rules-unit retrieval contract: return a bounded self-contained rule section,
governing headings, exact revision/citation and explicit coverage rather than an
arbitrary page fragment. Design that interface and its class-wide index/annotation
requirements before broad implementation; preserve source admission and read budgets.
Do not add individual passage patches or bulk-rewrite OCR. Constrained action-output
formatting is a separate shared interface defect, not a rules-data exception.

That next scope requires approval. Production remains `81e9eeb`, PID 24989, boot
14:01:12, with configuration, main source and imported summary-helper hashes unchanged.

## Evidence
Private data: `runtime/rule-review-integration-20261122/` (frozen set, raw Qwen drafts,
all handler results/traces, domain controls, tests, decoder parity, source hashes).
Harness/plan: `workfiles/rule-review-integration-20261122/`.
[Thinking-cap trial](2026-11-22-Thinking-Cap-Trial) and
[section-view pilot](2026-11-22-Section-View-Pilot) retain preceding evidence.
