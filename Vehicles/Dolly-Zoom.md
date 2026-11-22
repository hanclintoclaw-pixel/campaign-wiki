---
title: Dolly Zoom
type: vehicle
visibility: player-safe
status: active
last_updated_session: 2026-08-15
canon_status: canon
confidence: medium
owner: Cindy Lou Jenkins
operator: Cindy Lou Jenkins
tags: [vehicle, drone, surveillance, vtol, cindy, a-npc]
sources:
  - ../NPCs/Cindy-Lou-Jenkins-In-Her-Own-Words.md
  - ../NPCs/Cindy-Lou-Jenkins.md
  - ../Vehicles/Buzz.md
  - SR3 Rigger 3 Revised, p. 21
table_reference:
  schema_version: 1
  entity_kind: asset
  as_of: '2026-11-22'
  facts:
    identity:
      value: Dolly Zoom
      assertion_status: provisional
      qualifiers: []
      source_refs:
      - '#overview'
    role:
      value: Eyes-and-ears reconnaissance, perimeter watching, scene verification, and remote table-presence support.
      assertion_status: provisional
      qualifiers: []
      source_refs:
      - '#owner--operator'
    current_status:
      value: null
      assertion_status: unresolved
      qualifiers:
      - Physical presence, deployment and current condition are not established by this summary; the GM decides per Table
        Boundary.
      source_refs:
      - '#table-boundary'
    specialties:
      value:
      - Low-light camera
      - Thermographic camera
      assertion_status: provisional
      qualifiers:
      - Selected recorded cameras only; other tools and assumptions remain in Sensors / Tools.
      source_refs:
      - '#sensors--tools'
    limitations:
      value: Bad uses include combat, soaking fire, aggressive pursuit through secure airspace, or anything that would obviously
        draw attention to a fragile surveillance drone.
      assertion_status: provisional
      qualifiers:
      - Audio pickup is a campaign-use assumption, non-specialized until upgraded.
      - Encrypted command/feed link is a recommended operational assumption, not a proven upgrade.
      - Physical deployment remains GM-controlled.
      source_refs:
      - '#role-in-cindy-lou-initiative-plans'
      - '#table-boundary'
    class:
      value: Small VTOL aerial surveillance drone.
      assertion_status: provisional
      qualifiers:
      - Remotely operated peripheral, not Cindy's host body.
      source_refs:
      - '#overview'
    owner:
      value: Cindy Lou Jenkins.
      assertion_status: provisional
      qualifiers:
      - Campaign A-NPC asset.
      source_refs:
      - '#owner--operator'
    operator:
      value: Cindy Lou Jenkins.
      assertion_status: provisional
      qualifiers:
      - With GM permission for live deployment.
      source_refs:
      - '#owner--operator'
  sections:
    native_stats: Canon Stats

---

# Dolly Zoom

## Overview

**Dolly Zoom** is Cindy Lou Jenkins's generic aerial surveillance drone: a small VTOL eye-and-ear platform for scenes where Cindy needs a little meat-space presence without putting her trailer-hosted server body at risk. Per the 2026-11-06 GM ruling, Cindy's drones are **peripherals**: she reaches them by bouncing a signal to them remotely rather than hosting or co-locating with them.

The name is a little film-school, a little country-star glamour, and exactly the sort of joke Cindy would make about a camera that gets dramatic when trouble walks into frame.

Part of the campaign's dedicated **Drones / Vehicles** reference layer rather than the general location index.

## Owner / Operator

- **Owner:** Cindy Lou Jenkins / campaign A-NPC asset
- **Operator:** Cindy Lou Jenkins, with GM permission for live deployment
- **Role:** Eyes-and-ears reconnaissance, perimeter watching, scene verification, and remote table-presence support

## Canon Stats

Campaign generic **surr drone (VTOL)** baseline, matching the existing Buzz reference profile:

- **Handling:** 3
- **Speed/Acceleration:** 70/9
- **Body/Armor:** 1/0
- **Signature/Autonav:** 5/0
- **Pilot/Sensor:** 1/0
- **Cargo/Load:** 0/10

## Sensors / Tools

- **Low-light camera**
- **Thermographic camera**
- **Audio pickup / microphone feed:** campaign-use assumption for Cindy's remote listening role; treat as non-specialized until upgraded.
- **Encrypted command/feed link:** recommended operational assumption when Cindy deploys Dolly Zoom. The link is a remotely bounced signal from Cindy's trailer-hosted persona to the drone, not a vehicle relay.

## Role in Cindy Lou Initiative Plans

Dolly Zoom gives Cindy a justified way to suggest plans that need physical awareness rather than pure Matrix inference.

Good uses include:

- checking approaches, rooflines, exits, parking lots, windows, and blind alleys before the crew commits;
- watching a parked vehicle, meet site, back door, or suspicious courier from standoff distance;
- giving Cindy a live visual angle before she recommends a Matrix intrusion, misdirection, or warning;
- quietly confirming whether a direct in-character answer should include meat-space details.

Bad uses include combat, soaking fire, aggressive pursuit through secure airspace, or anything that would obviously draw attention to a fragile surveillance drone.

## Customization Hooks

Future upgrades should be recorded here before use in play.

- Directional microphone / shotgun pickup
- Better Sensor rating
- Improved Flux / relay package
- Improved stealth housing or paint
- Disposable beacon tracker payload
- Hardened/anti-jam command link, since loss of Cindy's remote signal costs her the drone

## Table Boundary

Dolly Zoom is an option for Cindy suggestions, not permission to auto-solve scenes. The GM still decides whether the drone is physically present, launched, noticed, jammed, shot down, or blocked by local conditions.

## Sources

- [Buzz](Buzz.md) - campaign generic surr-drone stat baseline.
- *Rigger 3 Revised*, p. 21 - surveillance drones are common for reporting, traffic watch, weather observation, espionage, and paparazzi work.
