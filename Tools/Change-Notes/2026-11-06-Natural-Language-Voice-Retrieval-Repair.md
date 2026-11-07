---
title: "Natural-language voice retrieval repair"
type: change-note
visibility: player-safe
updated: 2026-11-06
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-06
---

# Natural-language voice retrieval repair

## Shipped

Bridge commit `1b1d5da` removes bounded conversational framing from campaign queries while retaining the named subject and requested detail. Explicit requests for a sample NPC or campaign item can select a query hint from the already-approved public discovery catalog, then perform the same revision-bound lookup. Catalog names are not answer evidence. This adds no retry, legacy fallback, source access or coverage.

The captured "Sydney" clarification is handled only within its already-admitted clarification context, not as a new wake alias or an arbitrary name correction. Query wording is captured for later diagnosis.

The same commit clears inherited transcript, STT and audio activity timestamps at session start and refreshes the detailed worker snapshot after warmup completes.

Watchdog commit `e926ee9` clamps an inherited transcript timestamp to the current session's age. A successful warmup with a verified live worker PID outranks a stale pre-spawn worker snapshot; an explicit worker exit still alerts. This repairs misleading startup health reports, not voice-worker warmup speed.

The reviewed bridge was activated in one authorized idle restart after its commit. Current-boot evidence confirms the reviewed source hash, unchanged unified release and binding, Discord ready and an inactive restored session. The next session will load the repaired startup path; the restart itself did not start a session or initiate audio.

## Measured

- **Session capture:** the session beginning at 19:23:57 on 2026-11-06 contains three campaign lookups, all genuinely empty rather than unavailable. The full Curtis question failed despite a recognized identity. A separate entity-only adapter probe for Curtis succeeded: generic question words had displaced its covered passage in lexical top results.
- **Session capture/runtime log:** worker warmup completed in 52.314 seconds. A later false worker alert used the pre-spawn detailed snapshot despite that completion. This is a different session from the earlier note's approximately 101-second warmup.
- **Focused bridge tests:** 17 passed, including query handling, session-start status, preserved requested detail, unknown-identity behavior, clarification boundaries and refreshed post-warmup state.
- **Released-adapter integration checks:** 16 subcases passed through the actual thread and transcription handlers. They covered all captured query forms, the captured "Sydney" clarification via the actual clarification resolver, Mevin, a Curtis detail request, wiki/week wording and a genuine unknown-identity miss. Evidence reads used the released adapter with legacy reads blocked; external STT, answering model, Discord and audio were mocked. These are handler/backend checks, not new live microphone or playback results.
- **Real watchdog-script tests:** 19 scenarios passed (production patch `e926ee9`, expanded controls `bca0539`). Coverage includes inherited transcript age, completed warmup with a lagging detailed snapshot, missing bridge or worker PID, explicit worker exit, actual transcript stall and reason-specific recovery.
- **Activation and post-start ad-hoc probes:** the same restarted process showed zero stdout or stderr growth over a measured 28.54 seconds. The exact Curtis question then returned its approved public passage, and an invented identity returned empty, through the real bridge helper with legacy reads blocked. Qwen thinking off and existing model, TTS and playback settings were preserved. Python compilation and scoped whitespace checks were clean.

## Still open

The repaired startup status and watchdog behavior still need observation during a subsequent real session. Human microphone recognition, answering-model quality and audio-playback acceptance remain separate from retrieval probes and automated tests. No human voice acceptance is claimed here. Broader source coverage and completion of the memory migration remain outside this repair.

## Corrections

The [earlier runtime repair](2026-11-06-Voice-Memory-Runtime-Repair.md) restored backend availability and verified selected helper queries; it did not prove the natural-language path used by the next live question. Its reported measurements retain that narrower scope. A working entity-only lookup does not establish that a full conversational question retrieves the same evidence.
