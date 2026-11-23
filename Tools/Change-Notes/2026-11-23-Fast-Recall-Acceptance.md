---
title: Fast recall candidate — representative acceptance passed, rollout pending
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Fast recall candidate: acceptance passed, rollout pending

## Activation update
Subsequently activated with GM approval. See [deployment and remaining voice check](2026-11-23-Fast-Recall-Activation).
The isolated measurements and rollout status below describe the earlier acceptance stage.

## Shipped
Documentation only. Isolated bridge candidate `6f88641` is committed, not activated.
The live bridge remains `81e9eeb`; its environment and checked source hashes are unchanged.
The new `LIVE_WAKE_FAST_RECALL_ENABLED` switch defaults off. No restart, source grant,
registry refresh or broad-rules deployment occurred.

The candidate normalizes spoken integer ratings against native catalog names without
removing grades or other identity qualifiers. It exposes six stock-deck fields through
the same generic parser: MPCP, Hardening, active memory, storage memory, I/O speed and
Response Increase. Audited source rows and pins are unchanged; no computed formulas.
Stock-item requests stay distinct from owned equipment and campaign-specific state.
Unsupported recognized narrow fields receive a brief nonfactual boundary rather than
an accidental model invocation. This is bounded grammar, not universal question coverage.

## Measured
Final same-author representative replay: **31 real-handler cases**, with actual readers
and text formatting but mocked Discord transport and inference forbidden:
- 23 source-backed factual outputs and 8 honest unsupported/refusal boundaries.
- Zero attempted inference calls, zero operator CLI calls, no runtime errors.
- All 12 previously direct baseline outputs preserved byte-for-byte.
- Handler median 0.652 seconds, range 0.089–1.002 seconds in this run.
  A development run also observed about 1.601 seconds; these are not latency guarantees.
- Wired Reflexes 2 cost now returns 165000 nuyen; Fairlight Excalibur MPCP returns 12.
- Covered wiki identities/status, current balances, ownership/inventory and qualifiers
  remain intact. Unmapped skills/attributes and owned-deck fields can quickly refuse;
  they are not silently replaced with stock-item facts.

Focused final suite: 21 tests pass. Earlier regression run: 114 tests, five skipped;
these overlap the focused suite and must not be summed as unique tests. Legacy Hassil
integration passes and speech-emoji checks pass 38/38. Diff whitespace/compile checked.
The final source-context examples were checked against audited NSRCG rows; printed
Core 302 witnesses the Wired Reflexes prices, and Core 207 witnesses the class-wide
stock-deck MPCP/header mapping. Native NSRCG source tags remain unchanged and are not
misrepresented as verified printed folios.

Four real prepared replies rendered successfully without spoken citations. Clip lengths
were 2.575–10.250 seconds. A standalone prewarmed worker using the real bridge synthesis
method rendered those four in 0.313–1.119 seconds, after separate 6.202-second worker
startup. Cold one-shot generation took 6.029–49.699 seconds, so warm/cold are not
interchangeable. These are component observations, **not STT-to-first-audio timings**.
No Discord playback or human listening was performed in this acceptance.

## Still open
- Approve a controlled activation of this candidate, preserving rollback and source pins.
- Verify the deployed switch/build and a short voice check of the changed rated-item,
  deck-field and honest-boundary paths. Prior human voice acceptance retains its scope.
- Then label the deployed supported equipment/wiki scope 1.0 if those checks pass.
  Current status is **MVP candidate accepted in isolation; live 1.0 not yet declared**.

Whole-entry text remains fuller than the explicitly partial spoken snapshot. This is
not a whole-catalog accuracy audit, blind independent evaluation, arbitrary wiki-field
extractor or guarantee that every phrasing avoids fallback. Broader interpretative
rules, semantic reviewers and full-library expansion stay parked post-MVP; they must
not tax deterministic lookup latency or block this release.

## Corrections
The first 29-case replay exposed an empty wiki-field lookup still attempting fallback;
the generic empty-result boundary was repaired before the final 31-case replay. Both
reports are retained. Local Qwen-low drafted the rating helper and attempted one repair;
Sol corrected remaining tuple/collision handling, integrated and reviewed the candidate.
This is not untouched Qwen implementation and no paid-token savings percentage was
measured. The original frozen contract used an earlier flag name; the final generic
flag name above supersedes it, without rewriting the original record.

Private evidence: runtime/mvp-fast-fields-20261123, including handler-proof/report.json,
summary.json, gate-final-tests.log, regressions.log, printed witnesses, audio-report.json
and warm-worker-report.json. Harnesses remain in workfiles/mvp-fast-fields-20261123.
These tooling notes are published documentation, not a new live voice source binding.

[Project MVP scope](2026-11-23-Fast-Recall-MVP) · [Change notes](../Change-Notes)
