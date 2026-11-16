---
title: "2026-11-15 — Campaign hotwords behind an STT decode profile"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-15
generated_by: openai/gpt-6-luna
generated_at: 2026-11-15
---

# Campaign hotwords behind an STT decode profile

Speech-to-text can now run in one of two decode profiles chosen by `STT_DECODE_PROFILE` in the bridge's `.env`. `live` is the historical behaviour and the code default; `hot` adds beam search plus a fixed list of campaign terms that steers recognition toward words the table actually uses, such as Mevin Kitnick, Ares Predator, and wired reflexes.

## Shipped

- Commit `5d8f62d` in the voice bridge repository adds the profile switch, the glossary file `stt_glossary.txt` (12 terms, `sha256` `08f290ad856664bbf6dc27e0a5cfe5733f768399d5ad4ed7d85d40b0ac7a4d89`), and the plan and risk register at `docs/STT-FWHOT-PROFILE-PLAN-2026-11-15.md`.
- Hotwords steer CTranslate2 beam search, so they only work with a wider beam. `hot` therefore bundles `beam_size=5` and the glossary as one choice, and costs about 57 ms per utterance.
- One shared helper now builds the decode settings, used by both the warm-up call and the live transcription call. Before this change warm-up ran a single-beam pass without voice-activity filtering while live audio used the filter, so the warm-up primed a decode path the bridge never actually used.
- The change fails closed. An unknown profile value, or a missing or empty glossary, drops back to `live` and logs a `[stt]` line saying so. A run that silently lost its glossary is worse than no feature at all. The command-line fallback tags itself too, because it applies neither the wider beam nor hotwords.
- Evidence is stamped on every artifact so a later audit can tell which decoder produced a given transcript: `stt_profile`, `stt_glossary_sha256` and `stt_fallback` are written into recognized-text records and timeline events, and the profile plus glossary hash appear in the performance log lines, the session-start STT-ready message, the capture configuration snapshot, and the capture run directory name whenever the profile is not `live`.
- The bridge's `.env` now selects `hot`; the code default remains `live`, so the committed code landed inert and the opt-in is one reversible configuration line. The bridge restarted under launchd as PID 83119 at 17:42 EST with no live session running.

## Measured

These are the latest offline frozen-replay results for all 44 clips captured from the 2026-11-14 session, run in the bridge Python environment (faster-whisper 1.2.1, CTranslate2 4.7.1) through the deployed helpers. This run uses the GM-reviewed references below. Clip043 was garbled in capture; its reference records the GM's intended words, but the clip remains in the aggregate, so its errors are not evidence about hotword quality. None of these are live-session measurements.

- `live`: word error rate 13.1 percent; wake word recovered 24 of 27 times; exact canonical campaign names 37 of 47; one false glossary insertion; median warm latency 273 ms.
- `hot`: word error rate 9.7 percent; wake word recovered 27 of 27 times; exact canonical campaign names 47 of 47; one false glossary insertion; median warm latency 330 ms, +57 ms versus `live`. The acceptance gate passes. (evidence: latest acceptance replay, bridge venv, 44 clips)
- Hot changed the transcript on 21 of 44 clips. It improved several canonical names, including the Ares Predator in clips034 and 042 and Mevin in clip033. It also regressed short or disfluent speech: clip005 added “Yo, yo”; clip016 dropped the real “and we can”; and clip004 changed “Can you link them together?” to “and you link them together.” Clip043 was garbled and remains unsuitable for judging the profile. (evidence: latest acceptance replay and GM-reviewed references)
- Unit checks on the deployed helpers passed: `live` never carries hotwords; `hot` sets `beam_size=5` with voice-activity filtering on; the hotwords string matches the benched glossary; unknown profile and missing glossary both fail closed to `live`. (evidence: unit checks on deployed helpers)

The reference set now includes GM listening verdicts for all eight selected clips. Those rulings corrected clip033 to “Mevin, who is Curtis?”; confirmed clip007's audible “um”; selected “fake out” for clip008; corrected clip013's opening to “read him” while its trailing sound remains indeterminate; confirmed clip016's full text includes “and we can”; and identified clip043's intended words as “What are the stats for Grandpa?” despite the garbled capture. Clip030 is an anti-hallucination canary, not a campaign character, and is not a glossary term. These are benchmark reference decisions, not campaign canon additions.

## Still open

- GM listening review is complete for the eight selected clips. The first live session on `hot` still needs its wake decisions counted one by one against the 2026-11-14 baseline of 25 of 28; hotwords can help genuine wake misses but also risk turning a stranger's sentence into an apparent address to Cindy, so offline replay cannot establish how the profile behaves in play.
- The shipped code default stays `live`. Flipping the default to `hot` waits for two clean supervised sessions.
- Rollback is one line: set `STT_DECODE_PROFILE=live` in `.env` while the bridge is idle and restart with `launchctl kickstart -k`. There is no model, environment or cache state to unwind.

## Corrections

The original replay scores and the claim that all references were unverified are superseded by the GM-reviewed-reference rerun above. The Mevin ruling on clip033 corrected an erroneous reference rather than exposing an STT miss. Clip043 is marked as degraded capture and its intended wording is not treated as a reliable audio transcript.
