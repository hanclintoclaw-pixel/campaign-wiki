---
title: Cindy Lou Live Session Monitoring Design
type: tech-note
visibility: player-safe
status: draft
updated: 2026-05-15
tags: [cindy, discord, voice, monitoring, design]
---

# Cindy Lou Live Session Monitoring Design

## Version notes - 2026-05-15 live monitor rollout draft

This document now reflects the new live-monitor architecture drafted for deployment and partially wired into the active Discord voice bridge runtime.

### Runtime implementation target

Active runtime code path:

- `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py`

### Version-control / deployment notes

- Wiki design draft expanded and pushed through these repo commits:
  - `92cb5fe` - refine live-session ping rules
  - `cabbe18` - add layered scratch-pad design for state drift
  - `c6f4855` - draft mature live scene-analysis rollout plan
- Live runtime code was updated in-place in `voice_chat.py` on `2026-05-15`.
- Safety backup created before live edit:
  - `/Users/hanclaw/claw/projects/discord_voice_patch/voice_chat.py.bak.20260515-101444`

### New features in this version

- added `recent-delta.json` as a short-horizon noisy analysis buffer
- added `scene-scratchpad.json` as a persistent stable scene-memory layer
- added explicit mode classification:
  - `in_game`
  - `mixed`
  - `table_talk`
- added a transition gate so casual chatter does not automatically rewrite stable scene state
- added mention-only suppression so Cindy name mention by itself does **not** trigger a GM ping
- added richer ping reasoning with reason classes and a `silent / draft_ready / ping_now` ladder
- expanded ping audit details so later review can show why a ping fired

### Behavior change summary

Old behavior leaned too hard on the newest transcript window.
That meant direct name mentions and casual drift could distort state or produce low-value ping pressure.

New behavior separates:

- what the scene still is (`scene-scratchpad.json`)
- what just changed (`recent-delta.json`)
- whether recent talk is allowed to rewrite stable state (mode classifier + transition gate)

That is the core change for reducing state drift and table-talk corruption.

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

## State-drift and table-talk mitigation

A single rolling summary is too fragile.
If casual banter arrives after a meaningful tactical scene, a naive updater can overwrite good state with junk.

A better design is a **layered rolling scene model** with a persistent scratch pad:

### Layer 1: stable scene scratch pad

Keep a durable file that preserves the last strongly-supported in-game state.
This should only change when the system has positive evidence that the scene has materially advanced.

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/scene-scratchpad.json`

Suggested contents:

- current in-game scene label
- current location / site
- current objective
- current plan
- known threats
- open tactical questions
- matrix hooks
- active NPC / system actors
- evidence supporting the current scene frame
- confidence score for each field
- `last_in_game_update_at`

This file is the anchor. Casual chatter should not overwrite it unless the model is confident the table has actually pivoted.

### Layer 2: volatile recent-delta buffer

Keep a short-horizon buffer of the last N meaningful transcript events or last few minutes of speech.
This layer is allowed to be noisy.
Its job is to capture what is happening **right now** without destroying the stable state.

Example path:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/recent-delta.json`

Suggested contents:

- recent transcript snippets
- speakers active in the last window
- candidate new plan language
- candidate confusion/stall markers
- candidate scene-pivot markers
- candidate Cindy-relevance markers
- estimated mode: `in_game`, `mixed`, or `table_talk`

### Layer 3: table-talk / banter detector

Instead of treating table-talk as a bad summary, treat it as a separate mode classification.
The system should explicitly ask:

- is this in-character or tactical play?
- is this logistics / jokes / device talk / side chatter?
- is this a transition between the two?

If the answer is `table_talk`, the updater should usually:

- preserve the stable scratch pad unchanged
- update only the recent-delta buffer
- lower urgency for new pings
- avoid resetting current plan/current goal

### Layer 4: scene transition gate

The stable scratch pad should only update when a transition gate is met.
For example, require two or more of:

- a new goal is stated clearly
- the party physically changes location / target
- initiative / combat begins or ends
- a new system/NPC/host starts directly interacting with the crew
- the table converges on a new plan
- multiple recent lines reinforce the same pivot

This prevents one stray line of banter from redefining the whole scene.

### Layer 5: field-level overwrite rules

Not every field should update equally fast.

Example policy:

- `current_plan`: medium stickiness
- `current_goal`: high stickiness
- `location`: very high stickiness
- `open_questions`: medium stickiness
- `matrix_hooks`: additive rather than replace-on-write
- `active_speakers`: fast-changing
- `scene_label`: only update on transition gate

That lets the system absorb chatter without losing the mission spine.

### Layer 6: confidence + decay

Every important field should have:

- confidence
- last-supported timestamp
- last-evidence snippet ids

If no new in-game support arrives for a while, confidence may decay slowly, but the field should not instantly collapse into `table-talk`.

### Layer 7: ping decision reads from both layers

A GM ping decision should not read only the last few lines.
It should combine:

- the stable scratch pad (what scene are we actually in?)
- the recent-delta buffer (what just happened?)
- the mode classifier (`in_game`, `mixed`, `table_talk`)

That means a Cindy mention during table-talk does almost nothing, while the same mention during an unresolved matrix-planning beat carries real weight.

### Practical rule of thumb

Think of the system as:

- **scratch pad = what the scene still is**
- **recent delta = what just changed**
- **mode classifier = whether the new speech deserves to rewrite the scratch pad**

That separation is probably the cleanest fix for state drift.

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
- Cindy is mentioned by name **and** another scene-state indicator suggests she has a concrete opening

A direct name mention by itself should **not** create a GM ping. At most, it should raise Cindy's relevance score or queue a closer scene-state check.

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

- a major planning beat depends on matrix/legwork Cindy is suited for
- the table is stuck and Cindy could unblock it
- a contradiction or blind spot emerged that Cindy would naturally catch
- a major scene pivot happened and Cindy now has a strong tactical opening
- Cindy was mentioned by name **and** the scene state independently shows unresolved relevance

Direct invocation alone is insufficient. The system should behave as though Cindy is already passively aware of the session; mention only matters if it coincides with a real reason to intervene.

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

## Mature implementation plan (draft)

This is a more production-shaped plan aimed at eventual live deployment, not just experimentation.

### Operational goal

Maintain a trustworthy rolling understanding of session state during live play while keeping Cindy quiet by default and useful when she does speak.

### Success conditions

A good live system should:

- preserve important in-game state across temporary table-talk drift
- detect real scene pivots quickly
- avoid duplicate or low-value GM nudges
- produce pings only when Cindy has a concrete reason to matter
- make it possible to inspect later **why** a ping fired or did not fire

### Core runtime components

#### 1. Transcript log

Append-only JSONL of normalized utterances.

Responsibilities:

- durable raw record
- source for replay/debugging
- event ids for checkpointing

#### 2. Checkpoint manager

Tracks the last processed event and the last successful stable-state update.

Responsibilities:

- delta-only processing
- resumability after crash/restart
- separation between transcript ingestion and scene analysis

#### 3. Recent-delta analyzer

Consumes only new transcript lines since the last checkpoint.

Responsibilities:

- extract candidate plan language
- detect confusion/stall markers
- detect scene-pivot markers
- detect Cindy-relevance markers
- classify recent mode: `in_game`, `mixed`, `table_talk`

This can start heuristic-heavy and become model-assisted later.

#### 4. Stable scratch-pad manager

Owns the persistent in-game scene spine.

Responsibilities:

- preserve current objective, plan, location, threats, hooks
- require evidence before rewriting stable state
- track confidence + supporting evidence
- prevent casual chatter from wiping important state

#### 5. Transition gate

Decides whether recent evidence is strong enough to modify the stable scratch pad.

Suggested gate inputs:

- new location/target established
- initiative/combat start or end
- explicit plan commitment
- newly interactive NPC/host/system
- repeated reinforcement across several utterances
- strong contradiction with previous state

#### 6. Ping decision layer

Reads the stable scratch pad and recent-delta buffer together.

Responsibilities:

- decide between `silent`, `draft_ready`, and `ping_now`
- require nontrivial evidence for a visible GM ping
- apply cooldown and de-duplication
- ensure name mention alone never fires a ping

#### 7. Ping composer

Builds the actual GM-facing nudge only after the ping decision layer approves it.

Responsibilities:

- produce short reasoned message
- optionally draft Cindy line / voice payload
- record why that wording was chosen

### Recommended state files

#### `transcript.jsonl`

Raw utterances.

#### `checkpoint.json`

Operational pointers.

Suggested fields:

- `last_event_id`
- `last_analyzed_at`
- `last_stable_update_at`
- `last_ping_at`
- `last_ping_reason`

#### `recent-delta.json`

Short-lived current-window analysis.

Suggested fields:

- recent utterance ids
- recent speakers
- mode classification
- candidate scene-pivot markers
- candidate plan markers
- candidate confusion markers
- candidate Cindy-relevance markers
- window confidence

#### `scene-scratchpad.json`

Stable in-game scene memory.

Suggested fields:

- `scene_id`
- `scene_label`
- `location`
- `current_goal`
- `current_plan`
- `known_threats`
- `open_questions`
- `matrix_hooks`
- `active_entities`
- `supporting_evidence`
- `field_confidence`
- `last_in_game_update_at`

#### `pings.jsonl`

Audit trail for outward nudges.

Suggested fields:

- timestamp
- scene id
- reason class
- evidence ids
- visible message
- Cindy draft line if any
- delivery result

### Update cadence

Suggested default cycle:

- transcript ingestion: continuous / append-only
- recent-delta analysis: every 20-60 seconds depending on activity
- stable scratch-pad update: only when transition gate passes
- ping evaluation: after each recent-delta analysis pass

The important point is that not every cycle should rewrite stable scene state.

### Decision ladder

Use a three-step decision ladder instead of boolean yes/no.

#### `silent`

No meaningful Cindy action.
Update logs, keep watching.

#### `draft_ready`

Cindy probably has an angle, but the situation does not yet justify interrupting the GM.
Store a candidate reason/line without sending it.

#### `ping_now`

There is a concrete, evidence-backed reason to interrupt.
Send a concise GM ping.

This is probably the single best structural change for reducing false positives.

### Field overwrite policy

Suggested defaults:

- `location`: very sticky
- `scene_label`: sticky
- `current_goal`: sticky
- `current_plan`: medium stickiness
- `open_questions`: additive/replace by confidence
- `matrix_hooks`: additive
- `active_entities`: additive with aging
- `active_speakers`: fast-changing
- `recent_evidence`: rotating window

### Mode-classification policy

The mode classifier should explicitly separate:

- `in_game`
- `mixed`
- `table_talk`
- `post_session_debrief`

Suggested behavior:

- `in_game`: full analysis allowed
- `mixed`: update recent-delta; stable scratch pad only on strong evidence
- `table_talk`: do not rewrite stable scratch pad
- `post_session_debrief`: preserve the final in-game scene and start a separate debrief summary track

### Ping policy (mature form)

Visible GM ping requires all of:

- Cindy relevance is genuinely high
- the scene is `in_game` or strongly `mixed`
- a concrete reason class exists
- no recent duplicate ping on the same reason class
- the message is more specific than "Cindy may have a useful opening"

Suggested reason classes:

- `matrix_plan_dependency`
- `technical_stall`
- `blind_spot`
- `host_or_security_opening`
- `explicit_cindy_relevance`
- `scene_pivot_into_cindy_lane`

### Anti-spam controls

Recommended controls:

- cooldown per reason class
- cooldown per scene id
- require stronger evidence for repeated pings in the same scene
- suppress mention-only triggers entirely
- suppress low-specificity messages

### Observability and review

To tune this sanely, every cycle should leave enough evidence to inspect later.

Recommended logging:

- why mode was classified the way it was
- whether the transition gate passed or failed
- what fields were updated and why
- why a ping was suppressed
- why a ping was emitted

That turns tuning from vibes into evidence.

### Staged rollout plan

#### Phase 0: audit mode

- no visible pings
- produce transcript, recent-delta, scratch-pad, and candidate ping logs only
- compare candidate pings against human judgment after sessions

#### Phase 1: draft-only mode

- still no autonomous visible pings
- produce `draft_ready` outputs in the GM thread or an internal log for review
- tune reason classes, transition gates, and cooldowns

#### Phase 2: conservative live mode

- allow autonomous visible GM pings only for strongest reason classes
- long cooldowns
- no mention-only behavior
- require concrete message specificity

#### Phase 3: broadened live mode

- allow more reason classes after false-positive rate drops
- keep audit trail and post-session review loop

### Go-live checklist

Before turning this on live, confirm:

- stable scratch pad survives table-talk without corruption
- scene transitions are detected reliably across at least several sessions
- mention-only pings are fully suppressed
- duplicate pings in one scene are rare
- every visible ping has a reviewable evidence trail
- final session state remains usable even after post-session chatter

### Practical implementation order

1. Add `recent-delta.json`
2. Add `scene-scratchpad.json`
3. Add mode classifier
4. Add transition gate
5. Add `silent / draft_ready / ping_now`
6. Add reason classes + anti-spam logic
7. Run audit mode on several sessions
8. Tune using post-session miss review
9. Enable conservative live mode

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
