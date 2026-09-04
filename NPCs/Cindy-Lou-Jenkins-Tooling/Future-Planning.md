---
title: Cindy Lou Tooling Future Planning
type: planning
visibility: player-safe
status: future-planning
updated: 2026-09-04
tags: [cindy, tooling, minigames, workflow, future-planning, discord, vtt]
sources:
  - Discord discussion 2026-09-04
---

# Cindy Lou Tooling Future Planning

This page preserves future build ideas for the Nashville Shadowrun table's Cindy Lou tooling, mini-tools, and play workflow aids.

The main design judgment from the 2026-09-04 discussion: the best next tools are not more autonomous advice. They are **shared table state, lower friction, GM-controlled affordances, and better continuity** across Discord voice, the virtual tabletop, the wiki, and player-facing web apps.

## Planning Principles

- Build tools that make the table's own memory sharper instead of replacing player problem-solving.
- Keep the GM in control of pacing, canon, spoilers, and Cindy's table presence.
- Prefer browser-accessible pages and static web apps, because players may use different technical setups while still sharing Discord, the wiki, and the internet.
- Treat Cindy as an active NPC / operations layer, not a co-GM that interrupts with optimal tactics.
- Favor small, reliable tools that preserve state, expose context, or reduce bookkeeping.

## 1. Live Session Dashboard

A lightweight web page everyone can open during play.

Possible contents:

- current scene
- active location
- visible NPCs
- current objective
- open questions
- combat / status notes
- session clock
- links to relevant wiki pages

Cindy could update it from transcript and manual prompts, but the GM should be able to pin or correct facts instantly. This would be especially useful for new players joining mid-campaign.

## 2. What Do We Know? Lead Board

A player-facing clue and lead tracker tied to the wiki.

Possible states:

- active leads
- dead leads
- unresolved questions
- who knows what
- next plausible actions
- confirmed / suspected / table theory

The wiki already has [Loose Threads / Unpulled Threads / Lead Board](../../Clues/), so this should improve or web-app-ify that page rather than create a competing tracker. The important distinction is spoiler-safe confidence: **confirmed**, **suspected**, and **wild table theory** should not blur together.

## 3. Session Closeout Button

A structured post-session workflow that starts from the existing live transcript and wiki archive process.

Ideal flow:

1. Session ends.
2. Transcript is preserved.
3. Cindy drafts summary, entities, rewards, open hooks, and state changes.
4. GM approves or corrects the draft.
5. Wiki updates land as committed, deployed pages.

The key improvement is a GM review screen. Fully autonomous public publishing should remain gated by explicit or workflow-level GM approval.

## 4. New Player Orientation Mode

A one-page generated packet for alternate PCs, starter characters, or guests.

Possible contents:

- current crew
- current job
- important recurring names
- things this character would know
- current table conventions
- links to the wiki pages most relevant tonight

The 2026-09-03 Kilimanjaro session showed the need clearly: a starter character can work well, but the onboarding packet should make the middle-of-season campaign context easier to enter.

## 5. VTT Companion Overlay

A browser-based companion for virtual tabletop play.

This should not require deep integration with every player's VTT setup. It could instead provide quick references and shared state:

- common SR3 target-number reminders
- dice-pool / TN notes
- current combat pools
- wound modifiers
- initiative passes
- vehicle and drone quick stats
- PC page links
- active-scene notes

A web companion is safer and more portable than relying on one specific virtual tabletop integration.

## 6. GM Private Control Panel for Cindy

A small GM-facing panel for controlling Cindy's live behavior.

Possible buttons:

- Cindy stay silent
- Cindy give short in-character line
- Cindy analyze Matrix angle
- generate saved voice clip
- summarize last 5 minutes
- mark this as canon
- mark this GM-only

This would make Cindy feel present without making her unpredictable. It should route Cindy's initiative through GM control when the moment is not a direct player request.

## 7. NPC / Voice Line Scratchpad

A live scratchpad for preserving NPC moments, voice cues, and future callbacks.

Possible captured fields:

- quote
- mood
- pronunciation
- relationship shift
- future callback
- relevant session and scene
- whether the note is player-safe or GM-only

This would support recurring NPC consistency for figures like Mucky, Melchizedek, Herrick, Taco, and Cindy Lou herself. It can feed wiki updates, voice-clip planning, and post-session entity notes.

## 8. Player-Facing Previously On Generator

A pre-session recap generator pulling from the last session, Current State, and active leads.

Possible outputs:

- short text recap
- bullet-point version for Discord
- wiki-linked version
- optional short Cindy-voiced version for continuity-heavy weeks

This does not need full production value every session, but it would help players re-enter long-running investigations quickly.

## What Not To Build First

Do **not** prioritize deep autonomous tactical advice.

The table already has strong players, and Cindy interrupting with optimal plans risks flattening play. The better first builds are tools that preserve shared state, expose relevant memory, and reduce GM/player bookkeeping while leaving tactical decisions at the table.

## Likely Priority Order

1. **Live Session Dashboard** - highest table value, especially for guests and returning players.
2. **Session Closeout Button** - reduces the biggest recurring maintenance burden.
3. **GM Private Control Panel for Cindy** - improves live control and reduces unwanted interruptions.
4. **New Player Orientation Mode** - useful immediately for Kilimanjaro / alternate-PC onboarding.
5. **Lead Board improvements** - build on the existing Clues board rather than splitting sources.
6. **Previously On Generator** - strong quality-of-life improvement before sessions.
7. **VTT Companion Overlay** - useful, but needs careful scope control.
8. **NPC / Voice Line Scratchpad** - valuable once live dashboard and closeout flows exist.

## Related Pages

- [Minigames and Web Apps](../../Minigames.md)
- [Loose Threads / Unpulled Threads / Lead Board](../../Clues/)
- [Cindy Lou Live Session Monitoring Design](Live-Session-Monitoring-Design.md)
- [Cindy Lou Post-Session Automation](Post-Session-Automation.md)
- [Cindy Lou Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md)
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md)
