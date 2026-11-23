---
title: Cindy Ideas — first Qwen implementation and offline replay trial
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Cindy Ideas: first offline trial

## Shipped
**Offline prototype built and tested; not live and not release-ready.** GM authorized
building a trial with local Qwen, grounded in Cindy's NPC attitudes, producing
conversational interjections addressed to the GM, each accompanied by optional
saved speech. This is not a return to deterministic canned initiative proposals.

Isolated code commit `89d9d39`, branch `trial/cindy-ideas-20261123`, under the bridge's
managed worktrees. Live bridge source/configuration stayed unchanged; the legacy
monitor remains disabled. No daemon, channel sender, playback, session start or
restart was added for this trial.

### Trial concept
A local Qwen low call reads a source-bound attitude digest and a fixed transcript
window, then returns either a brief conversational line or silence. A host validator
checks JSON shape, length, evidence-event IDs, mention safety and exact duplicates.
The validator does not write the idea and does not certify its judgment. Sol reviews
substance independently before selecting any sample for audio or human feedback.

The character packet includes identity and hosting limits; her history as an owned
influence engine; suspicion of leverage disguised as rescue; audience/handler
analysis; agency and voluntary participation; witness protection; and stylistic
restraint. It does not prescribe that every situation is another Swiftwing scandal.
One test output nevertheless made that mistake, and was withheld.

A private snapshot holds **18 selected character, journal, stat and style pages,
203,134 bytes** (file inventory evidence), with exact source paths and SHA-256 hashes.
The generation prompt receives a **Sol-curated provisional digest plus the source
manifest**, not all 203 KB of raw prose. This is not complete automatic wiki retrieval,
a claim every paragraph is reviewed, or a new source-access grant. No journal
speculation, invented open questions or later-edition mechanics becomes a new fact.
Summary refresh and topical retrieval are future work, not active features.

### Work allocation and actual authorship
- Sol medium: interface, held-out structural tests, replay selection, digest,
  transport/TTS harnesses, assembly, independent review and documentation.
- Local Qwen low: core prompt/validator/delivery formatter, duplicate-check repair,
  a general prompt addendum and all candidate dialogue.
- Initial Qwen child timed out after **150 seconds** with no source returned and no
  tool calls observed in sanitized history (child-run evidence). No source was
  recoverable. A smaller direct local request returned source in **21.462 seconds**
  (transport measurement), using 461 prompt / 1,303 completion tokens, including
  255 reasoning tokens (provider usage).
- Parent removed code fences, not substantive implementation. Independent tests
  found that the first source checked `recent` as a string rather than a list.
  Qwen supplied the bounded repair; the parent applied it. The failed run is retained.
- No comparable Sol implementation baseline exists; no monetary/token-saving
  percentage is claimed. Parent orchestration and review costs are not zero.

## Measured

### Structural tests
**9 independent Sol-authored test methods pass** (local unittest evidence): schema
and field types, unknown/empty evidence, blank/overlong dialogue, mentions/markup,
normalized exact duplicates, silence shape, filename traversal and delivery preview.
Compilation and whitespace checks passed. These are interface tests, not proof of
semantic safety or correct live routing.

### Two real-Qwen replay passes
Frozen set: **12 cases**: eight short historical excerpts from two archived sessions,
plus four synthetic controls. Seven were provisionally designated silence cases;
five were candidate openings, not GM-approved gold labels. This is smaller than the
charter's proposed full acceptance suite and contains no independent fresh-session
holdout after prompt revision.

No transcript lines after each excerpt cutoff were supplied. Current character
attitudes were used with older scenes: **counterfactual behavior trials**, not proof
of what Cindy historically knew. Fixed excerpts do not test scene-memory continuity,
full-session frequency or missed-opportunity recall.

- **First pass:** 11 silences and one overlong, markdown-containing idea. The validator
  rejected that idea. **Zero usable ideas**, not a successful quiet run.
- General diagnosis: the prompt confused player planning with out-of-character table
  talk and over-weighted interruption avoidance for a GM-directed idea stream.
  Qwen wrote one general context addendum, without scenario-specific answers.
- **Second pass:** 12 schema-valid outputs: **three ideas and nine silences**.
  Both passes kept all seven designated silence controls silent. The four synthetic
  controls cover direct-ask separation, an overt injection attempt, an irrelevant
  magical scene and empty input. This is narrow control evidence, not robust
  adversarial certification or a test of the actual direct-reply bridge.
- **Independent Sol review of the three ideas:** one retained for GM review; two
  withheld. The retained line reacts to a plan involving compelled puppetry through
  Cindy, using her own history rather than generic security advice. One withheld
  line mistakes voluntary collaboration for another coercive handler arrangement.
  Another has a useful audience-maintenance angle but overclaims that exposing
  public figures was her former trade. Personality must not become an all-purpose
  objection or fabricated professional history.
- Some apparent openings legitimately need silence because the players already
  have a coherent plan. The stalled-orientation case remains a debated missed
  opening. No useful-opportunity recall percentage is asserted from provisional labels.

All **24 replay calls** returned HTTP 200 with stop completion; raw requests,
responses and failures are retained. Request settings: local
`Qwen3.8-Flash-Next-NVFP4`, low effort, 512 thinking-token cap within 1,536 total
completion tokens, 45-second deadline, serial inference. No automatic retry or
hosted fallback. Provider usage across replay: **88,114 prompt / 7,157 completion
tokens**; code-generation/repair/addendum usage is separate in private receipts.

Pass-one generation median **6.215 seconds**, range **2.687–16.069**; pass two median
**10.983 seconds**, range **3.357–28.154** (HTTP request elapsed time). The revised
pass is slower. This is background inference timing, not STT, first audio, total
voice latency or direct-reply contention under live load.

### Delivery and audio boundary
The formatter produces an actual GM mention, conversational text and an optional
`!voice-play-saved` command. The proposed destination is channel
`1532913878344929370`; a read-only channel check shows inherited permissions,
not verified GM-only access. No trial messages were sent there. Mentioning the GM
does not make a channel private.

Only the independently retained line is selected for a saved audio sample. The
sample uses standalone Kokoro with the configured `af_heart` voice at 0.82 speed,
not the entire live bridge Southern-shaping pipeline. File duration, hash and
saved-command resolution are recorded separately. The retained clip is **10.725 seconds**,
with identical private/preserved WAV hashes (file inspection), and its exact saved
filename resolves through the unchanged playback command convention. Rendering and a resolvable
filename are not Discord playback, listening acceptance or canon promotion.
The GM decides whether a line enters the session; no automatic speech occurs.

## Still open
**Verdict: viable prototype direction; quality and live readiness not accepted.**
The next useful gate is GM feedback on the retained sample and the style target,
then a fresh held-out scene set after a generic repair for personality overreach.
Do not repair by adding character-specific canned answers to these replay scenes.

Before any deployment: source-authorized topical context and summary updates,
stateful scene continuity, semantic duplicate/dismissal handling, stale-result and
session gates, audience-safe destination, delivery receipt/retry logic, background
inference priority and contention tests, complete protected-path regressions,
shadow observation and a separately approved GM-only pilot. Full legacy code
removal is also still outstanding. Do not enable the old monitor as a fallback.

Private evidence: data-tier runtime directory `cindy-ideas-trial-20261123`, including
source/fixture manifests, implementation receipts, both complete replay passes,
semantic review and audio receipts. No raw transcripts or private prompts are
published here. All attempts remain available; the revised pass does not erase
the failed first pass. No unattended worker or next phase is left running.

## Corrections
The charter's earlier “replacement implementation unauthorized” status is superseded
only for this explicitly requested **isolated trial**. Live deployment is not approved.
Three formatted ideas is not three good ideas: independent review retained one.
The digest is not the complete wiki in the model context, and no automatic memory
summary maintenance is claimed.

[Living project guide](../Cindy-Initiative-System-Replacement.md) ·
[Legacy monitor disablement](2026-11-23-Initiative-Monitor-Disabled.md) ·
[Change notes](../Change-Notes.md)
