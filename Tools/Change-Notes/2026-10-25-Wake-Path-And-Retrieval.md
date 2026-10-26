---
title: Voice Bridge Change Note 2026-10-25 — Wake Path Latency, Retrieval Ranking, and Two Self-Corrections
type: change-note
visibility: player-safe
updated: 2026-10-25
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-25
---

# Voice Bridge Change Note — 2026-10-25

## Shipped

- **cindylou-voice-bridge-backup** `27072c0` — pipelined TTS playback, instrumented the wake path, fixed Kokoro readiness paging. First-audio latency 1.51s to 0.30s. 8/8 unit tests pass.
- **cindylou-voice-bridge-backup** `24d7a97` — wake generation routed to a configurable model and thinking level via `OPENCLAW_WAKE_MODEL` and `OPENCLAW_WAKE_THINKING`. Wakes now run on `dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4` with thinking off.
- **cindylou-voice-bridge-backup** `c0330f6` — bounded tool use on wake turns; the watchdog test now reads its bridge pid from launchd instead of a hardcoded value.
- **cindylou-voice-bridge-backup** `a3c8c78` — the bounded-lookup rule moved to a single shared constant used by both wake paths.
- **cindylou-voice-bridge-backup** `9425a72` — internal failures no longer get spoken aloud, and recap questions read the prebuilt session closeout instead of searching.
- **memory-system** `e629098` — retrieval ranking fixed (whole-word matching, saturating term frequency, smooth inverse-document frequency, length normalisation, filename boost) and campaign-wiki documents made fetchable through namespaced doc ids.

## Measured

- All latency figures come from session capture `run_timeline.jsonl` logs under `/Volumes/falcon/claw/data/cindylou/session-captures/`. These are the only trustworthy wake timings; ad-hoc probes are not (see Corrections). (Evidence: session capture logs.)
- 14 wake calls recorded between Aug 27 and Oct 22: median about 13.9s, 90th percentile about 30s, worst 81.3s against a 90s timeout. (Session capture logs.)
- Per session: Aug 27 gave 33.7, 17.8, 9.7 and 8.9s. Sep 10 gave 30.3s. Oct 8 gave 19.2, 14.6, 12.3, 8.4 and 7.9s. Oct 15 gave 16.6 and 4.6s. Oct 22 gave 81.3 and 13.3s. (Session capture logs.)
- Prompt size does not predict wake latency: the slowest recorded wake had the smallest prompt (1431 characters to 81.3s); a 2235-character prompt answered in 4.6s. (Session capture logs.)
- Attributable components: openclaw CLI startup 0.13s; faster_whisper speech-to-text median 0.307s (90th percentile 1.04s, worst 6.8s, 143 samples); warmed Kokoro synthesis about 0.3s per chunk; text-to-speech median 2.82s. These total roughly 4s against a 13.9s median, leaving about 10s inside the agent turn. (Session capture logs plus ad-hoc probes for CLI startup.)
- Before the retrieval fix, a named NPC query scored 331 against a 768 KB OCR'd rulebook through substring hits in automobile, kingdom and bottom. True whole-word hits: 3; the correct NPC page missed the top five. Afterward, 10 of 10 real NPC, host and location queries return the correct page in the top five; rules-scoped search is unaffected. (Unit-test style query battery, before/after.)
- Tokens are not the retrieval constraint: injected chunks median 1174 characters, top-five results about 1640 tokens, whole NPC pages 1.6k to 3.9k tokens, at roughly 0.22s per 1000 tokens. Round trips are the constraint. (Ad-hoc probes against the retrieval store.)
- Table lookback: 10 transcript rows totalling 262 characters (median row 41 characters), about 73 tokens, negligible. (Session capture transcript.)

## Still open

- Every latency figure above predates today's model and thinking change. The last real session was Oct 22; the current configuration is unvalidated.
- About 10s per wake remains unexplained inside the OpenClaw agent turn — the largest remaining latency term.
- Wake reply payloads grew from about 2–3 KB to about 28–30 KB between Sep 10 and Oct 8 for the same prompt type; uninvestigated.
- No single-flight lock: two quick wake phrases start two 90s processes and two playbacks. Rarely observed; deprioritised by the GM.
- No staged deadline: silence can last the full 90s timeout. What Cindy says early needs a design decision.
- Semantic search is a stub returning keyword results; both modes are identical.
- The watchdog deliberately stays page-only: the bridge already respawns a dead synthesis worker itself.

## Corrections

- The claim that the campaign wiki was absent from retrieval was wrong: an embedding index holding three path prefixes was queried instead of the search roots, which already included 362 wiki markdown files.
- The claim that a synthesis-worker death means silence until paging was wrong: the render path checks and respawns the worker, with a cold command-line fallback. Worker death costs next-reply latency, not silence.
- The 17:21 bounded-lookup rule did not affect real wakes: it landed on the configuration-disabled spoken path. `a3c8c78` made it shared with the path that actually fires.
- Ad-hoc probes of the wake path run inside an agent session are not wake timings: they return a guard error in about 0.6s. Any wake number under one second is that error, not a result.
- Observed failure at the table: asked for a 60-second voice summary of last week's session, Cindy said session transcript search was unavailable. That did not mean a recap was unavailable — a written closeout for that date already existed on disk.
