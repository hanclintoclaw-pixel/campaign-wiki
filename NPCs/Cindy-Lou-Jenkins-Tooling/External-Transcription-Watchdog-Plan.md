---
title: Cindy Lou External Transcription Watchdog Plan
type: tech-note
visibility: player-safe
status: active
updated: 2026-05-22
tags: [cindy, discord, voice, monitoring, watchdog, implementation-plan]
---

# Cindy Lou External Transcription Watchdog Plan

## Goal

Detect a **live transcription stall during an active session** and send a **GM ping** even if the main voice bridge has stopped transcribing correctly.

The key requirement is architectural:

> this watchdog must live **outside** the voice bridge process, but be **activated by** the voice bridge when a session starts.

That way, a stuck or degraded transcription loop cannot be trusted as the only thing responsible for reporting its own failure.

## Current implementation status

As of **2026-05-22**, the first-pass version of this watchdog has been wired into the live voice bridge runtime.

Implemented now:

- voice bridge writes `session-status.json`
- voice bridge launches an external `voice_bridge_watchdog.py` process on session start
- watchdog polls live session health on a timer
- watchdog detects **recent audio + stale transcript**
- watchdog logs alerts to `watchdog-alerts.jsonl`
- watchdog posts a GM ping through an independent Discord REST message path
- watchdog exits when the session is marked inactive

Still worth improving later:

- richer STT error counters in exported health status
- more nuanced queue/backpressure heuristics
- optional dedicated webhook or notifier identity separate from the bot token
- a cleaner operator test harness for simulated failures

## Why this exists

The specific failure we want to catch is not simply “the bridge process died.”

The more dangerous case is:

- the session is still active
- the bridge process may still be running
- people are still talking
- but transcript output has stopped or become unhealthy
- nobody notices for too long

This design is for that case.

## Non-goals

This watchdog is **not** intended to:

- replace the main voice bridge
- interpret scene meaning
- decide when Cindy should roleplay
- burn model tokens for periodic checks

It should be a **cheap local process** with deterministic rules.

## Recommended architecture

Use a **sidecar watchdog** process launched on session start.

### Main pieces

1. **Voice bridge**
   - owns voice connection, buffering, STT, and transcript emission
   - writes health/status data to disk
   - starts the watchdog when a session starts
   - marks the session inactive when it ends

2. **External watchdog process**
   - separate PID from the voice bridge
   - polls status files and transcript output on a timer
   - sends GM alerts through an **independent notifier path**

3. **Independent alert path**
   - preferred: a Discord webhook for the GM monitoring destination
   - alternate: a minimal separate notifier process or alert bot

The important property is that the alerting route should not depend on the stuck transcription loop.

## Session lifecycle

### On session start

The voice bridge should:

1. create or bind the live session thread as usual
2. write `session-status.json` with `session_active=true`
3. include enough metadata for alerting
4. launch `voice_bridge_watchdog.py` if not already running for that session

### During the session

The voice bridge should keep updating health fields whenever relevant events occur.

### On session end

The voice bridge should:

1. write `session_active=false`
2. write `ended_at`
3. optionally write `shutdown_reason`
4. allow the watchdog to exit cleanly on its next poll

## File contract

All files below should live under the existing live-session runtime directory:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/session-status.json`
- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/watchdog-status.json`
- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/watchdog-alerts.jsonl`

### `session-status.json`

This is the core contract from the voice bridge to the watchdog.

Suggested fields:

```json
{
  "session_active": true,
  "session_id": "2026-05-22T19-00-shadowrun",
  "thread_id": 1234567890,
  "voice_channel_id": 1234567890,
  "gm_mention_id": 430878744907874305,
  "started_at": "2026-05-22T19:02:11",
  "last_status_write_at": "2026-05-22T19:41:00",
  "voice_connected": true,
  "voice_bridge_pid": 63235,
  "last_audio_seen_at": "2026-05-22T19:40:56",
  "last_audio_user_id": 160506560831815681,
  "last_transcript_emit_at": "2026-05-22T19:39:37",
  "last_stt_success_at": "2026-05-22T19:39:37",
  "last_stt_error_at": "2026-05-22T19:38:12",
  "transcript_event_count": 418,
  "stt_queue_depth": 0,
  "consecutive_stt_errors": 0,
  "log_path": "/Users/hanclaw/.openclaw/workspace-cindylou/voice_bridge.log",
  "transcript_path": "/Volumes/carbonite/claw/data/cindylou/runtime/live-session/transcript.jsonl"
}
```

### `watchdog-status.json`

This is written by the watchdog for debugging and operator visibility.

Suggested fields:

```json
{
  "watchdog_pid": 70001,
  "session_id": "2026-05-22T19-00-shadowrun",
  "last_poll_at": "2026-05-22T19:41:00",
  "stall_condition": true,
  "stall_reason": "audio_recent_but_transcript_stale",
  "consecutive_bad_polls": 3,
  "last_alert_at": "2026-05-22T19:40:20",
  "last_recovery_at": null
}
```

### `watchdog-alerts.jsonl`

Append-only audit log of what the watchdog alerted on and when.

## Health signals the voice bridge must export

The watchdog only works if the bridge exports the right low-level signals.

Minimum required:

- `session_active`
- `voice_connected`
- `last_status_write_at`
- `last_audio_seen_at`
- `last_transcript_emit_at`
- `last_stt_success_at`
- `transcript_event_count`
- `log_path`

Strongly recommended:

- `last_stt_error_at`
- `consecutive_stt_errors`
- `stt_queue_depth`
- `voice_bridge_pid`

## Core detection logic

The watchdog should poll every **10 seconds**.

### Important distinction

We do **not** want to alert merely because nothing is being transcribed.

That would false-positive during:

- long pauses
- bathroom breaks
- table silence
- tactical thinking time

So the main signal is:

> **audio is still arriving, but transcript output is not advancing**

### Recommended stall rule

Flag a likely transcription stall if all are true:

- `session_active == true`
- `voice_connected == true`
- `now - last_audio_seen_at <= 20s`
- `now - last_transcript_emit_at >= 75s`

Equivalent alternate check:

- `transcript_event_count` unchanged for >= 75s
- while `last_audio_seen_at` remains recent

### Stronger error rule

Also treat the situation as degraded if:

- `consecutive_stt_errors >= 3`
- or `stt_queue_depth` keeps growing across polls
- or `last_status_write_at` itself goes stale while process is supposed to be active

## Debounce and cooldown

To avoid noisy alerts:

### Debounce

Require the stall condition to be true for **2 or 3 consecutive polls** before alerting.

At a 10-second poll interval, that means roughly **20–30 seconds of confirmation** before sending the first GM ping.

### Cooldown

After sending an alert:

- do not send the same alert again for **10 minutes**
- unless the reason class changes materially

### Recovery notice

If the watchdog has alerted and transcript flow resumes, send a short recovery note:

> Cindy watchdog: transcription resumed after 112s stall.

That closes the loop and reassures the GM that the issue cleared.

## Alert classes

Recommended reason classes:

- `audio_recent_but_transcript_stale`
- `stt_error_burst`
- `status_file_stale`
- `voice_bridge_process_missing`
- `voice_disconnected_while_session_active`

## Alert text

Keep the message short and operational.

Example:

> `<@GM_ID> Cindy watchdog: live session is active, audio is still arriving, but transcription has stalled for 94s. Check VB. Log: /Users/hanclaw/.openclaw/workspace-cindylou/voice_bridge.log`

The real GM mention token should come from config or session metadata, not be hardcoded in the watchdog source.

## Recommended notifier path

Preferred order:

1. **Discord webhook** to the GM monitoring destination
2. separate tiny alert bot/process
3. other local notifier that can post into the GM channel/thread

Recommendation: use a webhook if thread/channel routing is workable, because it is simple and independent.

## Process supervision model

### Best practical version

- the voice bridge launches the watchdog on session start
- the watchdog runs as a detached local process
- the watchdog exits when `session_active=false`

### Optional stronger version

Use a tiny supervisor script that launches both:

- voice bridge
- session watchdog

This makes orchestration cleaner, but it is not required for the first pass.

## Suggested implementation phases

### Phase 1 — minimal useful version

Implement:

- `session-status.json`
- watchdog process launch on session start
- 10-second polling
- recent-audio + stale-transcript rule
- single GM alert
- single recovery alert

This is the smallest version that solves the real operational problem.

### Phase 2 — stronger diagnostics

Add:

- `watchdog-status.json`
- alert audit log
- `consecutive_stt_errors`
- queue-depth monitoring
- reason classes in alerts

### Phase 3 — operator polish

Add:

- helper scripts for status and restart
- easy test mode / simulated stall mode
- optional synthetic health pings into a debug thread

## Concrete files to add

Recommended first-pass additions:

- `/Users/hanclaw/claw/projects/discord_voice_patch/voice_bridge_watchdog.py`
- `/Users/hanclaw/claw/projects/discord_voice_patch/watchdog_notify.py`
- `/Users/hanclaw/.openclaw/workspace-cindylou/bin/test_voice_watchdog.sh`

And extend:

- `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py`

## Config knobs

Suggested env/config values:

- `WATCHDOG_ENABLED=true`
- `WATCHDOG_POLL_INTERVAL_S=10`
- `WATCHDOG_AUDIO_RECENT_S=20`
- `WATCHDOG_TRANSCRIPT_STALE_S=75`
- `WATCHDOG_DEBOUNCE_POLLS=3`
- `WATCHDOG_ALERT_COOLDOWN_S=600`
- `WATCHDOG_WEBHOOK_URL=...`

## Testing plan

### Test 1 — silence should not alert

- start a session
- let the table sit quiet
- confirm no stall ping is sent

### Test 2 — healthy speech should not alert

- start a session
- speak normally
- confirm transcript keeps advancing
- confirm no alert

### Test 3 — simulated transcription freeze should alert

- start a session
- keep audio flowing
- deliberately block transcript emission or STT success updates
- confirm GM alert fires after threshold

### Test 4 — recovery should clear

- restore transcript flow
- confirm recovery message is sent
- confirm repeated alerts stop

## Recommendation summary

If this is implemented today, the best first cut is:

- **external watchdog process**
- **started by the voice bridge on session start**
- **reads status JSON + transcript progress**
- **alerts via independent Discord webhook**
- **uses recent-audio + stale-transcript logic with debounce**

That gets the right operational behavior without burning model tokens or overcomplicating the first version.

## Related pages

- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
