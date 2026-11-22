---
title: General question-contract repair candidate — 2026-11-22
type: tooling-note
status: isolated-candidate-not-live
generated_by: openai/gpt-6.1-sol medium
generated_at: "2026-11-22"
---
Candidate commit **fa44f65**. No production activation.

# General question-contract repair — isolated candidate, NOT LIVE

## Built
One stdlib-only question contract consumes the existing ask-span extractor; no new
parallel entity database, answer table, book/page locator or PC-specific branch.
It records original text, preserved ask span, question kind, operation, requested
fields, structurally missing inputs and any nonfactual clarification.

Kinds distinguish rules mechanics, item properties, campaign scope, unavailable
private observations and unknown language. Shared operation grammar handles edition/
politeness framing. Unknown language retains the legacy path; an empty missing-input
list is NOT proof that all mathematical inputs exist. It performs no rule calculations.

`LIVE_WAKE_QUESTION_CONTRACT_ENABLED` defaults OFF. With it enabled:
- Mechanic operations reach the existing SR3 reader instead of gear-stat tables.
- Clearly unspecified tests ask which test/conditions; actual damage outcomes with
  missing inputs ask for effect/ratings/modifiers/resistance result, not a character.
- Unavailable private-roll requests do not become catalog-name guesses. Historical
  wiki/session requests and potentially available public rolls are not blanket-blocked.
- Explicit campaign scope, named campaign context, legitimate named-item properties,
  permission/revision boundaries and independent explicit-rule outage behavior remain.
- Host-scoped rules misses/abstentions use a rules boundary, not campaign/name wording.
- A general model instruction requires matching the requested mechanic/action/entity
  context, preserving conditions/units and honest citation uncertainty. This is NOT
  a deterministic semantic validator and is not claimed to solve source provenance.
- Generic owner-error reasons are retained privately instead of being lost behind
  the same spoken refusal. Endpoint, model, effort and serving permissions are unchanged.

## Verification
-128 focused unit tests, one skipped, no failures; additional equipment/evidence15,
  original query-extractor18/18, query-wiring32/32, emoji38/38, compile/diff checks pass.
  An initial unittest invocation discovered0 function-style query tests; the correct
  script entry points were then run. No full-suite all-green claim.
-8 actual gear/campaign/balance/profile/owner controls are byte-identical on gate off/on.
-Source-specific outage, scope, gate-off parity, no-reader clarification, exact-request
  metadata and model-policy default-off/on cases are exercised. No sources are inferred
  or granted by parsing, and nonfactual decisions never masquerade as factual evidence.

## Frozen12-case replay and retained attempts
Original same-author source-informed baseline7bed4be3…0345 remains unchanged. Earlier
candidate runs and failed tests remain in evidence. One pass suffered7 generic inference
transport errors; the new trace named them. A model-list GET later returned200, but that
alone does not prove generation health. Its created timestamp is NOT treated as a runtime
identity or restart proof. No provider restart or model change was performed.

One subsequent full baseline/candidate pair was run sequentially and retained:
-Baseline7/8 requested facts,4/8 strict context/printed-source clearance.
-Candidate6/8 requested facts,4/8 strict clearance. Ranged staging now answers, but
  spellcasting Drain and sustaining abstain under the general provenance instruction.
  This is a coverage tradeoff, not a claim of universal correctness improvement.
-Three missing-input/private-observation controls now give appropriate model-free
  decisions in roughly1–4ms at the handler boundary, not an audible-latency SLA.
-The fourth control gets a domain-correct SR3 boundary without inventing a bonus.
-Nondeterministic model content and transient transport failures are not attributed
  solely to the parser. No independent unseen acceptance set is claimed.

After that pair, a small host-abstention-wording correction was checked with focused
unit tests and the final acoustic run. The full12 was not rerun after that last wording
change: the paired artifact hashes identify the preceding revision; do not call it a
whole final-build replay. Factual routing/policy code was otherwise unchanged.

## Final controlled acoustic run
Seven declared cases: five exact prior WAVs plus two newly synthesized missing-input
controls from the original frozen set. Actual STT/public owner/readers/model/display/
capped Kokoro; mocked Discord, no human listening or live playback acceptance.

-Three answerable cases return the requested fact. Two have responsive verified
  source contexts; staging cites core124's melee-context continuation rather than the
  directly applicable ranged source113. Matching values do not clear that context gap.
-Three controls give relevant clarifications/refusals without inventing outcomes.
-The target-number control's synthetic my -> ma recognition fails the conservative
  missing-input parse and safely refuses instead of asking the ideal clarification.
  No one-off ma spelling accommodation was added.
-All7 display-format checks and response synthesis pass; WAV lengths5.325–15.35s.
  These are clip durations, not answer latency. Earlier source/prompt/transport failures
  remain visible; nothing is retried out of the scorecard.

## Decision and next recommendation
The general routing/clarification component is built for review; activation remains
separate. Do not claim general SR3 answering solved or activate as a broad rules rollout.
Keep citation/context uncertainty and lost useful coverage as explicit remaining gaps.

Do NOT add page124/page169 exceptions or force familiar rule answers. Next work should
be a general mechanic-aware evidence/claim contract and source-provenance design, with
representative source structures and independent cases reviewed before implementation.
Parser/query policy can route a question; prompts alone cannot certify that a passage
supports the requested rule. Latency and ASR robustness remain separate measurements.
No bulk database cleanup or source-rights expansion is recommended from these results.

Private evidence: runtime/general-question-contract-20261122 (test logs, preserved
intermediate text runs, sequential paired runs,8 preservation controls, acoustic WAVs/
traces, source hashes and final preservation receipt). Source harnesses live under the
matching workfiles folder. Production bridge81e9eeb/PID24989 and existing binding/env/
source corpus remain unchanged; no restart, deployment or provider change performed.
