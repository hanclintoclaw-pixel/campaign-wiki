---
title: Sol–Qwen–Sol offline diagnostic trial — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Offline diagnostic trial

## Shipped
No live changes. Isolated commit `79e195f` adds a pure offline telemetry classifier
and Sol-authored independent tests to the evidence-candidate branch. Qwen authored
the implementation and sole correction; Sol specified, recovered, reviewed and
assembled it. Code model: `dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4`,
requested low reasoning. No per-rule, passage, book or character branches.

## Measured
Sol froze 21 withheld acceptance fixtures before Qwen ran (SHA `c1a8531b…f9a5168`).
First Qwen run timed out at 179.9 seconds after ten tool calls despite a text-only,
no-tools request. Its temporary source was recovered from sanitized session history,
not rewritten by Sol. It passed 21 fixtures but failed independent review: it
incorrectly classified error-like fields and unrelated events as transport failures.
Two additional review cases captured those defects. A collector follow-up was
refused because collectors are one-shot; no model repair ran through that attempt.

The sole allowed repair was a new bounded Qwen patch-only run, completing in 4.7
seconds with a visible replacement and no tool calls in its returned history.
Final code: 93 lines, SHA `0483f7a3…4a30e46`. All 23 fixtures passed, plus eight
malformed-input checks. Fifteen focused unittest methods including evidence-loop
regressions passed; compile/diff checks passed. Source retains a harmless unused
transport helper from the first draft; no extra cleanup/retry was spent on it.

Offline classification of the existing 12-case handler replay found, among eight
answerable turns: three explicit transport errors; five invalid claim envelopes;
three turn timeouts; two review-budget shortages. Signals overlap. No semantic
review succeeded in those turns. Four other nonfactual controls are unclassified
by this narrowly scoped tool, not labeled failures. No new model-answer, acoustic,
playback or end-to-end success evidence was produced by classifying old logs.

## Still open
Functional helper: **pass after one correction**. Initial delivery/instruction
following: **fail**. Cost savings: **unproven**. Exact model-token totals and
incremental Sol planning/review usage were unavailable in these run receipts;
elapsed time is not a substitute. There was no matched Sol-only cost baseline.
Use tiny patch-only jobs if continuing this architecture; prompting alone did not
enforce a tool sandbox. Independent review caught what the initial tests missed.

Recommended next repair, awaiting approval: remove the redundant free-text answer
representation and render directly from the validated canonical claim list. Preserve
quote/revision/qualification checks and the existing deadline; compare the same
frozen cases before considering activation. Five format retries motivate testing
this general simplification, not a guarantee of recovery. Separately diagnose the
three transport errors; their server/network/decode root cause remains unknown.

## Corrections
This trial does not fix or activate the [evidence candidate](2026-11-22-Rule-Evidence-Contract).
Its 0/8 answerable result still fails the table-experience goal. Production remains
`81e9eeb`, PID 24989, with unchanged configuration. Source harness and private
evidence use `workfiles/rule-diagnostic-qwen-20261122` and data-tier
`runtime/rule-diagnostic-qwen-20261122`. Planning/report/tests are Sol-authored;
the classifier and correction are Qwen-authored. The watcher registration was saved,
but scheduler verification was denied by this turn's automation authority; results
were explicitly collected and delivered in the parent turn instead.

## Subsequent approved repair

The [canonical-claims repair](2026-11-22-Canonical-Claims-Repair) is built and tested in isolation; broad voice acceptance still fails.
