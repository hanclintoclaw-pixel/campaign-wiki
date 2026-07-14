---
title: Cindy Lou Tooling and Discord Notes
type: tech-note
visibility: player-safe
status: draft
updated: 2026-07-14
tags: [cindy, tooling, discord, wiki, campaign-tech]
---

# Cindy Lou Tooling and Discord Notes

## Purpose

This page tracks the support systems around **Cindy Lou Jenkins** as a live campaign presence: the wiki layer, the campaign tool layer, and the custom Discord behavior that makes Cindy usable during play.

The goal of this page is twofold:

- keep the overall picture readable
- point to deeper technical pages detailed enough that the stack could be rebuilt

## Cindy's campaign role

Cindy currently sits in an unusual middle space between:

- **in-world character**
- **campaign memory interface**
- **Discord bot persona**
- **technical experiment in live table support**

That means the crew interacts with Cindy both as fiction and as infrastructure.

## High-level architecture

At a system level, the current Cindy stack is split into three major layers:

1. **wiki/documentation layer**
2. **tooling/application layer**
3. **Discord/voice runtime layer**

### Wiki/documentation layer

The campaign wiki currently gives Cindy at least three distinct surfaces:

- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md) — objective dossier
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md) — subjective/in-world voice page
- this page — operational/tooling notes

Current wiki goals for Cindy:

- keep continuity readable
- separate objective facts from Cindy's own voice
- track technical support work without losing campaign context
- make player-visible updates easy to surface quickly

### Tooling/application layer

The current tool stack around Cindy is being shaped to support three kinds of work:

- **campaign memory retrieval**
- **Shadowrun rules/reference support**
- **live session utility** such as summaries, prompts, audio support, and quick lookup

Practical near-term goals include:

- better indexing of Shadowrun 3rd Edition material
- cleaner campaign memory retrieval
- easier GM/player access to Cindy-specific tools
- preserving useful technical state between sessions

### Discord/voice runtime layer

The current Discord-side Cindy setup has already moved beyond a plain text bot.

Known/customized behavior includes:

- thread-aware Cindy interaction flows
- session-linked text handling
- custom wake / routing behavior for Cindy prompts
- voice chat integration work for joining, listening, and speaking in Discord audio
- saved-clip playback support through the local voice bridge
- an archived GM-facing soundboard experiment, now marked outdated

## Repo map

The current implementation is spread across three main code locations:

### Wiki repo

- `/Users/hanclaw/claw/projects/cindylou/campaign-wiki`

### Discord voice bridge repo

- `/Users/hanclaw/claw/projects/discord_voice_patch`

### Soundboard app repo _(outdated)_

- `/Users/hanclaw/claw/projects/cindylou/cindy-soundboard`

These are intentionally separate because they solve different problems:

- wiki repo = published documentation and player-facing pages
- voice bridge repo = live Discord voice runtime
- soundboard repo = outdated authenticated GM tool UI; keep only as archived prototype context

## Soundboard status _(outdated)_

The soundboard was an experiment to give the GM a fast way to trigger canned Cindy voice clips during play. The table has moved past that approach, and the soundboard app, tunnel URL, and clip catalog should not be maintained going forward.

Preserve the archived notes only for the useful implementation lesson:

- the first attempt relied on Cindy posting a Discord text command to herself
- that failed because bot-authored commands are ignored by the command processor
- the later prototype used a direct local queue bridge into the voice bot, but it is no longer the active direction

## Detailed technical pages

For reconstructable implementation detail, use these pages:

- [Cindy Lou Wiki and Tooling Topology](Cindy-Lou-Wiki-and-Tooling-Topology.md)
- [Cindy Lou Live Session Monitoring Design](Cindy-Lou-Live-Session-Monitoring-Design.md)
- [Cindy Lou External Transcription Watchdog Plan](Cindy-Lou-External-Transcription-Watchdog-Plan.md)
- [Cindy Lou Session Scratchpad Implementation Plan](Cindy-Lou-Session-Scratchpad-Implementation-Plan.md)
- [Cindy Lou Soundboard and Voice Bridge](Cindy-Lou-Soundboard-and-Voice-Bridge.md) _(outdated)_

## Known limitations

The current Cindy stack still has a few rough edges:

- public URL stability for local-only tools is still being improved
- some tooling is still prototype-grade rather than long-term hardened
- live voice and wiki integration are not fully unified yet
- the active system is documented well enough to rebuild, but not yet fully productized
- the old soundboard path is archived and should not receive routine maintenance

## Working direction / next steps

Likely next improvements:

- make direct live voice playback cleaner and more observable
- improve campaign/wiki tooling documentation
- keep a clearer record of what is canonical, what is operational, and what is experimental
- move from ad-hoc glue toward a cleaner long-term service boundary

## Related pages

- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md)
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md)
- [Cindy Lou Wiki and Tooling Topology](Cindy-Lou-Wiki-and-Tooling-Topology.md)
- [Cindy Lou Live Session Monitoring Design](Cindy-Lou-Live-Session-Monitoring-Design.md)
- [Cindy Lou External Transcription Watchdog Plan](Cindy-Lou-External-Transcription-Watchdog-Plan.md)
- [Cindy Lou Session Scratchpad Implementation Plan](Cindy-Lou-Session-Scratchpad-Implementation-Plan.md)
- [Campaign Navigation](../Navigation.md)
- [Cindy Lou Soundboard and Voice Bridge](Cindy-Lou-Soundboard-and-Voice-Bridge.md) _(outdated)_
