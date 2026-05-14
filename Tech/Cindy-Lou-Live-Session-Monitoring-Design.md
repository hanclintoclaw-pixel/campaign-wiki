---
title: Cindy Lou Live Session Monitoring Design
type: tech-note
visibility: player-safe
status: draft
updated: 2026-05-13
tags: [cindy, discord, voice, monitoring, design]
---

# Cindy Lou Live Session Monitoring Design

## Purpose

This page describes a proposed system that would let Cindy Lou Jenkins track live session flow from local voice transcriptions, maintain scene awareness efficiently, and decide when to nudge the GM during major planning or scene beats.

The goal is **not** constant full-session re-reading.

The goal is a token-efficient loop where Cindy:

- watches live transcript deltas
- maintains compact scene memory
- only escalates when something important is happening

## Problem statement

During active play, Cindy currently has useful technical and narrative context, but she does not yet maintain a strong rolling picture of longer live scenes unless prompted directly.

That creates three problems:

1. **scene drift**
   - Cindy can lose track of a longer plan discussion
2. **timing gaps**
   - Cindy may notice something only after the moment has passed
3. **token inefficiency**
   - re-feeding raw transcript history into a large model repeatedly is wasteful

## Design goals

### Primary goals

- keep transcript processing local-first
- minimize large-model token usage
- maintain rolling awareness of the current scene
- detect when Cindy should ping the GM like a player at the table
- preserve enough structured state that a new system could resume intelligently

### Non-goals

- full verbatim semantic understanding of every second of table talk
- constant reply generation
- replacing normal direct player/GM interaction
- building a giant generalized meeting-minutes system before the Cindy use case works

## Core design pattern

Use a **two-stage monitoring loop**:

1. **cheap local heuristics over new transcript lines**
2. **small local LLM summarization only when needed**

That local loop updates a rolling **scene-state JSON**.

Only when that scene state says a real intervention might be useful does Cindy escalate into a GM-facing ping.

## Data flow

### Step 1: transcript ingestion

Voice transcription events are appended locally to a transcript log.

Each transcript entry should preserve at least:

- timestamp
- speaker label / speaker id
- transcript text
- confidence if available
- channel / thread / session identifiers
- source event id or sequence number

### Step 2: incremental checkpointing

A checkpoint file tracks the last processed transcript item.

That lets the summarizer read only the **delta** since the previous pass instead of re-reading the full session.

### Step 3: local summarization pass

On a regular cadence, Cindy reads only the new transcript delta and updates scene state.

Recommended cadence:

- every 60 seconds by default
- faster during heavy planning if needed
- also allowed on pause/quiet windows after several meaningful lines land

### Step 4: scene-state update

The summarizer merges the new delta into a rolling scene-state file.

### Step 5: intervention decision

A small decision layer evaluates whether:

- no action is needed
- Cindy should keep watching silently
- Cindy should prepare a possible contribution
- Cindy should ping the GM now

## Proposed file/state layout

### Raw transcript log

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/transcript.jsonl`

Each line would be one utterance/event.

### Scene-state file

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/scene-state.json`

### Checkpoint file

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/checkpoint.json`

### Ping history log

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/pings.jsonl`

This prevents repeated nudges about the same issue.

## Scene-state schema (first draft)

A practical first-pass scene-state object could contain:

- `scene_id`
- `started_at`
- `last_updated_at`
- `active_channel`
- `active_thread`
- `active_speakers`
- `scene_label`
- `current_topic`
- `current_plan`
- `current_goal`
- `open_questions`
- `risks`
- `matrix_hooks`
- `cindy_relevance_score`
- `gm_ping_warranted`
- `gm_ping_reason`
- `recent_evidence`
- `last_ping_at`
- `last_ping_topic`

### Notes on the most important fields

#### `current_plan`

Short description of what the crew currently seems committed to.

#### `open_questions`

Unresolved points the table is still circling.

#### `matrix_hooks`

Anything Cindy should naturally notice, such as:

- matrix intrusion options
- host/security angles
- surveillance exposure
- comms/trace risk
- data acquisition opportunities

#### `cindy_relevance_score`

Simple coarse scale, for example:

- `0` = irrelevant
- `1` = maybe relevant
- `2` = clearly relevant
- `3` = Cindy should probably speak up soon

#### `gm_ping_warranted`

Boolean field that says whether the current state justifies a direct GM nudge.

## Heuristic trigger layer

Before invoking a local LLM, run cheap tests over the new transcript delta.

Good first triggers:

- Cindy mentioned by name
- matrix / decking / host / trace / comms language appears
- strong planning language appears:
  - “plan”
  - “next step”
  - “what do we do”
  - “option”
- table confusion / contradiction appears
- players stall on a decision
- a scene pivot or mission-shift occurs
- someone asks for technical support, intel, or system access

If none of those triggers fire, Cindy can usually skip summarization entirely for that cycle.

## Local LLM summarization prompt shape

When the heuristic layer decides a local model should look, the prompt should stay narrow and structured.

Example questions:

- what changed in the last transcript delta?
- what is the current plan now?
- what unresolved question matters most?
- is Cindy relevant to this moment?
- should Cindy ping the GM now, later, or not at all?
- if yes, what is the one-sentence reason?

Output should be structured JSON, not freeform prose.

## GM ping policy

Cindy should not ping constantly.

A ping should happen only when one of these is true:

- Cindy was directly invoked and the table moved on without resolution
- a major planning beat depends on matrix/legwork Cindy is suited for
- the table is stuck and Cindy could unblock it
- a contradiction or blind spot emerged that Cindy would naturally catch
- a major scene pivot happened and Cindy now has a strong tactical opening

## Ping style

Pings should feel like a player leaning toward the GM, not a monitoring daemon dumping logs.

Good characteristics:

- short
- one point only
- optionally in Cindy's voice
- framed as an observation or opening, not a lecture

Examples:

- “GM, Cindy would absolutely flag a trace risk here.”
- “GM, this feels like a place where Cindy should ask to take a matrix angle.”
- “GM, the crew just committed to a plan that depends on host access.”

## Local vs main-model boundary

### Keep local

- transcript ingestion
- delta parsing
- heuristic trigger checks
- scene-state updates
- first-pass intervention scoring

### Escalate to main Cindy session only when needed

- final wording of a meaningful GM ping
- nuanced in-character tactical synthesis
- longer scene interpretation when a major beat changes

This keeps the expensive / richer reasoning step rare.

## MVP implementation plan

### Phase 1: logging + checkpointing

- persist transcript events to JSONL
- maintain a last-processed checkpoint

### Phase 2: scene-state updater

- add a local summarizer loop every 60 seconds
- output structured scene-state JSON

### Phase 3: ping trigger layer

- add heuristic checks
- add `gm_ping_warranted`
- prevent duplicate pings for the same reason

### Phase 4: Discord GM ping path

- post concise pings to the GM thread when warranted
- keep ping logging separate from raw transcript logging

### Phase 5: tuning

- refine trigger thresholds
- refine scene-state schema
- calibrate when Cindy should stay quiet vs intervene

## Why this is token-efficient

This design stays efficient because it avoids the worst possible pattern: repeatedly re-reading the full session transcript with a large model.

Instead it does:

- append-only local logs
- delta-only processing
- heuristics before LLM
- local LLM before main-model escalation
- structured state instead of repeated long prose summaries

## Rebuild requirements

A new implementation would need:

- a source of live transcript events
- a durable transcript log
- a checkpoint mechanism
- a local summarization loop
- a scene-state schema
- a GM ping rule set
- a Discord send path for nudges

## Related pages

- [Cindy Lou Tooling and Discord Notes](Cindy-Lou-Tooling-and-Discord.md)
- [Cindy Lou Wiki and Tooling Topology](Cindy-Lou-Wiki-and-Tooling-Topology.md)
- [Cindy Lou Soundboard and Voice Bridge](Cindy-Lou-Soundboard-and-Voice-Bridge.md)
