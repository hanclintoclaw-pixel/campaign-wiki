---
title: Ruby Falls Data Haven Host
type: matrix-host
visibility: player-safe
status: active
canon_status: campaign-derived
confidence: medium
last_updated_session: 2026-07-14
tags: [matrix, host, data-haven, ruby-falls, lookout-mountain-collective, chattanooga, mevin]
sources:
  - GM direction 2026-07-14
  - ../Factions/Lookout-Mountain-Collective.md
---

# Ruby Falls Data Haven Host

## Overview

**Ruby Falls** is the data haven maintained by the [Lookout Mountain Collective](../../Factions/Lookout-Mountain-Collective.md), a Chattanooga decker community with a strong anti-authoritarian streak and a deep respect for source protection. [Mevin Kitnick](../../PCs/Mevin-Kitnick.md) has access to the haven.

This page sketches Ruby Falls as a Matrix host for the Decker Experience. The public face is open, generous, and educational. The private and administrative depths are intentionally locked down. This profile does **not** build in Mevin's expected ad-hoc access advantage; if Mevin is using his standing access, the GM can add that manually in the tool.

## Host Stats (SR3-style)

- **Host Color / Security:** Blue/Green-6 data haven surface, with Red-grade administrative partitions
- **Host Rating:** 6
- **Access:** 6 public/member-facing; admin partitions 14+
- **Control:** 6 public/member-facing; admin partitions 16+
- **Index:** 6 public/member-facing; admin partitions 14+
- **Files:** 6 public/member-facing; admin partitions 16+
- **Slave:** 5 public/member-facing; admin partitions 14+
- **Typical IC mix:** polite Probe/Trace on public routes, Scramble/Tar Baby around member areas, serious nonpublic tripwires at the admin boundary
- **Routine decker task TNs:**
  - Public commons, public goods, zines, tool primers: **no roll / TN 4 if tested**
  - Member education rooms and basic haven navigation: **6-8**
  - Source-protection and verification rooms: **8-10**
  - Sealed member archive doors: **12**
  - Deep admin routing / root ops / trustee keys: **14-20**

## Decker Experience profile

- **Profile ID:** `ruby-falls-data-haven-host`
- **Name:** Ruby Falls Data Haven Host
- **Security code:** Green / Red partitioned
- **Security value:** 6
- **Shutdown Tally:** 30
- **Design note:** Mevin's standing access can be represented with a manually-added ad-hoc Run Advantage. Do not bake that modifier into this profile.

## What deckers find inside

Public visitors can find:

- anti-authoritarian zines and public-interest data packets;
- beginner decker primers;
- safety notes about source protection, route hygiene, and not burning community infrastructure;
- public goods such as mutual-aid resource lists, repair notes, and sanitized civic records;
- the Ruby Falls marketplace, where Sister Anode's paydata broker panel lives.

Member-facing or deeper routes can expose educational rooms and capability prompts, but not conventional paydata. Ruby Falls is a haven, not a loot box.

Administrative routes should mostly communicate that the decker has reached a boundary they should not cross casually. Do not sketch the true internal admin host in player-facing play unless the GM deliberately opens that material.

## Host feel

Ruby Falls looks like a tourist cavern, a public library, a ham-radio shack, a church basement archive, and a hacker zine table all folded into one glowing underground river. Public shelves are bright and welcoming. Deeper doors are not dramatic; they are simply firm. The message is: knowledge wants to be free, sources do not.

## Public education rooms

The public and member-safe layer includes rooms meant to teach aspiring new deckers how to operate without getting themselves or their communities hurt:

- **Public Zine Rack** — anti-authoritarian pamphlets, public data, mutual-aid lists.
- **New Decker Orientation Pool** — beginner Matrix safety, legal/illegal distinctions, and etiquette.
- **Route Hygiene Switchback** — how to avoid dragging heat back to a haven.
- **Source Protection Chapel** — consent, redaction, handling whistleblower data.
- **Utility Practice Alcove** — safe toy examples for Analyze, Browse, Deception, Validate, and Read/Write concepts.
- **Verification Table** — how to separate leaks, rumors, bait, and forged paydata.

## Ruby Falls marketplace and paydata broker

The old central placeholder has been rebranded as the **Ruby Falls Marketplace**: a source-safe exchange floor for public goods, vetted requests, and carefully handled paydata. Inside it, **Sister Anode's Paydata Broker Table** provides a reusable in-app paydata broker panel for Mevin to sell paydata through Ruby Falls.

Canon anchor from *Matrix*: paydata has a base street price of **5,000¥ per Paydata Point**, and ordinary stolen paydata loses value quickly if it is not sold. Ruby Falls wraps that in a haven workflow: source protection, appraisal, sale mode, buyer hygiene, and a Discord-ready payout report.

### Inputs

- **Paydata Points:** how many points Mevin recovered.
- **Age:** days since recovery.
- **Quality:** clean, partial, messy, or radioactive/hot.
- **Sale mode:** Quick Buyout, Haven Listing, Blind Auction, or Quarantine. The panel explains these modes in-place.
- **Tags:** optional context such as corp, gang, civic, medical, blackmail, logistics, magical, security, zero-day, public-interest.

### Freshness

- Day 0: 100%
- Day 1: 90%
- Day 2: 75%
- Day 3: 55%
- Day 4: 35%
- Day 5+: 20%

Story-specific, archival, blackmail, or legal-proof files can ignore or alter decay at GM discretion. Market intel, schedules, access codes, and zero-day chatter should usually decay faster.

### Quality

- **Clean:** 100%
- **Partial:** 65%
- **Messy:** 45%
- **Radioactive / hot:** 85% before sale-mode payout, but increases heat and may require redaction or auction handling.

### Sale modes

- **Quick Buyout:** Sister Anode or a trusted standing buyer takes the data immediately. Lowest overhead and fastest cash, but lower upside.
- **Haven Listing:** Ruby Falls lists the data under protected terms for a vetted buyer pool. This is the default safe-market choice: better expected payout than a buyout, usually with a short delay.
- **Blind Auction:** Ruby Falls anonymizes the source and lets vetted buyers bid. Highest upside and best for spicy paydata, but more delay and hook potential.
- **Quarantine:** Sister Anode refuses to sell immediately. Use this for bait, source-exposing files, dangerous leaks, or anything that needs redaction or ethical review.

### In-app output

The Decker Experience renders a special **Paydata Broker** panel on Sister Anode's node. Mevin navigates into the marketplace, opens the broker table, completes the sale in the panel, copies the `@CindyLouBot RUBY FALLS PAYDATA SALE` report, and then uses the single **Back out to the Ruby Falls marketplace** option when finished. Legacy sale-mode branch nodes are intentionally removed; the panel handles the math and output.

## Admin boundary

The admin side is present only as a hard boundary. It includes sealed trustee routing, source-key custody, archive integrity controls, and root operational surfaces. The Decker Experience profile gives these routes TNs of **14+** and no rewarding content. Reaching the boundary should tell the player they are at an admin wall, not reveal the inner machinery.

## Open Questions

- What are Mevin's exact Ruby Falls access terms?
- Who vouched him in?
- Which public rooms does Mevin already know well?
- What other reusable tools, if any, should live in the Ruby Falls marketplace?
- What does Ruby Falls do with dangerous evidence like the Pixel Sticks critical-services sabotage material?

## Related Pages

- [Lookout Mountain Collective](../../Factions/Lookout-Mountain-Collective.md)
- [Mevin Kitnick](../../PCs/Mevin-Kitnick.md)
- [Maribel "Switchback" Pruitt](../../NPCs/Maribel-Switchback-Pruitt.md)
- [Jonah "Cave Cricket" Bell](../../NPCs/Jonah-Cave-Cricket-Bell.md)
- [Rosalind "Sister Anode" Pike](../../NPCs/Rosalind-Sister-Anode-Pike.md)
- [Earl "Railgun" Dunlap](../../NPCs/Earl-Railgun-Dunlap.md)
