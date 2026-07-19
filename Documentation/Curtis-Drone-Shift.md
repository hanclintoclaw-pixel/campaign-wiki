---
title: Curtis Drone Shift Documentation
type: documentation
visibility: player-safe
updated: 2026-07-19
---

# Curtis Drone Shift Documentation

For daily work-order construction rules, see the [Curtis Drone Shift Work Order Guidelines](Curtis-Drone-Shift-Work-Order-Guidelines.md).

## What it is

[Curtis Drone Shift](https://hanclintoclaw-pixel.github.io/curtis-drone-shift/) is a lightweight downtime minigame for Curtis's drone, vehicle, garage, salvage, and Taco-shop maintenance scenes.

The tool turns a small work order into a staged repair shift. Curtis makes a few skill checks, watches a running nuyen ledger, records maintenance quality, and exports a Discord-ready report for Cindy/GM ingestion.

The goal is not to replace SR3 repair rules or the Drone Dashboard. It is a daily side-quest lane: a quick way to give Curtis something practical and flavorful to do between sessions or during downtime without creating homework or punishment for missed days.

## Who it is for

- **Curtis / Ace Malone:** plays through the active Work Order, makes repair choices, rolls, and posts the final report when finished.
- **GM / Cindy:** reviews the final report, decides whether anything becomes campaign-canon, and ingests the result into memory.
- **Maintainers:** rotate daily Work Orders, keep the tool deployed, and follow the Work Order Guidelines when writing new jobs.

## Live tool and related pages

- Live app: [Curtis Drone Shift](https://hanclintoclaw-pixel.github.io/curtis-drone-shift/)
- Curtis page: [PCs/Curtis](../PCs/Curtis.md)
- Work Order Guidelines: [Curtis Drone Shift Work Order Guidelines](Curtis-Drone-Shift-Work-Order-Guidelines.md)
- Drone roster tracker: [Curtis Drone Dashboard](https://hanclintoclaw-pixel.github.io/drone-dashboard/)

## Current prototype status

Drone Shift is currently a first-draft testing tool. It uses dummy Curtis skill values in the UI and should not automatically mutate drone stats or broader campaign canon.

A final report can recommend a downtime note, nuyen delta, spare part, warning, or possible drone state implication. Small routine nuyen deltas should be applied to Curtis's running total when Cindy ingests the final report; larger payouts/penalties and permanent drone effects require GM confirmation.

## Daily Work Order rotation

A daily cron creates or rotates the active Work Order each morning at **7:00 AM America/New_York**.

Routine behavior:

1. Retire the previous active Work Order.
2. If no report was submitted, treat it as **Discarded / no change / no penalty**.
3. Create the next named Work Order using a short descriptive title, without a `Tutorial N` prefix.
4. Deploy the updated app.
5. Ping Ace Malone in the designated Curtis/Ace channel with the Work Order title and live link.
6. Announce the update in the originating Cindy thread.

This is explicitly a player-engagement prompt, not an obligation. Missed Work Orders should not stack, create debt, or punish the player.

## Table flow

A typical Work Order has 3-6 stages:

1. **Intake** - safe the asset, identify the ticket, and frame the problem.
2. **Diagnosis** - find the real fault or opportunity.
3. **Parts / scrounge** - buy, salvage, improvise, or trade for components.
4. **Repair / fabrication** - perform the core fix.
5. **Calibration / test** - verify that the repair holds.
6. **Closeout** - write the final maintenance note and export the report.

Each stage may have one procedural choice or a small set of meaningful options. Multi-option stages must have real follow-up effects, such as later target-number changes, nuyen swings, quality changes, complication tags, or final-report notes.

## Nuyen ledger

The tool keeps the nuyen movement visible throughout the run:

- **Running total** in the hero area shows the current projected cost or payoff.
- **Shop ledger** repeats the current total and quality label.
- **Success/failure swing cards** show how the selected roll can change the total before the player commits.
- The final report records the total as `Nuyen delta`.

Routine Work Orders should stay close to break-even. Small wins, parts costs, tips, or salvage finds are expected and should be applied to Curtis's running nuyen total during ingestion; large windfalls or penalties should wait for GM approval.

## Quality score

Quality is a temporary maintenance summary, not a permanent drone stat.

The current labels are:

- **Clean shop win** - very strong result, possible minor goodwill/spare-part note.
- **Solid repair** - fixed cleanly.
- **Break-even maintenance** - routine success or acceptable repair.
- **Needs GM review** - possible issue, but no automatic penalty.

Quality helps Cindy/GM interpret the final report. It should not automatically change vehicle or drone stats.

## Final report and ingestion

When Curtis completes a Work Order, the app provides a copyable report beginning with:

```text
@CindyLouBot CURTIS DRONE SHIFT REPORT
```

The report includes:

- job title;
- asset/context;
- status;
- nuyen delta;
- maintenance quality;
- notable work log;
- Cindy ingest/closeout note.

When the report is posted with `@CindyLouBot`, Cindy should:

1. ingest it into campaign memory as a Curtis downtime/maintenance event;
2. mark the active Work Order as **Job Completed**;
3. apply small routine nuyen deltas to Curtis's running total;
4. avoid permanent drone stat changes unless the GM confirms them;
5. preserve useful notes for future Work Orders or drone continuity.

## Relationship to the Drone Dashboard

The [Curtis Drone Dashboard](https://hanclintoclaw-pixel.github.io/drone-dashboard/) is the canonical session tracker for Curtis's drones and vehicles. It tracks units, damage, equipment, weapons, ammo, notes, and persistence requests.

Drone Shift is different. It is a daily guided downtime prompt. It may mention assets from the Drone Dashboard, but it should not automatically write back to the dashboard. If a Work Order result should become canonical, Cindy/GM should review the final report and then update the dashboard/wiki through the normal persistence workflow.

## Relationship to SR3 rules

Drone Shift is SR3-inspired but simplified. It uses Curtis-relevant skills and target numbers to create quick repair beats. The GM can override target numbers, skill use, costs, timing, or consequences whenever SR3 RAW or the live scene demands it.

The app should keep repair play moving, not become a full build/repair subsystem.

## Maintaining the tool

Source repo:

```text
/Users/hanclaw/claw/projects/cindylou/curtis-drone-shift
```

Public repo:

```text
hanclintoclaw-pixel/curtis-drone-shift
```

Validation before deploy:

```sh
npm run lint
npm run build
```

Deployment uses GitHub Pages through the repo's `deploy.yml` workflow. After pushing changes, wait for Pages to deploy and verify the live app serves the new bundle.

## Limitations

Current limitations:

- only the current active Work Order is implemented in the app;
- dummy skill values are shown until a better Curtis data sync/import exists;
- no automatic Drone Dashboard writeback;
- no automatic campaign-memory ingestion until Curtis posts the final report and pings Cindy;
- daily Work Order generation is still template-driven and may need manual tuning;
- missed Work Orders are intentionally discarded rather than queued.

The useful mental model is: **daily garage spotlight lane**. It gives Curtis a small, tactile workshop scene and a little nuyen/quality movement while leaving canon authority with the GM.
