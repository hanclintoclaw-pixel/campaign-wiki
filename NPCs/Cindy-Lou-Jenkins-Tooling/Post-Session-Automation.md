---
title: Cindy Lou Post-Session Automation
type: tech-note
visibility: player-safe
status: brainstorm
updated: 2026-05-15
tags: [cindy, automation, sessions, wiki, memory, design]
---

# Cindy Lou Post-Session Automation

## What this page is

This page sketches a higher-level idea for what should happen **automatically when a live session ends**.

The goal is to move Cindy beyond being only a live-session participant and toward being a reliable **post-session operations layer** for the campaign.

This is still brainstorming. It describes the shape of the system we want, not a finished implementation.

## Big idea

When a session is closed, Cindy should be able to detect that the session is a **real live game session**, then automatically run a follow-up workflow that handles both:

- **campaign housekeeping**
- **Cindy Lou Jenkins A-NPC follow-through**

The ideal version requires **no direct user prompting after the session ends**.

## Why this matters

Right now, some of the most valuable work happens *after* the game:

- turning rough notes into a proper session record
- preserving clues, NPCs, and unresolved questions
- updating Cindy’s own memory and continuity
- turning transient play into durable campaign knowledge

That work is easy to postpone, fragment, or forget if it depends on manual follow-up every time.

A post-session automation pass would make the campaign feel more alive and more continuous.

## Desired trigger

The system should wake up when a session is clearly over.

Possible trigger signals:

- the Discord session thread is archived or marked ended
- the voice session closes cleanly
- a session-end marker is posted by the tooling
- a scheduled follow-up check notices that the live session has gone idle and then closed

The important design principle is:

> do not fire just because people stopped talking for a minute; fire when the system has strong evidence that the actual session has ended.

## First gate: confirm this was a real live session

Before doing any record-keeping, Cindy should confirm that the closed session was actually a real game session and not:

- a test thread
- setup chatter
- a tech rehearsal
- a short out-of-character planning conversation
- a false start that never became real play

This page will call that check **authentic campaign notes detection**.

### What should count as authentic campaign notes?

Possible evidence:

- sustained in-character or tactical play
- meaningful scene progression
- named locations, NPCs, clues, or action choices
- enough transcript/note density to support a proper session write-up
- evidence that the table actually played through scenes, not just tested the tool

This does **not** need to be perfect truth detection. It just needs to be strong enough that Cindy does not create junk session pages for non-sessions.

## Main outputs

If the authenticity gate passes, the automation should create or update several things.

### 1. A player-visible wiki Session page

The most obvious output is a new session page in the campaign wiki.

That page should include, in some cleaned-up form:

- session date
- in-world date if known
- attendance
- high-level summary
- major scenes
- clues gained
- decisions made
- changes to campaign state
- open threads
- source references back to the session thread / notes

The ideal experience is that a real session ends and a first-pass player-safe session record appears without anyone having to ask for it.

### 2. Cindy’s internal notes and memory

The automation should also update Cindy’s own continuity layer.

That likely includes:

- raw daily notes in the current memory log
- internal campaign memory or dossier updates
- unresolved questions that Cindy should keep watching
- notable changes in relationships, threats, plans, or active mysteries

This is not just bookkeeping. It is how Cindy remains a coherent recurring presence instead of waking up half-forgetful every time.

### 3. Entity and knowledge extraction

A finished version should probably also identify structured follow-up items such as:

- new NPCs
- new locations
- organizations
- matrix/system elements
- newly revealed clues
- unresolved entities needing later cleanup

That extracted material can feed later wiki work, campaign memory, and search/index systems.

### 4. Cindy-specific A-NPC follow-through

This is the part that makes the system feel like *Cindy*, not just a generic note bot.

After a session, Cindy may have campaign-facing follow-up worth preserving, such as:

- what Cindy learned
- what Cindy is now worried about
- what technical angles Cindy would want to investigate next
- what details Cindy would naturally remember or fixate on
- whether Cindy should surface a short in-character or quasi-in-character reflection

That reflection should be used carefully. The point is not to turn every session into fanfiction; the point is to keep Cindy’s non-player-character continuity feeling alive.

## Suggested high-level workflow

A reasonable post-session pipeline might look like this:

1. **Session closes**
2. **Trigger fires**
3. **Authenticity gate runs**
4. If not authentic, do nothing or log a quiet note
5. If authentic:
   - collect source transcript / notes
   - generate a first-pass session summary
   - create or update the wiki Session page
   - update Cindy’s internal notes
   - extract entities / open threads / follow-up tasks
   - queue anything uncertain for later review
6. Optionally produce a short audit log explaining what was updated

## Important safety / quality rules

This kind of automation only works if it is conservative.

### Player-visible pages should stay player-safe

Anything written to the public-facing wiki should be filtered for:

- spoilers that should remain hidden
- GM-only framing
- rough or misleading transcript artifacts
- private implementation details that do not belong in campaign-facing notes

### Internal notes can be richer than the public page

Cindy’s internal notes may preserve uncertainty, guesses, and follow-up questions that should not all be dumped onto the player-facing wiki.

That separation is healthy.

### The system should prefer “quietly do nothing” over creating bad records

If the session is ambiguous, the right answer may be to skip automation or leave behind a draft-only artifact for review.

## What makes this more than a session summarizer

A generic session summarizer would only write a recap.

The higher-level function envisioned here is broader:

- it detects when a session truly ended
- it decides whether the material is authentic enough to count
- it updates player-visible canon
- it updates Cindy’s private continuity
- it extracts structured campaign knowledge
- it keeps Cindy’s A-NPC identity in motion between sessions

That is closer to a **post-session operations system** than a simple note generator.

## Open design questions

This page is intentionally preliminary. Some good unresolved questions:

- What exact combination of signals should count as “session closed”?
- What evidence threshold should count as authentic campaign notes?
- Should the first wiki page be published immediately, or created as draft-first and then promoted?
- How much of Cindy’s own post-session reflection should ever be player-visible?
- Should entity extraction happen in the same workflow, or as a second pass?
- What should be logged for auditability when the automation runs on its own?

## A likely end state

The long-term vision is something like this:

> A real Shadowrun session ends, Cindy recognizes that it was real play, writes the first pass of the session record, updates her own memory, extracts important campaign facts, and leaves the campaign in a cleaner and more searchable state than it was before the session ended.

That is the higher-level function this page is sketching.

## Related pages

- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
- [Cindy Lou Wiki and Tooling Topology](Wiki-and-Tooling-Topology.md)
