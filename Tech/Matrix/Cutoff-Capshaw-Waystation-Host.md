---
title: Cutoff Capshaw Waystation Host
type: matrix-host
visibility: player-safe
status: active
canon_status: canon
confidence: high
last_updated_session: 2026-09-06
tags: [matrix, host, cutoff, capshaw-mountain, waystation, sr3, blue-host, decker-experience]
sources:
  - GM direction 2026-09-06
  - /Volumes/carbonite/claw/data/cindylou/cleaned/memory/00_sources/rules_references/sourcebooks/SR3_Matrix_7909/source.md
---

# Cutoff Capshaw Waystation Host

## Overview

The **Cutoff Capshaw Waystation Host** is the public Matrix board and private maintenance system for **the Cutoff**, a wildcat outcast community on Capshaw Mountain. The Cutoff presents itself as a rough but functional stop between wasteland roads and civilized supply lines: a place to trade, repair, wash dust off, buy a meal token, hear road warnings, and decide whether the city below is worth dealing with today.

This Host has a [machine-readable Decker Experience profile](../../data/matrix-hosts/cutoff-capshaw-waystation-host.json). The Decker Experience version keeps the public areas completely open: no checks, no required rolls, and no lockouts for normal public browsing or departure. The private maintenance layer is a low-security Blue host with reportable camera and turret access, plus a deeper final check that can reveal the host maintainer's corporate betrayal.

## SR3 Rules Model

Use normal SR3 Matrix host assumptions:

- Treat the system as a **Blue-4 host** with mostly low-grade subsystem ratings.
- Public waystation surfaces are ordinary visitor traffic and require **no checks** in the prepared Host profile.
- Private maintenance access uses standard decker intrusion rolls against Access, Index, Files, Control, or Slave as appropriate.
- Passive alert raises subsystem ratings by +2 for users in the system, per *Matrix* alert guidance.
- Security should feel cheap, patched, and community-scale: Probe/Trace pressure, minor Scramble, Tar Baby delays, and human notification before lethal host combat.
- The buried corporate dead-drop files are the exception: use the higher final check in the profile or an equivalent GM-adjudicated harder file/decrypt operation.

## Host Stats (SR3-style)

- **Host Color / Security:** Blue-4
- **Host Rating:** 4
- **Shutdown Tally:** 16
- **Access:** 4
- **Control:** 4
- **Index:** 4
- **Files:** 5
- **Slave:** 4
- **Buried Files / Corporate Dead Drop:** 7-8
- **Typical IC mix:** Probe-4, Trace-4, Scramble-5, Tar Baby-5, radio-check notification to a local watcher or the host maintainer
- **IC not normally present:** Black IC, lethal gray constructs, military-grade killer suites, or corporate-grade security unless an outside actor has added them
- **Routine decker task TNs:**
  - Browse public trade ads, service menus, waystation explanations, and road notices: **no roll** in the Decker Experience profile; TN 3-4 only if the GM calls for an unusual public search
  - Breach the locked maintenance shack: **4**
  - Search community movement records: **5**
  - Access the limited camera network: **5**
  - Access or spoof the small defense turret network: **6**
  - Find buried maintainer irregularities: **7**
  - Break the corporate dead-drop cipher: **8**
  - Evade trace / human-notification pressure: **5**

## Decker Experience profile

- **Profile ID:** `cutoff-capshaw-waystation-host`
- **Name:** Cutoff Capshaw Waystation Host
- **Security code:** Blue
- **Security value:** 4
- **Shutdown Tally:** 16
- **Design note:** Public areas are intentionally open and roll-free. The locked private area contains limited camera access, a small turret network, community movement records, and a harder buried final reveal: the rigger/decker who maintains the Host is selling citizen and traveler intelligence to local corps.

## What public visitors find

The public side is not a puzzle and not a trap. It exists because the Cutoff needs strangers to understand the rules before they arrive.

- barter offers for water, batteries, canned food, spare parts, fuel additives, ammunition components, tires, seeds, boot leather, and salvage;
- service listings for generator repair, patch medicine, water testing, guide introductions, low-grade Matrix message drops, meal tokens, and shelter supplies;
- plain-language explanations that the Cutoff is not a town, not a corp, and not a gang, but a mountain waystation for outcasts, travelers, and border people;
- road and footpath notices covering washed-out switchbacks, bad bridges, patrol rumors, safe water hours, animal trouble, and least-bad routes toward city services;
- warnings against corporate recruiters, bounty hunters, and anyone bringing heat through the gates.

Public users can enter, browse, return to the entrance, and leave without rolling.

## What deckers find inside

Private maintenance access can expose:

- rough movement records: arrivals, exits, aliases, barter disputes, service tokens, watch notes, and guide assignments;
- a limited camera network: trail-cams, fuel-shed angles, barter-lane views, stored clips, blind spots, broken feeds, and feeds intentionally pointed at useless trees;
- a small defense turret network: old pintle mounts, warning lights, limited remote traverse, safety locks, ammo-state indicators, and watch-status panels;
- hidden maintainer ledgers disguised as dead repeater diagnostics;
- payment marks and transmission windows that suggest outside buyers;
- buried corporate dead-drop files showing the host's rigger/decker maintainer is feeding local corps intelligence on citizens and travelers who pass through the Cutoff.

Exact corporate recipients, proof quality, exposed citizens, and fallout should remain GM-confirmed during play.

## Host feel

The public sculpting looks like a patched mountain message board: hand-painted arrows, dusty trade signs, CB radio chatter, water-tank gauges, salvage stall labels, clinic notes, route warnings, and flickering low-bandwidth service icons. It feels practical rather than welcoming.

The private layer looks like a plywood maintenance shack behind the board. Cable spools, radio repeaters, trail-camera monitors, turret warning panels, and greasy logbooks crowd a cheap workbench. The deeper betrayal is not presented as a villain lair; it hides as diagnostics, invoices, dead repeater notes, and small payment ticks nobody was supposed to reconcile.

## Iconography

- **Access:** mountain signpost, public board, locked maintenance shack, rusted hasp.
- **Control:** water-pump relays, warning lights, radio repeaters, turret panels, camera switches.
- **Index:** hand-written tags, road maps, barter tabs, repeater labels, ledger strings.
- **Files:** logbooks, clipboards, grease-stained envelopes, folded road warnings.
- **Slave:** trail cameras, gate sensors, old turret mounts, warning horns, fuel-shed locks.
- **Probe IC:** a trail camera tilting toward the intruder.
- **Trace IC:** a fence line crawling back toward the jackpoint.
- **Scramble IC:** CB static and bad photocopy ghosts fuzzing copied notes.
- **Tar Baby IC:** a rusted gate latch and warning cable catching the icon.

## Security Sheaf (SR3-style)

Use this as a prepared Blue-host sheaf guideline. Adjust exact trigger steps if the live table already has a Security Tally in motion.

| Tally | Event |
| ---: | --- |
| 4 | Trail-Cam Probe-4 compares the icon against local maintenance habits. |
| 7 | Fence-Line Trace-4 starts following the decker's route through patched rural relays. |
| 10 | Passive Alert: a maintenance radio starts asking for a human check-in. |
| 12 | Static Scramble-5 risks partial, noisy, or corrupted recovered ledgers. |
| 14 | Gate-Latch Tar Baby-5 tries to hold the icon until someone on the mountain responds. |
| 16 | Host shutdown; resolve host shutdown / dump-shock guidance if the decker remains online. |

## Decker use

Useful for checking who passed between the wastelands and city-adjacent civilization, what the Cutoff publicly offers, where its limited cameras can see, and whether its defensive systems can be spoofed or understood. The major hidden payoff is the corporate-intel dead drop: evidence that the maintainer has been selling community trust to local corporate buyers.

Good concrete successes include:

- public waystation information without rolls;
- community movement-record access;
- limited camera-network access, with GM scope confirmation;
- small defense turret-network access, with GM scope confirmation;
- modest traveler-pattern or camera-gap paydata;
- circumstantial maintainer-irregularity paydata;
- major proof of corporate intelligence feeding from the Cutoff host.

Permanent changes, such as spoofing turret status, altering records, suppressing camera footage, or tampering with dead-drop files, must be explicitly reported to the GM.

## Paydata Guidance

The host may contain **small local paydata** from ordinary records and **one sensitive major reveal** from the buried dead drop.

Possible smaller finds:

- traveler pattern notes between wasteland routes and city services;
- guide-route pressure and recurring barter rhythms;
- camera gaps, suspicious blank windows, and repeat visitor traces;
- maintainer irregularities that suggest an outside relationship without proving it.

The corporate dead-drop proof is more dangerous than ordinary paydata. Selling or mishandling it may expose vulnerable Cutoff citizens, burn travelers who trusted the waystation, or tell the corrupt maintainer that someone has cracked the ledger.

## Open Questions

- Which local corps are buying the maintainer's intelligence?
- Does the Cutoff leadership suspect the rigger/decker, or is this betrayal still hidden?
- Which travelers or citizens would be endangered if the dead-drop proof became public?
- Are the defense turrets mostly deterrent, or can one of them still do real harm?

## Related Pages

- [Matrix Host Construction Guide](Host-Construction-Guide.md)
- [Mevin Decker Experience Documentation](../../Documentation/Mevin-Decker-Experience.md)
- [Minigames and Web Apps](../../Minigames.md)

## Sources

- GM direction, 2026-09-06.
- *Matrix* (SR3), host security/alert/shutdown/paydata guidance, local source file listed in front matter.
