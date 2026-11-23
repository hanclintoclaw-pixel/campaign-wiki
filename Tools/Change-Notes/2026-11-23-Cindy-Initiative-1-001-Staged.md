---
title: Cindy Initiative System 1.001 — staged, activation held
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Cindy Initiative System 1.001: staged, NOT enabled

**Historical staging record.** The GM resolved the quality hold and 1.001 is now [activated and armed](2026-11-23-Cindy-Initiative-1-001-Activated.md). Statements below describe the earlier hold, not current runtime status.

## Shipped
**No live deployment. The next voice session will not run this version yet.**
GM approved the puppet-history sample as good, natural character work and requested
version **1.001**, activation, and staging for the next voice session. That activation
request remains open. The implementation was staged, but final reviewer checks
failed the current independent quality labels; the parent explicitly held activation
and asked the GM to judge the two disputed drafts rather than silently enable them.

Staged code: `8170f93`, branch `feature/cindy-initiative-1001`, in the existing
`cindy-ideas-trial-20261123` bridge worktree. The live bridge stays `6f88641`, PID
12233; source and environment hashes match the pre-task baseline. No restart,
channel post, playback, new launchd service or Gateway automation was performed.
The old deterministic proposal monitor remains disabled, not deleted.

### Staged behavior
- Native bridge-owned background task, rather than a Gateway automation or a second
  Discord client. Six additive bridge lines attach the task and protect the new
  producer's playback files. Existing direct-response bodies are unchanged.
- Fixed, revision-hashed character digest, not all wiki text or GM-only records.
  Personal history is a legitimate influence, not a quality defect by itself.
- Local Qwen low generates a conversational thought or silence; a separate low-effort
  Qwen review checks the candidate before synthesis. No hosted fallback or model tools.
- Active, connected, newly started session after activation time only. Same-thread
  transcript, three-minute/40-event context, fresh results, direct-reply/client
  cancellation guards, 90-second evaluation cadence, maximum 120 evaluations and
  one message/attempt per session. These are staged controls, not live measurements.
- Intended destination is the GM-proposed channel `1532913878344929370`, with only
  the real GM mention allowed. The channel is not verified private. Inputs are
  limited to the reviewed character digest and the table transcript; no GM-only
  wiki material is admitted. No message has been sent there by this component.
- Optional/not-canon label and a saved `!voice-play-saved` command; never automatic
  playback. New initiative-prefixed clips require the GM, including case-insensitive
  filename checks. Legacy clips retain their existing behavior.
- Own one-shot Kokoro subprocess using current voice/speed and the bridge's text/
  pronunciation preparation. Cancelling an initiative render cannot stop the shared
  voice-answer Kokoro worker. Actual audio must measure no more than 20 seconds.
- Persist send intent before the external effect. Uncertain delivery consumes the
  quota rather than blindly retrying; confirmed delivery stores its receipt.

### Actual authorship
Qwen authored the existing generation core, session-window/reviewer module, a
bounded gate repair, and a general critic prompt. Sol authored the adapter,
transport/schema wrapper, independent tests, playback guard, source assembly and
review. This is not a wholly Qwen-authored system. Qwen's gate initially accepted
malformed event IDs and failed to checkpoint direct requests; independent tests
caught both, and Qwen supplied the repair. Sol corrected its own case-sensitive
playback guard after a failing test. Failed attempts are retained privately.

## Measured
- **27 lifecycle/emitter/renderer tests pass** (local unittest evidence), including
  session scope/reset, old-session exclusion, fresh/stale windows, budgets,
  direct-request separation, busy/public-owner priority, reviewer withhold before
  audio, profile drift, kill-switch changes, wrong destination guild, uncertain-send
  quota and child-process cancellation/reaping. These use controlled fixtures and
  mock delivery; they are not live Discord acceptance.
- **46 public-wake/corrective and 21 fast-field tests pass** (local unittest evidence).
  Duration checks passed in the separate voice-cap script; **38/38** speech-sanitizing
  checks passed in its script. Compilation, Node syntax and whitespace checks passed.
  An initial combined test-import command exited through the speech script before
  running the unittest suite; the 46 tests were subsequently run separately. The
  report does not credit the import command as those tests.
- The installed Node 22 binary failed on a missing `libsimdjson.33.dylib` dependency.
  This new component uses the working `/opt/homebrew/bin/node`, version 24.22.3.
  No Homebrew install or unrelated voice configuration was changed.
- Initial local review had an overlong explanation rejected by schema and then a
  transport failure. A compact constrained JSON review protocol was added. Its
  completed six-case pass agreed with Sol's current labels on **4/6** cases, not six.
- One bounded Qwen-authored general critic correction was then tested on the same
  six cases. Agreement remained **4/6**: the retained puppet-history idea was accepted,
  three clear negatives were rejected (invented completed hack, ungranted astral
  power, extreme coercion inference), but both disputed drafts were still accepted.
  These are repeated probes, not fresh held-out validation. No failed response was
  discarded or relabelled as a technical success.

### The remaining judgment
Sol withheld a draft that treats voluntary crew collaboration as another handler
arrangement, and another that describes exposing public figures as Cindy's former
trade rather than the established audience-shaping work. Qwen continues to consider
both grounded character reactions. The exact lines were posted to the GM in this
project thread for judgment. This is not a failure of mentioning her history: the
GM has explicitly approved that focus.

**Current gate: failed against Sol's conservative labels, pending GM ruling.** If the
GM accepts either line as character work, record that as a changed human quality
label, not as a code repair or retroactive passing result. Otherwise the filter
needs further work before enabling. Do not leave the next-session promise ambiguous.

## Still open
Private staged configuration has `enabled=false`, `not_before=0` and the reviewed
persona/addendum hashes. The bridge adapter is committed only in the isolated
worktree, not merged or loaded. No worker is active, and no automatic background
repair or deployment is pending.

After resolving the quality decision: inspect then-current live changes and session
inactivity, preserve the environment, integrate without removing later fixes, set
the approved activation time, perform the authorized idle reload, and verify the
loaded source, native Node inference/destination preflight and idle readiness.
Only then can the next session be said to run 1.001. Actual session usefulness,
message delivery, playback and listener acceptance remain separate evidence.

Shared-model contention and server-side inference preemption are unproven; client
cancellation does not establish either. The independent Kokoro child avoids shared
IPC cancellation but adds transient CPU/memory load. No live-load latency promise.
Full legacy code removal and automatic digest refresh remain separate work.

Gateway automation management was refused for this caller. Those jobs were not
retried or modified through another route. The staged native app component is not
an automation-management repair, and no new scheduled job was created.

Evidence: private runtime directory `cindy-initiative-1001`, staged source README,
original/repaired gate tests, all reviewer attempts and `staging-receipt.json`.
No raw transcripts or private prompts are published here.

## Corrections
The GM authorized activation, but authorization is not evidence of deployment.
“Staged” here means committed code and disabled configuration, not a running
shadow observer. **The next session will still use the existing voice system
without new initiative until this hold is resolved and deployment is verified.**

[Living project guide](../Cindy-Initiative-System-Replacement.md) ·
[Offline trial](2026-11-23-Cindy-Ideas-Offline-Trial.md) ·
[Change notes](../Change-Notes.md)
