---
title: "Voice memory runtime repair"
type: change-note
visibility: player-safe
updated: 2026-11-06
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-06
---

# Voice memory runtime repair

## Shipped

The repaired memory release and bridge commit `2d76d0b` were activated in one authorized idle restart. Current-boot evidence confirms the reviewed bridge source hash, unified release selection and binding, Discord ready, and an inactive restored session. The restarted process remained stable in the post-start observation.

Memory commit `cf47323` updates the native adapter's approved OpenClaw revision from `4d94a9f` to `ba92b70`, including the revision test. Review of that runtime difference found callback-delivery custody detachment and its test, with no campaign-memory interface change. The adapter still checks its approved runtime rather than accepting an arbitrary installed revision. The same patch is retained on the main unification branch as `6ec339d` so a later export does not restore the obsolete pin.

The bridge now gives deterministic unavailable, stale and denied replies without asking the answering model to reinterpret those statuses or inviting a pointless clarification. Genuine empty searches and supported results retain their existing handling. The visible text and saved speech use the same status answer.

The watchdog distinguishes a warming voice worker from a failed worker, applies a bounded startup grace, and names the component that recovered. This corrects false startup/recovery alarms; it does not make Kokoro warm faster. The updated watchdog will load when the next session starts; it is not running while the bridge is idle.

The public source inputs, partial coverage and access boundaries are unchanged. This is a compatibility repair, not a source reindex, new campaign evidence, broader coverage or completion of the memory migration.

## Measured

- **Unit tests:** 34 native-runtime and campaign-adapter tests passed for the repinned candidate.
- **Released-command ad-hoc checks:** ten passed. Eight functional cases covered: disabled-before, a supporting Mevin passage, exact revision read, a supporting Curtis passage, an invented identity returning empty, a stale read returning stale, a private read denied, and disabled-after. The other two controls verified that a missing binding returned unavailable and oversized input bounds were enforced. Campaign passages are deliberately not reproduced here.
- **Real bridge-helper ad-hoc probes:** a Tom Erlichman question returned supporting public evidence and an invented name returned empty using the released adapter. Legacy reader methods were deliberately blocked during both probes; neither silently fell back.
- **Release comparison:** source input hashes were unchanged; the reviewed public partial scope was retained.

- **Bridge unit tests:** 38 passed, including ten status-by-path subcases through the real thread runner and transcription handler with mocked STT, model and Discord boundaries. Denied, stale and unavailable cases skipped model generation and cleared clarification state; empty and supported controls retained their behavior.
- **Real watchdog-script tests:** 13 scenarios passed, including a worker still warming after 101 seconds, a worker exiting during startup grace, a warmup timeout, and reason-specific recovery notices.
- **Focused regressions:** 38 speech/emoji-filter, 55 equipment and five audio-duration tests passed. Python compilation and scoped whitespace checks were clean.
- **Activation evidence:** the clean-baseline bridge was backed up before the idle restart. The new process's current-boot source hash matched the reviewed source, and startup reached Discord ready and the idle report. An ad-hoc post-start stability probe observed the same process with no stdout or stderr growth over 51.27 seconds. After restart, the real bridge-helper hit and empty probes passed again against the released adapter. Qwen thinking off and the existing model, TTS and manual-playback settings were unchanged.

Automated probes and mocked-boundary tests are not live microphone recognition, answering-model quality or human audio-playback acceptance.

## Still open

A subsequent human voice test remains necessary for end-to-end acceptance; no human voice acceptance is claimed by the automated probes. The updated watchdog must also be observed during the next real session start.

The existing manual saved-clip workflow and no automatic playback remain unchanged. Broader campaign coverage and migration work remain outside this repair.

## Corrections

The 18:29-18:34 voice test did not demonstrate missing campaign facts. Inspection of its captured prompts found all five retrieval attempts unavailable, not genuine empty search results. The adapter rejected the OpenClaw revision after the callback repair advanced the runtime without a corresponding approved adapter pin.

The replies then described an outage as failure to retrieve supporting information and invited clarification that could not restore the backend. The readiness statement before that test was incomplete: bridge availability did not establish campaign-memory dependency readiness. The repaired unavailable handling explicitly identifies the outage instead of implying that another character name will fix it.

The repaired startup alerts distinguish warming components from lost transcription. The session's Kokoro warmup took about 101 seconds (session capture/runtime log), during which an immediate watchdog alarm and later recovery wording gave a misleading account of startup.
