---
title: Cindy Lou's STT Hotword Glossary
type: documentation
visibility: player-safe
canon_status: operational-record
updated: 2026-11-16
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-16
---

# Cindy Lou's STT Hotword Glossary

This is the browsable form of Cindy Lou's live speech-to-text (STT) glossary: `stt_glossary.txt`, committed next to `voice_chat.py` in the voice-bridge repository. Its SHA-256 is `08f290ad856664bbf6dc27e0a5cfe5733f768399d5ad4ed7d85d40b0ac7a4d89`. Glossary-enabled decode profiles use these terms; the shipped code default remains `live`, which does not use the glossary.

## Current terms

Terms appear in file order. Counts refer to the 44 benchmark reference clips.

| Term | Kind | In benchmark clips | Why it is there |
| --- | --- | --- | --- |
| `Cindy Lou` | Wake/addressing form | 0 of 44 | Cindy's addressing form, carried on campaign-frequency grounds rather than measured coverage. |
| `Cindy` | Wake word | 27 of 44 | The recogniser was missing or inventing it. |
| `Mevin Kitnick` | PC | 3 of 44 | Heard as "Maven's", "Evan", and "sendee who is mevin kittnick". Live state had been carrying the misheard variant "Nevyn Kipnick". |
| `Kurgan` | PC | 4 of 44 | A public campaign name the table says aloud. |
| `Valgaut` | PC | 0 of 44 | A public campaign name, carried on campaign-frequency grounds rather than measured coverage. |
| `Ares Predator` | Printed SR3 firearm | 2 of 44 | The table asks stat questions about it. Both clips actually said "Ares Predator 2"; the trailing digit is not in the glossary. |
| `Curtis` | PC | 7 of 44 | A public campaign name the table says aloud. |
| `decker` | Generic SR3 vocabulary | 1 of 44 | Heard as "decor". |
| `drone` | Generic SR3 vocabulary | 0 of 44 | Table vocabulary, carried on campaign-frequency grounds rather than measured coverage. |
| `cyberware` | Generic SR3 vocabulary | 1 of 44 | An SR3 noun the table uses. |
| `grenade` | Generic SR3 vocabulary | 2 of 44 | An SR3 noun the table uses. |
| `wired reflexes` | Printed SR3 cyberware | 1 of 44 | Heard as "wire reflexes". |

## How it is loaded

The file contains one term per line. Blank lines and `#` comments are ignored. Terms are joined in file order with `, ` into one string, which is what the decoder receives.

The bridge's `.env` selects the decode profile through `STT_DECODE_PROFILE`:

| Profile | Decode settings | Glossary use |
| --- | --- | --- |
| `live` | `beam_size` 1, VAD on | None. Historical behaviour and the code default. |
| `hot` | `beam_size` 5 | Glossary string supplied as CTranslate2 `hotwords`. |
| `prompt` | `beam_size` 1 | Same glossary string supplied as `initial_prompt`. |

Both glossary-carrying profiles fail closed to `live`, with a loud `[stt]` log line, if the file is missing or empty.

If the bridge falls back to the command-line `whisper` binary, neither hotwords nor `initial_prompt` is applied. That fallback logs `glossary_not_applied`.

The profile name and glossary hash are stamped into per-utterance performance logs, recognized-text capture records, timeline events, the session-start STT-ready message, and the capture run directory name.

## How the list was chosen

The list is player-safe: nothing GM-licensed and nothing unpublished. It targets names the table says aloud that the recogniser demonstrably mangled, plus SR3 nouns the table leans on.

One fixed list was used identically by every engine in the benchmark. It was not tuned per clip or answer, so no engine received a list fitted specifically to its test results.

The terms have different provenance:

- PC and character names came from public campaign-wiki entity pages. Mevin Kitnick, Kurgan, Valgaut, and Curtis each have a page under `PCs/`; Cindy Lou is Cindy herself.
- `Ares Predator` has no wiki entity page. It is a printed SR3 item the table asks about, and appears in `NPCs/Ivan.md` and older change notes.
- `decker`, `drone`, `cyberware`, `grenade`, and `wired reflexes` are printed SR3 vocabulary, not campaign entities.

The benchmark's own note describes the list as "fixed, identical for all engines, built 2026-11-15 from public campaign-wiki entity pages. Not tuned per clip or per answer." That overstates uniformity of provenance for the last six terms: Curtis has a PC page, but the following five are printed SR3 vocabulary rather than campaign entities. `Ares Predator`, earlier in the list, also has no wiki entity page.

The list is deliberately short. A hotword applies to every utterance, so a wrong term can distort unrelated transcriptions. A small list limits that blast radius. Adding a term is a canon decision requiring GM sign-off, not merely a configuration tweak.

## Deliberately excluded

Anything not canon is excluded.

`Marzipan Quasar` is a Cindy-invented anti-hallucination canary. The GM ruled it is not a campaign character, and it has zero wiki mentions. The glossary file header documents it as a decided-out term. It is not a glossary entry.

## Measured effect

These results are from an offline frozen replay of 44 clips from the 2026-11-14 session, using GM-reviewed references. The bridge virtual environment used faster-whisper 1.2.1, CTranslate2 4.7.1, `base.en`, and CPU int8. Timing is warm median.

| Profile | Word error rate | Wake recognition | Canonical campaign names | False glossary insertions | Warm median |
| --- | --- | --- | --- | --- | --- |
| `live` | 13.1% | 24/27 | 37/47 | 1 | 273 ms |
| `prompt` | 11.1% | 27/27 | 47/47 | 1 | 282 ms |
| `hot` | 9.7% | 27/27 | 47/47 | 1 | 328 ms |

The one false insertion occurred in the same clip under all three profiles. The GM flagged that clip as garbled in capture.

## Known gaps

- `Cindy Lou`, `Valgaut`, and `drone` never appeared in the benchmark clips. This replay exercised none of them; they are carried on campaign-frequency grounds, not measured ones.
- `Grandpa`, the campaign's RV, is not in the glossary. It has its own wiki page at `Locations/Grandpa.md` and roughly 30 mentions across the wiki. It is the strongest candidate for the next term and needs a GM ruling.
- Whether to add the trailing-digit form `Ares Predator 2` is unresolved.
- No live session has yet run on a glossary profile. All reported measurements are offline.
- The shipped code default is still `live`.

## Changing the list

Obtain GM sign-off before adding a term. Keep additions canonical and player-safe, and retain one term per line.

Adding any term changes the file's SHA-256, requiring redeployment and re-verification. Update this reference to match the resulting file and hash. A changed list must not inherit the current list's measured results as evidence of its own performance.

## Open items for the GM

- Rule on adding `Grandpa`.
- Decide whether to add `Ares Predator 2`, including its trailing digit.
- Live-session validation of a glossary profile remains pending; offline results do not settle live-session performance.

This page describes bridge configuration, not campaign canon; the figures are offline replay, not live-session measurement.
