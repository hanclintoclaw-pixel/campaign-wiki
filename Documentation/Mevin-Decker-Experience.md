---
title: Mevin Decker Experience Documentation
type: documentation
visibility: player-safe
updated: 2026-07-17
---

# Mevin Decker Experience Documentation

For player-facing step-by-step use at the table, see the [Mevin Decker Experience Player Manual](Mevin-Decker-Experience-Manual.md).

## What it is

The [Mevin Decker Experience](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) is a live-table Matrix host crawl tool for Shadowrun 3rd Edition play. It turns a wiki-hosted Matrix host profile into a clickable, roll-gated flowchart that a decker player can use while the rest of the team continues acting in meatspace.

The design goal is not to replace SR3 Matrix rules. It is a table helper: a fast, readable way to give the decker meaningful choices, rolls, Security Tally pressure, IC interruptions, and concrete rewards without making the GM run an entire separate rules subsystem from scratch every time someone jacks in.

## Who it is for

- **Deckers / players:** use it as a guided host crawl. Pick an action, roll, see whether the route opens, and record what you uncover.
- **GMs:** use it to present prepared host topology, rewards, security pressure, and GM-confirmation prompts without revealing hidden layers too early.
- **Wiki maintainers:** use host JSON profiles in `data/matrix-hosts/` to publish loadable Matrix runs from campaign wiki records.

## How the table experience works

A host starts with up to two initial entry doors plus a quiet-exit option:

- **Public visitor door:** usually no roll. It shows harmless, official, on-theme public Matrix content.
- **Secure / hidden decker door:** requires a roll. Failure can lock that route for the current crawl and reveal nothing else.
- **Graceful Logoff:** exits from the front door quietly and records that quiet exit in the GM report.

Once inside the private side, the decker sees featured actions: subsystem access, file archives, camera networks, shipping records, hidden seams, control hooks, or paydata opportunities. A successful action either opens a new node or grants a specific result the player can tell the GM or note for later. Host profiles should not stack two locked doors in a row when both gates lead to the same single location; the first successful gate needs to reveal something usable.

If the decker wants to do something outside the featured options, the player should tell the GM directly. The GM adjudicates the SR3-style test, time cost, Tally pressure, and outcome.

## Rolls and branch locking

Most featured private actions have a `testId`, target number, and success threshold. When the player rolls:

- success unlocks the destination node or reward;
- failure locks that route for the current crawl;
- hidden or deeper nodes stay invisible until unlocked;
- current-crawl lockouts are not automatically permanent in-world failures. After enough in-world time passes, the GM may allow a reset and retry.

This makes weak attempts bounce off hard hosts cleanly while still letting a table come back later with better prep, better tools, or another opportunity.

## Security Tally and IC checkpoints

The tool tracks **Security Tally** as tested actions occur. Host profiles define a `securitySheaf`: threshold events such as Probe IC, Trace IC, Scramble IC, Tar Baby pressure, Sparky IC, or corporate escalation.

The tool also displays alert state based on the Host's Shutdown limit inside the Current Node card: **Passive Alert** at roughly one-third of Shutdown with an orange card, **Active Alert** at roughly two-thirds with a red card, and **Shutdown / dumpshock** when the limit is reached.

When Tally crosses a sheaf threshold, normal navigation pauses and the player gets a **Security checkpoint**. The player can:

- suppress / evade White IC, which moves it to a blank higher Security Tally slot so it may return later;
- fight IC, which crashes and removes it from the ongoing run on success;
- ignore it and continue;
- jack out.

Grey IC and Black IC cannot be suppressed in the tool; suppression controls are disabled for those categories. Ignored or failed checkpoints become **active pressure**. Active pressure increases future Tally risk until handled, giving the decker a little combat/IC-management loop without turning the whole app into a full cybercombat simulator. A failed jackout while trapped in a host ends the run with dumpshock and a GM-facing consequence prompt.

## Rewards and permanent outcomes

Rewards should be concrete but often GM-scoped. Good examples include:

- customer files;
- shipping records;
- camera-network access;
- supplier irregularity paydata;
- future-plan cache;
- member list cache;
- recurring order inserted into fulfillment systems.

Permanent outcomes must tell the player to **notify the GM**. If a player changes records, schedules a delivery, inserts a recurring order, plants a file, disables a device, or otherwise changes campaign state, the GM does not know it happened until the player reports it.

The final Discord-ready report intentionally excludes pure fluff, but it should preserve concrete discoveries: camera access, records, paydata, device control, account access, permanent changes, and GM-confirmation nodes. Host authors can force that with reportable node kinds such as `confirmation`, `reward`, `paydata`, or `permanent-outcome`, or with explicit `report` metadata in scenario JSON.

## Host library and data model

The app loads host profiles from the campaign wiki host index:

- Host index: [data/matrix-hosts/index.json](../data/matrix-hosts/index.json)
- Host design guide: [Matrix Host Construction Guide](../Tech/Matrix/Host-Construction-Guide.md)
- Matrix host records: [Tech/Matrix/](../Tech/Matrix/)

Each host profile is JSON with:

- host stats: security code/value, host rating, subsystem ratings, task target numbers;
- security sheaf thresholds and effects;
- sculpting and notes;
- a `flow` graph of nodes and choices;
- optional per-choice overrides for harder hidden layers, such as higher target numbers or security values;
- optional node-granted `advantages` for targeted rewards such as passcodes, keycards, found passwords, or borrowed equipment.

The app can also sync decker/deck data from the [Mevin Matrix Deck Manager](https://hanclintoclaw-pixel.github.io/mevin-deck-manager/) when browser origin/localStorage conditions allow it, or load manual deck JSON. During play, the GM / table modifiers panel can add manual Run Advantages that grant bonus dice, lower target numbers, or reduce required successes for all rolls or named test IDs.

## Host map and location state

The Decker Experience renders a branching Host map from the scenario flow graph. The map sits below the main crawl on desktop and remains compact/horizontally scrollable on mobile.

Location states are color-coded across both the map and the verb menu:

- **Current:** the active node.
- **Found:** a node the decker has visited before.
- **Revealed:** a known node that has appeared but has not been visited.
- **Hidden:** an obscured placeholder for an unrevealed Host zone.

Hidden zones may show structure without revealing labels, preserving the sense that a Host has more branches while keeping unrevealed node names out of player view.

## Current loadable examples

The Host Library currently includes several wiki-backed profiles, including:

- **Happy Cat Public Storefront Host** — starter host with harmless public side, private store records, a strange pet-food clue, and a hidden Pixel Sticks layer.
- **Augmented Beef and Bacon Social Club Host** — consumer-brand host with multiple generic paydata opportunities and a permanent off-books luxury snack order outcome.
- **Lafayette Tower CAT Entertainment Host** — high-danger megacorp entertainment host with a deeply hidden Ultraviolet layer.
- Other campaign hosts such as Ares Nashville, Humanis Nashville, Nashville City Government, and SC Music.

## Limitations and table caveats

The Decker Experience is a **guided table tool**, not a full SR3 Matrix rules engine.

Important limitations:

- It abstracts many RAW Matrix operations into featured actions.
- It does not fully model every utility, operation, IC stat block, cybercombat option, damage track, account privilege, or host subsystem rule from SR3 / Matrix.
- It relies on GM interpretation for exact file contents, camera coverage, physical device scope, paydata value, and permanent campaign-state changes.
- It cannot know whether the meatspace team has created new modifiers, distractions, credentials, or consequences unless the GM/player applies them manually.
- Hidden-host surprise depends on players not reading GM-only wiki details before play.
- The app records and guides the crawl; it does not replace GM authority over what is actually true in the scene.

The useful mental model is: **prepared Matrix spotlight lane**. It gives the decker something tactile to do for a few minutes while the rest of the team operates, while still preserving the GM's role as arbiter of exact SR3 rules and campaign consequences.
