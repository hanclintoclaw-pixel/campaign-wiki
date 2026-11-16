---
title: "2026-11-15 — Campaign hotwords behind an STT decode profile"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-15
generated_by: dgx-spark/local-inference-lab/Qwen3.8-Flash-Next-NVFP4
generated_at: 2026-11-15
---

# Campaign hotwords behind an STT decode profile

Speech-to-text can now run in one of three decode profiles chosen by `STT_DECODE_PROFILE` in the bridge's `.env`. `live` is the historical behaviour and the code default. `hot` adds beam search plus a fixed list of campaign terms that steers recognition toward words the table actually uses, such as Mevin Kitnick, Ares Predator, and wired reflexes. `prompt` is the gentler version of the same idea: same beam width as `live`, same term list, but handed to the decoder as a starting prompt instead of as beam-steering hotwords.

## Shipped

- Commit `5d8f62d` in the voice bridge repository adds the profile switch, the glossary file `stt_glossary.txt` (12 terms, `sha256` `08f290ad856664bbf6dc27e0a5cfe5733f768399d5ad4ed7d85d40b0ac7a4d89`), and the plan and risk register at `docs/STT-FWHOT-PROFILE-PLAN-2026-11-15.md`.
- Hotwords steer CTranslate2 beam search, so they only work with a wider beam. `hot` therefore bundles `beam_size=5` and the glossary as one choice, and costs about 57 ms per utterance.
- Commit `7101f91` adds the third profile, `prompt`: `beam_size=1` with the byte-identical glossary string passed to the decoder as `initial_prompt`. It is the zero-risk fallback the benchmark recommended alongside `hot`, and it exists in the code now rather than only in the spike. An in-repo test file, `test_stt_profiles.py`, guards what each profile is allowed to carry.
- One shared helper now builds the decode settings, used by both the warm-up call and the live transcription call. Before this change warm-up ran a single-beam pass without voice-activity filtering while live audio used the filter, so the warm-up primed a decode path the bridge never actually used.
- The change fails closed. An unknown profile value, or a missing or empty glossary, drops back to `live` and logs a `[stt]` line saying so — for `hot` and `prompt` alike, because a run that silently lost its glossary is worse than no feature at all. The command-line fallback tags itself too, because it applies neither the wider beam, the hotwords, nor the prompt.
- Evidence is stamped on every artifact so a later audit can tell which decoder produced a given transcript: `stt_profile`, `stt_glossary_sha256` and `stt_fallback` are written into recognized-text records and timeline events, and the profile plus glossary hash appear in the performance log lines, the session-start STT-ready message, the capture configuration snapshot, and the capture run directory name whenever the profile is not `live`.
- The bridge's `.env` now selects `hot`; the code default remains `live`, so the committed code landed inert and the opt-in is one reversible configuration line. The bridge restarted under launchd as PID 83119 at 17:42 EST with no live session running.

## Measured

These are the current offline frozen-replay results for all 44 clips captured from the 2026-11-14 session, run in the bridge Python environment (faster-whisper 1.2.1, CTranslate2 4.7.1) through the deployed helpers, imported rather than copied. This run uses the GM-reviewed references below and reproduces exactly on the committed code. Clip043 was garbled in capture; its reference records the GM's intended words, but the clip remains in the aggregate, so its errors are not evidence about any profile. None of these are live-session measurements.

- `live`: word error rate 13.1 percent; wake word recovered 24 of 27 times; exact canonical campaign names 37 of 47; one false glossary insertion; median warm latency 273 ms.
- `prompt`: word error rate 11.1 percent; wake word recovered 27 of 27 times; exact canonical campaign names 47 of 47; one false glossary insertion; median warm latency 282 ms.
- `hot`: word error rate 9.7 percent; wake word recovered 27 of 27 times; exact canonical campaign names 47 of 47; one false glossary insertion; median warm latency 328 ms. (evidence: three-profile acceptance replay, bridge venv, 44 GM-reviewed clips, `results/acceptance_bridge_profiles.json`)

Read across the three rows rather than down any one of them. Both glossary profiles recover every campaign name and every missed wake word; that part is the glossary, and it is available at today's beam width for nine milliseconds. `hot` buys a further 1.4 points of word error rate on ordinary prose, and pays 46 more milliseconds for it. The one false insertion is the same clip in all three profiles: clip043, the garbled one, where every engine puts a "Cindy" into a sentence that never contained one. (evidence: same replay, per-clip outputs in `results/acceptance_bridge_outputs.json`)
- `hot` changed the transcript on 21 of 44 clips and `prompt` on 19; the two profiles agree with each other on 37. It improved several canonical names, including the Ares Predator in clips034 and 042 and Mevin in clip033. It also regressed short or disfluent speech: clip005 added “Yo, yo”; clip016 dropped the real “and we can”; and clip004 changed “Can you link them together?” to “and you link them together.” Clip043 was garbled and remains unsuitable for judging the profile. (evidence: latest acceptance replay and GM-reviewed references)
- Fourteen unit checks on the deployed helpers passed, including that `live` carries neither hotwords nor a prompt, that `prompt` carries no hotwords and keeps `beam_size=1`, that both glossary strings match the benched glossary byte for byte, that each profile reports its own name in the evidence stamping, and that a missing glossary fails either one closed to `live`. Seven of these now live in the repository as `test_stt_profiles.py`. (evidence: unit checks on deployed helpers)

The reference set now includes GM listening verdicts for all eight selected clips. Those rulings corrected clip033 to “Mevin, who is Curtis?”; confirmed clip007's audible “um”; selected “fake out” for clip008; corrected clip013's opening to “read him” while its trailing sound remains indeterminate; confirmed clip016's full text includes “and we can”; and identified clip043's intended words as “What are the stats for Grandpa?” despite the garbled capture. Clip030 is an anti-hallucination canary, not a campaign character, and is not a glossary term. These are benchmark reference decisions, not campaign canon additions.

## Still open

- GM listening review is complete for the eight selected clips. The first live session on a glossary profile still needs its wake decisions counted one by one, against the `live` replay baseline of 24 of 27 and the 2026-11-14 session's own wake record; hotwords can help genuine wake misses but also risk turning a stranger's sentence into an apparent address to Cindy, so offline replay cannot establish how the profile behaves in play.
- `prompt` has not been heard in play at all. It is the rung to step down to if beam-5 search misbehaves during a session, and it is the profile to try first if the latency of `hot` turns out to matter.
- The shipped code default stays `live`. Flipping the default to `hot` waits for two clean supervised sessions.
- Rollback is one line: set `STT_DECODE_PROFILE=live` in `.env` while the bridge is idle and restart with `launchctl kickstart -k`. There is no model, environment or cache state to unwind.

## Corrections

This note has been corrected twice, and the second correction is the more instructive one.

- The original replay scores, and the claim that all references were unverified, are superseded by the GM-reviewed-reference rerun above.
- A version of this page published earlier today reported 11.3 / 7.1 percent word error rate, wake 28 of 28, names 48 of 48 and zero false insertions. Those numbers came from a run taken *before* the last six GM listen-in verdicts were folded into the reference set — before clip016 gained its real "and we can" and before clip043 became "What are the stats for Grandpa?", which removed a wake word from the denominator. They were re-quoted over a set of scores that had been correct at the time and were then mistaken for stale. They do not reproduce against the current references and are retired here. The 13.1 / 11.1 / 9.7 figures above do.
- The Mevin ruling on clip033 corrected an erroneous reference rather than exposing a transcription miss.
- Clip043 is marked as degraded capture, its intended wording is not treated as a reliable audio transcript, and it is where all three profiles insert the single false "Cindy" counted above.
