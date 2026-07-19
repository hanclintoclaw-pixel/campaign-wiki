---
title: Curtis Drone Shift Work Order Guidelines
type: documentation
visibility: player-safe
updated: 2026-07-19
---

# Curtis Drone Shift Work Order Guidelines

These guidelines define the routine structure for [Curtis Drone Shift](https://hanclintoclaw-pixel.github.io/curtis-drone-shift/) work orders. Use them when creating daily drone, vehicle, shop, salvage, or Taco's mechanical side quests for Curtis.

The goal is a short, fun downtime prompt that keeps Curtis's player connected to the campaign without turning daily maintenance into homework. A missed work order should rotate out quietly as **Discarded / no change / no penalty**.

## Design goals

A good Drone Shift work order should:

- take about 3-6 staged steps;
- use Curtis-relevant skills such as Electronics, Electronics B/R, Car B/R, Rotor Aircraft B/R, Vector Thrust Aircraft B/R, vehicle skills, Etiquette, or a fitting Knowledge skill;
- hover near break-even by default;
- offer small nuyen movement, usually around -¥100 to +¥200 unless the GM explicitly wants bigger stakes;
- create texture for Curtis's drones, Taco's shop, Grandpa, salvage bins, or campaign logistics;
- produce a final Discord-ready report Cindy can ingest;
- avoid automatic permanent drone stat changes unless the GM confirms them.

## Standard work order shape

Each work order should have:

1. **Descriptive title** - for example, `Grandpa's Back-Step Rattle`; do not prefix new work orders with `Tutorial N`.
2. **Asset/context** - the drone, vehicle, shop fixture, customer item, or salvage lot involved.
3. **Hook** - one paragraph explaining the weird noise, failure, opportunity, or customer request.
4. **Baseline expectation** - usually break-even, no penalty if ignored, and no canon mutation until reported.
5. **Stages** - a small chain of work cards.
6. **Nuyen ledger** - immediate step-by-step cost/payoff and a prominent running total.
7. **Final report** - a copyable `@CindyLouBot CURTIS DRONE SHIFT REPORT` with rolls, nuyen delta, quality, and ingestion note.

## Recommended stages

Use 3-6 of these, in order. Not every work order needs every stage.

| Stage | Purpose | Common skills |
| --- | --- | --- |
| Intake | identify the ticket, safe the asset, define the risk | Electronics, vehicle skill, Etiquette |
| Diagnosis | find the actual fault or hidden opportunity | Electronics, Knowledge, B/R skill |
| Parts / scrounge | decide whether to salvage, buy, trade, or improvise | B/R skill, Negotiation, Etiquette |
| Repair / fabrication | perform the core fix | relevant B/R skill |
| Calibration / test | verify the result under safe load | vehicle/drone B/R, vehicle skill |
| Closeout | write the maintenance note and final report | Electronics, Knowledge, Etiquette |

## Daily choice cadence

Going forward, each daily Work Order should normally include **1-2 stages with multiple options** for Curtis to choose from. These should be small, concrete shop tradeoffs rather than big branching quests: buy fresh or scrounge, tune safe or tune spicy, patch fast or take the proper teardown, ask Taco for a favor or keep it quiet.

Default cadence:

- **3-stage Work Order:** include 1 multi-option stage.
- **4-6 stage Work Order:** include 1-2 multi-option stages.
- **Occasional complex Work Order:** rarely, use 3 multi-option stages or one stage with 3 choices when the job is meant to feel unusually fussy, but keep the consequences in the normal small risk/reward band.

Even when spicing up a ticket, keep the total expected movement close to break-even. The point is to give Curtis a little agency and workshop texture, not to turn the daily prompt into a major income engine, punishment track, or full repair subsystem.

## Single-choice stages

Use a single choice when the stage is mostly procedural: there is one obvious way to continue, and the roll determines only how cleanly it goes.

Single-choice stages are best for:

- intake and safety checks;
- ordinary diagnosis;
- simple cleanup;
- final documentation;
- low-stakes calibration.

A single-choice roll should still matter. It should change at least one of:

- nuyen delta;
- quality score;
- final report text;
- a later target number;
- whether a minor complication appears.

Example:

```text
Stage: Diagnose the coolant chirp
Choice: Run a careful bench diagnosis
Success: identify the failing pump bearing early; +1 quality; next Repair TN -1
Failure: identify the pump late after wasting a seal kit; -¥35; no TN bonus
```

## Multiple-choice stages

Use multiple options when Curtis is making a real tradeoff. Every option must have a follow-up effect later in the work order. Do not offer a choice that only changes flavor text.

At least one stage per daily Work Order should usually use this structure, and two is preferred when the ticket has enough room. Most choices should have two options; three-option stages are reserved for occasional higher-complexity tickets.

Good multi-choice tradeoffs include:

- **Scrounge vs buy fresh parts** - scrounge has better payoff but higher test risk; fresh parts cost more but reduce later TN or prevent a complication.
- **Fast patch vs proper teardown** - fast patch saves time or nuyen but creates a final-test penalty; proper teardown costs more but improves quality.
- **Tune for reliability vs performance** - reliability reduces future complication risk; performance increases payoff but raises failure consequences.
- **Call in a favor vs keep it in-house** - favor reduces cost or TN now but adds a social note for Cindy/GM.
- **Customer-facing repair vs hidden shop fix** - customer-facing may earn tip/goodwill; hidden fix may protect secrets or avoid attention.

## Required follow-up effects for multiple choices

Every multi-choice option should set or imply at least one concrete modifier that affects a later stage. Use plain language in the card so the player understands the tradeoff.

Allowed follow-up effects:

- later target number modifier, usually -1 or +1;
- later required-success modifier, usually -1 or +1;
- later nuyen modifier;
- later quality modifier;
- complication tag that changes final-report language;
- unlock or suppress a later action option;
- change what the final report asks Cindy/GM to ingest.

Avoid stacking too many effects. One strong effect or two small effects is enough.

Example multi-choice stage:

```text
Stage: Repair or replace the rotor shim
Option A: Scrounge a donor shim
Immediate: +¥60 if successful, -¥45 if failed
Follow-up: Test Run TN +1 because the part is improvised

Option B: Use fresh parts
Immediate: -¥20 if successful, -¥75 if failed
Follow-up: Test Run TN -1 because the fit is clean
```

The key is that the later Test Run actually reads the selected flag and changes its target number. If the app cannot enforce that yet, the work order text should not imply it does.

## Work order state tags

When the app supports it, use simple internal tags to carry choices forward. Suggested tags:

- `freshParts` - lowers later test risk, costs nuyen now.
- `scroungedParts` - improves payoff, raises later test risk.
- `rushJob` - saves immediate cost/time, worsens final quality/test.
- `properTeardown` - costs now, improves quality/test.
- `customerGoodwill` - adds final report note or small payoff.
- `hiddenDamage` - adds final report warning and possible GM follow-up.
- `salvageFind` - adds small payoff or future spare-part note.

Tags should be visible enough that the final report can explain why the result changed.

## Nuyen and quality guidance

Routine work orders should stay small. The player should feel the ledger move, but the daily side quest should not become a major income engine or major punishment.

Recommended values:

- procedural success: ¥0 to +¥25;
- procedural failure: ¥0 to -¥35;
- good salvage/scrounge success: +¥40 to +¥120;
- fresh parts cost: -¥20 to -¥100;
- customer tip/goodwill: +¥25 to +¥100;
- unusual GM-approved windfall: +¥150 to +¥300.

Quality is an abstract tool rating, not a permanent drone stat. Use it to describe the final outcome:

- **6+ Clean shop win** - worth noting, possible small goodwill/spare-part benefit.
- **3-5 Solid repair** - fixed cleanly, no follow-up needed.
- **0-2 Break-even maintenance** - fixed enough, routine note only.
- **Below 0 Needs GM review** - no automatic penalty; final report asks GM whether anything matters.

## Discarding untouched work orders

If the daily cron rotates a work order and the previous one was not completed or reported, mark it conceptually as:

```text
Discarded: no change, no nuyen movement, no drone state change, no penalty.
```

Then remove it from the active app/page and publish the next named work order. Do not shame the player, stack missed jobs, or create debt from ignored prompts.

## Final report requirements

Every work order must end with a copyable report containing:

- job title;
- asset/context;
- completion status;
- final nuyen delta;
- final quality label/score;
- notable roll log;
- selected tradeoff tags or follow-up effects;
- Cindy ingest note.

Suggested closing line:

```text
Cindy ingest note: Add this as a Curtis downtime/maintenance event. Apply small routine nuyen deltas to Curtis's running total, but do not apply permanent drone stat changes unless the GM confirms them.
```

## Daily generation checklist

When creating a new daily work order:

1. Pick a short descriptive title that fits the specific shift; do not add a Tutorial number.
2. Retire the previous active order as Discarded / no change / no penalty if no report was submitted.
3. Pick one asset or context: a drone, Grandpa, Taco's shop, salvage, customer repair, or field-prep task.
4. Write a hook with one concrete sensory detail.
5. Build 3-6 stages.
6. Include 1-2 multi-choice stages by default; use a third or a three-option stage only as an occasional more-complex ticket.
7. If any stage has multiple options, make every option affect a later stage or final report.
8. Keep nuyen near break-even.
9. Keep the running nuyen total prominent.
10. End with a Cindy/GM ingest report.

## Common work order seeds

- Buzz has battery swelling or a rotor hum.
- Belmont's track tension is drifting.
- The Finisher needs a feed-path cleaning after dust exposure.
- Mr. Clean swallowed a screw and sounds proud of it.
- Waddles has sensor gunk under the synthetic fur.
- Grandpa has an electrical rattle behind a modified dwarf-height control panel.
- Taco's walk-in cooler fan is making a bad bearing noise.
- A customer brings in a dead courier drone with one suspiciously expensive intact part.
- A scrap lot has two bad drones and maybe one good sensor package.
- Field prep reveals a cracked battery clip before a run.

## Tone

The tone should be practical, greasy, and a little funny. Curtis is competent; the tool should give him satisfying little workshop beats, not make him look foolish. Complications should be ordinary shop problems: stripped screws, brittle tabs, mystery grease, bad connectors, missing receipts, cheap aftermarket parts, or Taco yelling from the kitchen.
