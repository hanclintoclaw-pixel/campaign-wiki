---
title: SR3 rules diagnostic baseline — 2026-11-22
type: tooling-note
status: diagnosis-complete-awaiting-approval
generated_by: openai/gpt-6.1-sol medium
generated_at: "2026-11-22"
---
# General SR3 rules baseline — diagnosis complete, no production change

## Scope and method
GM approved the bounded diagnostic phase at15:50 November22. Current bridge81e9eeb,
PID24989, existing lexical campaign binding and public SR3 reader were tested unchanged.
The dormant proactive-rules flag is off, but explicit full-source SR3 retrieval works;
turning that flag on is not an evidence-backed fix for these failures.

Frozen set7bed4be3f3d66a8a3a517ad4b12a3c5ef9d950875d44b300b585676fec5e0345:
8 source-answerable core-only questions across combat, magic, Matrix and rigging,
plus4 ambiguity/unavailable controls. Gold read from responsive core text; native PDF
folios checked individually, edition affirmed in PDF front matter. Questions/gold
frozen before testing. Same-author source-informed grading, not blind/unseen acceptance,
not representative whole-library or multispeaker coverage. Post-run responsive alternative
pages40 and134 validated without rewriting frozen gold.

Text path: real thread/public owner, authorized readers and configured Qwen/low transport;
real display formatter, mocked Discord delivery. No operator-agent CLI. Controlled voice:
7 declared cases selected after text review across four domains plus known routing and
unavailable controls; synthetic Southern Kokoro question WAV -> real STT/voice handler/
readers/model -> real display/capped response synthesis, mocked Discord. Every failed
attempt retained. No actual playback/listener or first-audible latency claim. No source
rights, production configuration/code/model, corpus or index changes.

## Text results — keep boundaries separate
- Required requested fact returned correctly:7/8 answerables. One unnecessary refusal.
- Fully cleared answer plus responsive verified printed citation:4/8 answerables.
- Among8 fact-bearing outputs (7 affirmative answers plus the conditional Drain
  explanation),4 met that strict context/qualification/printed-source criterion.
  This is strict output clearance, not a claim that half the numeric facts were wrong.
- Controls:4/4 avoided inventing a specific TN, exact Drain damage, Quasar bonus or
  hidden dice result. However, none is a clean helpful resolution under strict review:
  two misdirected name clarifications, one rules refusal labeled campaign information,
  one conditional explanation with unclear +2 units and an unhelpful spoken head cut.
- All12 handler runs completed without harness exceptions. No full-suite or legacy
  retrieval-proxy pass claimed; this is an unchanged-path final-answer baseline.

Per answerable case:
- Combat action economy: correct two Simple OR one Complex, cited responsive core40.
- Ranged damage staging: wrongly routed as equipment; reviewed-table refusal although
  core113 states two net successes per damage level. A routing miss, not absent data.
- Spellcasting Drain attribute: Willpower is correct, but emitted core169 quote is
  adept Attribute Boost Drain, not Sorcery. Same word/number does not validate context;
  responsive Sorcery source is core162.
- Sustaining: correct +2 TN per sustained spell and Damage Resistance exception;
  responsive Quick Start text retrieved, but printed-page citation explicitly unverified.
- Hacking Pool: correct base (INT + MPCP)/3, round down. Additional cyberware/context
  prose raises qualification burden; emitted Matrix/Man-and-Machine folios unverified.
- Detection Factor: correct average of Masking/Sleaze, round up, responsive core207.
- Manual driving: correct no Control Pool when not rigged, responsive core134.
- Control Pool cap: correct base skill dice limit, responsive core44.

Controls observed:
- Unspecified test TN -> asks character name instead of which test/circumstances.
- Exact Drain with no inputs -> No fixed number plus broad rules; sustaining adds +2
  lacks TN units/scope, final speech is merely No fixed number. No exact damage invented.
- Invented Quasar Pool -> no supporting campaign information, rather than an honest
  domain-correct SR3 boundary. No global nonexistence ruling inferred from grep.
- Hidden GM roll -> Did you mean Seren Hensley? instead of unavailable current evidence.

## Controlled acoustic subset — not a replacement denominator
Five answerable cases:3 requested facts correct,2 unnecessary refusals;2 have verified
responsive printed citations, while sustaining retains its explicitly uncertain citation.
Two controls: no numerical invention, but the wrong-domain refusal and irrelevant name
hypothesis recur. All7 emitted displays preserved the complete formatted replies; all7
response WAVs synthesized successfully, durations2.475–14.225seconds. No human audition.

Text-successful action economy became a generic public-owner error/refusal after a
search. The exact cause is unclassified, not proven to be ASR alone; recognized wording
retained the action alternatives, with synthetic my -> maw accent noise. Do not retry it
out of the scorecard. Detection Factor survived running -> run-in recognition noise.
Ranged-staging equipment refusal reproduced after actual STT. Sustaining, Detection
Factor and non-rigged Control Pool facts/qualifications survived into final spoken text.

Text answerables took0.18–14.93s including the fast failed refusal; the ambiguous Drain
case took20.87s. These are handler timings, not audible latency. For the3 correct voice
answers, STT+handler took8.19–12.52s before response synthesis. One voice error/refusal
took21.31s. WAV duration is not response time; no first-audible/Discord SLA is inferred.

## Findings and recommendation for separate approval
1. Repair shared question-kind/domain admission and clarification first: distinguish
   rules mechanics from named equipment, campaign identities and unavailable current
   observations; require missing test parameters rather than unrelated name recovery.
   Preserve real named-item/gear and campaign-negative controls. No per-question/PC fixes.
2. Strengthen responsive mechanic context and provenance, not merely word overlap:
   spellcasting Drain must not be sourced to adept Boost. Preserve complete units,
   exceptions and source-page uncertainty; do not invent folios or repair books silently.
3. Make refusals domain-correct and useful in speech; then investigate the generic
   owner error/model-loop latency with bounded retained replays. Do not attribute the
   one error to ASR or fix latency by raising effort/changing models without evidence.

Do not start broad corpus cleanup, bulk page conversion or another gear-table expansion.
The corpus supplied all8 positive gold rules; data availability alone does not make the
current interpretation/answer path reliable. Proposed next implementation is a bounded
shared admission/clarification repair, frozen cross-domain controls and source-context
checks, followed by the same12-case replay. Code/source expansion/activation need their
own approval. The working campaign pilot remains live and unchanged.

## Evidence
Private runtime/sr3-rules-baseline-20261122: frozen-set+hash, source-review, native PDF
page witnesses, text-1/report+per-case traces, text-scorecard, audio-1 selection/questions/
results/WAVs, voice-scorecard and preservation receipt. Source harnesses under matching
workfiles folder. The action checker rejects intentionally wrong control answers;
semantic/context grades remain explicit same-author review, not automatic accuracy.
