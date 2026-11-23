---
title: Operation and field responsiveness trial — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Operation/field responsiveness — isolated trial

## Shipped
Nothing integrated or activated. Qwen-low's initial function-writing task timed out
after 74.9 seconds. A smaller 29.8-second retry supplied declarative generic
operation/field patterns. Sol wrote the verification interpreter, review envelope,
decoder and tests. This is not represented as an untouched Qwen implementation.

The existing ask-span extractor feeds calculation, quantity, permission, rounding,
procedure, property-lookup or unknown requirements. These are fallible hints, not
rules facts, completeness proof or source access. No book, page or character branch.
The original question remains authoritative when a grammar hint is wrong.

The responsive arm adds a whole-answer S/U/? verdict: do the joined claims answer
the requested operation and material fields? True facts about a related subject are
insufficient. Context cannot supply an answer absent from the claims. Supported
responsiveness is required in addition to all existing per-claim applicability,
entailment and qualification checks. Missing, malformed or incomplete verdicts
refuse. Endpoint/model, low effort, 512 tokens, 12-second transport limit, source
rights and exact-quote checks are unchanged; no extra call or timeout increase.

## Measured
Frozen inputs: previous 23 proposals plus eight cross-family contrasts, 31 pairs
and 62 review calls. Input SHA `3c096e1f…e1adca1`. New contrasts distinguish bonuses
from a base calculation, Free Action timing from a Simple Action count, a dice cap
from permission to use the pool, and a modifier from a requested attribute. Each
has a responsive counterpart using the same source and claim; pages are not banned.
These are same-author/source-informed controls, not independently unseen tests.

Eight verification unittest methods pass, including the frozen generic-operation
cases and strict whole-answer verdict handling. The frozen test content was moved
into the experiment directory, with an interpreter import shim; it was not shipped
as a nonexistent runtime module. The Qwen-authored patterns and Sol adapters are
separately attributable in the source harness.

Across the 14 scored supported proposals (original ten plus four responsive
counterparts), **both arms accepted 14/14**. Across the 12 scored negative proposals,
compact accepted **2/12** and responsive accepted **1/12**. Accepted-output precision
within those scored controls was **14/16 (87.5%)** and **14/15 (93.3%)**; the five
exact prior packets are excluded from these figures. Neither rate is release-grade.

The new four responsiveness negatives had one false acceptance in compact and zero
in responsive. Responsive explicitly rejected three; the attribute/modifier case
truncated in both arms, so it is not a proven semantic rejection. All four responsive
counterparts were accepted. The new base-calculation/bonus contrast received an
explicit unsupported responsiveness verdict. The original captured formula/bonus
packet was blocked only by truncation, not by a completed semantic judgment.

Both arms **incorrectly accepted the original melee-staging quotation for a ranged
attack question**. An applicable numerical value is not applicable-source evidence.
The original wrong-Drain context and six other original negatives were explicitly
rejected; the staging false acceptance is retained, not tuned away or retried.

Compact had one truncated completion; responsive had two. Median review-only wall
times were **6.99 seconds** and **8.63 seconds** respectively. The responsive contract
therefore did not improve observed median speed. No full-handler replay was run.

**Release decision: fail; no integration or activation.** A bounded inspection of
the missed staging excerpt found a page beginning mid-section, with a ranged-combat
cross-reference, a Melee Modifiers reference, and later mixed-mechanic material.
That is evidence of an ambiguous review window, not a diagnosis of the whole corpus.
Next recommended scope, awaiting approval: a read-only audit of parent headings,
section ancestry and mixed-mechanic windows across representative rule families,
then propose a general section-aware reader/source metadata standard if warranted.
Do not ban a page, hardcode a rule answer, bulk rewrite sources or add another
prompt-only patch on the strength of this one case.

## Still open
The operation hints and responsiveness verdict remain probabilistic semantic
machinery, not an independent correctness oracle. A refusal caused by a truncated
verdict is not a demonstrated semantic rejection. Positive coverage matters too.
Compact always preceded responsive within each pair; cache/order effects limit
causal timing comparisons. Review-only measurements are not voice latency.

Production remains `81e9eeb`. No configuration, live source, model, permission,
restart or audio change. No full-handler, STT or listener acceptance is claimed.
Local Qwen tokens are not paid Sol tokens; the aim remains reduced paid Sol work,
without claiming quantified savings from unavailable comparative accounting.

## Corrections
This follows the [compact-review experiment](2026-11-22-Compact-Review-Trial), not a
deployment. The last actual handler replay remains 1/8 answerables; proposal-review
scores do not replace it. Private evidence is under data-tier
`runtime/answer-responsiveness-20261122`; the plan, declarative patterns and Sol
harness are under project `workfiles/answer-responsiveness-20261122`.

## Subsequent read-only audit

The [source-context audit](2026-11-22-Source-Context-Audit) supports a general reader-view pilot, not a corpus rebuild. No candidate implementation or activation followed automatically.
