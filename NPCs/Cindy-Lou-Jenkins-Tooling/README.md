---
title: Cindy Lou Tooling
permalink: /NPCs/Cindy-Lou-Jenkins-Tooling/
type: npc-tooling-index
visibility: player-safe
status: active
updated: 2026-09-04
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

## Active behavior tools

- [Cindy Lou Voice Clip Phrase Library](Voice-Clip-Phrase-Library.md) - short reusable clips, saved-line playback, stalling cues, and chaining behavior for fast live voice responses.
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - current `!session-*`, `!voice-*`, live voice, stalling voice, playback, and wake-control command reference.
- [Cindy Lou TTS Middle Layer](TTS-Middle-Layer.md) - local text cleanup, pronunciation guides, and Southern cadence shaping before Kokoro renders speech.
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md) - current overview of Cindy's wiki, Discord, voice, and runtime support.
- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md) - how Cindy watches live sessions, classifies prompts, and decides when a GM nudge or direct answer is warranted.
- [Cindy Lou Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md) - active session-scoped working memory for live play.
- [Cindy Lou External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md) - sidecar alerting for stalled live transcription.
- [Cindy Lou Post-Session Automation](Post-Session-Automation.md) - planned end-of-session cleanup, memory, and wiki workflow.
- [Cindy Lou Tooling Future Planning](Future-Planning.md) - future mini-tool and workflow ideas for shared table state, GM controls, session closeout, onboarding, and VTT companion aids.
- [Cindy Lou Anti-LLM In-Character Voice Pass](Anti-LLM-In-Character-Voice.md) - prose-shaping rules for in-character Cindy text so she sounds less like a generic model and more like a specific SA-knowbot.

## Architecture and archives

- [Cindy Lou Wiki and Tooling Topology](Wiki-and-Tooling-Topology.md) - how Cindy's wiki, tooling, and Discord surfaces fit together.
- [Cindy Lou Soundboard and Voice Bridge](Soundboard-and-Voice-Bridge.md) _(outdated)_ - archived notes from the old custom soundboard web-app prototype.

## Operating principle

Cindy-specific tools should live here by default. Broader campaign apps and player-facing SR3 workflow aids belong under [Minigames and Web Apps](../../Minigames.md), but NPC behavior, voice clips, live-session monitoring, and Cindy-specific Discord workflow should point back to this section.
