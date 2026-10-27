---
title: Voice Bridge Change Notes
type: documentation
visibility: player-safe
updated: 2026-10-25
generated_by: openai/gpt-6.1-sol
generated_at: 2026-10-25
---

# Voice Bridge Change Notes

## What this area is for

This area records dated changes to Cindy's live-session voice bridge: the wake path from wake phrase detection through transcript capture, reply generation, and spoken audio, plus the campaign retrieval that answers table questions. Entries record what shipped, what was measured, and what is still open.

The bridge code lives in `cindylou-voice-bridge-backup`; campaign retrieval lives in `memory-system`. Entries cite commit hashes so each change can be read back in git history.

## How to add an entry

1. Create one dated file per work session in `Tools/Change-Notes/`, named `YYYY-MM-DD-<slug>.md`.
2. Include frontmatter fields `title`, `type: change-note`, `visibility: player-safe`, `updated`, `generated_by`, and `generated_at`.
3. Use four sections in this order: `Shipped`, `Measured`, `Still open`, `Corrections`.
4. Write commit hashes in short form, using 7 characters inside inline code.
5. Every reported number must name its evidence type: session capture log, unit test, or ad-hoc probe. An unsourced measurement in this project has already led to a wrong decision, so provenance is not decoration.
6. Link each new entry from the Entries list on this page.

## Entries

- [2026-10-27 — Roster prefetch and first-token stall](Change-Notes/2026-10-27-Roster-Prefetch-And-First-Token-Stall.md)

- [2026-10-26 — Voice bridge prefetch and wake-latency corrections](Change-Notes/2026-10-26-Wake-Prefetch-And-Latency-Corrections.md)
- [2026-10-25 — Wake path latency, retrieval ranking, and two self-corrections](Change-Notes/2026-10-25-Wake-Path-And-Retrieval.md)
