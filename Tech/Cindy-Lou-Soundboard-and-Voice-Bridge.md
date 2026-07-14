---
title: Cindy Lou Soundboard and Voice Bridge
type: tech-note
visibility: player-safe
status: outdated
updated: 2026-07-14
tags: [cindy, soundboard, discord, voice, tech, outdated]
---

# Cindy Lou Soundboard and Voice Bridge _(outdated)_

> **Outdated:** The table has moved past the soundboard approach. Preserve this page as an archive of the old prototype and queue-bridge lesson, but do not maintain the soundboard app, tunnel URL, or clip catalog going forward.

## Purpose

This page describes the old soundboard-to-Discord-audio path in enough detail that the same system could be understood later if needed. It is no longer the active direction for Cindy's live voice support.

## Archived repositories and runtime locations

### Soundboard app _(outdated)_

- Repo path: `/Users/hanclaw/claw/projects/cindylou/cindy-soundboard`
- Runtime entry: `server.js`
- Static UI: `public/`
- Clip catalog: `data/clips.json`

### Discord voice bridge

- Repo path: `/Users/hanclaw/claw/projects/discord_voice_patch`
- Runtime entry: `voice_chat.py`
- Discord bot command used historically: `!voice-play-saved <clip_name>`

### Shared audio asset location

- Preserved clip directory: `/Users/hanclaw/.openclaw/workspace-cindylou/preserved_voice`

### Shared queue location _(outdated)_

- Queue directory: `/Volumes/carbonite/claw/data/cindylou/runtime/soundboard-queue`

## Why the architecture changed

The first soundboard implementation posted a Discord text command into a thread and expected Cindy's own bot process to execute it.

That failed for a structural reason:

- the soundboard posted using a bot token
- the message author therefore appeared as a bot
- `discord.py` command processing ignores bot-authored messages
- Cindy therefore would not execute her own `!voice-play-saved ...` command

So the later prototype used **direct local playback triggering** instead of trying to route audio playback back through a Discord text-command loop.

## Outdated architecture

### Browser/UI layer

The GM previously opened the soundboard web app and logged in through a shared-password page.

Main characteristics were:

- Express server
- cookie-backed session auth
- small hardcoded clip catalog in JSON
- category/grouped button rendering in the browser

### Soundboard server layer _(outdated)_

`server.js` handled four important jobs:

1. authenticates the GM session
2. exposes clip metadata to the browser
3. writes playback requests into the local queue directory
4. still posts a raw voice command line into the Discord request thread for visibility/debugging

Important fields/config used by the server were:

- `PORT`
- `SESSION_SECRET`
- `SOUNDBOARD_USERNAME`
- `SOUNDBOARD_PASSWORD`
- `DISCORD_BOT_TOKEN`
- `DISCORD_THREAD_ID`
- `SOUNDBOARD_QUEUE_DIR`

### Local queue bridge

A button click created a JSON request file in:

- `/Volumes/carbonite/claw/data/cindylou/runtime/soundboard-queue`

For a play action, the queued payload contains at least:

- `action: play`
- `clipId`
- `filename`
- `requestedBy`
- `requestedAt`

For a stop action, the queued payload contains:

- `action: stop`
- `requestedBy`
- `requestedAt`

### Voice bridge consumer

`voice_chat.py` included a `soundboard_queue_watchdog()` loop for this prototype.

That loop:

1. scans the queue directory for `*.json`
2. renames each request to `.processing`
3. reads the JSON payload
4. resolves the requested clip against `preserved_voice`
5. calls `ensure_join_if_needed(force_join=True)`
6. calls `play_audio_file(...)`
7. deletes the processed request on success
8. writes a `.failed.json` record on failure

## Playback path step-by-step

### Play request

1. GM clicks a soundboard button
2. browser sends `POST /api/request`
3. soundboard server validates the session
4. soundboard server resolves the clip metadata from `data/clips.json`
5. soundboard server writes a queue file to `soundboard-queue`
6. soundboard server posts the raw `!voice-play-saved ...` line to the Discord request thread for observability
7. `voice_chat.py` queue watchdog notices the new file
8. voice bridge ensures it is joined to the Discord voice channel
9. voice bridge loads the referenced file from `preserved_voice`
10. voice bridge plays the clip into Discord audio through `play_audio_file(...)`

### Stop request

1. GM hits the stop control
2. soundboard server writes `action: stop` into the queue
3. voice bridge sees that request
4. if audio is currently playing, `voice_client.stop()` is called

## Clip catalog structure

The archived clip catalog lived in `data/clips.json`.

Each entry carried:

- `id`
- `label`
- `category`
- `tags`
- `filename`
- `text`

Example fields from the archived set:

- `on-it` → `cindy_soundboard_on_it.mp3`
- `copy-that` → `cindy_soundboard_copy_that.mp3`
- `lemme-check` → `cindy_soundboard_lemme_check.mp3`
- `hold-up` → `cindy_soundboard_hold_up.mp3`
- `gimme-sec` → `cindy_soundboard_gimme_sec.mp3`
- `gotcha-sugar` → `cindy_soundboard_gotcha_sugar.mp3`
- `running-it` → `cindy_soundboard_running_it.mp3`
- `that-tracks` → `cindy_soundboard_that_tracks.mp3`
- `try-this` → `cindy_soundboard_try_this.mp3`
- `were-golden` → `cindy_soundboard_were_golden.mp3`

## Audio asset generation

The first-pass Cindy clips were generated into `preserved_voice` and were meant to be playable by filename through the voice bridge.

The useful design rule was:

- the soundboard catalog references stable filenames
- the voice bridge resolves playback by local filename, not by Discord text parsing

## Rebuild recipe

To rebuild this subsystem from scratch, a new system would need:

1. a small authenticated soundboard web UI
2. a clip catalog with stable IDs and filenames
3. a local shared queue or local playback API
4. a Discord voice process that can join/play local audio files
5. a shared preserved-audio directory
6. a predictable path from clip button -> local request -> voice playback

The key lesson is that **bot-to-self text commands are the wrong control path**. The reliable control path is local IPC (queue, socket, or local HTTP) into the voice process.

## Maintenance status

Do not spend maintenance time on this soundboard unless the GM explicitly revives it. Future Cindy voice work should favor generated/saved voice lines and direct GM-triggered playback commands over a maintained button-board UI.

## Related pages

- [Cindy Lou Tooling and Discord Notes](Cindy-Lou-Tooling-and-Discord.md)
- [Cindy Lou Wiki and Tooling Topology](Cindy-Lou-Wiki-and-Tooling-Topology.md)
