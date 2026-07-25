---
title: H-Block Crew Vanishing SAN Host
type: matrix-host
visibility: player-safe
status: active
canon_status: table-created
confidence: medium
last_updated_session: 2026-07-25
tags: [matrix, host, h-block-crew, gang, ork, vanishing-san, paydata]
sources:
  - GM/table-created host request on 2026-07-25
  - Mevin Host Run Simulator seed profile
---

# H-Block Crew Vanishing SAN Host

## Overview

A low-tech Matrix host run by the **H-Block Crew**, a primarily ork-based street gang that mixes small-time Matrix crime with for-hire meat-space actions. The host sits behind a **vanishing SAN**: the access path is not impossible to find, but it appears only in short, dirty windows among local LTG noise, burner aliases, and gang-tag chatter.

The profile below mirrors the current seed profile used by the [Mevin Host Run Simulator](https://hanclintoclaw-pixel.github.io/mevin-host-run-simulator/) and has a [machine-readable host profile](../../data/matrix-hosts/h-block-crew-vanishing-san-host.json) for Matrix minigame tools, including the [Mevin Decker Experience](https://hanclintoclaw-pixel.github.io/mevin-decker-experience/).

## Host Stats (SR3-style)

- **Host Color / Security:** Green-6
- **Host Rating:** 6
- **Access:** 4
- **Control:** 4
- **Index:** 4
- **Files:** 5
- **Slave:** 3
- **Typical IC mix:** Probe, Trace, Tar Baby, Killer/Blaster-style attack IC, Gray IC, and one terminal Black IC event at the end of the sheaf
- **Routine decker task TNs:**
  - Catch the vanishing SAN window: **5**
  - Log on through the private gang door: **4**
  - Analyze host structure or gang-tag routing: **4**
  - Search routine private files, ledgers, and message drops: **4-5**
  - Copy ordinary paydata chunks: **5**
  - Spoof minor controls or burner-account functions: **5**
  - Evade trace or suppress local alarm pressure: **5**
  - Open the bottom-level **Secure Stash** alias: **6**, **2 successes**

## Host Run Simulator profile

- **Profile ID:** `h-block-crew-vanishing-san-host`
- **Name:** H-Block Crew Vanishing SAN Host
- **Security code:** Green
- **Security value:** 6
- **Subsystems:** Access 4, Control 4, Index 4, Files 5, Slave 3
- **IC rating:** 6
- **Sculpting:** A flickering block-party alley host: cinderblock walls, tagged roll-up doors, stolen utility crates, burner-phone shrines, and a vanishing back door that only appears when the gang's tag animation finishes stuttering.
- **Simulator notes:** Low-tech H-Block Crew resource host. Easy private-side TNs and mostly one-success gates, but the Security Tally escalates into serious IC if a decker lingers.

## What deckers find inside

- burner-account settlements, street payroll notes, and short-lived job receipts
- chop-shop parts lists, stolen gear ledgers, and barter/value notes
- for-hire action fragments, lookout rosters, and meat-space errand trails
- gang-tag chatter, neighborhood bragging, and low-grade Matrix vandalism tools
- up to **5 Paydata Points** split across four recoverable chunks:
  - **Chop-Shop Parts Ledger** - 1 Paydata Point
  - **Burner Account Settlements** - 1 Paydata Point
  - **Street Payroll Scraps** - 1 Paydata Point
  - **Corporate Hire** hidden under the alias **Secure Stash** - 2 Paydata Points, bottom of the host

## Host feel

This is not a polished corporate environment. It feels like a gang resource welded together from stolen admin tools, cracked utilities, recycled host code, and stubborn local knowledge. The private side is not hard to enter once the vanishing SAN is caught; the danger is staying too long while the host's crude but nasty IC wakes up.

The host rewards fast, decisive decking. A quiet decker can get in, grab ledgers, and leave. A greedy decker who keeps digging will find the system's defenses disproportionate to its cheap exterior.

## Iconography

- the vanishing SAN appears as a **spray-painted alley door** that flickers in and out of the LTG wall
- private directories appear as **tagged cinderblock bays, dented lockers, phone crates, and milk crates full of receipts**
- ordinary paydata appears as **oil-stained binders, cracked credstick jars, and stolen parts tags**
- **Secure Stash** appears as a mislabeled, grime-caked lockbox at the bottom of a freight-elevator shaft
- IC manifests as **lookouts, chain dogs, masked debt collectors, shock-glove bruisers, gray-faced enforcers, and one black-armored executioner icon**
- alerts make the alley close in: shutters slam, watchers whistle, and every tag starts pointing at the intruder

## Decker use

Useful for learning who has hired the H-Block Crew, where their money and gear are moving, what street jobs they recently accepted, and whether a corporate patron is using them as disposable muscle.

<details>
<summary>GM Information only - reward notes</summary>

Prepared reward structure:

- **Chop-Shop Parts Ledger:** mundane 1-point paydata; stolen parts, buyers, and parts-flow timing.
- **Burner Account Settlements:** mundane 1-point paydata; credstick cash-out patterns, burner Matrix accounts, and payment intermediaries.
- **Street Payroll Scraps:** mundane 1-point paydata; lookout payments, crew stipends, errand payouts, and short-term job receipts.
- **Corporate Hire / Secure Stash:** session-specific 2-point paydata hidden under the alias **Secure Stash** at the bottom of the host. This is the only prepared node requiring more than 1 success. If recovered, the GM should provide the actual corporate hire details.

The Host is intentionally easy to penetrate but dangerous to overstay: keep most private checks low, then let the Security Tally and IC sheaf create the pressure.

</details>

## Related Pages

- [Matrix Host Construction Guide](Host-Construction-Guide.md)
