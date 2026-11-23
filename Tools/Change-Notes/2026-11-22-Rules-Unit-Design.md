---
title: General rules-unit retrieval contract — proposed design
type: change-note
visibility: player-safe
canon_status: tooling-reference
updated: 2026-11-22
generated_by: openai/gpt-6.1-sol
generated_at: 2026-11-22
---
# Rules-unit retrieval — design only

## Decision
Change the retrieval unit, not the rules or individual questions. A unit is a bounded,
reviewed section of source text with its governing headings, explicit dependencies,
source revision and coverage. Search should discover that unit directly; get should
return precisely that unit. The answerer still has to interpret it correctly.

This is an additive, default-off interface proposal, not an implemented index,
corpus repair, expanded grant or live change. Production remains the working existing
bridge; isolated candidate 336d706 failed full-handler acceptance (0/8 useful answers).

## Why the previous integration could not work reliably
Its post-retrieval projector required every heading/continuation to have already
been read through page retrieval. The small annotation pilot omitted an alternate
page; another unit was unresolved; a third needed a parent heading outside the read.
Adding unseen sidecar text afterward would bypass that contract, so it refused.

The new contract must authorize the **whole reviewed unit when it is discovered**.
This changes read granularity explicitly; it is not an exception to the already-read
rule and must not be represented as a drop-in page-view fix. New unit locators need
separate host validation and generation approval before any real read is permitted.

## 1. Source and unit manifest
Immutable source bytes remain unchanged. A separate versioned manifest contains:
- `schema_version`, generation ID, independently pinned manifest digest and exact
  underlying source revisions. Sources must remain in the existing edition-admitted
  public SR3 set. A filename, metadata status or model assertion cannot admit a book.
- Unit ID and exact source-heading title/path, each heading backed by source revision,
  page marker, character interval and slice hash. Mixed case is valid; uppercase text
  alone is not proof of a heading. Tables and cross-references are not governing parents.
- Ordered body spans: source identity/revision, page marker, start/end offsets, slice
  hash and paragraph/table role. The manifest declares the offset convention and
  text-decoding version. No arbitrary file paths, model URLs or alternate roots.
- Explicit dependency edges: heading context, continuation, table header/rows or
  separately required rule. Each edge points to exact source spans and records why
  they belong together. A page's mention of another rule is not automatic inheritance.
- `layout_status`, `scope_status`, `unit_completeness`, unresolved dependencies and
  citation status. Proposed values distinguish verified/unknown/held and complete/
  partial/oversized; a boolean confidence shortcut is insufficient.

Candidate extraction can identify headings, paragraph boundaries and tables generically.
It cannot promote candidates to verified layout or scope. The first prototype should
inventory one fixed already-admitted book (proposed: SR3 core), not repeatedly patch
individual failed passages. Freeze representative contiguous review windows spanning
layout/mechanic classes and the known/held-out source witnesses before implementation.
The candidate inventory may cover the book; only reviewed units enter the test serving
partition. Do not claim the whole book is verified from a sample. Human source review
checks ambiguous reading order, governing context and material dependencies.
Unresolved candidates remain held. This is class-wide data normalization, not a branch
for a particular page, character, mechanic or question.

## 2. Discovery and permission contract
Proposed locators use a distinct typed form under `sr3/unit/...`, containing generation
and unit identity—not filesystem paths. Existing `#page-N` requests keep their old
meaning. Neither a model-guessed unit ID nor the manifest alone grants access.

Host-owned search validates the pinned manifest and current admitted source revisions,
then ranks unit title/body terms using the existing lexical approach initially.
Snippets and scores are context, never factual evidence. No embedding rebuild is
assumed: this path currently has no rules embedding/chunk index to refresh.

Search returns up to five bounded candidates with locator, generation, revision,
coverage status and citation status. The existing request-local handle mechanism
records discovered locator+generation+revision. Get accepts only that exact triple
from this turn. A host prefetch may search/read one unit explicitly and record it as
initial evidence; a mere snippet does not count as a read.

Every body/context span must remain within the existing book-level admission, at the
pinned revision. A new unit-generation review approves its exact composition, not
additional books or private roots. Permission to read a unit does not grant its other
pages, neighbors or dependencies separately. Parent/continuation content is available
only when already included in that approved unit, or through another independently
discovered/read unit. No on-demand adjacent-page expansion or hidden extra reads.

## 3. Get response and budgets
A successful response contains locator, generation, revision, host citation mapping,
separate exact body blocks and governing-heading metadata, completeness and unresolved
coverage. Entire serialized unit content, including context metadata, must fit a
proposed conservative **5,700-character cap**. Also preserve the existing downstream
6,000-character passage cap and 24,000-character review-envelope cap; do not rely on
one cap to enforce another. The current 120-line get argument is only a hint in the
SR3 implementation, not a demonstrated enforced limit.

Keep at most two additional searches and two additional reads, reserving counters
before awaiting operations. Initial prefetch remains explicit; no recursive expansion
escapes accounting. Keep the existing 25-second owner, 13-second child and 12-second
fetch limits, model and low reasoning effort. No claim that these limits alone make
answers fast. The existing candidate's 128 thinking / 512 total budget stays unchanged.

If a whole paragraph/table plus required qualifiers cannot fit, return oversized or
incomplete coverage without silently cutting it. Subunits are permissible only where
reviewed dependency closure is complete. Unknown layout or missing material conditions
cannot yield a complete unit. Partial material may be listed as unavailable coverage;
the first prototype should not offer it as answer evidence. Preserve denied, stale,
unavailable and empty distinctions; none implies that a rule does not exist.

## 4. Claims and citations
The model may cite only actual unit reads. Exact quotes must occur contiguously inside
one original body block, never across artificial joins, metadata or snippets. Keep
headings separate from factual quote text. Claim/source binding includes the unit
revision and underlying source-span identity. A citation names the actual book/pages
supporting the quote, not all pages in the unit. Printed folios require existing page
proof; an OCR marker stays explicitly unverified, never a guessed global offset.

Do not silently loosen the current one-quote-per-claim contract. If a single claim
requires multiple noncontiguous evidence spans, it remains unsupported by that contract
unless a separately reviewed bounded multi-span claim change is approved. Context can
disambiguate a quote; it cannot fabricate missing quoted support.

The compact reviewer remains probabilistic, with uncertain distinct from rejected.
No supported verdict overrides a failed source/quote check. Completeness of a unit
is not proof of a correct answer, and a safe refusal is not useful-answer success.

## 5. Acceptance gates (proposed, not measurements)
Freeze before implementation:
- The existing eight answerable / four boundary questions, expected mechanics and
  applicable source witnesses. Add a separately frozen held-out set of the same size
  across at least four mechanic families; the implementer does not receive its gold.
- Synthetic counterexamples for stale source/manifest, forged or foreign handles,
  changed span hashes, unread dependencies, mixed-mechanic headings, unresolved OCR
  order, whole-table overflow, missing qualifiers and quote-across-join attempts.
- Existing campaign/equipment/balance gates and exact output controls.

First gate: structural tests all pass, no source-rights/counter/deadline expansion,
and every known answerable has a reviewed complete unit discoverable within the
existing budgets. Report coverage misses explicitly; do not hide them in accuracy.

Second gate: full-handler known and held-out sets each achieve at least 7/8 correct,
useful answers with applicable citations, **zero wrong factual answers**, and all
four boundary controls appropriate. These small-sample thresholds are proposed gates
for advancing to a voice pilot, not evidence that the system is generally solved.
Report denominator, uncertainty, failures and all attempts. Do not retry until green.
Proposed speed target: median factual handler time at most 10 seconds with no overall
deadline increase; measure before TTS separately from first-audio/user latency.

Final gate: separate synthetic-audio/STT and human playback acceptance, then explicit
activation approval. A text test, code commit or published design is not activation.
The broad suite's known baseline issues remain separately recorded.

## 6. Implementation sequence, awaiting approval
1. Sol freezes the admitted book and review windows, fixtures, criteria and gold/held-out
   separation. No corpus rewrite or bulk library migration.
2. Qwen-low drafts a bounded candidate span/manifest builder and pure read assembler
   in separate small jobs. Sol validates generic logic and actual source relationships;
   machine-generated candidate headings never self-authorize.
3. Sol reviews a new isolated unit generation. Only then wire a default-off search/get
   adapter, preserving existing domains, counters and page-locator behavior.
4. Run discovery coverage first; only after that passes run full handler/negative and
   cross-domain regressions. Separately address malformed action JSON with a generic
   action schema; this reader is not a cure for generation formatting.
5. Present measured pass/fail and remaining gaps. Stop short of live activation.

## Status and evidence
This turn created only design/project documentation. No parser, builder, unit index,
source annotation, model call, configuration change or service restart was performed.
Basis: inspected SR3Reader page search/get, Investigation counters, public model
read/claim limits, and the saved integration failure traces.
[Previous failed integration](2026-11-22-Rule-Review-Integration).
