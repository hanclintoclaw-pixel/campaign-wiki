---
title: Cindy Lou Tooling
permalink: /NPCs/Cindy-Lou-Jenkins-Tooling/
type: npc-tooling-index
visibility: player-safe
status: active
updated: 2026-09-09
parent_page: ../Cindy-Lou-Jenkins.md
tags: [cindy, tooling, voice, discord, npc-tools, sr3]
---

# Cindy Lou Tooling

This section collects the tools, voice behavior, and support systems that make **Cindy Lou Jenkins** work as a live NPC / A-NPC at the table.

For the objective character dossier, see [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md). For the in-world voice page, see [Cindy Lou Jenkins, In Her Own Words](../Cindy-Lou-Jenkins-In-Her-Own-Words.md).

## Project goal

The Cindy Lou tooling project is aimed at making Cindy feel like an **active NPC at the virtual table**, not just a wiki entry or a chatbot waiting off-screen.

The current build is working toward four connected goals:

- **live awareness:** Cindy can follow session transcript/context closely enough to notice direct requests, Matrix/security openings, and moments where a GM nudge would actually help;
- **disciplined table presence:** the live monitor is intentionally conservative, so Cindy stays quiet during ordinary chatter and avoids interrupting just because someone said her name;
- **fast table voice:** short saved clips, generated lines, and GM-triggered playback let Cindy answer in her own voice without forcing the table to wait on long synthesis jobs;
- **campaign continuity:** session scratchpads, memory ingestion, wiki updates, and post-session plans keep useful play facts from evaporating after the call ends.

The desired end state is a table companion that can listen, remember, speak when invited, help with Shadowrun 3rd Edition reference and Matrix/campaign tooling, and preserve continuity between sessions while still respecting the GM's control of pacing and canon.

## Current operating snapshot

As of 2026-09-09, the active Cindy Lou runtime is the local Discord voice bridge at `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py`.

Current live posture:

- **active-thread wakes are on:** direct Cindy prompts in the active session thread can route to Cindy without a `!` command;
- **voice wake is off by default:** spoken transcript wakes are not the primary control path unless explicitly enabled;
- **proactive monitor is enabled but GM-gated:** the live monitor can create private Cindy Initiative proposals for the GM, but it does not publicly act or auto-speak those suggestions;
- **voice is GM-controlled:** saved/generated clips are enabled, live playback can be toggled, and panel-generated lines are played manually through the GM panel by default;
- **Kokoro worker and stalling voice are enabled:** short lines and small presence barks are pre-warmed/cached for live-table latency, with interrupt/silence controls nearby;
- **session capture is enabled:** raw audio, transcript events, prompt contexts, model outputs, and TTS outputs can be preserved for debugging, replay, and future tuning.

The system is therefore best described as **active support with GM approval**, not autonomous co-GM behavior.

## Active behavior tools

- [Cindy Lou Voice Clip Phrase Library](Voice-Clip-Phrase-Library.md) - short reusable clips, saved-line playback, stalling cues, and chaining behavior for fast live voice responses.
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - current `!session-*`, `!voice-*`, `!cindy-*`, live voice, stalling voice, playback, panel, and wake-control command reference.
- [Cindy Lou GM Control Panel](GM-Control-Panel.md) - Discord-native GM button panel for silence/resume, summaries, Cindy action suggestions, SR3 roll tests, saved/generated/custom voice-line playback, interruption, 12-phrase soundboard dropdown, canon markers, and closeout prompts.
- [Cindy Lou TTS Middle Layer](TTS-Middle-Layer.md) - local text cleanup, pronunciation guides, and Southern cadence shaping before Kokoro renders speech.
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md) - current overview of Cindy's wiki, Discord, voice, and runtime support.
- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md) - how Cindy watches live sessions, classifies prompts, and decides when a GM nudge or direct answer is warranted.
- [Cindy Lou Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md) - active session-scoped working memory for live play.
- [Cindy Lou External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md) - sidecar alerting for stalled live transcription.
- [Cindy Lou Live Session Capture and Replay](Live-Session-Capture-and-Replay.md) - evidence capture for raw audio, STT, prompts, model outputs, and TTS artifacts used to debug and tune live behavior.
- [Cindy Lou Post-Session Automation](Post-Session-Automation.md) - local `scripts/cindy-session-closeout` packet builder plus end-of-session cleanup, memory, and wiki workflow.
- [Cindy Lou Tooling Future Planning](Future-Planning.md) - future mini-tool and workflow ideas for shared table state, GM controls, session closeout, onboarding, and VTT companion aids.
- [Cindy Lou Anti-LLM In-Character Voice Pass](Anti-LLM-In-Character-Voice.md) - prose-shaping rules for in-character Cindy text so she sounds less like a generic model and more like a specific SA-knowbot.

## Architecture and archives

- [Cindy Lou Wiki and Tooling Topology](Wiki-and-Tooling-Topology.md) - how Cindy's wiki, tooling, and Discord surfaces fit together.
- [Cindy Lou Soundboard and Voice Bridge](Soundboard-and-Voice-Bridge.md) _(outdated)_ - archived notes from the old custom soundboard web-app prototype.

## Operating principle

Cindy-specific tools should live here by default. Broader campaign apps and player-facing SR3 workflow aids belong under [Minigames and Web Apps](../../Minigames.md), but NPC behavior, voice clips, live-session monitoring, and Cindy-specific Discord workflow should point back to this section.
