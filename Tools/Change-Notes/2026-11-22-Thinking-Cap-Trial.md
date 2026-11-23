---
title: Isolated thinking-token cap trial — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Thinking-cap trial — promising, NOT LIVE

## Shipped
An isolated measurement harness and independent Sol scoring; no bridge integration,
configuration change, restart, new source grant or activation. Qwen was the local
reviewer under test, always low effort. No delegated implementation job was needed
for this measurement-only step; paid-token savings were not quantified.

All 42 inference calls retained the fixed model, 512 total completion-token limit,
12-second transport timeout and included reasoning metadata. The only experimental
parameter was a positive thinking-token cap: absent, 128 or 256. No none/no-thinking
mode, longer deadline or larger total completion budget was used.

## Measured
Six neutral arithmetic calls ran first. Both caps were accepted by the provider.
On the longer control, reported reasoning reached 127 and 255 tokens under the
128/256 caps, versus 509 uncapped. This supports active enforcement on this deployment,
not merely schema acceptance. The short arithmetic control completed correctly in
all arms without reaching the caps. The uncapped longer control exhausted 512 total
and returned an incomplete integer. The 256 arm reached the correct final number
but included unwanted continuation prose; it did not follow the integer-only format.
Thus thinking-cap enforcement alone is not output-quality acceptance.

Before evidence calls, 12 existing source-reviewed cases were frozen: six supported,
six misleading, spanning actions, combat staging, Drain, Hacking/Control Pool and
cyberware bonuses. All used the same revision-bound section-view evidence and strict
responsive-verdict schema. No source content or case-specific parser was changed.
Each case ran in all three arms; arm order rotated across cases. These are previously
seen, selected controls, not an unseen benchmark or independent real-world sample.

Thirty-six review calls produced:

- Uncapped: 10/12 complete verdicts, 6/6 supported proposals accepted; four misleading
  proposals explicitly rejected and two truncated. No misleading proposal accepted.
- 128 cap: 12/12 complete verdicts, 6/6 supported accepted; five misleading proposals
  explicitly rejected and the wrong-mechanic staging proposal marked uncertain.
- 256 cap: the same acceptance/verdict counts as 128.
- Neither capped arm accepted any of the six misleading proposals. Both completed
  the previously truncated formula-versus-bonus and wrong-mechanic checks. The former
  was explicitly rejected; the latter remains uncertainty, not proof of semantic rejection.
- Median reviewer wall time: uncapped 7.240 seconds, 128 cap 2.821 seconds, 256 cap
  5.682 seconds. No transport errors/timeouts in this run. Maximum reported reasoning
  was 512, 127 and 255 respectively.

These are review-only measurements, not end-to-end voice latency. Rotating arm order
reduces one obvious ordering bias but does not remove cache, scheduling or sampling
variation. One call per case/arm is not a reliability estimate. No STT, synthesis,
Discord playback, full handler or new human acceptance test was performed.

## Corrections
Initial scoring treated all non-supported per-claim labels as explicit rejection.
Sol's raw-verdict inspection found the staging result was uncertain. The scorer was
corrected, an uncertainty regression added, and all saved responses rescored without
rerunning inference. The progress update was corrected in-thread. Eight scorer
verification methods now pass; Node syntax and frozen request invariants pass.
No failed model outcome was replaced by a retry.

## Still open / recommendation
Use the 128 cap as the next isolated integration candidate, not a live setting.
With separate approval: Sol specifies the shared transport/reader contract; local
Qwen-low implements a bounded default-off patch; Sol independently reviews it and
reruns the frozen full-handler rules/negative controls plus campaign/equipment
regressions. Integrate the compact responsive verdict and approved section-view
prototype without widening source discovery or read budgets. If current per-turn
admission cannot authorize a view, retain an honest boundary rather than grant it.

The purpose is to discover whether better reviewer completion actually improves
answers within the existing whole-turn deadline. Preserve evidence checks, whole
qualified speech and the current model. No per-page/rule exceptions, bulk corpus
rewrite or activation. Last full-handler acceptance remains 1/8 until a fresh
integration replay proves otherwise. Unconstrained answer generation needs its own
format/fidelity checks; this review trial does not validate it.

Production remains 81e9eeb, PID 24989, boot 14:01:12; configuration, main source and
imported summary helper hashes match the preceding checkpoint.

## Evidence
Private data: `runtime/thinking-cap-trial-20261122/`: frozen neutral and review
requests with hashes, all 42 raw results, corrected scores, summary and manifest.
Source harness: `workfiles/thinking-cap-trial-20261122/` (run, prepare, score).
[Provider audit](2026-11-22-Provider-Controls-Audit) and
[section-view pilot](2026-11-22-Section-View-Pilot) describe prior limits.

Follow-up: [Isolated full-handler integration failed release acceptance](2026-11-22-Rule-Review-Integration). No activation.
