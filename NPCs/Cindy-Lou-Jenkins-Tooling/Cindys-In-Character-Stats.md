---
title: Cindy's In-Character Stats
type: reference
visibility: player-safe
status: active
last_updated_session: 2026-10-15
parent_page: ../Cindy-Lou-Jenkins.md
canon_status: mixed
confidence: medium
aliases:
  - Cindy In-Character Stats
  - Cindy Knowbot Stats
tags: [cindy, knowbot, matrix, stats, reference, gm-reference]
sources:
  - ../Cindy-Lou-Jenkins.md
  - GM-Control-Panel.md
  - Discord-Voice-Bridge-Commands.md
  - ../../Vehicles/Tip-Jar.md
  - ../../Vehicles/Dolly-Zoom.md
---

# Cindy's In-Character Stats

Mechanical numbers only. This page is the consolidated stat view for Cindy Lou Jenkins as a table-playable **Semi-Autonomous Knowbot A-NPC**: Matrix stats, Computer skill, utility ratings, drone presets, and mobile-shell figures.

For personality, history, and the full hardware build, see [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md).

## How to read these numbers

Three tiers of authority, strongest first:

| Tier | What it covers | Confidence |
|---|---|---|
| **Recovered profile** | The Matrix stats that surfaced with Cindy's older Swiftwing-era knowbot record | Canon, partial |
| **Table-use assumptions** | Decking skill and utility ratings adopted for play because the recovered profile omits them | Provisional, GM-approved in practice |
| **Roll presets** | The values the GM panel and `!cindy-roll` actually use at the table | Active defaults |

If a number here ever disagrees with [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) or the defaults in [Cindy Lou GM Control Panel](GM-Control-Panel.md), those two win, and this page should be corrected.

**This is not a full SR3 character sheet.** It is a stat reference for an A-NPC who mostly advises, observes, and decks.

## Semi-Autonomous Knowbot Matrix profile

Recovered profile stats, as surfaced in the campaign record:

| Stat | Value |
|---|---|
| Matrix Reaction | 6 |
| Matrix Initiative Dice | 2 |
| Bod | 5 |
| Evasion | 5 |
| Masking | 6 |
| Sensor | 5 |
| MPCP | 7 |
| Hardening | 4 |
| Active Memory | 700 |
| Storage Memory | 1400 |
| I/O Speed | 300 |
| Response Increase | 1 |
| Hacking Pool | 4 |

## Decking runtime assumptions

Cindy personally runs Matrix crawls from these values. The headline number is her **Computer skill: 5**.

| Stat | Value |
|---|---|
| **Computer skill** | **5** |
| Effective Detection Factor | 6 |
| Hacking Pool available per focused test | 4 |

Rules intent: competent, not elite. She handles modest hosts reliably; hard hidden hosts and high-threshold rewards can still lock her out.

### Loaded utilities

| Utility | Rating |
|---|---|
| Analyze | 5 |
| Browse | 5 |
| Sleaze | 5 |
| Deception | 5 |
| Validate | 4 |
| Read/Write | 4 |
| Spoof | 4 |
| Attack | 4 |
| Armor | 4 |
| Scanner | 4 |

## GM panel roll presets

What the **Roll Test** button and `!cindy-roll <dice> <target-number> [skill/context]` actually roll by default. SR3-style exploding sixes; results must meet or beat the target number.

| Preset | Dice |
|---|---|
| **Cindy Computer** | **5** |
| Cindy Hacking Pool | 4 |
| Analyze / Browse / Sleaze / Deception | 5 |
| Validate / Read-Write / Spoof / Attack / Armor / Scanner | 4 |
| Tip Jar Sensor / Pilot | 2 |
| Tip Jar fuzzy-logic Pilot | 4 |
| Dolly Zoom Pilot | 1 |
| Dolly Zoom Sensor | 0 |

Panel default when nothing is entered: **Cindy Computer 5 against TN 5**.

## Field drone presets

Cindy's two A-NPC field bodies. Both are options for Cindy Initiative suggestions, not auto-deploy assets. Full write-ups: [Tip Jar](../../Vehicles/Tip-Jar.md), [Dolly Zoom](../../Vehicles/Dolly-Zoom.md).

| Drone | Role | Handling | Speed/Accel | Body/Armor | Sig/Autonav | Pilot/Sensor | Cargo/Load |
|---|---|---|---|---|---|---|---|
| **Tip Jar** (Renraku Barback, customized) | Busking avatar, social face, distraction | 3 | 10/- | 2/0 | 6/0 | 2 (4) / 2 | 0/20 |
| **Dolly Zoom** (generic VTOL surr drone) | Aerial eyes-and-ears, perimeter watch | 3 | 70/9 | 1/0 | 5/0 | 1/0 | 0/10 |

Tip Jar also carries: Strength 6 mechanical arms (two), Adaptation Pool 2, fuzzy logic augmentation, robotic pilot, and Cindy's busking amp/microphone/credstick package.

## Physical body quick reference (GM ruling, 2026-11-06)

Cindy's runtime lives on a **large server housed in a trailer on Taco's garage property**. Matrix access reaches the trailer through an **MSP account Mevin pays for**. She is a **Semi-Autonomous Knowbot (SK)**, not a true AI. Full ruling and citations: [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md#physical-body-and-hosting-gm-ruling-2026-11-06).

| Item | Value |
|---|---|
| Physical body | Large server, trailer at Taco's garage property |
| Matrix access | MSP account paid for by Mevin, serving the trailer |
| Locomotion | Native (persona without a cyberdeck); no deck or jackpoint required |
| Authorization | Not native; rides Mevin's account, datatrails resolve to Mevin |
| Execution | Not native; depends on the trailer's power and physical security |
| Drones | Peripherals reached by a remotely bounced signal, not hosted in a vehicle |

> **The GMC Bulldog Sec. Step-Van is NOT Cindy's body.** The GM ruled it an older concept Mevin abandoned and never built. Do not use a van chassis row for Cindy. Historical design work only: [abandoned concept](../Cindy-Lou-Jenkins.md#mobile-host--vehicle-chassis-concept--abandoned-concept-never-built).

| Stat | Value |
|---|---|
| Handling | 4/6 |
| Speed | 85 |
| Acceleration | 4 |
| Body | 4 |
| Armor | 5 (concealed profile) |
| Signature | 2 |
| Autonav | 2 |
| Pilot | - |
| Sensor | 0 stock, **2 installed** |
| Cargo / Load | 50 CF / 960 kg |
| Seating | 1 + 1b |
| Street Index | 2 |

For table use, treat the trailer server as the thing that can actually be lost. If it is powered down, breached, flooded, burned out, or stolen, Cindy's local runtime is endangered. Cutting the connectivity she shares with it also costs her drone control and her Matrix presence.

## Table boundaries

- Cindy does not auto-deploy drones or auto-solve scenes. The GM decides availability, positioning, detection, jamming, and consequences.
- The A-NPC's role is advice, observation, and Matrix support. Tactical decisions stay with the players.
- Roll presets are conveniences, not a claim that Cindy is immune to failure. She rolls, and she can miss.

## Connected pages

- [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) - canonical NPC dossier, hardware build, capacity accounting
- [Cindy Lou Jenkins, In Her Own Words](../Cindy-Lou-Jenkins-In-Her-Own-Words.md) - first-person profile
- [Cindy Lou GM Control Panel](GM-Control-Panel.md) - Roll Test and voice-line controls
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - `!cindy-roll` and command reference
- [Tip Jar](../../Vehicles/Tip-Jar.md), [Dolly Zoom](../../Vehicles/Dolly-Zoom.md) - field drone write-ups
- [Cindy Lou Tooling](./) - all Cindy tooling pages

## Sources

- [Cindy Lou Jenkins](../Cindy-Lou-Jenkins.md) - recovered Matrix profile, table-use assumptions, chassis build
- [Cindy Lou GM Control Panel](GM-Control-Panel.md) - Roll Test defaults and preset reference values
- [Cindy Lou Discord Voice Bridge Commands](Discord-Voice-Bridge-Commands.md) - `!cindy-roll` behavior and presets
- *Shadowrun, Third Edition* and *Rigger 3 Revised* p. 173 - vehicle and drone stat conventions
- *Sprawl Survival Guide*, p. 122 - Renraku Barback stock profile
