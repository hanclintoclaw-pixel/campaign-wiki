---
title: Compact constrained review trial — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Compact constrained review — isolated experiment

## Shipped
Nothing deployed or integrated into the live bridge. Five exact prior review packets
were recovered through the existing authorized reader and matched their original
packet digests. They were frozen alongside the original 18 source-context proposals:
23 inputs, one verbose and one compact-constrained review per input, serially.
Paired-input SHA `b584285a…9e268e`. No retry-to-green, corpus rewrite or new grant.

Qwen-low's initial full-adapter task timed out after 89.8 seconds without code. A
smaller 6.1-second retry supplied the fixed JSON schema. Sol wrote the verification
harness and strict decoder; no untouched Qwen adapter implementation is claimed.
The schema encodes claim index plus applicability/entailment/qualification labels
as S/U/? in a bounded object, with extra fields forbidden. The existing model,
low effort, 512-token completion budget and 12-second transport deadline were retained.
The compact arm adds constrained output; the verbose arm does not. Both use the
same underlying rubric, sources, question and claims. No 25-second owner budget
was increased; these are review-only probes, not full voice turns.

## Measured
Four verification test methods pass for the schema/decoder, including malformed,
extra-field, duplicate-index and Boolean-index closure. Test import/exception
adaptations for the Sol harness are preserved alongside the original frozen tests.
The decoder preserves model identity, finish reason and usage; the existing
host binder still refuses truncated or wrong-model reviews.

The local endpoint accepted the constrained JSON-schema requests. Across the 23
paired packets, verbose review produced **14/23 structurally valid verdicts**;
compact produced **21/23**. Verbose had eight truncated completions and one other
malformed review; compact had two truncated completions. No transport timeout
reproduced in either arm, so this does not establish the cause of earlier failures.

On the unchanged original 18-proposal diagnostic:
- Supported proposals accepted: verbose **5/10**, compact **10/10**.
- Adversarial proposals accepted: **0/8 in either arm**. Seven had explicit rejection
  in each arm; the wrong-context staging case truncated in both, so it remains an
  unproven semantic control rather than a demonstrated rejection.
- Accepted-output precision within that set: verbose **5/5**, compact **10/10**.
  These small same-author figures exclude the separate exact-packet relevance miss.
- Median review-only wall time: verbose **8.85 seconds**, compact **7.52 seconds**.
  Observed ranges were 5.78–11.48 and 4.01–12.01 seconds respectively.

Crucial failure in the five exact prior packets: **both formats approved a claim
about Hacking Pool cyberware bonuses when asked how to calculate the pool**. The
facts were quoted correctly but did not supply the requested formula. Applicability
must include responsiveness to the operation/fields, not just the named mechanic.
The compact arm also accepted the two previously failed action/staging packets and
preserved the supported Control Pool-limit verdict; the manual-rigging packet
still truncated. These are proposal-admission results, not regenerated answers.

**Release decision: not ready for activation or integration.** Compact encoding
reduces output failures in this experiment, but neither schema validity nor a model
verdict guarantees that an answer actually answers the question. Next recommended
scope, awaiting approval: a general operation/field responsiveness contract and
cross-family negatives (e.g. a bonus instead of a calculation, a related effect
instead of the requested quantity), then retrieval/generation/review replay. No
individual rule/page exception or extra time budget; retain the failed cases.

## Still open
This is a source-informed, same-author diagnostic, not blind/unseen acceptance.
Baseline always preceded compact within each pair, so cache/load/order effects
limit causal latency claims. Review-only times exclude initial generation,
retrieval and audio. One provider/model reviewing its own generator is not an
independent correctness guarantee, even when the output matches a JSON schema.

Production stays `81e9eeb`; no configuration, model, source rights, restart, saved
audio or playback mode changed. The paused full deployment remains unapproved.
Local Qwen implementation remains preferred when it reduces paid Sol work; no
quantified savings are claimed without comparative incremental Sol accounting.

## Corrections
The [canonical-claims repair](2026-11-22-Canonical-Claims-Repair) remains isolated.
This experiment does not retrospectively turn its 1/8 answer coverage into a pass.
Private evidence is under data-tier `runtime/compact-review-20261122`; source plan,
Qwen-authored schema and Sol-authored probes are under project
`workfiles/compact-review-20261122`. This report is not a newly admitted voice source.
