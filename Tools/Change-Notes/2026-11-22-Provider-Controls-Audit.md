---
title: Local provider controls audit — 2026-11-22
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Provider controls audit — no deployment

## Shipped
Read-only investigation and four inference observations; no production code,
configuration, model, effort, source grant, service or deadline changes. Sol performed
this bounded audit directly; no Qwen implementation job was needed.

The provider reports version `0.1.dev21810+g740e3776b.d20261009`. Its live OpenAPI
schema exposes `thinking_token_budget`, `include_reasoning`, `reasoning_effort`,
`max_tokens` and `max_completion_tokens`. Public upstream source at the reported
commit was inspected, not an independently attested copy of the running container.

## Measured
The current voice helper sends low effort and a total completion budget (review:
512 tokens). It does not forward a separate thinking budget. That total can be
consumed before any visible answer appears. Merely renaming the deprecated
`max_tokens` to `max_completion_tokens` does not establish a separate answer reserve.

Four serial observations kept model, low effort, 512-token ceiling and 12-second
client deadline fixed. Two inputs each ran with reasoning included, then hidden:

- Simple JSON control: both completed with the same visible answer, 25 completion
  tokens including 17 reasoning tokens. Hiding reasoning removed its response field,
  not its token cost. Wall times 0.743 and 0.569 seconds.
- Existing wrong-mechanic review packet: included reasoning exhausted all 512 tokens
  as reasoning, returned null content, and ended with length at 10.979 seconds.
  Hidden reasoning ended with stop at 0.961 seconds but also returned null content
  (59 completion tokens, 58 reported reasoning). Neither supplied a verdict.

This is four observations, not an acceptance benchmark or a causal speed comparison.
Order/cache effects remain. No transport timeout occurred in these four requests.
A stop finish reason alone is not proof of a usable answer.

Upstream serving code also makes `include_reasoning=false` set the engine's
`reasoning_ended` state before generation. With structured output this is not safe
to assume to be an inert display-only switch. The observed empty review reinforces
that hiding reasoning is not our proposed repair.

The distinct `thinking_token_budget` is passed into sampling parameters; upstream
sampling code tracks thinking and forces closing tokens at its limit. Enforcement
requires an active reasoning configuration and token markers. Schema exposure and
upstream tests do not prove enforcement for our deployed model. No thinking-budget
parameter was applied in this audit, preserving the approved no-budget-change scope.

## Still open
Next recommendation, requiring approval: an isolated capability trial with low
reasoning effort, the same 512 total tokens and existing 12-second transport limit,
comparing no explicit thinking cap against small positive thinking caps (128/256).
First verify actual enforcement and visible output on neutral controls, then replay
supported and wrong-mechanic packets. Keep all failures; measure complete verdicts,
false acceptance, answer retention and wall time. Unsupported or ineffective caps
stop the trial, not trigger a provider reconfiguration or a longer deadline.

This reserves a possible path to a final verdict; it does not prove semantic accuracy.
No integration or activation is recommended yet. The last full-handler result remains
one of eight answerable rules questions answered correctly.

## Corrections / timeout boundary
The helper aborts fetch after 12 seconds; Python permits 13 seconds for its child;
the owner has a 25-second overall deadline. Helper failures collapse into a generic
transport-unavailable error, so old generic failures cannot all be called timeouts.
Previous detailed probes did observe a fetch TimeoutError; this run did not reproduce
one. Server-side cancellation after client abort was not established. No deadline
increase or none/no-thinking request was tested or proposed here.

Production remains `81e9eeb`, PID 24989, boot 14:01:12, with the previously recorded
configuration, main source and imported summary-helper hashes unchanged.

## Evidence
Private artifacts: `runtime/provider-controls-audit-20261122/` on the data tier:
live OpenAPI, four raw observations, frozen review request, source snapshots and
manifest. Audit harness: `workfiles/provider-controls-audit-20261122/probe.mjs`.
Source references: upstream commit `740e3776b`, chat-completion protocol/serving,
sampling parameters, thinking-budget state and associated provider tests.
Prior checkpoint: [Section-view pilot](2026-11-22-Section-View-Pilot).

Follow-up: [Completed isolated thinking-cap trial](2026-11-22-Thinking-Cap-Trial). Integration still awaits approval.
