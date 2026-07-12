---
title: Mevin Decker Experience Player Manual
type: documentation
visibility: player-safe
updated: 2026-07-11
---

# Mevin Decker Experience Player Manual

This manual explains how to use the [Mevin Decker Experience](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/) during play.

Use it when your character is jacked into a Matrix host and the GM wants the decking run to proceed as a focused table minigame while the rest of the team continues acting outside the Matrix.

## Quick start

1. Open the [Mevin Matrix Deck Manager](https://hanclintoclaw-pixel.github.io/mevin-deck-manager/) and confirm your deck, persona, and utilities are current.
2. Open the [Mevin Decker Experience](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/).
3. Click **Sync Deck Manager**.
4. Click **Load Host List** if the host list is not already visible.
5. Choose the Host the GM told you to enter.
6. Pick public or secure entry, then keep making choices until the tool reaches **RUN OVER — ALERT THE GM**.
7. Tell the GM the final outcome, recovered paydata, permanent changes, unresolved IC, and whether you logged off cleanly or got forced out.

## Step 1: prepare the deck

The Decker Experience can sync from the [Mevin Matrix Deck Manager](https://hanclintoclaw-pixel.github.io/mevin-deck-manager/) when both apps are opened from the same GitHub Pages site origin in the same browser.

Before starting a run, check the Deck Manager for:

- deck name and owner;
- persona ratings;
- Detection Factor;
- loaded utilities;
- utility status.

If sync fails, use the Deck Manager export option and import the JSON manually in the Decker Experience with **Import Deck JSON**.

## Step 2: load the deck in the Decker Experience

In the Decker Experience:

1. Click **Sync Deck Manager**.
2. Confirm the Deck status card updates.
3. If it does not update, import the deck JSON manually.

The current tool uses deck data mainly for Detection Factor, persona context, and utility ratings. The GM may still adjust dice pools, target numbers, or modifiers based on SR3 rules and the live scene.

## Step 3: load a Host profile

The Decker Experience can load wiki-hosted Host profiles from the Host Library.

1. Click **Load Host List** if no list appears.
2. Choose a Host from **Wiki Host Library**.
3. Confirm the Matrix Host status card changes to the chosen Host.

You can also paste a direct scenario JSON URL into **Scenario JSON URL** and click **Fetch Scenario**, or use **Import Scenario JSON** for a downloaded file.

## Step 4: understand the first doors

Most Hosts begin with up to two doors:

- **Public visitor door:** usually no roll. It shows harmless official Matrix content.
- **Secure / hidden decker door:** requires a roll and leads to private subsystems.

The public door is useful for flavor, cover, or harmless surface information. The secure door is where actual intrusion begins.

A hidden or high-security Host may have no public door.

## Step 5: make choices and roll

Each node shows **Featured actions**. These are the most relevant options for that part of the Host.

When you select a tested action, the tool shows:

- target number;
- required successes;
- Computer skill;
- total Hacking Pool;
- effective free Hacking Pool automatically added to the roll;
- any Hacking Pool reserved for Detection Factor;
- any Hacking Pool tied up suppressing IC;
- relevant persona / utility context;
- Host response check details.

Click **Roll to unlock this branch** to attempt the action.

If you succeed, the new node opens. If you fail, that route locks for the current crawl and may reveal nothing further.

## Host map

The bottom of the app shows a branching Host map. It starts at the entry point and draws directional lines through public, private, and deeper Host sections.

Map colors help you avoid retreading old ground:

- **Current:** where you are now.
- **Found:** locations you have already visited and can jump back to from the map.
- **Revealed:** known locations that are visible but not yet visited.
- **Hidden:** obscured zones the crawl has not revealed yet.

The verb menu uses the same destination labels, so each choice tells you whether it leads toward a found location, a revealed-but-unvisited location, or a hidden zone.

On mobile, the map is compact and horizontally scrollable so the full Host tree stays legible without becoming another long vertical list.

## Off-menu RAW actions

The tool does not list every possible SR3 Matrix operation. If you want to do something outside the featured actions, tell the GM directly. The GM can call for the appropriate SR3-style test, time cost, tally pressure, utility use, or fictional consequence.

## Security Tally

Tested actions can increase **Security Tally**. The Host status area shows the current Tally, the inferred Shutdown limit, and the next sheaf event.

At roughly one-third of the way to Shutdown, the tool shows **Passive Alert** with a warning panel. At roughly two-thirds, it shows **Active Alert** with a red warning panel. If Tally reaches Shutdown, the run ends immediately with dumpshock.

When Tally crosses a sheaf threshold, the tool pauses normal navigation and shows a **Security checkpoint**.

## Security checkpoints and IC

A checkpoint represents IC or host security pressure that has just entered the scene.

The checkpoint tells you:

- what IC/security event appeared;
- the inferred IC type;
- what that IC generally does;
- what consequence may matter at run end;
- what each response option risks.

The main choices are:

### Suppress / Evade

The safer roll-based option for **White IC only**. Usually needs 1 success. If it works, the checkpoint clears for now, but the IC finds a blank higher Security Tally slot and may return later in the same run.

Grey IC and Black IC cannot be suppressed in the tool; those suppression buttons are disabled. If suppression fails, the IC may become active pressure or, for severe IC, force a run-ending consequence.

### Suppress with Pool

The resource option for **White IC only**. You tie up 1 free Hacking Pool die to suppress the IC without rolling. The IC moves to a blank higher Security Tally slot, and the tied-up die frees when that IC returns.

### Fight IC

The harder direct option. Usually needs 2 successes. On success, the IC is crashed and removed from the ongoing run instead of being reinserted higher on the Security Tally. Failure is riskier.

### Ignore and Continue

You do not roll. For most IC, the threat becomes **active pressure** and adds Tally risk to later tested actions.

For Trace-style threats, ignoring may complete the trace and end the run.

### Jack Out

You try to cut the run short. If successful, the run ends as **Emergency Jack Out**. This is safer than being trapped, but it is not the same as a graceful logoff. If you fail a jackout roll while stuck in the host, the run ends with dumpshock and the GM should resolve consequences as close to SR3 RAW as the table wants.

## Hacking Pool allocations

The app normally auto-adds free Hacking Pool to tested rolls. You do not need to calculate Computer + Hacking Pool every time.

Two choices can reduce your free Hacking Pool for the current run:

- **Pool reserved for DF:** every 2 reserved Hacking Pool dice increases effective Detection Factor by 1, up to +3.
- **Suppress with Pool:** tying up 1 Hacking Pool die suppresses White IC without a roll until that IC returns at its new higher Tally slot.

The tool shows current pool allocations above the crawl when they exist.

## Active pressure

If you ignore or fail to clear some IC, it may become active pressure.

Active pressure stays visible and adds extra risk to later tested actions. If the run ends while active pressure remains, tell the GM.

## Rewards and notes

Some nodes are reward or confirmation nodes. They may say things like:

- customer files are accessible;
- shipping records were found;
- camera network access exists;
- paydata was recovered;
- a permanent order or file change was made.

When the tool says **Tell the GM**, do it. The GM does not automatically know what the tool showed you.

If the tool says to make a personal note, write it down or tell the GM before you forget.

## Permanent outcomes

Permanent outcomes include things like:

- altered records;
- inserted orders;
- disabled or spoofed devices;
- planted files;
- changed access;
- recurring deliveries;
- recovered paydata that needs valuation.

The tool will tell you to notify the GM. Until you do, the table should not assume the outcome has entered the shared fiction.

## Lockouts and retries

A failed route can lock for the current crawl. This means you are blocked right now.

It does not automatically mean the route is impossible forever. After enough in-world time passes, the GM may allow you to reset the crawl and try again, possibly with new prep, tools, credentials, or consequences.

## Ending the run

Keep playing until the tool reaches a final card that says:

> **RUN OVER — ALERT THE GM**

A run can end by:

- graceful logoff;
- emergency jack out;
- objective complete;
- host shutdown / dumpshock;
- failed jackout / dumpshock;
- trace completed;
- ICON crashed / deck damaged;
- black IC harm;
- psychotropic IC consequence.

The final card summarizes:

- final Security Tally;
- recovered or changed outcomes;
- unresolved active threats;
- the final notification text for the GM.

Read that final card to the GM before returning to normal table play.

## What to tell the GM at the end

At minimum, report:

- how the run ended;
- any paydata recovered;
- any permanent changes made;
- any GM-detail prompts you found;
- any active IC or consequences still unresolved;
- whether you logged off cleanly, jacked out, got traced, or crashed.

## Limitations

The Decker Experience is a guided table aid, not a full SR3 Matrix emulator.

It does not fully model every utility, Matrix operation, IC rule, damage track, account privilege, subsystem nuance, or cybercombat option. The GM remains the final authority for exact SR3 rules, modifiers, fiction, and consequences.
