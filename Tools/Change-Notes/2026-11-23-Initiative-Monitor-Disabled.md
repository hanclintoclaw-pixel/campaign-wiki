---
title: Legacy Cindy initiative monitor disabled
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Legacy Cindy initiative monitor disabled

## Shipped
GM authorized disabling or removing the unwanted proposal system. Applied the existing monitor-only startup switch: `LIVE_MONITOR_ENABLED=false`, formerly true. Its configured destination remains the old proposal channel, but the disabled monitor returns before scanning, generating clips or sending messages. No fallback destination was substituted. No channel was closed or deleted.

Reloaded the idle, disconnected bridge through launchd: PID 98279 replaced by 12233 at 15:41:49 EST. Source remains `6f88641`; no code change, model change, source-rights change or voice-recall repair. Only one environment key changed. The legacy code is **disabled, not removed**. Full deletion remains project work, not an accomplished result.

## Measured
- Source-trace check: `live_session_monitor_watchdog` returns immediately when its startup flag is false; its task is separate from direct replies, transcription, presence and health watchdogs.
- Executed the actual AST-extracted monitor method with a false flag and a minimal object lacking all send, synthesis and state methods: returned cleanly before any side effect. This is a focused gate test, not a full voice test.
- Private byte comparison proves only the one environment key changed; bridge source SHA-256 unchanged before/after reload. Private backup and receipt retained under the data-tier runtime directory `initiative-retirement-20261123`.
- New boot logged Discord readiness and direct public wake `enabled=True`; current monitor status reports `enabled: false`. Its legacy `state: enabled_idle` label is misleading and is not evidence that the gate is enabled.
- Before restart: ended session, disconnected voice, zero unclaimed response events, writable capture root. No active table was interrupted.

## Still open
Full legacy code/config/state/test retirement and replacement design remain separate follow-up work. No Qwen implementation job was needed for this existing one-key switch. Replacement implementation and activation remain unapproved.

No new live utterance, human listening test or end-to-end capture test was performed. Preserved configuration and startup readiness are not proof of every voice interaction. Existing accepted voice 1.0 issues remain hard parked. Do not re-enable this flag as a fallback when designing the replacement.

## Corrections
This is operational disablement, not code deletion or a replacement deployment. The earlier charter's documentation-only status is superseded only for this explicitly requested retirement action.

[Living project guide](../Cindy-Initiative-System-Replacement.md) · [Change notes](../Change-Notes.md)
