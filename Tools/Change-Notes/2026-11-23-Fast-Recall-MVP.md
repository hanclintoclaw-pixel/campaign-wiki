---
title: Fast equipment/wiki recall MVP — project refocus
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# MVP: fast equipment and wiki recall

## Authoritative scope reset
GM clarification at 11:14: the Minimum Viable Product is fast equipment/wiki recall.
Broad rules interpretation and the experimental general-rules reader are optional
post-MVP goals. They are parked, not prerequisites for 1.0. Preserve their work;
do not keep adding those milestones to the MVP's blocking checklist.

The product should return a short source-backed equipment fact/entry or covered wiki
fact quickly, or a short honest clarification/refusal. A slow general model/reviewer
must not be placed in front of deterministic lookups. Citations remain visible in
text, not narrated. Preserve uncertainty, current-balance qualifiers and exact field
meaning; speed is not permission to invent a value.

## Readiness decision: MVP candidate, not 1.0 yet
The existing system already has useful live equipment and wiki foundations, including
human-accepted equipment and campaign-summary voice pilots. It does not need another
general-rules research phase to establish that value. But a fresh bounded diagnostic
found two ordinary narrow requests still reaching interpretation rather than a fast
answer/boundary. Do not stamp general fast-recall 1.0 while silently retaining those
slow-path gaps.

Fourteen diagnostic questions were frozen before the read-only check, using the
live-bound lookup configuration with all experimental general-rules flags off:
- 12/14 had a deterministic response ready at initial lookup: 11 source-backed factual
  outputs and one honest refusal. The refusal is not counted as a factual answer.
- Eight sampled wiki requests were direct: identity for Curtis, Mevin, Valgaut and
  Kyron; Dolly status; Curtis nuyen; Kurgan Karma; Mevin gear. They retained provisional,
  partial-inventory and balance qualifiers rather than claiming universal coverage.
- Three sampled equipment requests returned direct Predator damage, cost and snapshot;
  the generic Ingram Smartgun request promptly refused an unverified subject.
- Wired Reflexes 2 cost and Fairlight Excalibur MPCP returned interpretation-required
  results, not deterministic answers. This diagnostic did not execute their model
  fallback or grade a generated answer.

Direct wiki initial-lookup times were 0.364–0.441 seconds; direct equipment response
paths were 0.177–0.967 seconds. The two interpretation-required initial lookups took
1.543 and 1.848 seconds, before any fallback model. These are single observations,
not a latency guarantee or percentile. They exclude STT, TTS and playback. Today's
check is routing/source-output evidence, not a new independent accuracy certification
or human audio acceptance. Prior tests and live approvals retain their original scope.

This is a small diagnostic, not all-catalog or whole-wiki coverage. Existing structured
wiki profiles extend beyond the four table-reference summaries, but arbitrary fields
are not thereby proven fast. Missing data must remain honest missing data.

## Blocking 1.0 checklist — narrow and finite
- Done: existing equipment cache/parser, covered wiki profiles/status, balances and
  ownership/inventory paths, speech shaping and live voice foundations.
- Open: diagnose and repair generic entity/rating/field coverage or routing causing
  the two demonstrated slow-path cases. No item/PC-specific answer branches.
- Open: ensure unsupported narrow requests receive a quick honest boundary instead
  of an accidental lengthy interpretative answer. Preserve explicit ambiguity.
- Open: a representative frozen equipment/wiki acceptance pass covering whole-entry
  snapshots, individual fields, identity, status, ownership, balances and safe misses;
  record useful factual answers separately from appropriate refusals.
- Open: check answer fidelity against the selected structured/wiki source and measure
  lookup/handler versus STT/audio separately. Reuse prior human acceptance honestly;
  ask for another voice check only where a changed path lacks audio evidence.
- Then: record supported coverage and known limits, and declare 1.0 after acceptance.
  A version label does not require generic rules, every sourcebook, every wiki field,
  a corpus rewrite or completion of all long-term work. Activation of any code/config
  change remains a separate explicit step.

## Parked post-MVP work
General rules units, semantic evidence-review research, broad interpretative questions,
expanded book coverage and the earlier generic action-schema/rules pilot are optional
ancillary work. Their historical 7/8 known-case handler result is not an MVP blocker
and should not be confused with equipment/wiki speed. Broader standardization can
continue later where real use demonstrates a need.

The earlier 1–3-day estimate concerned the Core rules diversion, not this refocused
MVP. It is superseded as a project schedule. No replacement calendar promise is made
before the two narrow routing/field gaps are diagnosed. No new live code, source grant,
configuration, restart or audio playback was performed in this refocus.

## Evidence and navigation
Private runtime/mvp-check-20261123: frozen 14 questions and initial lookup results.
Harness: workfiles/mvp-check-20261123/check.py. Source outputs preserve the active
reviewed-table/NSRCG/public-wiki provenance; a source tag is not a verified printed page.
[Live summary milestone](2026-11-22-Four-Summary-Live-Pilot) and
[parked ancillary unit-adapter checkpoint](2026-11-23-Unit-Adapter-Replay).
