---
title: Isolated unit adapter and real handler replay — 2026-11-23
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Unit adapter replay — useful known-case answers, NOT LIVE

## Built
Isolated candidate 8cf33e9 adds a request-local unit search/get prototype and a
host-side manifest/source verifier. Get requires a discovered nonce handle, exact
generation/revision and fresh host identity checks. Guessed IDs and foreign-turn
handles deny; mismatched generations are stale. Two searches/two reads are reserved
before execution, failures consume budget, and close invalidates handles. Returned
views are exact copies of the approved source blocks, not arbitrary file/page reads.

Host verification checks independent manifest digest, actual source bytes, record
and unit identity, reconstructed source spans, headings, text and views. These pure
Python components are trusted-host dependencies, not a sandbox against arbitrary
Python callers. No model-selected paths or backend URLs are accepted.

The public model gains an optional host-supplied unit projector; its default remains
None. The isolated single-turn test factory injects the verified unit reader and
only supplies actual reads to that projector. Quotes must occur inside one original
body block, never in metadata or across a join. Governing context comes from the
unit explicitly read. Initial prefetch is explicit and separate from the two
additional investigation reads; no hidden dependency expansion is performed.

This factory is a Core-rules-only test wiring, not a deployed multi-domain/concurrent
service route. Production routing, request lifecycle and deployment remain separate
acceptance work. No live source grant, config, model, deadline or service changed.

## Verification and authorship
Qwen-low drafted the adapter. Sol found a filename prefix, list/map mismatch,
whole-unit rather than bounded-view return, malformed-handle behavior and non-atomic
foreign-result handling. The sole Qwen repair returned only a filename. Sol corrected
the original draft, authored host validation and isolated wiring, and independently
verified behavior. This is not untouched-Qwen implementation. Raw failed drafts are
retained. No quantified paid-token savings claim is made.

- 11 adapter/host tests pass: exact bounded reads, request isolation, guessed handles,
  stale generations, counters, closure, freshness before/after work, atomic refusal,
  no returned-object mutation, manifest/source pins and tampered-view rejection.
- 23 existing bridge regressions pass. Four normal campaign/equipment handler pairs
  retain exact gate-off/on reply, speech and display parity. Those controls use the
  normal path, not the Core-only injected factory; mixed-domain unit routing is not proven.
- Compilation/diff checks pass, and handler-tested bridge source hashes match the
  committed candidate. The broad suite's previously recorded problems remain separate.

## New-phrasing applicability check
Eight questions were frozen before the adapter draft, with source-informed expected
units withheld from the implementer. This is new wording by the same author, not a
blind independent benchmark. Their applicable source was available within the two
actual read slots. The test then supplied controlled, source-backed claim proposals:
8/8 supported proposals accepted; 0/5 contradictory proposals accepted.

The retained original ranged-versus-melee proposal was explicitly rejected by the
reviewer using the original exact quote. The first harness attempt incorrectly used
an over-budget whole-unit quote; that structural failure remains saved. Only the
correct original quote was then tested, without repeating prior semantic judgments.

These are controlled applicability verdicts, NOT generated held-out answers. Every
review kept low effort, 128 thinking / 512 total tokens and the existing transport
limits. No review retry was made to replace a bad semantic outcome.

## Real handler replay
After the applicability gate, the unchanged 12-question known diagnostic suite ran
through the real thread handler, public owner, local Qwen action loop, source-backed
unit reader, evidence reviewer and real text/speech-selection emitter. Only Discord
transport was mocked; no operator CLI was allowed. It was an isolated single-turn
fixture using the selected eight-excerpt partition, not the live bridge.

**7/8 answerable questions produced correct useful answers with applicable citations;
all four ambiguity/private/unsupported controls stayed appropriate.** No wrong factual
answer was observed in this small set. The historical prior result was 0/8; this fresh
selected-path measurement is not a paired one-knob causal experiment or proof of
whole-library reliability.

Ranged staging recovered: after the wrong-mechanic initial hit, the model searched
for ranged-combat staging, read the applicable unit within the existing investigation
budget, and answered from Core printed p.113. First-hit ranking remains a real weakness;
it was not patched with a rule-specific exception.

The remaining action-phase miss failed exact-quote validation, then emitted malformed
action JSON after the existing correction nudge. Detection Factor also needed one
existing format correction before a valid answer. No additional outcome reruns were
used. The shared action-output contract is therefore the next clear repair target.

Factual-answer handler median: **9.25 seconds** across seven factual answers. Median
across all eight answerable cases: **9.64 seconds**; range **8.80–16.26 seconds**.
These are before TTS/Discord playback, not first-audio latency. Three missing-input/
private controls were model-free; the invented-pool refusal took 7.87 seconds.

No generated-answer held-out suite, STT, synthesis, actual Discord playback or human
acceptance was run. The known-case pilot threshold is met, but the complete release
gates are not. Live HEAD remains 81e9eeb; configuration, main source and imported
summary-helper hashes match the preceding checkpoint.

## Next recommended objective
Repair the shared action JSON/claim-envelope format behind an isolated gate, then
run generated-answer tests on the frozen new-phrasing questions and contrast controls.
Do not loosen exact quotes to manufacture success. Follow with multi-domain/session
unit-routing checks and audio acceptance before requesting activation. No individual
passage exceptions, larger deadlines, broader source grants or live cutover now.

## Evidence
Private runtime/unit-adapter-20261123: frozen questions/partition identity, raw drafts,
adapter and bridge tests, controlled proposal verdicts, retained failure plus exact
quote test, complete handler traces/emitted text/speech, domain parity and manifests.
Harness: workfiles/unit-adapter-20261123. Generic helpers are under
tools/rules_unit_prototype; the injectable projector is in voice_public_query.py.
[Source partition](2026-11-23-Reviewed-Excerpt-Discovery) and
[estimated completion checklist](2026-11-23-Unit-Relationships).

Scope superseded: [Fast equipment/wiki MVP](2026-11-23-Fast-Recall-MVP). General-rules work is parked as optional post-MVP work, not a 1.0 blocker.
