---
title: Cindy Lou Live Session Capture and Replay
type: tech-note
visibility: player-safe
status: active
updated: 2026-09-09
parent_page: README.md
tags: [cindy, discord, voice, monitoring, capture, replay, npc-tools]
---

# Cindy Lou Live Session Capture and Replay

This page documents the evidence-capture layer in Cindy Lou's Discord voice bridge.

It is not a player-facing feature during play. It is an operator/debugging layer that preserves enough live-session material to understand what Cindy heard, what prompts were built, what the model returned, and what audio was rendered.

## Current implementation

The active implementation lives in:

```text
/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py
```

Current configured capture root:

```text
/Volumes/falcon/claw/data/cindylou/session-captures
```

The bridge starts capture when a live session starts and stops it when the session is archived/ended. Each session receives a capture directory, and each run inside that session receives its own run directory.

## Current config posture

The active bridge environment enables the capture layer:

```text
SESSION_CAPTURE_ENABLED=true
SESSION_CAPTURE_RAW_PCM=true
SESSION_CAPTURE_PROMPTS=true
SESSION_CAPTURE_MODEL_OUTPUTS=true
SESSION_CAPTURE_TTS_OUTPUTS=true
```

Those settings mean Cindy can retain both raw evidence and generated artifacts for later inspection. This is especially useful when tuning the live monitor, active-thread wakes, stalling voice, and Kokoro latency.

## Capture layout

The bridge creates an immutable session-level capture root plus one or more generated run directories.

Session-level files include:

- `manifest.json` - configuration snapshot for the session capture root
- `raw_timeline.jsonl` - raw capture timeline
- `01_raw_audio/` - per-user raw PCM files when raw capture is enabled
- `runs/` - generated interpretations and outputs

Run-level files include:

- `manifest.json` - configuration snapshot for that run
- `run_timeline.jsonl` - interpreted runtime timeline
- `02_audio_windows/` - WAV windows sent to STT
- `03_recognized_text/` - STT recognition records
- `04_transcript_events/` - transcript event JSON snapshots
- `05_wake_detection/` - wake-detection artifacts when available
- `06_prompt_contexts/` - prompt payloads sent to OpenClaw
- `07_llm_outputs/` - model response records
- `08_tts_outputs/` - rendered TTS artifacts copied for inspection
- `09_eval/` - reserved evaluation output area

## What it is for

Use capture artifacts to answer questions like:

- did STT hear the player correctly?
- did the active session thread include the right context?
- did the monitor's prompt view include stale or missing scene state?
- did OpenClaw latency dominate the response time?
- did Kokoro render the right spoken text with the expected pronunciation guides?
- did a stalling cue help or just add noise?
- would a different Cindy Initiative threshold have caught or suppressed a moment?

## Safety and retention posture

These artifacts can include raw player audio, transcript text, prompt context, and generated model output. Treat them as local operational evidence, not public wiki content.

Player-visible wiki updates should be distilled from approved session notes and closeout workflow, not copied directly from raw capture directories.

## Relationship to other tools

- [Live Session Monitoring Design](Live-Session-Monitoring-Design.md) explains the monitor that capture helps tune.
- [Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md) explains the scene-state files capture can help evaluate.
- [External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md) explains the health sidecar that watches live transcription.
- [Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) documents the commands that start/end sessions and generate voice artifacts.
- [Post-Session Automation](Post-Session-Automation.md) describes the later closeout workflow that may consume preserved transcript/session evidence.
