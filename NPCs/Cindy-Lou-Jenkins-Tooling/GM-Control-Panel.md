---
title: Cindy Lou GM Control Panel
type: tech-note
visibility: player-safe
status: first-effort-live
updated: 2026-09-04
parent_page: README.md
tags: [cindy, discord, voice, gm-tools, control-panel, npc-tools]
sources:
  - Discord planning discussion 2026-09-04
  - Private voice bridge backup commits ff4777e and ed8e9be
---

# Cindy Lou GM Control Panel

The **Cindy Lou GM Control Panel** is a first-effort Discord-native control surface for managing Cindy's live-session behavior during online Shadowrun play.

It is not a separate website yet. It runs inside the local Discord voice bridge and appears as a Discord message with buttons, opened by command.

## Current status

- **First live effort built:** 2026-09-04.
- **Runtime:** local Discord voice bridge at `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py`.
- **Backup:** private `cindylou-voice-bridge-backup` repository.
- **Known-good pre-panel rollback:** `e56435a`.
- **Initial panel commit:** `ff4777e`.
- **Voice replay / interrupt controls commit:** `ed8e9be`.
- **Marker note modal commit:** `fb8cea1`.

## How to open it

In the configured GM/control Discord channel, run:

```text
!cindy-panel
```

Aliases:

```text
!gm-panel
!cindy-gm-panel
```

The panel posts a button card. Buttons expire after about one hour; run `!cindy-panel` again for a fresh card.

## Authorization

The panel is controlled by environment settings in the local voice bridge:

```text
GM_CONTROL_PANEL_ENABLED=true
GM_CONTROL_ALLOWED_USER_IDS=
```

If `GM_CONTROL_ALLOWED_USER_IDS` is set, only those comma/space-separated Discord user IDs can use the panel.

If the allow-list is empty, the bridge allows use from the configured control channel and by guild managers/admins. This makes the default practical for the GM channel while still preventing random table use elsewhere.

## Buttons

### Status

Shows current bridge state:

- active session ID
- active session thread
- target voice channel
- local/guild voice connection state
- wake/live-voice/stalling-voice state
- last GM-panel voice line saved this session
- Kokoro worker running state

Text fallback:

```text
!cindy-status
```

### Stay Silent

Disables the noisy/live parts of Cindy until resumed or restart:

- voice wake
- active-thread wake
- proactive live monitor
- live playback
- stalling voice

Text fallback:

```text
!cindy-silent
```

### Resume Wakes

Resumes active-thread Cindy wakes and live playback. Voice wake and proactive monitor remain at their configured startup defaults unless separately enabled.

Text fallback:

```text
!cindy-resume
```

### Summarize 5m

Reads recent live transcript lines and asks Cindy for a short GM-facing summary of the last five minutes.

Intended output:

- 3-5 concise bullets
- current scene state
- choices made
- unresolved questions
- direct Cindy relevance if any

Text fallback:

```text
!cindy-summary
```

### Suggest Cindy Action

Reads recent live transcript context and asks Cindy for at most one optional GM-facing action, or **HOLD SILENCE**.

The prompt explicitly tells Cindy to protect player agency and avoid solving the scene for the players.

Text fallback:

```text
!cindy-suggest
```

### Generate Voice Line

Drafts one short Cindy Lou in-character voice line for the current scene and renders it as a saved clip.

Important behavior:

- The clip is **not auto-played**.
- The generated line becomes the panel's **last saved voice line** for the current session.
- The last saved panel voice line starts empty on each `!session-start`.
- If Cindy returns **HOLD SILENCE**, no clip is generated.

Text fallback:

```text
!cindy-voice-line
```

### Play Last Voice

Plays the most recent GM-panel-generated voice line for the current session.

This exists so the GM does not need to copy and paste the generated `!voice-play-saved ...` command.

Text fallback:

```text
!cindy-play-last-voice
```

Aliases:

```text
!cindy-play-last
!cindy-play
```

### Interrupt Cindy

Stops current Cindy voice playback. This uses the same safety behavior as `!voice-stop`.

Text fallback:

```text
!cindy-interrupt
```

Aliases:

```text
!cindy-interrupt-voice
!cindy-shush
```

### Mark Canon

Opens a Discord text-entry modal for a canon note.

The submitted note is saved with an optional short label, recent transcript context, session ID, thread ID, timestamp, user ID, and intended use `session_closeout`. It does **not** edit the wiki by itself; it creates durable closeout material for Cindy to sweep into the later session archive.

Text fallback:

```text
!cindy-mark canon Belisarius must miss court because of the HEMP liability hearing
```

### Mark GM-Only

Opens a Discord text-entry modal for a GM-only or spoiler-sensitive note.

The submitted note is saved with the same context as a canon note, but marked `gm_only` so later closeout knows not to put it on player-visible wiki pages by accident. It does **not** publish, hide, or edit wiki content by itself.

Text fallback:

```text
!cindy-mark gm-only Dupree is secretly working for the judge's rival
```

### Closeout Prompt

Posts a reminder checklist for ending a session cleanly.

It does **not** end the session. The actual session lifecycle command remains:

```text
!session-end
```

The prompt reminds the GM to confirm:

- in-world end time
- rewards / Karma / nuyen
- gear, damage, favors, heat, or reputation changes
- public-safe vs GM-only details
- immediate next-scene state

Text fallback:

```text
!cindy-closeout-prompt
```

## Runtime files

The panel writes local audit files under the live-session runtime directory:

```text
gm-control-panel.jsonl
gm-control-panel-markers.jsonl
```

`gm-control-panel-markers.jsonl` is the important closeout file for typed Canon / GM-only modal notes. Each record includes `marker_type`, `label`, `note`, `session_id`, `thread_id`, `recent_transcript`, and `intended_use`.

`!session-start` clears per-session panel state, including the last saved panel voice line and marker/audit files. `!session-end` archives those files with the rest of the session runtime state.

## Basic test flow

1. Join the Shadowrun voice channel.
2. Run `!session-start`.
3. Run `!cindy-panel` in the GM/control channel.
4. Click **Status**.
5. Talk long enough to create transcript.
6. Click **Summarize 5m**.
7. Click **Generate Voice Line**.
8. Click **Play Last Voice**.
9. If needed, click **Interrupt Cindy**.
10. At the end of play, use **Closeout Prompt**, then run `!session-end` when the session is truly over.

## Design notes

The panel intentionally starts inside Discord because Discord is already live, permissioned, and connected to the voice bridge. A GitHub Pages web panel would need an additional live backend before buttons could actually control Cindy.

The current implementation is deliberately conservative:

- no wiki publishing button yet;
- no automatic canon mutation;
- no hidden irreversible behavior;
- generated voice lines are saved first and GM-played second;
- silence/interruption controls are easy to reach.

## Related pages

- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md)
- [Cindy Lou Voice Clip Phrase Library](Voice-Clip-Phrase-Library.md)
- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou Post-Session Automation](Post-Session-Automation.md)
- [Cindy Lou Tooling Future Planning](Future-Planning.md)
