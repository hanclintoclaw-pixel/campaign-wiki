---
title: Barrage 1918 Host
type: matrix-host
visibility: player-safe
status: active
canon_status: provisional
confidence: medium
last_updated_session: 2026-07-24
tags: [matrix, host, nashville, restaurant, barrage-1918, sr3, green-host]
sources:
  - GM direction 2026-07-24
  - /Volumes/carbonite/claw/data/cindylou/cleaned/memory/00_sources/rules_references/sourcebooks/SR3_Matrix_7909/source.md
---

# Barrage 1918 Host

## Overview

The **Barrage 1918 Host** is the public reservations, menu, publicity, and house-security Matrix host for **Barrage 1918**, a themed upscale restaurant whose rotating menus are associated with historical wars. The public sculpting sells theater: candlelit officer clubs, trench-map table diagrams, gilded campaign menus, polished museum captions, and celebrity endorsements from people who want to be seen eating somewhere expensive and clever.

The Host is a [machine-readable Decker Experience profile](../../data/matrix-hosts/barrage-1918-host.json). Its public side is restaurant-facing and harmless. The secure side contains routine paydata, security systems, and one private-event planning file whose actual contents are intentionally labeled **Ask GM**.

## SR3 Rules Model

Use normal SR3 Matrix host assumptions:

- Treat the system as a **Green-6 host**: a legal commercial host with a relatively approachable security code, but with enough rating and money behind it to make careless intrusion risky.
- Decker operations use the relevant subsystem rating as the base target number, adjusted by access route, alert state, legitimate credentials, utilities, and GM modifiers.
- Green hosts should lean toward Probe, Trace, Scramble, Tar Baby, passive alert, and human/security escalation rather than lethal IC.
- Black IC is not part of the normal Barrage 1918 security posture. If Black IC appears here, it is evidence of outside tampering or a hidden third-party asset.
- Paydata should be mundane restaurant/business data, not corporate-vault loot. Each listed paydata store is worth **1 Paydata Point** by default unless the GM says otherwise.

## Host Stats (SR3-style)

- **Host Color / Security:** Green-6
- **Host Rating:** 6
- **Shutdown Tally:** 21
- **Access:** 6
- **Control:** 6
- **Index:** 5
- **Files:** 6
- **Slave:** 6
- **Typical IC mix:** Probe-5/6, Trace-5/6, Scramble-5, Tar Baby-5, alarm/notification routines to restaurant security
- **IC not normally present:** Black IC, psychotropic IC, military-grade killer suites, or lethal gray constructs
- **Routine decker task TNs:**
  - Browse public menus, hours, reservation policy, and public endorsements: **4**
  - Log on through ordinary public customer paths: **4**
  - Break into secure staff/management access: **6**
  - Search staff records, event ledgers, vendor records, or guest histories: **6**
  - Reach or command security/device systems: **6**
  - Locate the private-event planning file: **6**, **2 successes** in the Decker Experience profile
  - Evade trace / leave under pressure: **6**

## Decker Experience profile

- **Profile ID:** `barrage-1918-host`
- **Name:** Barrage 1918 Host
- **Security code:** Green
- **Security value:** 6
- **Shutdown Tally:** 21
- **Default tool tuning:** With default tool stats (**Computer 8 + Hacking Pool 6 = 14 dice**), the main clue route requires two key checks: secure entry at **TN 6 / 2 successes** and private-event file access at **TN 6 / 2 successes**. Each check is about 70.4% by raw binomial odds, so reaching the **Ask GM** private-event clue through the direct route is about **49.6%** before table choices, IC handling, or manual advantages.

## What deckers find inside

Public routes expose ordinary restaurant-facing material:

- historical-war themed tasting menus and wine/cocktail pairings;
- public reservation rules, private dining packages, and dining-room dress codes;
- endorsements, critic quotes, sanitized celebrity visits, and curated social feeds;
- museum-like historical blurbs that are theatrical, polished, and aggressively non-secret.

Private or staff-side routes can reveal:

- VIP spend ledgers and comp history;
- procurement and rare-bottle/vendor records;
- staff tip-out, payroll-adjacent, and disciplinary fragments;
- security-camera, reservation-door, kitchen-access, panic-button, and private-room device clusters;
- a hidden private-event planning file marked **Ask GM** for the actual specifics.

## Host feel

The public sculpting feels like walking through a prestige war museum rebuilt as a restaurant: polished brass, map tables, menu cards, campaign medals, old uniforms behind glass, and tasteful theatrical smoke curling through dining rooms named after battlefields. Public search results appear as menu cards, endorsement plaques, reservation ledgers, and maître d' note cards.

The secure side gets colder and more practical. Staff files look like locked wine cellars, officer's safes, requisition crates, clipboard manifests, and security-room wall maps. Security pressure manifests as museum lights dimming, velvet ropes sliding into place, and a host icon in formal servicewear asking why the decker is beyond the dining room.

## Iconography

- **Access:** reservation desk, maître d' stand, velvet rope, staff corridor.
- **Control:** cameras, private-room locks, kitchen pass, panic buttons, door chimes, reservation terminals.
- **Index:** menu cards, campaign maps, endorsement plaques, guest ledgers.
- **Files:** wine ledgers, staff binders, event folders, procurement crates, officer's safes.
- **Slave:** camera lenses, lock plates, kitchen screens, service bells, alarm buttons.
- **Probe IC:** a maître d' icon checking the decker's reservation.
- **Trace IC:** a red wax seal stamping the decker's route back through the reservation book.
- **Scramble IC:** menu cards reshuffling dates, guest names, and event notes into unusable historical trivia.
- **Tar Baby IC:** velvet ropes and polished brass stanchions trying to hold the icon in place.

## Security Sheaf (SR3-style)

Use this as a prepared Green-host sheaf guideline. Adjust if the live table already has a Security Tally in motion.

| Tally | Event |
| ---: | --- |
| 3 | Probe-5 checks the icon, credentials, and apparent reservation status. |
| 6 | Trace-5 starts through reservation and LTG routing records. |
| 9 | Scramble-5 threatens copied ledgers, menus, and event files with noisy historical filler. |
| 12 | Passive Alert: velvet-rope lockdown mood; restaurant security may become quietly aware. |
| 15 | Tar Baby-5 attempts to hold the intruder for security follow-up. |
| 18 | Active Alert: management/security receives an actionable intrusion warning. |
| 21 | Host shutdown sequence begins; resolve per SR3 host shutdown / dump-shock guidance if the decker remains online. |

## Paydata Guidance

Each mundane paydata store below is worth **1 Paydata Point** by default:

- VIP spend ledger;
- rare-bottle / procurement records;
- staff tip-out and disciplinary fragments.

This data is useful but not explosive. It may identify wealthy regulars, vendor pressure, staffing problems, or blackmail-adjacent restaurant gossip, but it should not become a major campaign reveal unless the GM explicitly upgrades it.

## Private Event File

The hidden private-event planning file is the Host's main GM-facing clue. The profile labels it **Ask GM**. If Mevin reaches it, tell the GM he found the private-event planning file and ask for specifics.

## Related Pages

- [Matrix Host Construction Guide](Host-Construction-Guide.md)

## Sources

- GM direction, 2026-07-24.
- *Matrix* (SR3), host security/alert/shutdown/paydata guidance, local source file listed in front matter.
