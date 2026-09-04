---
title: Cindy Lou Post-Session Automation
type: tech-note
visibility: player-safe
status: brainstorm
updated: 2026-08-23
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

The near-term version should still include one deliberate GM confirmation step: preserve the transcript quickly, then ask the GM to approve the canon ingest and answer any date / current-state questions before the public wiki is treated as settled.

For the future locally hosted build, this should be treated as a **campaign maintenance harness** around local model reasoning, not as a free-form chat response. Local Qwen or a successor local model can read and classify messy transcript material, but deterministic code should own source collection, date discipline, ledger checks, link updates, status transitions, and acceptance gates.

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

### 1a. Current Situation, Current State, and chronology maintenance

The session page is not enough by itself. Every session ingest should also decide whether the front-page **Current Situation**, the campaign's **Current State**, and **Session Chronology** need to move.

The workflow should explicitly check:

- the starting in-world date and time
- the ending in-world date and time
- whether any downtime, stakeout, travel, healing, shopping, legwork, or project work advanced the clock
- whether the latest active scene is now a new canonical date
- whether the session is a backdated interlude that should not move the main current-state clock
- whether the front page needs a new concise Current Situation paragraph
- whether the fuller Current State focus, recent runs, in-world date, immediate leads, and open questions need changes
- whether new immediate leads replaced, resolved, or reprioritized the old Current State leads
- whether newly introduced clues should become open questions, active hooks, or closed threads

If the date or current-state movement cannot be inferred cleanly from the transcript, Cindy should not silently leave it loose. She should ask a compact clarification before marking the ingest complete.

### 2. Cindy’s internal notes and memory

The automation should also update Cindy’s own continuity layer.

That likely includes:

- raw daily notes in the current memory log
- internal campaign memory or dossier updates
- unresolved questions that Cindy should keep watching
- notable changes in relationships, threats, plans, or active mysteries

This is not just bookkeeping. It is how Cindy remains a coherent recurring presence instead of waking up half-forgetful every time.

### 3. Entity, lead, and knowledge extraction

A finished version should probably also identify structured follow-up items such as:

- new NPCs
- new locations
- organizations
- matrix/system elements
- newly revealed clues
- unresolved entities needing later cleanup
- unresolved leads or high-value unanswered questions that should remain visible as possible player actions

That extracted material can feed later wiki work, campaign memory, search/index systems, and a rebuilt clue registry or lead board.

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
   - draft a short front-page Current Situation paragraph
   - draft fuller Current State updates for focus, recent runs, dates, immediate leads, and open questions
   - run a chronology/current-state checkpoint
   - update Cindy’s internal notes
   - extract entities / open threads / follow-up tasks
   - queue anything uncertain for later review
6. Ask the GM to approve the canon ingest if the session materially changed the campaign state
7. After approval, publish the wiki updates and produce a short audit log explaining what was updated

## Proposed GM confirmation loop

The practical solution is a **two-stage closeout**.

### Stage 1: immediate transcript preservation

As soon as a session ends, Cindy should save or index the raw transcript and any live scratchpad notes. This can happen without waiting on the GM because it is preservation, not canon publication.

Output should be quiet unless something failed.

### Stage 2: 12-hour canon-ingest prompt

Roughly **12 hours after the session ends**, Cindy should post a short prompt in the session channel asking whether to run the canon ingest.

Suggested prompt shape:

> Session transcript is preserved. Approve canon ingest for the wiki? I have three continuity checks before publish: current in-world date/time, whether this advances Current State, and any GM-only details to keep out of player-safe pages.

The delay gives the GM time to sleep on the session while keeping the record fresh. The prompt should be tied to the session thread/channel so the context is obvious.

### Stage 3: pushback when ingest is manually requested

If the GM manually asks Cindy to ingest a session, Cindy should run a fast preflight before writing public pages. If any of the following are unclear, Cindy should ask before final publish:

- **Date / time:** What in-world date and approximate time did the session end on?
- **Clock movement:** Did downtime, travel, stakeout, healing, shopping, legwork, or project work advance the day?
- **Current State:** Is this now the latest active campaign moment, or a backdated / side interlude?
- **Public safety:** Are any transcript details GM-only even if players heard some adjacent table talk?
- **Rewards and ledgers:** Were nuyen, Karma, gear, damage, favors, contacts, heat, or reputation changes final?
- **Open hooks:** Which unresolved leads should be listed as immediate next actions rather than background mysteries?

The pushback should be short and concrete, not a questionnaire dump. If only one or two items are uncertain, ask only those.

## Deterministic handling for "summarize last night's session"

When the GM asks Cindy to "summarize last night's session" or equivalent, the local-hosted build should treat that as a specific workflow, not an ordinary open-ended summarization prompt.

### Request resolver

1. Determine the intended session source before writing canon:
   - prefer the most recent closed live-session transcript if it ended within the last 24 hours;
   - otherwise use the most recent session thread with strong authentic-session signals;
   - if multiple sessions qualify, ask which one instead of guessing.
2. Resolve the output target:
   - brief chat recap only;
   - player-visible wiki Session page;
   - full post-session closeout with Current State, chronology, character state, and lead-board checks.
3. Apply the authentic campaign notes gate before making public wiki changes. Tech tests, planning-only chatter, and short debriefs should not create session pages.

### Evidence packet

Before asking a model to summarize, deterministic code should gather a compact packet:

- transcript/thread id and time span;
- attendance if available;
- candidate played date and in-world date/time;
- scene breaks or speaker/time clusters;
- explicit GM reward/closeout posts;
- extracted named NPCs, locations, factions, vehicles, Matrix hosts, clues, and player decisions;
- candidate state changes: nuyen, Karma, gear, damage, heat, favors, contacts, projects, vehicles/drones, and ongoing conditions;
- existing pages that may need updates.

### Model role

Local Qwen should be used for interpretation and drafting:

- scene summary;
- notable decisions;
- player-safe wording;
- candidate open threads;
- ambiguity detection.

It should not be the accountant of record. Deterministic code should verify date status, links, ledgers, required fields, duplicate page creation, and whether public output is allowed.

### Required output classes

The workflow should produce one of these explicit outcomes:

- **chat recap only:** answer in Discord, no wiki mutation;
- **draft session page:** create a provisional page or patch for GM review;
- **publish-ready ingest:** session page plus required Current Situation, Current State, chronology, lead-board, and related-page updates are coherent;
- **needs GM clarification:** ask concrete questions before publishing;
- **no real session found:** explain that no authentic session source was found.

The pushback should be narrow. If the only uncertainty is in-world date, ask only that. If rewards or equipment are unclear, ask those questions in concrete accounting language.

## Lead board / unpulled-thread maintenance

If the old Clue Registry is rebuilt, the better target is a **player-safe Lead Board** backed by an optional GM-facing thread ledger. The local-hosted post-session harness should maintain it as part of closeout.

### Purpose

The player-facing board should answer: "What could the crew still follow up on?" The GM-facing ledger should answer: "What unresolved pressure points are still available to pay off?"

### Candidate entry schema

Each lead/thread should have:

- short hook name;
- status: open, active, dormant, resolved, false lead, superseded, GM-only;
- first seen and last touched session;
- why it matters in one or two sentences;
- player-known facts only;
- concrete player-facing questions;
- suggested next actions;
- connected NPCs, factions, locations, sessions, artifacts, and Matrix systems;
- confidence / spoiler-safety flag;
- optional private GM notes or payoff ideas kept out of player-safe pages.

### Post-session maintenance pass

After each authentic session, deterministic code plus model assistance should classify leads into:

- **new:** a new clue, mystery, lead, or unanswered question appeared;
- **touched:** the session added evidence or changed priority;
- **resolved:** the crew answered it, closed it, or made it irrelevant;
- **dormant:** still valid but not an immediate next action;
- **superseded:** replaced by a clearer question or newer lead;
- **do not publish:** too spoiler-heavy, speculative, or GM-only.

A session ingest is not complete until the lead board has either been updated or explicitly marked "no player-visible lead changes." This keeps the board from decaying into another stale index.

### Quality bar

Lead-board entries should be actionable, not archival. Prefer questions and next moves over vague lore labels.

Good shape:

- "Who owned the second drone tailing Jet Set Morgan?"
- "Can the anonymous satellite sponsor be caught during the next live contact?"
- "Which Late January headline threads are background color versus active campaign drivers?"

Bad shape:

- "Jet Set Morgan clue"
- "Satellite thing"
- "Investigate everything"

## Current situation / state maintenance rule

Every public session ingest should produce one of these explicit outcomes for `index.md` and `Current-State.md`:

- **Front-page situation changed:** replace the `## Current Situation` paragraph in `index.md` with a short, player-safe description of where the crew stands now.
- **Front-page situation unchanged:** say why, usually because the session was a backdated interlude, pure bookkeeping, or did not alter the public campaign posture.
- **Current State changed:** update `Current-State.md` more fully, including current focus, recent runs/follow-ups, in-world date, immediate leads, and open questions as needed.
- **Current State unchanged:** say why and confirm that the existing focus, dates, leads, and open questions remain accurate.
- **State unresolved:** leave the ingest provisional and queue a GM clarification instead of letting uncertainty disappear.

Use `scripts/update_current_campaign_state.py` to apply approved state text from a JSON payload. The session-summary model should draft the prose; the deterministic script should own section replacement and frontmatter dates.

Example payload:

```json
{
  "current_situation": "The crew has just finished the Radnor Lake handoff and is deciding whether to pursue the scorpion-drone evidence, Wyrmwatch fallout, or the Core 7 / Dead Soldier lead next.",
  "current_state": {
    "current_focus": [
      "The latest player-visible focus is the aftermath of the Radnor Lake / Wyrmwatch handoff.",
      "The crew's most immediate practical choice is whether to analyze the recovered scorpion drone, follow Wyrmwatch's custody of Chunky Sparkles, or pursue the Core 7 / Dead Soldier trace."
    ],
    "recent_runs": [
      "The Chunky Sparkles / Wyrmwatch follow-up remains the latest completed run.",
      "The Pixel Sticks scorpion drone recovery remains an active evidence and salvage follow-up."
    ],
    "in_world_date": [
      "Current campaign year: **2066**",
      "Current active date: **2066-05-15**, canon."
    ],
    "immediate_leads": [
      "diagnose the recovered Pixel Sticks Scorpion Drone",
      "determine what Wyrmwatch does with Chunky Sparkles"
    ],
    "open_questions": [
      "What does the recovered scorpion drone still contain?",
      "Who taught the Chunky Sparkles command phrases?"
    ]
  }
}
```

## Date discipline rule

Every public session ingest should end with one of these explicit outcomes:

- **Advances current date:** update `Current-State.md`, `index.md`, and `Timeline/Session-Chronology.md`.
- **Does not advance current date:** say why, usually because it is a backdated interlude, same-night continuation, or side scene.
- **Date unresolved:** leave the session marked provisional and queue a GM clarification instead of letting the uncertainty disappear.

This should become part of the acceptance check for session closeout: no ingest is considered done until the session page, Current Situation, Current State, and chronology agree about date status.

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
- Should the Lead Board live under `Clues/`, replace `Clues/README.md`, or become a new top-level `Leads/` section with `Clues/` retained for evidence pages?
- How should GM-only lead-ledger notes be stored so public wiki pages never leak hidden payoffs?

## A likely end state

The long-term vision is something like this:

> A real Shadowrun session ends, Cindy recognizes that it was real play, writes the first pass of the session record, updates her own memory, extracts important campaign facts, and leaves the campaign in a cleaner and more searchable state than it was before the session ended.

That is the higher-level function this page is sketching.

## Related pages

- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou Tooling and Discord Notes](Tooling-and-Discord.md)
- [Cindy Lou Wiki and Tooling Topology](Wiki-and-Tooling-Topology.md)
- [Cindy Lou GM Control Panel](GM-Control-Panel.md)
