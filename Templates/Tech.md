---
title: Tech Template
type: tech
visibility: player-safe
status: active
canon_status: provisional
confidence: medium
updated: YYYY-MM-DD
aliases: []
tags: [tech]
sources: []
---

# [Tech / Matrix Page Name]

## Overview

[One-paragraph summary.]

## Function

- [What it does]

## Architecture / Components

- [Component]

## Access / Security

- [Access or security note]

## Operational Notes

- [Note]

## Optional: Data Haven Paydata Broker

Use this block only for data havens or broker nodes that help a decker sell recovered paydata.

- **Broker NPC / haven:** [Name]
- **Canon anchor:** SR3 *Matrix* paydata starts at **5,000¥ per Paydata Point**; ordinary stolen paydata decays quickly if not sold.
- **Inputs:** Paydata Points, age in days, quality, sale mode, tags.
- **Freshness:** Day 0 100%, Day 1 90%, Day 2 75%, Day 3 55%, Day 4 35%, Day 5+ 20% unless GM marks the file as story-specific or archival.
- **Quality:** clean 100%, partial 65%, messy 45%, radioactive/hot 85% plus heat.
- **Sale modes:** Quick Buyout, Haven Listing, Blind Auction, Quarantine / Refusal.
- **App hook:** add `tool.type: "paydataBroker"` on the broker node when using Decker Experience.
- **Discord output:** include or generate a copyable `@CindyLouBot [HAVEN] PAYDATA SALE` report with seller, broker/haven, mode, points, age, adjusted value, sale roll, final payout / nuyen delta, heat/status note, and Cindy ingest note.

## Connected Pages

- [Page](../Path/Page.md)

## Open Questions

- [Question]

## Sources

- [Source]
