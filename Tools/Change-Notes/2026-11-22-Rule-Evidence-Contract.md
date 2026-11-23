---
title: General rule evidence and provenance candidate — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
status: isolated-candidate-not-live
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# General rule evidence/provenance — NOT LIVE

## Shipped
Nothing deployed. Isolated candidate `d43411c`, built on parser candidate `fa44f65`,
adds `LIVE_WAKE_RULE_PROVENANCE_ENABLED`, default OFF. Production stays `81e9eeb`.

Every proposed claim must bind to an exact quote from an already-authorized read at
the discovered revision. All answer prose must belong to those claims. Citation
labels come from the host, not the model; detected OCR folios are not independently
verified PDF citations. Conditions, units and exceptions must fit the whole answer;
speech omits citations but never chops off a qualification to meet a shorter cap.

One separate review request to the same configured Qwen model at low effort judges
mechanic applicability, quote entailment and qualifications. Unsupported, uncertain,
malformed, truncated, wrong-model or failed reviews refuse. The existing 25-second
overall deadline remains. No source expansion, corpus rewrite, endpoint/model change,
production restart or page/character/mechanic-specific exception was introduced.

**This reviewer is probabilistic and shares the generator's model. It is not an
independent authority or a guarantee of correctness.** Quote matching establishes
provenance, not semantic applicability. Source strings remain untrusted data.

## Measured
Frozen same-author/source-informed admission diagnostic: 18 proposals across four
rule families, ten supported and eight context/value/qualification mutations.
The same passages are positive for their proper mechanic and negative for another;
no passage ban. Fixture SHA `d5163891…b30acb`, frozen before implementation.

- Supported-proposal acceptance: **5/10**.
- Adversarial-proposal acceptance: **0/8**. Four received explicit unsupported
  judgments; four failed transport and do **not** prove semantic discrimination.
- Accepted-output precision: **5/5** on this small diagnostic, not general acceptance.
- Across all 18: eight transport failures and one completion exhausted its 512-token
  budget in reasoning without a visible verdict. Root cause of transport failures
  is unclassified. No semantic retry-to-green or passage-specific prompt tuning.
- Review-only observed wall time: **6.7–12.1 seconds**, excluding retrieval, initial
  generation, synthesis and playback. The final negative case overlapped the start
  of the handler replay; this was not a fully load-isolated benchmark.
- Focused unit/controlled-loop tests: **140 run, one skip, no failures**. They exercise
  quote/revision/claim mutations, malformed review output, semantic rejection,
  transport/deadline closure, gate-off parity and the real speech selector.
  Syntax/diff checks pass. Known full-suite issues are not claimed fixed.

Full existing-handler replay of the unchanged 12-case baseline (real readers/model,
mock Discord): **0/8 answerable questions produced a factual answer**; all four
missing-input/unsupported/private-observation controls stayed nonfactual. Three
positive turns hit the overall deadline; the other five refused or errored safely.
Positive-turn handler times were **12.9–25.0 seconds**, not first-audio latency.
Five positive turns needed a claim-format correction; two then had insufficient
remaining review budget. No supported live-generation improvement is demonstrated.
This failed release criterion, despite passing unit tests and accepting five
preconstructed proposals. No fresh paired-parent run establishes a causal delta.

## Still open
**Not ready for activation.** The structural contract is implemented, but useful
coverage and latency do not meet the casual voice goal. The two critical
wrong-mechanic comparisons failed transport rather than receiving semantic verdicts.

Next recommendation: diagnose bounded visible-output/transport reliability at the
fixed inference boundary, then rerun the frozen controls serially without wider
deadlines, extra source permissions or passage exceptions. Only then evaluate
end-to-end answer coverage and latency for a possible pilot. Do not mistake a
refusal for a correct answer or a successful structural check for semantic proof.

## Corrections
This supersedes no live deployment. The [parent parser candidate](2026-11-22-General-Question-Contract)
remains isolated too. Earlier reported facts and source-context errors remain in
the [baseline](2026-11-22-SR3-Rules-Baseline); no retrospective success claim.

Private evidence is preserved under data-tier `runtime/rule-evidence-contract-20261122/`;
source harness under project `workfiles/rule-evidence-contract-20261122/`.
All attempts are retained. No new acoustic replay, synthesis, Discord delivery or
human playback acceptance is claimed for this candidate. The source-only shape
hardening after handler startup is covered by final unit tests, not described as
a fresh full-code handler replay.

## Subsequent diagnostic trial

The [Sol–Qwen–Sol trial](2026-11-22-Qwen-Diagnostic-Trial) classifies the retained failures; it does not change the failed release decision.
