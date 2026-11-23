---
title: Fast recall MVP activated — changed-path voice confirmation open
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Fast recall MVP activated

## Shipped
GM approved activation. Live bridge fast-forwarded from `81e9eeb` to reviewed
`6f88641`. Only the new `LIVE_WAKE_FAST_RECALL_ENABLED=true` setting was added;
all other parsed environment values were verified unchanged. Source pins, source
rights, model/effort and playback settings remain unchanged. General interpretative
rules work remains parked post-MVP.

Launchd restarted the idle disconnected bridge: PID 98279, boot 2026-11-23
11:59:08 EST, after the candidate commit. Startup main/helper hashes match the
reviewed source manifest. Precache 15/15, on_ready and idle report present;
no new stderr and both log sizes stable over a 36-second observation. Capture root
is mounted/writable and no unclaimed response work was present. Existing unrelated
untracked documentation/report files were preserved, not shipped as edits.

## Measured
Fresh deployed-checkout handler replay, real readers/text formatter, mocked Discord
transport: 31/31 handled; all outputs byte-equal to the accepted candidate. This is
23 factual outputs plus 8 honest boundaries, not 31 factual answers. Zero attempted
model or operator CLI calls. Observed handler median 0.661 seconds, range
0.229–1.616 seconds; not STT, first audio or an SLO. Focused tests pass 21/21 in
the deployed checkout; touched Python files compile. These source-level probes do
not claim that an actual voice turn has yet exercised the new running process.

## Still open
A short changed-path live voice confirmation before declaring supported scope 1.0:
- Cindy, how much does Wired Reflexes 2 cost? Expected: 165000 nuyen.
- Cindy, what is the MPCP of a Fairlight Excalibur? Expected: 12.
- Cindy, what is Mevin's Intelligence? Expected: a brief honest field boundary.
- Optional unchanged control: Cindy, who is Mevin?

Check intelligible playback and corresponding session-thread text/citations. Spoken
citations should remain absent. No need to retest the entire library. Supported
coverage and limitations remain those in the acceptance report; activation does
not create missing wiki fields or universal natural-language understanding.

## Corrections
Prior acceptance was isolated, not live. This note records the subsequent approved
activation, not new human audio acceptance. An exact environment backup and changed
source copies are retained privately. Rollback while idle: revert only `6f88641`,
restore the saved pre-activation environment, and restart; preserve later work.
Evidence: private runtime/mvp-fast-recall-activation-20261123, rollback.json,
restart offsets, boot sample, deployed source manifest, idle-stability.json,
handler-proof/report.json and summary.json. No live audio was played by this test.

[Accepted candidate and limits](2026-11-23-Fast-Recall-Acceptance) ·
[MVP scope](2026-11-23-Fast-Recall-MVP) · [Change notes](../Change-Notes)
