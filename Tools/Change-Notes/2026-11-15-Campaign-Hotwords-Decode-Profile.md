---
title: "2026-11-15 — Campaign hotwords behind an STT decode profile"
type: change-note
visibility: player-safe
canon_status: operational-record
updated: 2026-11-15
generated_by: openai/gpt-6.1-sol
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

Every number below comes from an offline frozen replay of 44 clips captured from the 2026-11-14 session, run in the bridge's own Python environment (faster-whisper 1.2.1, CTranslate2 4.7.1), importing the deployed helpers rather than a copy. None of them are live-session measurements.

- `live` profile: word error rate 11.0 percent, wake word recovered 25 of 28 times, exact canonical campaign names 38 of 47, zero false glossary insertions, median warm recognition latency 271 ms. (evidence: offline frozen-replay probe, bridge venv, 44 captured clips)
- `hot` profile: word error rate 7.4 percent, wake word 28 of 28, exact canonical names 47 of 47, zero false glossary insertions, median warm latency 328 ms, which is +57 ms. (evidence: offline frozen-replay probe, bridge venv, 44 captured clips)
- These reproduce the earlier three-engine-family benchmark, which ran on a newer CTranslate2, so the result is not an artifact of that version. (evidence: offline replay comparison against the 2026-11-15 engine benchmark)
- Unit checks on the deployed helpers all passed: `live` never carries hotwords; `hot` sets `beam_size=5` with voice-activity filtering on; the joined hotwords string is byte-identical to the benched glossary; an unknown profile value falls back to `live`; a missing glossary file fails closed to `live`. (evidence: unit checks on deployed helpers)
- Text changed on 21 of 44 clips, mostly for the better. Named costs: one ordinary sentence, "Can you link them together?", came out "and you link them together"; another degraded "Crap, I forgot his name" to "Crapper for Guy's name"; a third lost a leading "and we can". Overall error rate still favours `hot`. (evidence: offline frozen-replay transcript comparison, 44 captured clips)
- The reference transcripts used for scoring are cross-family model consensus plus canon adjudication from the campaign wiki and SR3 sources. Every clip is still marked `human_verified=false`. (evidence: reference-transcript provenance recorded in the benchmark)

## Still open

- The GM has not listen-verified the 8 ambiguous clips (31.9 seconds total). One may contain a campaign name that has no wiki page. This matters for the numbers above: on one clip the reference says "Evan, who is Curtis?" and `hot` hears "Mevin, who is Curtis", so the disagreement may be a reference error rather than a recognition error.
- The first live session on `hot` needs its wake decisions counted one by one against the 2026-11-14 baseline of 25 of 28. Hotwords push text toward the wake word, which is exactly right on genuine misses and exactly wrong if a stranger's sentence starts reading as an address to Cindy. That side effect is reasoned about but not yet measured in play.
- The shipped code default stays `live`. Flipping the default to `hot` waits for two clean supervised sessions.
- Rollback is one line: set `STT_DECODE_PROFILE=live` in `.env` while the bridge is idle and restart with `launchctl kickstart -k`. There is no model, environment or cache state to unwind.

## Corrections

None.
