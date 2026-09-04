---
title: Cindy Lou Discord Voice Bridge Commands
type: tech-note
visibility: player-safe
status: active
updated: 2026-09-04
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
- panel-generated voice lines are saved first, then played with the GM's **Play Last Voice** button or `!cindy-play-last-voice`;
- Kokoro worker health is treated as part of session readiness because warm local TTS is what makes short live lines practical;
- the GM control panel provides one-click silence/resume, summary, suggestion, voice-line, playback, interrupt, marker, and closeout controls.

## GM control panel commands

### `!cindy-panel`

Aliases: `!gm-panel`, `!cindy-gm-panel`

Opens the Discord-native GM control panel as a button card.

Current buttons:

- **Status** - compact session / voice / wake / Kokoro state.
- **Stay Silent** - disables live wakes, active-thread wakes, proactive monitor, live playback, and stalling voice until resumed or restart.
- **Resume Wakes** - resumes active-thread wakes and live playback.
- **Summarize 5m** - asks Cindy for a concise GM-facing summary of recent transcript.
- **Suggest Cindy Action** - asks Cindy for one optional GM-facing action or HOLD SILENCE.
- **Generate Voice Line** - drafts and saves one short Cindy voice line without playing it.
- **Roll Test** - opens a modal for skill/pool, dice, target number, and context; posts a 🤠 session-thread result and speaks it if connected.
- **Speak Line** - opens a text modal for the GM to type an exact Cindy line, then saves, posts, and plays it immediately.
- **Play Last Voice** - plays the most recent GM-panel-generated or custom-spoken voice line for this session.
- **Interrupt Cindy** - stops current voice playback.
- **Soundboard dropdown** - plays one of 12 pre-rendered canon-voice Cindy stock phrases.
- **Mark Canon** - opens a text-entry modal and saves a canon note with recent transcript context.
- **Mark GM-Only** - opens a text-entry modal and saves a GM-only note with recent transcript context.
- **Closeout Prompt** - posts the end-session checklist without ending the session.

See [Cindy Lou GM Control Panel](GM-Control-Panel.md) for the full workflow.

### `!cindy-status`

Text fallback for the panel's **Status** button.

### `!cindy-silent`

Text fallback for **Stay Silent**.

### `!cindy-resume`

Text fallback for **Resume Wakes**.

### `!cindy-summary`

Text fallback for **Summarize 5m**.

### `!cindy-suggest`

Text fallback for **Suggest Cindy Action**.

### `!cindy-voice-line`

Text fallback for **Generate Voice Line**.

### `!cindy-roll <dice> <target-number> [skill/context]`

Text fallback for **Roll Test**.

Example:

```text
!cindy-roll 5 6 Cindy Computer
```

The button version opens a modal. It defaults to **Cindy Computer 5** against **TN 5**, supports an optional purpose/context field, uses SR3-style exploding sixes, posts the result to the active session thread with Cindy's 🤠 icon, logs the roll, and speaks the success count if Cindy is connected to voice.

Default/preset reference values include Cindy Computer 5, Cindy Hacking Pool 4, common utility ratings from Cindy's table-use assumptions, Tip Jar Sensor/Pilot 2, Tip Jar fuzzy Pilot 4, Dolly Zoom Pilot 1, and Dolly Zoom Sensor 0.

### `!cindy-speak-line <line>`

Alias: `!cindy-speak-now`

Text fallback for **Speak Line**. The button version opens a modal with an optional header and required line text. The text-command version speaks the provided line without a header.

It saves the line as a preserved clip, posts the line text plus saved-clip command into the active session thread, makes it the panel's latest saved voice line, and plays it immediately if Cindy is connected to voice.

### `!cindy-play-last-voice`

Aliases: `!cindy-play-last`, `!cindy-play`

Text fallback for **Play Last Voice**. It plays the most recent GM-panel-generated or custom-spoken voice line saved in the current session. The last saved panel line starts empty at each `!session-start`.

### `!cindy-interrupt`

Aliases: `!cindy-interrupt-voice`, `!cindy-shush`

Text fallback for **Interrupt Cindy**. It stops current Cindy voice playback, matching the safety intent of `!voice-stop`.

### Soundboard dropdown

The panel dropdown **Play Cindy stock phrase...** is not a text command. It is a Discord select menu embedded in `!cindy-panel`.

The first stock set contains 12 fresh canon-voice clips:

- On it, sugar.
- Give me a beat.
- That tracks.
- Hold up now.
- I smell trouble.
- Ask the GM.
- Jack out, now.
- Keep it quiet.
- We got heat.
- Little victory.
- No promises.
- I'm listening.

The bridge resolves these by stable filenames under Cindy's `preserved_voice` folder, with private repo fallback copies under `soundboard_clips/`.

### `!cindy-mark canon|gm-only [note text]`

Text fallback for **Mark Canon** and **Mark GM-Only**. The button version opens a Discord modal; the text-command version stores the note text after the marker type.

### `!cindy-closeout-prompt`

Text fallback for **Closeout Prompt**. It does not run `!session-end`.

## Session lifecycle commands

### `!session-start`

Aliases: `!session-open`, `!session-begin`

Starts a live Cindy session.

What it does:

- creates or reopens today's `Session YYYY-MM-DD` public thread in the configured text channel;
- binds that thread as the active session thread;
- resets live-session runtime state, transcript counters, panel audit files, GM-only/canon marker files, and the panel's last saved voice line;
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

When enabled, the runtime uses the current fresh-Kokoro path: generate/preserve the clip, then play it into Discord voice if the reply actually emitted and prompt-level no-voice suppression did not apply. The preferred table workflow is still GM-controlled saved playback through the panel or `!voice-play-saved`, so automatic playback should be treated as optional and scene-dependent.

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

### `!voice-attach <text>`

Aliases: `!cindy-attach`, `!voice-file`

Generates preserved Cindy voice clip files from supplied text and attaches the resulting audio files directly in Discord.

This is useful when the GM wants a downloadable/replayable clip artifact in chat rather than only a local saved-clip command. For live play, the GM control panel's **Generate Voice Line** plus **Play Last Voice** path is usually lower friction.

### `!voice-stop`

Aliases: `!voice-shush`, `!cindy-stop`

Stops current Discord voice playback.

Responses distinguish three cases:

- not connected;
- connected but nothing is playing;
- playback stopped successfully.

Use this if a clip is wrong, too long, overlapping, or no longer useful to the table.

## GM panel runtime files

The panel writes per-session local runtime files under the live-session runtime directory:

```text
gm-control-panel.jsonl
gm-control-panel-markers.jsonl
```

`gm-control-panel-markers.jsonl` stores typed Canon / GM-only notes plus optional label, recent transcript context, session ID, thread ID, timestamp, user ID, and intended use `session_closeout`.

`!session-start` clears them for the new session. `!session-end` archives them with the rest of the session runtime files.

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
