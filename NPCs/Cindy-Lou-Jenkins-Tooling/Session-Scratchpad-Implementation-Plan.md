---
title: Cindy Lou Session Scratchpad Implementation Plan
type: tech-note
visibility: player-safe
status: active
updated: 2026-05-22
tags: [cindy, discord, voice, monitoring, scratchpad, implementation-plan]
---

# Cindy Lou Session Scratchpad Implementation Plan

## Goal

Build a **session-scoped scratchpad** that gives Cindy enough current context to:

- generate relevant in-character replies
- produce fresher and more situational GM nudges
- track changing scene state over the course of a live session
- forget stale material when the table has clearly moved on

The scratchpad should be a **working memory for one live session**, not a semi-permanent dump of whatever happened to be important yesterday.

## Current implementation status

As of **2026-05-22**, the first implementation pass of this design has been started in the live voice bridge runtime.

Implemented now:

- scratchpad resets on `session-start`
- a session id is created for each live session
- active working files remain under the live-session runtime root
- finished session files are archived under `sessions/<session_id>/`
- a new `event-ledger.jsonl` file is created for each session
- transcript-derived ledger events are now written alongside the raw transcript
- active participants (`active_pcs`, `active_npcs`) are now tracked in scratchpad/state
- `recent_entities`, `direct_requests_to_cindy`, and `cindy_hooks` are now populated
- `prompt-view.json` is now emitted as a reply/ping-facing projection
- `field_last_reinforced_at` groundwork is now present in the scratchpad state
- the old cross-session scratchpad contamination path is cut off at session start

Not implemented yet:

- stronger event typing beyond the current heuristic first pass
- more aggressive scene-transition-driven rebuilds outside the timed loop
- fuller decay/confidence aging logic across all fields
- richer entity bucket handling (`active_now` / `recent` / `background`)
- a fully mature pre-ping short-horizon guard pass

So this page is now partly a plan and partly a record of the staged rollout.

## Core problem with the current version

The current scratchpad is failing in three main ways:

1. **it is too sticky across sessions**
   - old matrix/warehouse context can bleed into a later session

2. **it is too shallow**
   - it does not capture enough structured detail about the evolving table state

3. **it is too slow and too blunt**
   - it updates on a timer, but not with enough scene-awareness or transition logic

The result is a scratchpad that can preserve some useful facts, but often does not reflect the actual current table moment well enough to drive sharp Cindy behavior.

## Design principle

The scratchpad should not try to be the raw transcript.

It should be a **derived, structured current-state model** built from transcript events.

That means the design should separate:

- **raw input**
- **recent interpreted events**
- **stable current scene state**
- **reply/ping-specific prompt context**

## Recommended architecture

Use a **3-layer session memory model**.

### Layer 1 — Event Ledger

This is a rolling structured log of transcript-derived events.

Every important beat from the transcript becomes a small event object.

Examples:

- a player asks a direct question
- a plan is proposed
- an NPC becomes the focus
- the table shifts from in-world scene to tooling/table-talk
- someone directly solicits Cindy’s opinion
- a matrix/security angle appears
- a scene objective changes

This layer is **append-only for the session**.

### Layer 2 — Scene Scratchpad

This is the higher-level working state built from the event ledger.

It should answer:

- what scene are we in right now?
- who is relevant right now?
- what is the current objective?
- what is the current plan?
- what just changed?
- what remains unresolved?
- what does Cindy care about?

This is the actual scratchpad Cindy uses as session memory.

### Layer 3 — Prompt View

This is a trimmed context projection for:

- Cindy voice-line generation
- proactive GM ping generation
- direct-response drafting

The prompt view should be derived from the scratchpad plus a short recent lookback.

It should be optimized for **relevance**, not completeness.

## Session lifecycle rules

### Session start

On every `session-start`:

- create a **fresh empty scratchpad**
- create a **fresh empty event ledger**
- create a fresh prompt-state file if needed
- archive the previous session’s final state under a session-specific filename

This is mandatory.

No scratchpad from a prior session should ever be reused as the starting point for a new one.

### Session end

On `session-end`:

- persist the final scratchpad
- persist final event ledger metadata
- write a compact end-of-session summary if useful
- mark the files with the session id and end timestamp

That allows later review without contaminating the next session.

## Recommended files

Under the live-session runtime directory, create a session-specific subdirectory:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/sessions/<session_id>/`

Recommended files inside it:

- `transcript.jsonl`
- `event-ledger.jsonl`
- `scene-scratchpad.json`
- `prompt-view.json`
- `checkpoint.json`
- `pings.jsonl`
- `voice-lines.jsonl`

And maintain a thin pointer file for the current active session:

- `/Volumes/carbonite/claw/data/cindylou/runtime/live-session/current-session.json`

That lets the runtime keep the current path obvious without flattening all history into one directory.

## Event ledger schema

Each event should be small, typed, and timestamped.

Suggested shape:

```json
{
  "event_id": 1779460000000000000,
  "timestamp": "2026-05-22T19:14:33",
  "speaker": "Curtis(Lee)",
  "source": "voice",
  "kind": "plan_proposal",
  "mode_hint": "in_game",
  "entities": ["Curtis", "SCMusic"],
  "directed_to_cindy": false,
  "cindy_relevance": 1,
  "text": "We should put the page under Curtis and sketch the habitat there.",
  "scene_effect": {
    "scene_shift": false,
    "goal_update": true,
    "entity_focus_change": true
  }
}
```

## Event kinds

Recommended starting set:

- `plan_proposal`
- `plan_revision`
- `question`
- `answer`
- `scene_transition`
- `location_reference`
- `npc_focus`
- `pc_focus`
- `matrix_hook`
- `combat_beat`
- `tooling_talk`
- `joke_or_banter`
- `direct_cindy_request`
- `gm_prompt`
- `problem_or_blocker`
- `decision`
- `reveal`

These do not need to be perfect at first. They need to be good enough to let the scratchpad reason about current state.

## Scene scratchpad schema

Recommended top-level fields:

```json
{
  "session_id": "2026-05-22T19-00-shadowrun",
  "scene_id": "planning-dolphin-habitat",
  "scene_label": "planning",
  "scene_started_at": "2026-05-22T19:10:00",
  "last_scene_update_at": "2026-05-22T19:14:33",
  "location": "discussion / planning around Curtis wiki page",
  "active_pcs": ["Curtis", "Valgaut"],
  "active_npcs": ["Cindy Lou"],
  "recent_entities": ["SCMusic", "dolphin habitat"],
  "current_objective": "decide how to represent the dolphin habitat idea",
  "current_plan": "sketch the idea under Curtis's wiki page",
  "recent_reveals": [],
  "open_questions": [],
  "blockers": [],
  "risks": [],
  "cindy_hooks": [],
  "direct_requests_to_cindy": [],
  "field_confidence": {},
  "field_last_reinforced_at": {},
  "supporting_evidence": []
}
```

## Required scratchpad fields

At minimum, the scratchpad should maintain:

- `session_id`
- `scene_id`
- `scene_label`
- `scene_started_at`
- `last_scene_update_at`
- `location`
- `active_pcs`
- `active_npcs`
- `recent_entities`
- `current_objective`
- `current_plan`
- `open_questions`
- `blockers`
- `risks`
- `recent_reveals`
- `direct_requests_to_cindy`
- `cindy_hooks`
- `supporting_evidence`
- `field_confidence`
- `field_last_reinforced_at`

## Entity model

A major improvement should be separating entities into three buckets:

### Active now

People/things currently central to the scene.

### Recently referenced

Things still nearby in the conversation but not necessarily central.

### Background continuity

Things the session still knows about, but that should not dominate current behavior.

This avoids the current problem where an old matrix thread continues to feel “active” just because it was once important.

## Update cadence

### Continuous ingest

As transcript chunks arrive:

- append normalized events into the event ledger
- update only very light counters immediately

### Regular scratchpad rebuild

Every **15–30 seconds**:

- rebuild the scratchpad from the last **3–5 minutes** of event ledger
- merge with still-valid current state
- decay fields that have not been reinforced
- update prompt-view state

### Immediate transition rebuilds

Do not wait for the timer when a strong transition is detected.

Force an immediate rebuild when:

- location clearly changes
- combat starts or ends
- matrix becomes the central focus
- a new plan becomes dominant
- someone directly requests Cindy’s input
- the talk shifts sharply between in-world and tooling/table-talk

## Transition logic

A scene transition should not be guessed from a single token.

Use weighted triggers such as:

- new dominant entities
- a different objective/plan pattern
- a different interaction mode
- sustained new evidence over multiple events

Recommended output:

- `scene_shift_detected: true/false`
- `scene_shift_reason`
- `scene_confidence`

## Recency and decay

This is the main fix for stale contamination.

Every field that can persist should carry:

- `last_reinforced_at`
- `confidence`
- optional `ttl` or decay behavior

### Suggested decay rules

- if a field is not reinforced for several minutes, lower confidence
- if confidence drops below threshold, remove it from “active” state
- keep it in the archived session record if needed, but not in current prompt view

Example:

- an old matrix hook may remain in the ledger
- but if nothing recent reinforces it, it should leave the active scratchpad

## Prompt-view design

The prompt view should be purpose-built for live behavior.

Suggested sections:

- current scene in one sentence
- who is active right now
- what the group is trying to do
- what changed in the last 60–90 seconds
- direct asks to Cindy
- best current Cindy hook
- recent evidence snippets
- recommended Cindy tone/mode

This should feed both:

- direct Cindy replies
- proactive GM ping drafting

## GM ping generation rule

Before sending a proactive GM ping:

1. inspect the current prompt view
2. do a fresh **60–90 second short-horizon lookback**
3. confirm that the immediate recent context still supports the ping
4. only then send it

That final short pass should sharply reduce stale or mistimed pings.

## Cindy reply generation rule

When Cindy is directly engaged:

- use the current prompt view
- include active entities and objective
- include recent changes and direct asks
- choose Cindy’s voice mode from the current scene posture

That should make replies sound more like they belong to the present table moment.

## Best suggested solution in one sentence

The best solution is:

> **a session-resetting event ledger feeding a decaying scene scratchpad, which then produces a compact prompt view for Cindy replies and GM pings.**

That is the right balance between continuity and freshness.

## Implementation phases

### Phase 1 — reset + structure

Ship first:

- fresh scratchpad at every session start
- session-specific directories
- event ledger file
- new scratchpad schema
- archive old session state instead of reusing it

This fixes the worst contamination bug immediately.

### Phase 2 — better updates

Add:

- typed event extraction
- 15–30 second rebuild loop
- transition-triggered rebuilds
- entity buckets
- field confidence + last reinforced timestamps

This makes the scratchpad actually responsive.

### Phase 3 — better prompting

Add:

- explicit prompt-view file
- short pre-ping lookback guard
- direct-request prioritization
- better Cindy hook scoring
- richer voice-mode selection

This makes the outputs feel current and sharp.

### Phase 4 — validation harness

Add replay and inspection tools that let us test:

- scene transition behavior
- entity churn
- stale decay
- prompt-view quality
- GM ping timing
- Cindy reply freshness

## Testing plan

### Test 1 — clean session reset

- end one session
- start another
- confirm scratchpad starts empty
- confirm old hooks do not bleed forward

### Test 2 — scene change recognition

- begin in one planning topic
- switch to a different topic
- confirm scene id/label changes appropriately

### Test 3 — entity churn

- introduce an NPC or object briefly
- shift away from it
- confirm it moves from active to recent to dropped state over time

### Test 4 — direct Cindy request in table-talk

- table is in a tooling/meta mode
- directly ask Cindy for input
- confirm prompt view still treats it as a direct invitation

### Test 5 — stale matrix residue removal

- create a strong matrix beat
- let the conversation move elsewhere
- confirm the hook decays out of active scratchpad if not reinforced

### Test 6 — proactive ping quality

- simulate high-relevance cues
- confirm the final short lookback still supports the ping
- confirm the ping reflects current, not stale, table context

## Recommended next implementation target

If this gets built soon, the best order is:

1. **reset scratchpad on session-start**
2. **move to session-scoped storage**
3. **add event-ledger layer**
4. **rebuild scratchpad from recent events instead of mutating one sticky object forever**
5. **add field decay and prompt-view projection**

That sequence gives the highest value fastest.

## Related pages

- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou External Transcription Watchdog Plan](External-Transcription-Watchdog-Plan.md)
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
