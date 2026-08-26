---
title: Minigames and Web Apps
type: index
visibility: player-safe
updated: 2026-08-26
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
- [Curtis Drone Shift](https://hanclintoclaw-pixel.github.io/curtis-drone-shift/) - daily garage work-order minigame for Curtis drone, vehicle, salvage, and Taco-shop maintenance scenes.
- [Mevin Matrix Deck Manager](https://hanclintoclaw-pixel.github.io/mevin-deck-manager/) - SR3 cyberdeck, utility loadout, and host-run note tracker.
- [Mevin Host Run Simulator](https://hanclintoclaw-pixel.github.io/mevin-host-run-simulator/) - click-through SR3-inspired Matrix host intrusion aid using Deck Manager exports and editable host profiles.
- [Mevin Decker Experience V1](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) - locked V1 branching cyber-dungeon crawl that syncs Deck Manager state and pulls wiki host profile JSON.
- [Mevin Decker Experience V2](https://hanclintoclaw-pixel.github.io/mevin-decker-experience-v2/) - V2 clone for future iteration, currently matching V1 behavior.
- [Matrix Search Guide](https://hanclintoclaw-pixel.github.io/matrix-search-guide/) - SR3 Matrix search workflow tool for choosing search paths, applying canon modifiers, and producing a GM-facing result report.
- [Contact Legwork Guide](https://hanclintoclaw-pixel.github.io/contact-legwork-guide/) - SR3 in-session contact workflow tool for contact knowledge, costs, Friends of Friends, wait times, Wrong Party risk, and GM-ruling prompts.
- [Buying New Items Guide](https://hanclintoclaw-pixel.github.io/buying-new-items-guide/) - SR3 in-world purchasing workflow tool for Availability, Street Index, Negotiation, legality, wrong-party risk, pickup, and installation status.
- [Spell Guide](https://hanclintoclaw-pixel.github.io/spell-guide/) - SR3 spell catalogue and Sorcery/Conjuring roll aid with a cybermystic UI shell.
- [SR3 GM Spirit Tool](Tools/SR3-GM-Spirit-Tool.md) - SR3 spirit and elemental calculator for Force-based attributes, attacks, initiative, powers, domains, and weaknesses.

## SR3 workflow aids

These are player-facing table procedures, with guided web-app versions where available.

- [Matrix Searches](Tech/Matrix/Matrix-Searches.md) - SR3 workflow for Matrix research, Shadowland/data haven legwork, and host-local file/access-node searches.
- [Matrix Search Guide](https://hanclintoclaw-pixel.github.io/matrix-search-guide/) - guided worksheet app for Matrix search paths, canon modifiers, and GM-facing result reports.
- [Contact Legwork](Tech/Matrix/Contact-Legwork.md) - SR3 workflow for contact asks, Friends of Friends, fees, wait times, and Wrong Party risk.
- [Contact Legwork Guide](https://hanclintoclaw-pixel.github.io/contact-legwork-guide/) - guided worksheet app for contact knowledge, costs, FOF routing, wait times, and GM-ruling prompts.
- [Buying New Items](Tech/Matrix/Buying-New-Items.md) - SR3 workflow for Availability, Street Index, contacts, negotiation, legality, wrong-party risk, pickup, and installation status.
- [Buying New Items Guide](https://hanclintoclaw-pixel.github.io/buying-new-items-guide/) - guided worksheet app for in-world purchases using campaign nuyen.

## Cindy Lou Tooling

- [Cindy Lou Tooling](NPCs/Cindy-Lou-Jenkins-Tooling/) - NPC behavior, live-session monitoring, voice clips, and Cindy-specific Discord support.

## Documentation

- [Mevin Decker Experience Documentation](Documentation/Mevin-Decker-Experience.md)
- [Mevin Decker Experience Player Manual](Documentation/Mevin-Decker-Experience-Manual.md)
- [Curtis Drone Shift Documentation](Documentation/Curtis-Drone-Shift.md)
- [Curtis Drone Shift Work Order Guidelines](Documentation/Curtis-Drone-Shift-Work-Order-Guidelines.md)

## Templates and implementation notes

- Template repository path: `/Users/hanclaw/claw/projects/cindylou/shadowrun-minigame-template`
- Persistence guidance: `shadowrun-minigame-template/docs/PERSISTENCE_PATTERN.md`
- Cindy ingestion workflow: `shadowrun-minigame-template/docs/INGESTION_WORKFLOW.md`
- WYSIWYG wiki editor persistence plan: [Wiki Editor Persistence](meta/Wiki-Editor-Persistence.md)

## Candidate future apps

- Dolphin habitat simulator for Ace Malone and related aquatic-support rolls.
- Drone maintenance simulator canonicalizing repairs, upgrades, ammunition, and downtime costs.
- Wiki WYSIWYG editor that stores drafts locally and persists proposed page edits through GitHub Issues.
