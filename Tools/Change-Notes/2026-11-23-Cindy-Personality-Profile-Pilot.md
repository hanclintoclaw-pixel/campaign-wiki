---
title: Cindy Personality Profile Pilot 0.1
type: change-note
visibility: player-safe
updated: 2026-11-23
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-23
---
# Cindy Personality Profile Pilot 0.1

## Shipped

**Offline pilot built; character-quality improvement not demonstrated; no live personality change.**

[Profile and GM refinement guide](../Cindy-Personality-Profile.md). Parent: [Cindy Initiative System](../Cindy-Initiative-System-Replacement.md).

Feature-checkout code `e9b42f2` adds `personality_profile/`: a source/hash/quote validator, versioned GM feedback compiler and preview serializer, offline CLI, independent tests, preparation and paired-comparison harnesses. Source inventory: **14 claims from six wiki pages**, source revision `a3ad2fa` (ad-hoc preparation manifest). Traits distinguish identity/ruling, subjective characterization, inference and presentation design. No real GM refinements have been received for this draft; initial feedback file is empty.

Sol medium authored the profile, contract, source review, independent tests, orchestration and documentation. Local Qwen low authored the compiler and one bounded repair. No third-party package or skill installed. No model weights trained. The existing local Qwen endpoint returned the expected model on both implementation calls. Code generation took 31.153 seconds (ad-hoc transport receipt), 576 prompt / 1,937 completion tokens; repair used 1,410 prompt / 564 completion tokens. No comparable Sol implementation baseline exists; no savings percentage claimed.

## Measured

- **21 unit tests pass** after the Qwen repair (independent unittest log). Checks include fixed schemas, quoted-source hashes, traversal and symlink escape, changed source, duplicate/invalid feedback, proposed-vs-approved handling, deep-copy/nonmutation and preview-only state.
- **Two ad-hoc integration probes pass:** a clearly synthetic approved correction alters only an offline preview; an existing preview output cannot be overwritten through the CLI. Synthetic fixture is not a GM statement or new personality fact.
- **Six real Qwen low requests** compare baseline and candidate on three identical illustrative scenes: two frozen historical windows and one synthetic leisure/music scene. Strict output validation accepted **1/3 baseline and 2/3 candidate** (ad-hoc comparison receipts; not a controlled reliability estimate). All malformed output retained; no extraction of embedded JSON or retries to green. No audio rendered or Discord idea emitted.
- **Sol semantic review:** simply appending the new traits to the existing digest did not demonstrate a balanced personality. Both arms remained preoccupied with risk, account liability and control; even the candidate leisure response emphasized the absence of sponsorship and risk. The observation response also imports account-risk framing into a physical scavenging discussion without fresh scene support. The GM's earlier acceptance of optional drafts remains respected; this is a concern about range/context fit, not an automatic veto of those accepted lines.
- Historical scenes use current characterization counterfactually, not a reconstruction of historical knowledge. These are illustrative, non-held-out, non-human-rated probes—not usefulness, frequency, latency, safety or personality acceptance benchmarks. One stochastic sample per arm cannot establish an improvement.
- Current live activation, persona and prompt-addendum hashes matched at end of work (ad-hoc file comparison). No active bridge source/config edit or restart. Live bridge remains the previously accepted Initiative 1.001 build; the new compiler is only in its feature checkout.

## Still open

1. GM review of the readable draft and actual refinements, including any desired differences between wanting attention, enjoying craft and reacting to help.
2. A compact candidate projection that replaces redundant attitude framing rather than merely appending traits, preserves approved hard limits and treats the profile as characterization rather than hidden knowledge.
3. A broader frozen GM-labeled comparison set with held-out cases, human evaluation and output-schema completion checks. Keep pleasure, cooperation, humor and relationship reads alongside genuine autonomy concerns; do not tune the latter out just to get pleasant answers.
4. Separately reviewed activation/pin update if the candidate earns approval. This new wiki tooling page is not bound into the live voice registry; publication is not prompt injection into the direct Qwen caller. No future background work scheduled or automatic activation promised.

## Corrections

The first Qwen response included explanatory text and a fenced source block; Sol extracted the complete code block without rewriting the implementation. Initial review/tests exposed an extra compiled key and newline-accepting ID regex. Two additional review tests were added after source inspection; 21 is the post-review suite, not a claim every test was withheld in advance. Qwen supplied five exact repair replacements, including fullmatch and closed source reads. Its patch envelope had double-escaped newlines/quotes and omitted the final array terminator; Sol normalized only that transport envelope before applying the Qwen replacements. No semantic Sol rewrite of core.py. Initial source, failed tests, raw repair and normalized patch list are retained privately. Host source existence/hash checks do not prove interpretation, disclosure rights, authentication or canon agreement.

Private evidence: personality-profile-20261123 runtime directory, including source-review, implementation receipts, test logs, preview, paired requests/responses and comparison-review. Public documentation contains no raw private transcript or credentials.
