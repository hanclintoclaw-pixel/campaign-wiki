---
title: Minigames and Web Apps
type: index
visibility: player-safe
updated: 2026-07-10
---

# Minigames and Web Apps

Static Shadowrun apps live on GitHub Pages and use the campaign wiki as the hub for discovery, canon links, and maintenance notes.

## Standard persistence pattern

- Apps are static GitHub Pages sites.
- Local drafts and per-user/session state live in browser `localStorage`.
- Global/canon changes are submitted through prefilled GitHub Issues with a human summary and fenced JSON payload.
- Cindy or a maintainer validates the issue author before applying any canonical repo/wiki updates.
- Canonical changes land as commits, trigger CI/CD, and then get closed out in GitHub and Discord.

## Permission gate

Public issue creation is not permission to mutate canon. Cindy should only act on a persistence issue when the issue author's GitHub association is `MEMBER`, `OWNER`, or `COLLABORATOR`, or a repo member explicitly approves the request in-thread.

## Active apps

- [Curtis Drone Dashboard](https://hanclintoclaw-pixel.github.io/drone-dashboard/) - SR3/Rigger 3-style drone and vehicle session tracker.
- [Mevin Matrix Deck Manager](https://hanclintoclaw-pixel.github.io/mevin-deck-manager/) - SR3 cyberdeck, utility loadout, and host-run note tracker.
- [Mevin Host Run Simulator](https://hanclintoclaw-pixel.github.io/mevin-host-run-simulator/) - click-through SR3-inspired Matrix host intrusion aid using Deck Manager exports and editable host profiles.
- [Mevin Decker Experience](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) - branching cyber-dungeon crawl that syncs Deck Manager state and pulls wiki host profile JSON.

## Templates and implementation notes

- Template repository path: `/Users/hanclaw/claw/projects/cindylou/shadowrun-minigame-template`
- Persistence guidance: `shadowrun-minigame-template/docs/PERSISTENCE_PATTERN.md`
- Cindy ingestion workflow: `shadowrun-minigame-template/docs/INGESTION_WORKFLOW.md`
- WYSIWYG wiki editor persistence plan: [Wiki Editor Persistence](meta/Wiki-Editor-Persistence.md)

## Candidate future apps

- Dolphin habitat simulator for Ace Malone and related aquatic-support rolls.
- Drone maintenance simulator canonicalizing repairs, upgrades, ammunition, and downtime costs.
- Wiki WYSIWYG editor that stores drafts locally and persists proposed page edits through GitHub Issues.
