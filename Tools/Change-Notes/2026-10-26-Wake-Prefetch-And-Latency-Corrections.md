---
title: "Voice bridge prefetch and wake-latency corrections"
type: change-note
visibility: player-safe
updated: 2026-10-26
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-26
---

# Voice bridge prefetch and wake-latency corrections

## Shipped

Phase 1 bridge-side retrieval prefetch was implemented and committed as `257a95b`. The bridge was restarted and verified with process 74930. This supersedes the earlier draft’s claim that prefetch remained unimplemented (ad-hoc probe).

Prefetch moves campaign retrieval ahead of the agent turn: the bridge matches the wake line against campaign entity names, fetches relevant passages, and injects context into the wake prompt. Its purpose is to let the agent answer a matched question without initiating retrieval itself. Deployment does not yet establish a live latency improvement.

The design specifies a 2.5-second total budget, fallback on misses, timeouts, or errors, an environment kill switch, and a `wake_prefetch` timeline event recording matched entities, documents fetched, characters injected, and elapsed seconds. These are implementation parameters, not measured production results (ad-hoc probe).

Launchd’s PATH is `/opt/homebrew/opt/node@22/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin`; it excludes `~/.local/bin`, where `cindylou` lives. Retrieval invokes the CLI by absolute path. An interactive-shell success with a bare command would not establish launchd compatibility (ad-hoc probe).

Configuration identifies the active route as `VOICE_WAKE_ENABLED=false`, `ACTIVE_THREAD_WAKE_ENABLED=true`, `OPENCLAW_WAKE_MODEL=dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4`, and `OPENCLAW_WAKE_THINKING=off`. Only the thread-transcript wake path fires (ad-hoc probe).

## Measured

Live evidence comes from `run_timeline.jsonl` for capture `2026-10-26T18-22-09-shadowrun`, run `2026-10-26T22-22-09Z_live_faster_whisper_base.en` (session capture log). Internal action evidence comes from `trajectory_runtime_events` in `openclaw-agent.sqlite`, session `500aefd4-12e5-4783-84dc-97eb7ed0e3f4` (harness trajectory store). Both are append-only records written during play, not probes.

Wake A asked who leads the Princeps Group. The transcript landed at 22:24:03.414 UTC, matched at 22:24:03.664, and queued at 22:24:04.221 with a 2365-character bridge prompt. The harness returned successfully after 55.548 seconds with a 104-character reply. Audio began 1.22 seconds after the reply; the spoken follow-up completed 9.627 seconds after it (session capture log).

Inside the harness, prompt submission occurred at 22:24:08.254 UTC. The only tool call began at 22:24:56.978, after a 48.72-second first-action delay. Campaign search returned 5555 characters in 1.18 seconds; the model finished 1.48 seconds later. Its answer identified Claude August as CEO (harness trajectory store).

The submitted prompt serialized to 32642 characters. The system prompt measured 63707 characters and was truncated to the trajectory recorder’s 32768-character limit. This establishes truncation in the recorded evidence, not demonstrated truncation of inference input (harness trajectory store).

Wake B asked Curtis’s race. Its bridge prompt contained 1771 characters; the harness completed in 11.659 seconds with the 22-character answer, “Curtis is a **dwarf**” (session capture log).

Campaign search began 1.91 seconds after prompt submission, returning 5601 characters in 1.10 seconds. A PCs-directory find followed 2.98 seconds later, returning 762 characters in 0.27 seconds. A bounded Curtis-page read followed 1.69 seconds later, returning 7556 characters in 0.26 seconds. The model finished 1.31 seconds afterward (harness trajectory store).

The decisive comparison is three lookups in 11.7 seconds for wake B against one lookup in 55.5 seconds for wake A. The dominant difference was first-action delay: 1.91 seconds versus 48.72 seconds. Tool count does not predict wake latency (harness trajectory store).

Across wake-shaped runs on this local model from August 26 through October 26, first-action delay ranged from about zero to 253.88 seconds without correlation to tool count or prompt size. Runs with zero and 56 tool calls both appeared at the slow end (harness trajectory store).

Both wakes requested `thinking=off`, and argument-building code passes it through. A missing thinking flag does not explain the delay (session capture log; ad-hoc probe). Other recorded GPU jobs did not overlap either wake. Contention remains plausible but unestablished; each wake supplies only one observation (harness trajectory store).

## Still open

The unexplained 48.72-second first-action delay remains the largest single known wake cost. Repeat measurement with the GPU idle is needed to distinguish model latency from host contention (harness trajectory store).

Phase 1 shipped in `257a95b`, followed by a verified restart to PID 74930. Live verification must now establish matching, bounded retrieval, context injection, fallback behavior, and effects on first-action and total response time. Earlier captures do not measure this deployment (ad-hoc probe).

The error-speech filter and prebuilt-closeout recap behavior in `9425a72` also await live-session verification. Reply-payload growth from roughly 2–3 KB to 28–30 KB remains unexplained. A single-flight lock and staged deadline remain absent and were previously deprioritized by the GM (campaign-wiki change note dated 2026-10-25).

## Corrections

Retired: “roughly 14 seconds per harness hop,” with wake A attributed to three hops. Wake A made one tool call in 55.5 seconds; wake B made three in 11.7 seconds. Tool round trips measured 0.26–1.18 seconds. First-action latency—not hop count—was the dominant observed difference (harness trajectory store).

Removing tool calls cannot by itself fix the observed 48.72-second first-action term. Evaluate prefetch against first-action latency and total response time, not merely tool count (harness trajectory store).

Reading per-action trajectory timestamps before proposing the design would have caught this error. Total elapsed time did not reveal where the time went. That is the durable lesson for this project.

Retired: the measured session validated the error filter and recap pointer. The previous process started at 19:44:53 EDT on October 25; `9425a72` was authored at 19:45:25 EDT, 32 seconds later. Those behaviors were absent from that process and await their first live execution (ad-hoc probe).

Also retired: prefetch remains only designed. Phase 1 shipped in `257a95b`, followed by the verified restart to PID 74930 (ad-hoc probe).

The earlier shared wake-lookup rule was applied to a path disabled by `VOICE_WAKE_ENABLED=false`. The current capture confirms only the thread path fires; it does not validate that rule’s claimed table benefit (session capture log).
