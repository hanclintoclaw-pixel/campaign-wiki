---
title: Canonical-claims repair — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Canonical-claims repair — isolated

## Shipped
Nothing deployed. Candidate `ffd5fe5` builds on the isolated evidence branch.
Qwen-low authored the validator and action-loop changes. Sol wrote the specification
and tests, reviewed the code and assembled the patch. The generator now supplies
one canonical claim list; the host joins its complete texts for display and speech.
Redundant legacy answer text is ignored, including contradictory or malformed text;
it cannot enter the review packet, rendered answer or speech. Gate-off behavior
retains the legacy answer path. Missing/malformed claims fail closed.

Quote/read-revision/citation/status/length checks, semantic review, source permissions,
model/effort and overall deadline are unchanged. No facts, names, page exceptions,
extra retry or budget increase. The redundant-field mismatch no longer causes a
format-repair round trip; other evidence failures are still not bypassed.

## Measured
Three new acceptance methods were frozen before implementation; their initial
suite failed, then passed after the patch. Final focused suite: **146 tests run, one skip, no failures**; compile/diff
checks pass. Actual model-loop controls demonstrate one generation plus one review
for absent or contradictory legacy text, with complete qualifications preserved.

Qwen's first patch draft arrived in 101.6 seconds but invented an incompatible
citation-object schema in its prompt. The sole allowed correction took 10.4 seconds
and restored string citations, but added an unsupported private-source example.
Sol removed that example and clarified top-level fields during review; these prompt
edits are explicitly Sol-authored, not represented as untouched Qwen output.

Unchanged 12-case real-handler replay (actual readers/local Qwen, mocked Discord):
**1/8 answerable questions answered correctly**, with all four nonfactual controls
appropriate. The accepted Control Pool limit preserves the base-skill-dice cap and
applicable Core printed p.44 citation; its complete speech omits the citation.
Five proposals reached structural eligibility; none failed duplicated-text matching.
Two other proposals failed exact-quote checks, which were not weakened. Five reviews
finished: one supported, two transport-unavailable and two truncated. Two positive
turns hit the overall deadline; one ended at the generic error boundary. Positive
handler wall times were **14.6–25.0 seconds**, not first-audio latency.

Compared with the previous historical run's 0/8, this run produced one useful answer.
There was no freshly paired parent replay, so do not attribute every timing or
coverage difference causally to this patch. The observed absence of text-mismatch
retries and controlled-loop tests establish the narrower structural repair.
**Activation remains rejected:** 1/8 is far short of the conversational goal.
Next proposed work, awaiting approval: replay the exact failed reviewer packets,
separate transport causes from truncated verdicts, and investigate a compact,
provider-supported constrained-output contract without changing model/effort,
source permissions or the overall deadline. Do not increase timeouts blindly or
replace semantic checks with passage whitelists.

## Still open
Local Qwen usage is not paid Sol usage. The optimization target is reduced paid Sol
work; local generation may use more tokens. Exact savings are unmeasured without
comparable incremental Sol usage, but small real savings remain worthwhile under
the GM's standing preference. Preserve independent review rather than transferring
acceptance to the implementing model.

This change removes redundant representation, not semantic uncertainty or transport
failures. The production service stays `81e9eeb`; no activation or restart is implied.
No new synthesis, STT, Discord delivery or human hearing acceptance is claimed.

## Corrections
This supersedes the duplicated-text requirement in the [earlier evidence prototype](2026-11-22-Rule-Evidence-Contract),
not its failed release decision or retained measurements. The [diagnostic trial](2026-11-22-Qwen-Diagnostic-Trial)
remains an offline tool. All attempts are retained under data-tier
`runtime/canonical-claims-20261122`; source harness and plan are under project
`workfiles/canonical-claims-20261122`. Tests/report are Sol-authored; core patch is
Qwen-authored with the disclosed prompt edits. This report is not itself admitted
as a live voice source.
