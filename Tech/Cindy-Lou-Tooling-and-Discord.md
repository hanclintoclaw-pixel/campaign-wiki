---
title: Cindy Lou Tooling and Discord Notes
type: tech-note
visibility: player-safe
status: draft
updated: 2026-05-13
tags: [cindy, tooling, discord, wiki, campaign-tech]
---

# Cindy Lou Tooling and Discord Notes

## Purpose

This page tracks the support systems around **Cindy Lou Jenkins** as a live campaign presence: the wiki layer, the campaign tool layer, and the custom Discord behavior that makes Cindy usable during play.

## Cindy's campaign role

Cindy currently sits in an unusual middle space between:

- **in-world character**
- **campaign memory interface**
- **Discord bot persona**
- **technical experiment in live table support**

That means the crew interacts with Cindy both as fiction and as infrastructure.

## Wiki layer

The campaign wiki currently gives Cindy at least three distinct surfaces:

- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md) — objective dossier
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md) — subjective/in-world voice page
- this page — operational/tooling notes

Current wiki goals for Cindy:

- keep continuity readable
- separate objective facts from Cindy's own voice
- track technical support work without losing campaign context
- make player-visible updates easy to surface quickly

## Campaign tool layer

The current tool stack around Cindy is being shaped to support three kinds of work:

- **campaign memory retrieval**
- **Shadowrun rules/reference support**
- **live session utility** such as summaries, prompts, audio support, and quick lookup

Practical near-term goals include:

- better indexing of Shadowrun 3rd Edition material
- cleaner campaign memory retrieval
- easier GM/player access to Cindy-specific tools
- preserving useful technical state between sessions

## Discord bot customizations

The current Discord-side Cindy setup has already moved beyond a plain text bot.

Known/customized behavior includes:

- thread-aware Cindy interaction flows
- session-linked text handling
- custom wake / routing behavior for Cindy prompts
- voice chat integration work for joining, listening, and speaking in Discord audio
- saved-clip playback support through the local voice bridge
- a GM-facing soundboard experiment tied to Cindy voice playback

## Soundboard status

The soundboard work is meant to give the GM a fast way to trigger Cindy voice clips during play.

Current direction:

- wiki-linked entry point
- password-gated soundboard UI
- hardcoded first-pass Cindy clip set
- local playback bridge into the Discord voice bot path

This is still active development rather than a finished polished subsystem.

## Known limitations

The current Cindy stack still has a few rough edges:

- public URL stability for local-only tools is still being improved
- Discord text-command loops do not work cleanly when Cindy is effectively trying to command herself
- some tooling is still prototype-grade rather than long-term hardened
- voice, soundboard, and wiki integration are not fully unified yet

## Working direction / next steps

Likely next improvements:

- stabilize the soundboard entry path
- make direct local playback cleaner and more observable
- improve campaign/wiki tooling documentation
- keep a clearer record of what is canonical, what is operational, and what is experimental

## Related pages

- [Cindy Lou Jenkins](../NPCs/Cindy-Lou-Jenkins.md)
- [Cindy Lou Jenkins, In Her Own Words](../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md)
- [Campaign Navigation](../Navigation.md)
