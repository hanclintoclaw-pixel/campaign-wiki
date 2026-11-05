---
title: "Unified campaign memory voice pilot"
type: change-note
visibility: player-safe
updated: 2026-11-05
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-05
---

# Unified campaign memory voice pilot

## Shipped

Bridge commit `787a819` selects the unified public campaign adapter for campaign prefetch and model lookup instructions, using memory release `593a0fb`. The selected route bypasses the old campaign lexicon, direct-file evidence and collection reader. Campaign misses or backend failures do not automatically fall back to legacy readers or the web. An explicit legacy route remains available for operator rollback between questions.

The reviewed public projection covers 23 wiki pages and 55 approved sections (saved coverage review), indexed as 55 files and 94 chunks (released health probe). It is not the whole wiki. Source revisions and section citations remain bound; unknown and private sections remain excluded.

The existing Qwen wake model and thinking-off setting, manual saved-clip workflow and no automatic playback are preserved. SR3 specialist lookup remains separate; disabled proactive rules search stays disabled. No other memory consumers or writers are retired by this pilot.

## Measured

Before the idle restart, an ad-hoc probe called the actual bridge prefetch helper and pinned adapter: Tom Erlichman returned the approved public contact section in 2.6384 seconds; an invented identity returned empty in 2.4867 seconds. Both worker receipts report reaped children. These are retrieval-only timings, excluding Discord, answering-model and audio latency.

Seven synthetic AST routing controls passed, covering legacy bypass, direct-read/lexicon denial, shared lookup instructions, campaign web-fallback blocking and legacy-policy rollback. Bridge Python compilation and scoped whitespace checks passed. Earlier supervisor timeout/output-cap controls were reused, not rerun.

The single idle launchd restart loaded the committed bridge after its commit time. Current-boot diagnostics report unified routing, the pinned release, matching source hash, Qwen thinking off, Discord ready and no restored active session. Capture storage was writable before restart.

## Still open

Actual spoken-question recognition, model answer quality, runtime tool compliance, saved clip generation and operator playback await the human voice test. Preflight probes are not live voice acceptance. Start with a covered known fact and an invented entity; full rollback restart rehearsal and broader coverage remain unproven.

The dedicated local embedding service is manually managed, without autostart or supervision. A backend outage must produce an honest unavailable answer, not a silent legacy fallback. This pilot is not full-wiki parity or completion of the unified-memory migration.

## Corrections

Earlier preparation notes described the route as unapplied; this dated entry records its subsequent authorized activation. Historical dependency failures remain part of the repair record. A preflight invocation initially used an abbreviated release-directory path and was corrected before the successful probe; a probe-only config attribute typo was likewise corrected before either lookup ran. Neither failure is credited as retrieval evidence.
