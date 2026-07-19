---
title: Cindy Lou TTS Middle Layer
type: tech-note
visibility: player-safe
status: active
updated: 2026-07-19
parent_page: README.md
tags: [cindy, voice, tts, kokoro, npc-tools]
---

# Cindy Lou TTS Middle Layer

This page describes the local voice-preparation layer that sits between Cindy's written reply and the final text sent to the TTS engine.

The short version: Cindy's displayed text and Cindy's spoken text are allowed to differ. The Discord/wiki-facing line should stay clean and readable, while the TTS-only line can be reshaped for pronunciation, cadence, and voice performance.

## Why this layer exists

Model-generated Cindy text already carries some character voice: Southern turns of phrase, stage-sweet phrasing, and knowbot/decker vocabulary. That is useful, but it is not enough for consistent audio.

TTS has different needs than written text:

- punctuation changes timing;
- respellings can improve or damage pronunciation;
- some names need IPA rather than rough phonetic spelling;
- long written sentences can sound rushed;
- markdown, quotes, and code formatting can be read aloud awkwardly;
- the table needs clear, repeatable pronunciations for recurring PCs, NPCs, gear, and Shadowrun terms.

The middle layer handles those issues locally before Kokoro renders audio.

## Current implementation

The active implementation lives in the Discord voice bridge:

```text
/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py
```

The main entry point is `_prepare_tts_text(...)`. It prepares a spoken-only version of the text before the bridge saves or plays a TTS clip.

The active Kokoro worker path also participates:

```text
/Users/hanclaw/claw/projects/discord_voice_patch/kokoro_worker.py
```

That worker now accepts an `ipa` guide map so approved Kokoro pronunciations can be passed through the warm worker instead of being lost during live rendering.

## Current flow

1. Cindy drafts or receives a text line.
2. The visible line is posted/saved as ordinary text.
3. The voice bridge creates a TTS-only spoken version.
4. The spoken version is cleaned, sculpted, and paired with pronunciation guides.
5. Kokoro renders a WAV from that spoken version.
6. The GM can manually play the saved clip, or live playback can use the same rendered file when enabled.

## What gets shaped

### Cleanup

The layer strips formatting that should not be spoken aloud:

- fenced code blocks;
- inline backticks;
- markdown bold/asterisks;
- quotation marks that can interrupt speech flow;
- excess whitespace.

### Pronunciation

Some terms are shaped directly in text because Kokoro handles them better that way:

- `Saab Dynamit` -> `Saab Dynamite`
- `roto-drone` -> `roto drone`

Recurring campaign names and terms that need exact pronunciation use Kokoro IPA guides instead of rough respelling:

| Term | Approved sound | Kokoro IPA guide |
| --- | --- | --- |
| Valgaut | VAHL-got | `Valgaut=vˈɑːlɡɑt` |
| Kurgan | CUR-guhn | `Kurgan=kˈɜːɹɡən` |
| nuyen | NEW-yen | `nuyen=nˈuːjɛn` |

The important rule is: for Kokoro, keep those words intact and pass the IPA guide. Do not replace `Valgaut` or `Kurgan` with rough spelling in the Kokoro path, because that was tested and sounded worse.

### Southern cadence

The active Southern setting is intentionally stronger than the first pass. It uses a slower Kokoro speed and TTS-only phrase shaping such as:

- `I am` -> `I'm`
- `I will` -> `I'll`
- `you all` -> `y'all`
- `going to` -> `gonna`
- `about to` / `ready to` -> `fixin' to`
- `nothing` -> `nothin'`
- `checking` -> `checkin'`
- `little` -> `li'l`
- `hold up` / `listen close` / `well now` get pause punctuation.

This is controlled by:

```text
TTS_SOUTHERN_SCULPT_ENABLED=true
KOKORO_SPEED=0.82
```

## Current live posture

The current live voice posture remains GM-controlled. Cindy can generate text and saved voice clips, but ordinary voice playback should not surprise the table.

Current defaults:

- Kokoro voice: `af_heart`
- Kokoro speed: `0.82`
- Southern sculpting: enabled
- saved/manual clips: enabled
- auto-speaking: disabled unless explicitly enabled by the live voice controls

## Design rules

- Keep display text and spoken text separate.
- Prefer IPA guides for stable Kokoro pronunciations.
- Use rough respelling only as a fallback for non-Kokoro engines.
- Keep live voiced clips short where possible, because Discord playback can cut out on longer lines.
- Treat cadence shaping as local performance polish, not a rewrite of campaign canon.
- If a generated voice clip is intended to become canon or a reusable asset, save the exact file/path that was approved.

## Recent test artifacts

Useful 2026-07-19 test uploads in the Cindy interaction thread included:

- `valgaut-kurgan-pronunciation-af_heart.wav` - approved Valgaut/Kurgan pronunciation baseline.
- `cindy-ipa-carrythrough-valgaut-kurgan-af_heart.wav` - verified IPA survived the sculpting layer and worker path.
- `cindy-southern-campaign-promo-af_heart.wav` - longer sample using the stronger Southern setting.

These are test artifacts, not campaign canon.

## Related pages

- [Cindy Lou Tooling](README.md)
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
- [Cindy Lou Voice Clip Phrase Library](Voice-Clip-Phrase-Library.md)
