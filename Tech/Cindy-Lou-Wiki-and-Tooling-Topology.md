---
title: Cindy Lou Wiki and Tooling Topology
type: tech-note
visibility: player-safe
status: draft
updated: 2026-07-14
tags: [cindy, wiki, tooling, architecture]
---

# Cindy Lou Wiki and Tooling Topology

## Purpose

This page documents how Cindy's wiki presence, live tooling, and Discord behavior fit together at a systems level.

## Main surfaces

Cindy currently has three active player-visible or operator-visible surfaces, plus one outdated archived surface:

1. **objective dossier page**
   - `NPCs/Cindy-Lou-Jenkins.md`
2. **subjective / in-world voice page**
   - `NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md`
3. **tooling summary page**
   - `Tech/Cindy-Lou-Tooling-and-Discord.md`
4. **GM soundboard entry point** _(outdated)_
   - formerly linked from the in-world Cindy page via the small `π` symbol; no longer maintained

## Functional separation

### Objective dossier

This page is where Cindy is described as campaign fact.

Use it for:

- canonical identity
- continuity reconciliation
- major relationships
- campaign-significant facts

### In-world voice page

This page is Cindy speaking for herself.

Use it for:

- voice and personality
- first-person interpretation
- flavor and perspective
- links to active Cindy-adjacent tools; the old soundboard link has been retired

### Tooling summary page

This page explains the support stack in broad terms.

Use it for:

- what systems exist
- what each one is for
- how the pieces relate
- where to look next for more technical detail

### Technical sub-pages

The technical sub-pages break the system into reconstructable parts.

Use them for:

- repo paths
- queue paths
- runtime responsibilities
- failure reasons
- design tradeoffs
- rebuild notes

## Repo and storage topology

### Wiki repo

- `/Users/hanclaw/claw/projects/cindylou/campaign-wiki`

This is the published campaign wiki.

### Discord voice bridge repo

- `/Users/hanclaw/claw/projects/discord_voice_patch`

This contains:

- Discord bot runtime
- text command handling
- voice join/play behavior
- archived queue consumer for the outdated soundboard prototype

### Soundboard app repo _(outdated)_

- `/Users/hanclaw/claw/projects/cindylou/cindy-soundboard`

This contained:

- Express server
- login/session handling
- clip catalog
- browser UI
- queue writer logic

Do not maintain this app, its tunnel URL, or its clip catalog unless the GM explicitly revives the soundboard.

### Runtime data areas

- preserved voice clips:
  - `/Users/hanclaw/.openclaw/workspace-cindylou/preserved_voice`
- logs:
  - `/Volumes/carbonite/claw/data/cindylou/logs`
- soundboard queue _(outdated)_:
  - `/Volumes/carbonite/claw/data/cindylou/runtime/soundboard-queue`

## Current integration pattern

### Archived soundboard path _(outdated)_

The wiki no longer advertises the soundboard as an active live tool. The old implementation was a separate local web app that wrote local request files for the voice bridge, but the table has moved past maintaining that button-board flow.

Preserve the notes only as a historical implementation lesson: Discord bot-to-self text commands were the wrong control path, and direct local control was more reliable.

## Key design decisions

### 1. Separate fiction from operations

Cindy's campaign identity is easier to understand when:

- objective facts live in one page
- Cindy's own voice lives in another
- operational notes live elsewhere

### 2. Prefer local control over Discord self-commanding

The system originally attempted to make Cindy trigger herself through Discord text.

That path failed because bot-authored commands are ignored by the command processor.

So the design shifted to direct local control.

### 3. Keep filenames stable

Clip playback is easier to reason about when a saved-clip workflow stores stable local filenames instead of freeform command text.

## Recommended future documentation growth

As the system grows, the next useful pages would likely be:

- Cindy memory/index pipeline notes
- Discord thread/session routing notes
- clip library conventions and naming rules
- deployment/public URL stabilization notes

## Related pages

- [Cindy Lou Tooling and Discord Notes](Cindy-Lou-Tooling-and-Discord.md)
- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md)
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md)
- [Cindy Lou Soundboard and Voice Bridge](Cindy-Lou-Soundboard-and-Voice-Bridge.md) _(outdated)_
