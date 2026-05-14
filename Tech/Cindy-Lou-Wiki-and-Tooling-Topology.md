---
title: Cindy Lou Wiki and Tooling Topology
type: tech-note
visibility: player-safe
status: draft
updated: 2026-05-13
tags: [cindy, wiki, tooling, architecture]
---

# Cindy Lou Wiki and Tooling Topology

## Purpose

This page documents how Cindy's wiki presence, live tooling, and Discord behavior fit together at a systems level.

## Main surfaces

Cindy currently has four distinct player-visible or operator-visible surfaces:

1. **objective dossier page**
   - `NPCs/Cindy-Lou-Jenkins.md`
2. **subjective / in-world voice page**
   - `NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md`
3. **tooling summary page**
   - `Tech/Cindy-Lou-Tooling-and-Discord.md`
4. **GM soundboard entry point**
   - linked from the in-world Cindy page via the small `π` symbol

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
- links to live Cindy-adjacent tools such as the soundboard

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

### Soundboard app repo

- `/Users/hanclaw/claw/projects/cindylou/cindy-soundboard`

This contains:

- Express server
- login/session handling
- clip catalog
- browser UI
- queue writer logic

### Discord voice bridge repo

- `/Users/hanclaw/claw/projects/discord_voice_patch`

This contains:

- Discord bot runtime
- text command handling
- voice join/play behavior
- queue consumer for direct soundboard playback

### Runtime data areas

- preserved voice clips:
  - `/Users/hanclaw/.openclaw/workspace-cindylou/preserved_voice`
- soundboard queue:
  - `/Volumes/carbonite/claw/data/cindylou/runtime/soundboard-queue`
- logs:
  - `/Volumes/carbonite/claw/data/cindylou/logs`

## Current integration pattern

### Wiki -> soundboard

The wiki does not host the soundboard logic directly.

Instead:

- the wiki is the visible doorway
- the soundboard is a separate local web app
- the `π` link on Cindy's page points into the soundboard entry path

### Soundboard -> voice bridge

The soundboard no longer tries to use Discord text as its primary control plane.

Instead it now:

- authenticates a user session
- writes a local request file
- lets the local voice bridge process consume that request directly

### Soundboard -> Discord thread

The soundboard still posts a raw command line into the designated Discord request thread for visibility/debugging, but that thread post is no longer the actual playback trigger.

## Key design decisions

### 1. Separate fiction from operations

Cindy's campaign identity is easier to understand when:

- objective facts live in one page
- Cindy's own voice lives in another
- operational notes live elsewhere

### 2. Keep the soundboard small

The soundboard is deliberately lightweight.

It is not intended to become a giant application before it proves useful.

### 3. Prefer local control over Discord self-commanding

The system originally attempted to make Cindy trigger herself through Discord text.

That path failed because bot-authored commands are ignored by the command processor.

So the design shifted to direct local control.

### 4. Keep filenames stable

Clip playback is easier to reason about when the clip catalog stores stable local filenames instead of freeform command text.

## Recommended future documentation growth

As the system grows, the next useful pages would likely be:

- Cindy memory/index pipeline notes
- Discord thread/session routing notes
- soundboard operations runbook
- clip library conventions and naming rules
- deployment/public URL stabilization notes

## Related pages

- [Cindy Lou Tooling and Discord Notes](Cindy-Lou-Tooling-and-Discord.md)
- [Cindy Lou Soundboard and Voice Bridge](Cindy-Lou-Soundboard-and-Voice-Bridge.md)
- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md)
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md)
