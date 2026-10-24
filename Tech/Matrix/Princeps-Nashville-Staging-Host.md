---
title: Princeps Nashville Staging Host
type: matrix-host
visibility: player-safe
status: active
canon_status: provisional
confidence: medium
last_updated_session: 2026-10-24
generated_by: local-inference-lab/Qwen3.8-Flash-Next-NVFP4
generated_at: 2026-10-24
tags: [matrix, host, princeps, cross-applied-technology, cas, miltech, hidden, decker-experience, sr3]
sources:
  - GM/table request 2026-10-24 (#Cindy GM Interaction Thread)
  - ../../Factions/The-Princeps-Group.md
  - ../../Organizations/Cross-Applied-Technology.md
  - ../../Factions/Pixel-Sticks.md
  - ../Host-Construction-Guide.md
  - /Volumes/carbonite/claw/data/cindylou/cleaned/memory/00_sources/rules_references/core_rules/SR3_Core_Rulebook_FanPro/source.md
---

# Princeps Nashville Staging Host

## Overview

What the public record shows is a regional procurement and liaison front: a modest Princeps Group node on the Nashville local grid, licensed under the Huntsville parent's outstate operating permits, advertising contract coordination for CAS defense supply chains. It exists to be boring. Its public services — requisition forms, liaison directories, a glossy Princeps press page — contain nothing worth stealing, which is the point. Behind it, keyed to an access tier the cover host's own registered sysadmin appears not to know exists, sits a second compartment that no index lists: an attack-planning platform pointed squarely at [Cross Applied Technology](../../Organizations/Cross-Applied-Technology.md)'s Nashville footprint.

The staging host is the missing link the [Pixel Sticks](../../Factions/Pixel-Sticks.md) affair has been without. Attacks on CAT subsidiaries and affiliates can be traced to a gang, the gang can be traced to a dead drop of military-grade utilities, and the trail goes quiet at exactly that point. A host like this either closes the gap or does not exist at all. Getting inside it is the most direct known route to attribution evidence that could survive a lawyer — tasking records, procurement paperwork, handler traffic tying Princeps money to Pixel Sticks hands.

This Host has a [machine-readable Decker Experience profile](../../data/matrix-hosts/princeps-nashville-staging-host.json).

## Host Stats (SR3-style)

Stat line in SR3 shorthand (`SecurityCode-SecurityValue/Access/Control/Index/Files/Slave`):

**Orange-9/13/11/14/12/11**

- **Host Color / Security:** Orange — significant security, confidential data
- **Security Value:** 9
- **Access:** 13
- **Control:** 11
- **Index:** 14
- **Files:** 12
- **Slave:** 11

All values are **GM-discretion picks drawn from the Average intrusion band** of the SR3 Host Rating Table (*Shadowrun Third Edition*, p. 205: Security Value `1D3+6` = 7–9, subsystem ratings `2D3+9` = 11–15). They are not the result of rolling a single dice column. The Host Rating Table permits the GM to set ratings by discretion, which is what this profile does.

Two design notes on the numbers:

- **Access 13 and Index 14 sit at the top of the band** because a covert platform depends on its entry route and its filing structure staying unguessable.
- **Slave 11 sits at the bottom of the band** on purpose. The meatspace footprint is a small leased office with a handful of cameras and a door badge reader. There is no building-scale infrastructure here to seize, which is also a clue: this is not where Princeps actually lives.

The tool profile additionally sets `hostRating: 9`, equal to the Security Value. That is a **Decker Experience abstraction** used as a target-number fallback and shutdown heuristic, not a separate SR3 statistic.

## Security and Alert Logic

- **Dormant is the start state.** The printed ratings above are pre-alert values. **Passive Alert is not active when the run begins.**
- **Passive Alert** activates only when the GM triggers it — a tripped alarm, a confirmed intruder, a botched suppression. Per core rules it raises **all five subsystem ratings by +2**: Access 15 / Control 13 / Index 16 / Files 14 / Slave 13. Announce it and re-read the adjusted values, because every subsystem target number in the profile shifts at once.
- **Shutdown Tally 21** in the tool profile. Passive Alert displays at roughly 7, Active Alert at roughly 14, and the run ends in dumpshock at 21.

## Routine Decker Task TNs

Printed pre-alert target numbers. The Decker Experience supplies decker dice and free Hacking Pool on top of these; Passive Alert adds +2 to anything subsystem-derived.

- Enter using a forged vendor credential chain: **10**
- Browse the public tender board and liaison directories: **5**
- Search buried approval references and archived routing: **11**
- Reach restricted vendor files, requisitions, and device ledgers: **10**
- Alter requisitions, vendor records, or tasking metadata: **11**
- Seize the leased site's cameras and door-badge slaves: **10**
- Evade a trace once the host has noticed the intrusion: **9**
- Fight serious IC or force progress under active alert: **10**
- Find the unindexed Deep Archive seam: **12**
- Breach the Deep Archive: **13**

## Security Sheaf (campaign abstraction)

The sheaf is a **table pacing aid**, not a quotation of sourcebook IC ratings. Encounter ratings are campaign/tool values chosen for escalation feel.

| Tally | Escalation | Effect |
| --- | --- | --- |
| 3 | Visitor Badge Challenge | The front desk runs the vendor credential against the day's approved buyer list and holds the lobby for a human verifier. |
| 6 | Threat Correlation | The intruder's signature is correlated against archived attack traffic on Cross Applied Technology; the visitor file is reclassified as suspect. |
| 9 | Tasking Fork | Session tasking metadata is forked into plant dossiers, and every requisition filed inherits a flagged-buyer routing code. |
| 12 | Handler Approval Loop | Each action is filed as a requisition awaiting a handler countersignature that never clears, pinning the decker to the counter. |
| 15 | Tasking Vault Custody | The vault custodian treats the session as hostile penetration of compartmented tasking and seals the compartment with the decker inside it. Terminal if not handled. |

Escalation is meant to read as **procedural military discipline tightening**, not horror. Nothing here wants to hurt the decker first. It wants to note them, file them, seal them out, and be finished — and only at the vault does it escalate to lethal custody.

## What Deckers Find Inside

Intended contents. These are discoverable in-fiction documents, so the GM confirms scope, exact wording, and what any of it actually means before the crew acts on it.

- Tasking memos to Pixel Sticks cell leaders, timestamped days before each incident against CAT affiliates, signed with a recurring handler handle rather than a name.
- Target dossiers on Lafayette Tower: camera coverage gaps, badge-reader topology, shift-change timings for the Entertainment Division floors.
- A pre-strike package on SC Music — floor plan, network demarc points, and a note annotating which CAT personnel were expected on-site during the attack.
- False-flag kits: planted evidence packets staged for recovery by Nashville secops, designed to read as a gang-territory dispute or a rival-external fixer job.
- Utility procurement records: exploit purchases routed through Huntsville shell vendors, with delivery windows that match the dead drop where the crew's military-grade utilities were found.
- Transponder provisioning logs for field drones, including one entry matching the scorpion-drone transponder already in crew hands, commissioned from the Nashville grid.
- Handler mail traffic with a CAT-opsian flavor: a watchlist keyed to Imogene Viola's known contacts and meeting patterns.
- A payment trail running from a CAS veterans' charity account through two intermediaries to Pixel Sticks-linked families, dated after each attack.
- Contingency scripts for a captured proxy: burn notices, identities scheduled for retirement, and a pre-written press release blaming organized crime.

## Host Feel

Jacking into the cover layer feels like standing in a government lobby at six in the morning: clean, evenly lit, unremarkable, and quiet in the specific way of a building where everyone knows exactly which rooms they are allowed to be in. Every door past the front requires a stated reason, and the reasons are checked, not believed.

The menace is procedural rather than theatrical — sequential door numbers, an arrivals log that records you before you finish arriving, corridors that terminate at obvious not-for-you. Nothing here wants to hurt you. It wants to note you, seal you out, and be finished.

## Iconography

- **Cover layer:** a spotless Princeps procurement office, too-normal — framed ribbon-cutting photos of Claude August, motivational CAS-industry posters. The dullness is deliberate camouflage.
- **Tiered access:** a barracks corridor of sequentially numbered doors, each unmarked. No ornament invites guessing.
- **Files:** wax-sealed dispatch boxes. A seal broken without authorization leaves visible damage in the audit trail — the host records tampering, not just theft.
- **IC:** two-man sentry pairs in disciplined patrol, not roaming berserking black ice. They respond in formation, withdraw to report, and return with more of themselves.
- **Alert states:** routine lamps-down; then, on intrusion, every lamp in the corridor comes on at once. Lights up means doors seal and the log is already filling.
- **One anomaly:** a single audit entry from the ops layer still carries the high-resolution draconic humanoid icon the crew saw during the Pixel Sticks investigation. Whether that is vanity, signature, or someone wearing a symbol for cover, nothing here says.

## Decker Use

This host serves investigative and attribution runs, not smash-and-grab: the payload is documents, and documents don't resist — the building does.

A **mid-grade decker** can work the cover layer safely, map the seams between it and the hidden compartment, and pull low-value liaison directories that corroborate the structure without triggering much. The first wrong door, though, starts a trace that terminates at a CAS defense contractor's internal security shop, which answers to lawyers and government liaisons rather than a corporate response team with a grudge.

A **strong decker** can push the ops compartment for the tasking memos and payment trails — the run's actual prize — but the reward scales with exposure: those files sit nearest the sentries, the tamper-evident seals, and the lamps-up lockdown. In practice, the smartest score is the smallest authentic document that connects two things the crew already has.

Calibration: this sits deliberately **between** the [Humanis Nashville Hidden Host](Humanis-Nashville-Hidden-Host.md) (Orange-5, a semi-hidden chapter cell) and the [Lafayette Tower CAT Entertainment Host](Lafayette-Tower-CAT-Entertainment-Host.md) (Red-9, Rating 10, Shutdown 30, with a hidden Ultraviolet layer). Professional military tradecraft, deliberately small footprint, one concealed compartment instead of a deep stack.

## Attribution and Table Safety

**This host is an investigative lead, not a verdict.** Nothing recovered from it establishes that [Claude August](../../NPCs/Claude-August.md) personally ordered the attacks on Cross Applied Technology. The GM should confirm scope before naming sources, because the material here is discoverable in-fiction evidence and may be a plant, a frame, or a deliberate signature.

The Security sheaf and IC ratings, along with `hostRating` (a target-number fallback set equal to the Security Value), are **campaign and tool abstractions** rather than quoted sourcebook IC values. The core-rules content on this page is the rating band, the five subsystem definitions, the shorthand format, and the Passive Alert modifier; everything else in the stat block is GM tuning.

## Open Questions

- Who authored the tasking memos — a Princeps executive chain, or an operator exploiting draconic imagery and miltech aesthetics to frame Huntsville?
- Does the host carry a counterintelligence file on the crew, given how much of the Pixel Sticks investigation has already surfaced in public?
- Is a dead-man protocol documented anywhere in the ops compartment, and does a scrub trigger fire if the host detects a specific breach pattern?
- Are Nashville's cover and staging compartments unique, or does Princeps operate sibling staging nodes aimed at other cities' CAT holdings — Memphis, Knoxville, Chattanooga?
- How much of the Huntsville leadership scandal that brought Claude August to power appears in the archived records here, and does it match the public story?
- What physical site is the leased office, and who holds the lease?

## Related Pages

- [The Princeps Group](../../Factions/The-Princeps-Group.md)
- [Cross Applied Technology](../../Organizations/Cross-Applied-Technology.md)
- [Pixel Sticks](../../Factions/Pixel-Sticks.md)
- [Claude August](../../NPCs/Claude-August.md)
- [Lafayette Tower](../../Locations/Lafayette-Tower.md)
- [Lafayette Tower CAT Entertainment Host](Lafayette-Tower-CAT-Entertainment-Host.md)
- [Humanis Nashville Hidden Host](Humanis-Nashville-Hidden-Host.md)
- [Matrix Host Construction Guide](Host-Construction-Guide.md)
- [Decker Experience profile](../../data/matrix-hosts/princeps-nashville-staging-host.json)

## Qwen Build Review

This page and its tool profile were authored by **Qwen 3.8 Flash Next (NVFP4)** at `thinking: "low"`, as a capability exercise requested on 2026-10-24. What the review found:

- **Caught and corrected:** the first mechanics draft rated this as **two separate Hosts** (a Green-4 cover and an Orange-8 ops host) and then invented subsystem names — "security code", "access ID", "control program". SR3 has exactly five subsystems (Access, Control, Index, Files, Slave) plus a separate Security Value. The published line `Orange-9/13/11/14/12/11` is the corrected single-host version.
- **Rules-grounded after review:** the original draft labeled its mixed subsystem values as coming from the Hard column's `1D6+12` while also claiming an Average Security Value. The published stat block states plainly that the values are **GM-discretion picks inside the Average band**, which the Host Rating Table explicitly allows, rather than pretending a mixed set came from one dice roll.
- **Kept from the draft:** the prose, the iconography, the "procedural rather than theatrical" tone, the attribution-paydata design, and the deliberate Slave-11 weakness that hints the site is not Princeps's real home.
- **Toned down:** the draft's IC list included a Blackout instance plus five other IC types with hard-coded ratings. That was reduced to a five-step sheaf with tool-recognized encounter types, and the lethal step was moved to the vault only.
- **Added in review:** the `attribution-cache` node as drafted had a single tested escape, which trips the Decker Experience's no-double-gate rule. Review added a second tested branch (the false-flag plant, a permanent outcome requiring GM notification) and renamed the escape so the tool does not treat it as a free back-out. Explicit `report` metadata was also added to the four concrete evidence nodes so discoveries survive into the Discord run report.
- **Not verified by Qwen:** the SR3 rating table, the tool JSON contract, and the campaign canon were checked by the reviewing model against the local SR3 corpus, `docs/SCENARIO_JSON.md`, and the app's own design checks. Qwen drafted; it did not adjudicate its own rules.
