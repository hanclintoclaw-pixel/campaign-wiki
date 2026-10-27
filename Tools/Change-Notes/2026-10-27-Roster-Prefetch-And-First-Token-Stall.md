---
title: "Roster prefetch and first-token stall"
type: change-note
visibility: player-safe
updated: 2026-10-27
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-27
---

# Roster prefetch and first-token stall

## Shipped

Commit `536d0b0`, “Prefetch the party roster for collection questions,” changes `voice_chat.py` and adds `test_collection_trigger.py` in `/Users/hanclaw/claw/projects/discord_voice_patch`, following Phase 1 commit `257a95b`. Backup: `voice_chat.py.bak.20261027-185218-pre-roster-trigger`. Collection matching requires both a normalized `WAKE_COLLECTION_TERMS` entry (`pcs`, `playercharacters`, `party`, `crew`, `roster`, `squad`) and `WAKE_COLLECTION_CUES` entry (`name`, `who`, `list`, `member`, `howmany`, `which`, `called`). `WAKE_COLLECTION_DOC="wiki/PCs/README.md"`, `WAKE_COLLECTION_NAME="Party roster"`, and `WAKE_COLLECTION_SCORE=0.6` configure injection below exact-entity matches, so named entities win the fetch budget. Entity matching cannot recognize an unnamed collection. Terms alone incorrectly matched “you're already splitting the party” and “the crew ran the numbers”; requiring cues excludes both (ad-hoc probe).

Using the bridge venv, real wiki and `cindylou` CLI, `test_collection_trigger.py` passed 6/6: roster prefetch returned `outcome=ok`, kind `collection`, 648 characters in 0.04s; Claude August’s company question retained exact matching to `wiki/NPCs/Claude-August.md`; both table-talk negatives returned `no-entity-match`, no documents; “who is in the party” and “How many crew members are active?” matched. Lexicon: 462 entries. This is local evidence, not live-session validation (smoke test).

At 19:01:05 EDT, launchd restart replaced PID 74930 with 66605. Startup reported `precache ok=True rendered=15 failed=0`, ready with one guild, `session_restore active=False`, and `idle_report_sent` (ad-hoc probe). The roster trigger has not executed in a live wake; no latency benefit is measured.

Read-only service `ai.cindylou.engine-sampler` now samples vLLM gauges and queue/TTFT/decode/generation-token histograms at 1 Hz into `probe/engine_samples.jsonl`. Python under launchd repeatedly returned `[Errno 65] No route to host`; the replacement uses node, which reaches the engine. Plist `ProgramArguments` changes require bootout/bootstrap: `kickstart -k` retains the cached definition. A PID in `launchctl list` proves loading, not successful sampling (ad-hoc probe).

## Measured

Evidence: `run_timeline.jsonl` for capture `2026-10-27T18-31-44-shadowrun`, run `2026-10-27T22-31-44Z_live_faster_whisper_base.en` (session capture log); `trajectory_runtime_events` in `~/.openclaw/agents/cindylou/agent/openclaw-agent.sqlite` (harness trajectory store). All six wakes used thread transcripts: `VOICE_WAKE_ENABLED=false`, `ACTIVE_THREAD_WAKE_ENABLED=true`, model `dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4`, recorded `thinkLevel=off`.

“What are the names of the PCs in our campaign?” missed prefetch: 0.037s, zero documents, 2,478-character bridge prompt; generation took 59.992s for 222 reply characters (session capture log). Run `fef11424` spent 0.03s starting the CLI, 57.18s in one model leg, with one tool call and 51.81s from prompt submission to first tool call (harness trajectory store). Four stalling phrases covered the wait: “Got it.”, “Tracing that.”, “Running the numbers.”, “Still tracing that.” (session capture log).

Claude August, Curtis and Core-7 fetched `wiki/NPCs/Claude-August.md`, `wiki/PCs/Curtis.md` and `wiki/NPCs/Core-7.md`: respectively 1,730/1,715/1,715 characters in 0.061/0.062/0.049s; generation 4.168/3.788/4.909s (session capture log). Runs `3e90d399`/`9bf16ba9`/`ab2e723e` had model legs 1.80/1.82/2.93s, zero tool calls (harness trajectory store). TTS took 0.957/0.739/3.723s, the last across two clips (session capture log).

The other no-match question and web-search ethics question took 0.002/0.003s prefetch and 9.536/4.701s generation (session capture log). Runs `add6ab27`/`a4d2c7d5` had 7.5/2.78s model legs and one/zero tool calls; `add6ab27` first-action delay was 2.02s (harness trajectory store).

A manual `/metrics` curl baseline at 22:23:46 UTC, diffed afterward, placed all 22 window requests in the ≤0.3s queue bucket: none queued. TTFT was ≤10s for 21 requests, with one 40–80s outlier. The roughly 60s wake waited roughly 55s for its first engine token despite its small bridge prompt. These aggregate counters are not per-request traces (ad-hoc probe).

## Still open

The trigger removes the known cold-agent-fallthrough failure mode for unnamed roster questions—the question class that produced this 60s-shaped failure—not the underlying, still-unattributed first-token stall. Live confirmation remains outstanding (ad-hoc probe).

October 26–27 probes exclude the tested alternatives: 220,031 prompt tokens reached first token in 4.78s (~46K tokens/s), estimating ~1.5s for the recorded 63,707-character system prompt; disabling thinking reduced reasoning 290→0 characters and elapsed time 2.28→0.79s; after 240s engine silence, first response took 1.08s versus 0.64–0.90s warm. Replay reasoning was insufficient to explain 55s (ad-hoc probe).

Contention is reproducible: 0.45s idle versus 75.95s with eight generators; engine history records ~1,457/16,216 requests waiting over 10s. However, zero-queue counters exclude that mechanism for this outlier (ad-hoc probe).

## Corrections

Retired: October 26’s “provider naming” lead. `isVllmQwenThinkingCompat()` supplies a default only when `reasoning` is omitted; explicit `reasoning: true` bypasses that gate. Emission requires `thinkingFormat` and `model.reasoning`, both present. Direct testing proved `enable_thinking:false` reaches the engine (ad-hoc probe).

Retired: “prefetch will cut wake latency by removing tool calls.” October 26 recorded 54.345s with zero calls versus 11.659s with three lookups. Today’s matched wakes took 3.8–4.9s without calls and misses were slower, but n=6 is small; the prior zero-call stall prevents crediting prefetch with removing it. Tool count does not predict wake latency (session capture log; harness trajectory store).

Retired: any claim that today’s session used sampler instrumentation. The sampler was broken then; engine attribution comes from the manual baseline curl diff, not `probe/engine_samples.jsonl` (ad-hoc probe).
