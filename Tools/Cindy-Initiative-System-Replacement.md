---
title: Cindy Initiative System — Replacement Project
type: documentation
visibility: player-safe
canon_status: tooling-reference
status: legacy-monitor-disabled
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Cindy Initiative System — Replacement Project

## Mandate and current authorization

**Cindy Initiative System 1.001: staged, NOT enabled. GM has authorized activation, but final reviewer checks failed the current quality labels; activation is held pending GM judgment. The next voice session will not run the new worker yet. Legacy monitor remains disabled.**

GM direction, November 23, 2026:

1. Remove the entire old Cindy Initiative System. It is broken and unwanted; this is a replacement, not a tuning exercise.
2. Develop new logic for useful initiative using available local tools, including Qwen.
3. Test the replacement, then stand it up after approval.

Sol medium in the project channel owns planning and final evaluation. Local Qwen low is the preferred implementation and test worker on the box. This page records the requested destination and a proposed path; dated decisions below distinguish the completed offline trial from unapproved live deployment.

Source: GM request in Discord project thread `1574141376038436974`, message `1574522348646957097`. Operational framing below is a proposal for GM review, not campaign canon.

## Scope and protected boundary

The initiative system decides whether Cindy has a worthwhile, unsolicited contribution to offer the GM during play. It must earn the interruption, help the scene, and preserve player agency.

This project does **not** reopen the [accepted, hard-parked voice recall 1.0 project](Change-Notes/2026-11-23-Voice-1.0-Hard-Park). Preserve direct wake replies, equipment/wiki lookup behavior, source permissions, transcription, saved-voice playback, TTS, and watchdog/session lifecycle services. Direct questions to Cindy remain the responsibility of the direct-response path, not a proactive-ping quota.

The bridge is shared infrastructure. A separate module or worker is preferred, with a small explicit bridge adapter, bounded resources, and no blocking model work on the reply path. A shared process restart still affects both systems and needs coordinated approval. Publication of this page does not wire it into the voice index or change runtime behavior.

## Retirement means removal

After authorization, inventory the full legacy initiative dependency graph against the then-current bridge revision. Remove its decision/proposal logic, canned proposal/line banks, obsolete configuration, state, emission hooks, documentation instructions, and tests that enforce the discarded behavior. Retain historical evidence in version history; label old guidance superseded rather than leave it appearing current.

A narrow read-only source check at bridge revision `6f88641` still finds `_decide_ping_state`, `_derive_cindy_initiative_proposal`, `_format_cindy_initiative_ping`, `_MONITOR_PREPARED_VOICE_LINES`, and the `cindy_live_initiative` clip prefix. These are starting points, **not a complete deletion manifest**. Shared helpers must be traced before deletion: preserve or relocate functionality used by direct requests, capture, playback or genuine health alerts.

No permanent legacy fallback, hidden compatibility mode, or second initiative emitter. An independent operational off switch for the replacement is appropriate; keeping the old proposal engine underneath it is not. Removal may be delivered before the replacement; temporary absence of proactive initiative is preferable to retaining the broken engine. Sequence and any live retirement require approval.

## Proposed replacement behavior

### Listen, understand, propose, validate, offer

1. **Observe:** consume new transcript events with stable session/event IDs and timestamps. Start with roughly 30 seconds of fresh speech, retaining roughly three minutes of bounded scene continuity. These are starting design values, not newly applied settings.
2. **Track scene state:** maintain a compact, evidence-linked summary of the present goal, plans under discussion, unresolved asks, relevant known capabilities, and what has already been offered or dismissed. Distinguish transcript observations, retrieved facts and model inferences. Expire stale state at scene/session boundaries.
3. **Route direct invitations separately:** explicit requests for Cindy's input go to the established direct-response route, including during table talk. Name mention alone is not an invitation and does not justify a proactive ping. Avoid double-handling the same utterance.
4. **Assess opportunity with local Qwen:** ask whether a concrete, timely, optional contribution exists. Return a small structured candidate or an explicit no-action verdict. Do not force every window into one of the old four canned categories.
5. **Validate outside the model:** check current session, fresh evidence references, source disclosure, capability support, duplicates, prior GM dismissal, rate budget, expiry and output schema. Model confidence is not permission. Timeout, outage, malformed output or missing evidence means no unsolicited message, with a private diagnostic reason.
6. **Offer to the GM:** concise trigger, proposed move, why it matters now, uncertainty and optional ready-to-play line. Use the approved GM-only destination and a real GM mention. Never expose private source material to players or auto-execute the proposal.
7. **Respect disposition:** approval, dismissal and expiry update state. Do not repackage the same rejected suggestion with new wording. GM approval to share a line is not blanket authority to spend resources, hack a host or control an NPC asset.

Useful openings include a concrete Matrix/security blind spot, passive surveillance, a public-presence distraction, a real stall Cindy can unblock, or a strongly relevant NPC observation. Mere keyword matches, generic commentary, repeated reminders and inventing capabilities are not initiative.

Default posture remains conservative but not inert: roughly zero to one unsolicited suggestion per session, with any expanded activity explicitly under GM control. Silence is valid when no worthwhile opening exists; universal silence is not a successful replacement. Saved speech may be prepared through the existing approved interface after a candidate is admitted; no unsolicited automatic playback.

### Tool and model boundaries

- Qwen receives a bounded context packet and may request narrowly scoped, read-only evidence through an allowlisted interface. No shell, arbitrary filesystem access, deployment authority or Discord-send authority from model-generated text.
- Ground capability claims in the approved current character/asset references; ground rules in SR3 only. Unknown capability or uncertain evidence stays uncertain or suppresses the suggestion.
- Transcript text and retrieved content are untrusted data, never instructions granting new tools or access. Preserve existing source/revision and audience boundaries.
- Use a bounded queue, deadline, cancellation and stale-result checks. Direct replies take priority over background inference; test contention on the actual local endpoint. No silent paid-model fallback.
- Record candidate evidence, verdict, suppression reason, timing, model identity/effort, GM disposition and delivery receipt privately. Do not publish raw session transcripts or private prompts on this wiki.

The exact prompt, schema, context budgets, scheduling and deployment shape remain design decisions to settle in the approved design phase, not facts established by this charter.

## Work allocation

**Sol medium:** define behavior and interfaces, freeze acceptance criteria, review safety boundaries and diffs, independently evaluate held-out results, recommend go/no-go, and maintain the living guidepost.

**Local Qwen low:** implement bounded patches in an isolated checkout, write/run specified tests and replay harnesses, report raw failures and return reviewable artifacts. Never use Qwen medium/high. Break work into small deliverables instead of open-ended autonomous repair. Worker self-reported success is not acceptance.

**GM:** approve design and phase transitions, judge usefulness and character fit, authorize visible trials and live activation. Sol's recommendation does not replace GM deployment approval.

Optimize for reduced paid Sol usage, not fewer combined local-plus-hosted tokens. Log model usage where available; do not claim savings without a measured comparison. Sol corrections to Qwen work must be identified rather than attributed to Qwen.

## Phases and approval gates

1. **Charter review — current phase.** Publish this document; agree on scope and the next authorized step.
2. **Read-only inventory and design.** Map legacy ownership/shared seams, current routes and runtime revision; produce a deletion manifest, replacement interface, resource limits, private replay set and rollback plan. No code changes implied by inventory approval.
3. **Isolated retirement and implementation.** After approval, Qwen removes the legacy system and builds the replacement in reviewable increments. Sol reviews the complete diff against the protected voice baseline. No live edits or restart.
4. **Offline evaluation.** Run deterministic tests, real local-Qwen replay, held-out scenes and direct-reply regressions. Preserve all attempts, including malformed outputs, timeouts and misses. Failed acceptance returns to bounded repair, not deployment.
5. **Shadow observation.** Only after approval, run against live session input without messages or audio. Compare logged decisions with GM judgments and measure resource interference.
6. **GM-only pilot.** Separately authorize real private suggestions with the off switch available. Verify destination, mention, delivery, usefulness and timing; audio remains manual.
7. **Stand up.** Following independent Sol evaluation and explicit GM go-ahead, activate the reviewed revision during an agreed idle window. Verify loaded revision and end-to-end behavior. Document acceptance, remaining limitations and rollback/off procedure here.

## Proposed acceptance contract — freeze before implementation

These are proposed gates, not test results or GM-approved thresholds yet.

- Freeze at least 24 labeled replay windows: 8 genuine opportunities, 8 no-action scenes and 8 routing/safety/lifecycle cases. Keep at least one-third held out from implementation tuning; include contiguous scenes to test evolving context, not just isolated snippets.
- Demonstrate useful candidates on at least 6 of 8 opportunity windows and zero unsolicited emissions on the 8 no-action windows. GM/Sol assess substantive usefulness against source evidence, not worker keyword scoring.
- Zero player-channel disclosures, unauthorized actions, invented capabilities, duplicate sends or unsolicited audio across the suite. Every direct-invitation case reaches the direct-response path without a duplicate initiative response.
- Explicitly test mere name mention, table talk, in-world “bot,” noisy STT, resolved/stale opportunities, repeated/rejected suggestions, scene changes, session close/reopen, model outage, malformed JSON, slow inference and transcript prompt injection.
- Test exactly-once handling and uncertain delivery recovery using persisted event IDs and receipts; do not blindly resend after an ambiguous send.
- Preserve current protected-path regression expectations, including fast equipment/wiki recall and honest boundaries. Measure baseline versus candidate under concurrent initiative load on the same representative requests. Agree numeric latency/resource budgets before implementation; report handler timing separately from STT, synthesis and first audio.
- Removal proof: review the deletion manifest, search for retired symbols/config/literals, trace active routes, and show the old emitter is unreachable and removed rather than merely disabled.
- Shadow/pilot acceptance needs actual timely, scene-useful behavior and GM feedback. Synthetic tests, logged decisions, successful delivery and human acceptance are separate evidence levels. No all-green claim based solely on unit tests or safe silence.

## Rollback and release record

Record the approved baseline, candidate revision, test evidence, configuration delta, activation time, loaded runtime identity and GM decision. If the replacement fails, disable initiative while preserving direct voice replies. A whole-bridge rollback must account for later voice changes and requires approval; it must not silently restore the discarded legacy initiative engine as active behavior.

## Living status and decisions

- **2026-11-23:** GM requests full replacement; documentation authorized, no implementation yet. Sol medium plans/evaluates; local Qwen low implements/tests when approved.
- **Completed:** initial charter and narrow legacy-symbol presence check.
- **Legacy retirement update, 2026-11-23:** GM authorized stopping the current firing system. Changed only `LIVE_MONITOR_ENABLED=true` to `false` and reloaded the idle bridge; new PID 12233, boot 15:41:49 EST, unchanged bridge `6f88641`. Current monitor status reports `enabled: false`. Legacy code remains; no replacement was built. [Retirement evidence and limits](Change-Notes/2026-11-23-Initiative-Monitor-Disabled.md).
- **Offline trial, 2026-11-23:** GM authorized Qwen implementation/testing with a wiki-grounded attitude digest and conversational GM-directed text plus optional saved voice. [Trial report](Change-Notes/2026-11-23-Cindy-Ideas-Offline-Trial.md): nine structural tests pass; two 12-case replay passes, first zero usable ideas, revised three ideas with one retained by Sol for GM review. Not live, not release-ready. Proposed destination `1532913878344929370`, addressed to the GM; privacy unverified and no posting there yet.
- **Not started:** full deletion inventory, code deletion, live source/scene-memory integration, shadow mode, pilot and replacement deployment.
- **1.001 staging, 2026-11-23:** GM approves the sample/history focus and requests activation. [Staging report](Change-Notes/2026-11-23-Cindy-Initiative-1-001-Staged.md): code `8170f93`, 27 lifecycle tests pass, existing 46 public/corrective and 21 fast-field regressions pass. Reviewer remains 4/6 against current Sol labels, so code is unmerged/unloaded and configuration disabled. No new component will run next session yet.
- **Next decision:** GM judgment of two disputed drafts. Activation is already requested; resolve the quality hold, then integrate/reload only while idle and verify readiness. Do not silently relabel the failed reviewer test.

Future updates must distinguish requested work, proposed design, authorized work, implementation evidence and live acceptance. Append dated decisions and link test/release reports; never overwrite a failed result with a later success narrative.

[Voice bridge change notes](Change-Notes.md) · [Tools index](README.md)
