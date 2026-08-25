---
title: Cindy Lou Discord Voice Bridge Commands
type: tech-note
visibility: player-safe
status: active
updated: 2026-08-25
parent_page: README.md
tags: [cindy, discord, voice, commands, npc-tools]
---

# Cindy Lou Discord Voice Bridge Commands

This page documents the Discord text commands registered by Cindy Lou's local voice bridge runtime.

These are **bridge commands**, not normal OpenClaw chat prompts. They control the local Discord voice process that joins the Shadowrun voice channel, writes live transcripts into a session thread, generates or plays Cindy voice clips, and exposes debug/status information for the GM/operator.

Current source of truth:

```text
/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py
```

## Operating model

The bridge is configured for one Shadowrun Discord guild and one target voice channel. Session commands create or reuse a dated public session thread under the configured transcript/text channel. Voice commands use the configured voice channel, the currently connected Discord voice client, and the local Kokoro/TTS stack.

The current posture is **text-first and GM-controlled for voice**:

- transcription and command/status messages go to the active session thread when one exists;
- generated live voice can be toggled separately from text replies;
- saved/generated clips are preserved first, then played manually or automatically only when the relevant gates allow it;
- automatic live playback speaks a short first-sentence summary while the full text reply stays in the session thread;
- Kokoro worker health is treated as part of session readiness because warm local TTS is what makes short live lines practical.

## Session lifecycle commands

### `!session-start`

Aliases: `!session-open`, `!session-begin`

Starts a live Cindy session.

What it does:

- creates or reopens today's `Session YYYY-MM-DD` public thread in the configured text channel;
- binds that thread as the active session thread;
- resets live-session runtime state and transcript counters;
- writes watchdog and live-monitor status files;
- starts the external watchdog;
- warms the Kokoro worker before treating the session as ready;
- starts Whisper/STT warmup in the background;
- forces the bridge to join the configured Discord voice channel;
- runs Discord voice join and Kokoro warmup in parallel to reduce session-start latency;
- starts the Kokoro worker health monitor;
- reports whether voice join and Kokoro warmup succeeded.

If Discord voice is blocked by DAVE / End-to-End Encryption, the command reports that separately and tells the operator to disable E2EE for the Shadowrun voice channel.

### `!voice-warm`

Alias: `!cindy-warm`

Pre-warms the live voice path before a session or before a likely Cindy-heavy scene.

What it does:

- cancels any pending Kokoro idle shutdown;
- warms the Kokoro worker;
- warms Whisper/STT;
- refreshes cached stalling clips when stalling voice is enabled;
- reports elapsed time, Kokoro readiness, stalling-cache counts, and the current idle-stop window.

Use this shortly before play if the operator wants the first Cindy response to avoid the cold Kokoro startup cost. It does not create a session thread or force Cindy into voice; use `!session-start` for the full session lifecycle.

### `!session-end`

Ends the active live Cindy session.

What it does:

- posts a session-ended marker into the active session thread;
- archives the thread;
- clears the active session thread binding;
- releases the voice hold so the bridge no longer tries to remain connected;
- marks watchdog/live-monitor state inactive;
- archives live-session runtime files;
- stops the Kokoro health monitor;
- schedules the Kokoro worker idle shutdown.

If no active session thread exists, it still clears session/voice hold state and schedules Kokoro idle shutdown.

## Voice connection and status commands

### `!voice-status`

Prints a compact status line for the voice bridge.

Reported fields include:

- whether the local and guild voice clients are connected;
- whether session voice hold is active;
- whether voice wake and active-thread wake are enabled;
- whether live voice playback and stalling voice are enabled;
- stalling voice timing and maximum phrase count;
- TTS chunking settings;
- Kokoro worker running/health/idle status;
- target voice channel name and non-bot member count;
- whether the Discord voice receive library is available.

Use this as the first quick check when Cindy is connected, silent, speaking unexpectedly, or failing to generate voice.

### `!voice-debug`

Prints a smaller low-level debug line.

Reported fields include:

- bridge process ID;
- whether session voice hold is active;
- local and guild voice connection booleans;
- local and guild voice channel names.

This is mainly useful when `!voice-status` says the bridge should be connected but Discord state looks stale or contradictory.

### `!voice-join`

Forces the bridge to join the configured Shadowrun voice channel.

What it does:

- enables session voice hold;
- cancels pending Kokoro idle shutdown;
- attempts a forced voice join;
- reports the join result;
- reports DAVE / E2EE blockage if detected;
- clears voice hold again if the forced join fails.

This is the manual recovery command when a session is active but Cindy is not in voice.

### `!voice-leave`

Disconnects the bridge from Discord voice.

What it does:

- disables session voice hold;
- clears rejoin attempts;
- force-disconnects the current voice client if connected;
- clears the audio sink;
- schedules Kokoro worker idle shutdown;
- reports the leave action to the active session thread, or the command channel as fallback.

This does not archive the session thread. Use `!session-end` when the whole live session is over.

## Live voice behavior commands

### `!live-voice [on|off|toggle|status]`

Aliases: `!cindy-live-voice`, `!voice-live`

Controls whether fresh generated live replies are played into Discord voice.

Modes:

- `on`, `enable`, `enabled`, `true`, `1`, `yes` - enable live playback;
- `off`, `disable`, `disabled`, `false`, `0`, `no` - disable live playback;
- `toggle`, `flip` - invert the current setting;
- `status`, `state`, `?` - report the current setting.

When enabled, the runtime uses the current fresh-Kokoro path: generate/preserve the clip, then play it into Discord voice if the reply actually emitted and prompt-level no-voice suppression did not apply. For automatic live playback, the spoken clip is capped to a short first-sentence summary by `LIVE_VOICE_SPOKEN_MAX_CHARS`; the full text reply remains in Discord.

### `!voice-stalling [on|off|toggle|status]`

Aliases: `!cindy-voice-stalling`, `!stalling-voice`

Controls short stalling barks while a bespoke Cindy reply is still generating.

Modes match `!live-voice`: `on`, `off`, `toggle`, or `status` with the same boolean synonyms.

The status response includes:

- whether stalling voice is enabled;
- initial, repeat, and long-running delay settings;
- maximum stalling phrase count;
- acknowledgement phrases;
- normal stalling phrases;
- long-running stalling phrase.

Stalling voice is a presence cue, not a replacement for the real answer. It only matters when the saved-voice/live-voice gates, voice connection, and prompt context allow it.

### `!voice-stalling-cache`

Alias: `!stalling-voice-cache`

Pre-renders or refreshes cached stalling voice clips.

The command reports:

- whether the cache operation succeeded;
- how many clips were rendered;
- how many failed.

Use this before a session if stalling voice is enabled and the operator wants the first cue to avoid a cold TTS render.

## Playback and TTS commands

### `!voice-say <text>`

Aliases: `!cindy-say`, `!Cindy-Say`

Generates local TTS for the supplied text and speaks it into Discord voice.

What it does:

- forces a voice join if needed;
- runs the configured TTS backend, currently usually Kokoro through the warm worker when available;
- applies the TTS middle-layer cleanup/pronunciation path;
- plays the generated temporary audio into Discord voice;
- reports success or a short error.

This is useful for ad-hoc operator-triggered Cindy speech. For reusable or generated live-session lines, prefer preserved saved clips when possible.

### `!voice-play-saved <clip_name>`

Plays a preserved/generated voice clip by name.

Lookup behavior:

- clips are resolved inside Cindy's `preserved_voice` folder;
- if an extension is supplied, only that filename is checked;
- without an extension, the bridge checks `.wav`, `.mp3`, `.ogg`, and `.aiff` variants;
- path traversal is rejected by resolving candidates under the preserved-voice directory.

This is the main manual GM playback path for voice lines Cindy has already generated and preserved. Cindy often reports commands in this shape after preparing a saved clip:

```text
!voice-play-saved cindy_live_ping_example_20260819_131200
```

### `!voice-play <audio_path>`

Plays a local audio file path through Discord voice.

This is a lower-level operator/debug command. Unlike `!voice-play-saved`, it accepts a local path and depends on that path being reachable by the bridge process. Use the saved-clip command for ordinary table workflow.

### `!voice-stop`

Aliases: `!voice-shush`, `!cindy-stop`

Stops current Discord voice playback.

Responses distinguish three cases:

- not connected;
- connected but nothing is playing;
- playback stopped successfully.

Use this if a clip is wrong, too long, overlapping, or no longer useful to the table.

## Wake behavior that is not a command

The bridge also has wake behavior controlled by configuration rather than Discord text commands.

- `VOICE_WAKE_ENABLED` controls whether voice-transcript wake phrases can summon Cindy from voice transcription.
- `ACTIVE_THREAD_WAKE_ENABLED` controls whether active session-thread messages/transcripts that mention Cindy can route to Cindy.
- `WAKE_WORD` defaults to `cindy`.
- `LIVE_WAKE_CONTEXT_LIMIT` limits how many recent thread messages are added to live wake prompts.
- `OPENCLAW_BRIDGE_TIMEOUT_S` and `OPENCLAW_BRIDGE_PROCESS_GRACE_S` cap the OpenClaw subprocess wait for live wake answers.
- `KOKORO_WORKER_IDLE_TIMEOUT_S` controls how long the warm Kokoro worker stays alive after session end or pre-warm.

When active-thread wake is enabled, a transcript line or in-session text message that targets Cindy can be handled as a wake event without someone typing a `!` command. That path is separate from the command list above.

## Related pages

- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
- [Cindy Lou Voice Clip Phrase Library](Voice-Clip-Phrase-Library.md)
- [Cindy Lou TTS Middle Layer](TTS-Middle-Layer.md)
- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md)
