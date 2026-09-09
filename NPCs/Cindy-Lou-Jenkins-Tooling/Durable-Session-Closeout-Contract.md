---
title: Cindy Lou Durable Session Closeout Contract
type: tech-note
visibility: player-safe
status: active
updated: 2026-09-09
tags: [cindy, closeout, wiki, automation, skill, workflow]
---

# Cindy Lou Durable Session Closeout Contract

This page documents the durable process reminder for Cindy's post-session summary and wiki-ingest workflow.

The goal is simple: vague requests such as "summarize last night," "do the wiki update," "close out the latest game," or "ingest yesterday's session" should route into the same evidence-first workflow instead of becoming a free-form chat summary.

## Durable process layer

The standing workflow is captured as a pending OpenClaw Skill Workshop proposal:

- Proposal: `cindy-session-closeout-contract-20260909-204f374a02`
- Skill name: `cindy-session-closeout-contract`
- Purpose: make Cindy's Shadowrun session closeout process repeatable across model changes and lower-token operation.

When applied, the skill should trigger for session recap, closeout, wiki-ingest, and "last night / latest game" phrasing. It tells Cindy to run the local closeout command first, then work from the generated artifacts rather than raw memory or broad transcript context.

## Local command layer

The local command is:

```bash
cindy-session-closeout
```

It is symlinked from `~/.local/bin` to:

```bash
/Users/hanclaw/claw/projects/cindylou/campaign-wiki/scripts/cindy-session-closeout
```

The command accepts fuzzy intent text:

```bash
cindy-session-closeout summarize last night
cindy-session-closeout do the wiki update
cindy-session-closeout close out the latest game
cindy-session-closeout ingest yesterday
```

Plain invocation prepares a closeout workspace. It does not publish by itself.

## Generated workspace

The command writes a low-token workspace under:

```bash
/Volumes/carbonite/claw/data/cindylou/runtime/session-closeout/<session-id>/
```

Current artifacts:

- `closeout-packet.md` - compact evidence packet and operational instructions.
- `closeout-facts.json` - structured source, authenticity, resolver, candidate output, and clarification facts.
- `closeout-plan.json` - workflow phases, hard stops, and model context order.
- `wiki-context.md` - capped wiki snapshots for required sweep surfaces.
- `agent-prompt.md` - small prompt for a local model/coding agent.
- `manifest.json` - checklist, expected pages, and acceptance criteria.

The important behavior is path-first prompting: the model starts from these files and opens the full transcript only for targeted follow-up.

## Source and authenticity rules

For fuzzy/default invocation, the command now prefers the best recent archived transcript by authentic-session score instead of blindly using newest file modification time.

It records:

- source resolver notes;
- transcript row counts;
- transcript duration;
- authentic-session signal count;
- authenticity verdict: `authentic`, `provisional`, or `not_authentic`;
- concrete clarification flags.

Mutating runs refuse non-authentic transcripts unless explicitly overridden:

```bash
cindy-session-closeout summarize last night --run-agent
cindy-session-closeout summarize last night --run-agent --allow-inauthentic
```

`--allow-inauthentic` should mean "the GM intentionally approved a provisional/manual run," not "skip the check because it is annoying."

## Mutation and publication rules

The command keeps publication explicit:

- no flag: prepare workspace only;
- `--run-agent`: feed `agent-prompt.md` to the configured local agent;
- `--commit`: commit validated wiki changes;
- `--push`: push after commit.

Mutating runs still refuse dirty campaign-wiki worktrees unless `--allow-dirty` is supplied.

The commit step stages only expected wiki content areas, not every dirty file in the repository.

## Lower-gear model contract

The lower-gear model should not be asked to infer the whole process from chat history.

It should do narrower work:

- classify/authenticate from `closeout-facts.json`;
- extract facts from `closeout-packet.md`;
- draft player-safe prose from structured facts;
- update the bounded wiki surfaces in `manifest.json`;
- validate and report concrete blockers.

The deterministic command owns source choice, preflight, artifact layout, and hard stops. The model owns judgment and prose.

## Required outcome

Every closeout should end with exactly one operational outcome:

- `publish-ready ingest`
- `draft/provisional ingest`
- `needs GM clarification`
- `no authentic session found`

The final report should include the session source, authenticity verdict, changed or explicitly unchanged wiki surfaces, unresolved GM questions, and commit/push/deploy status when applicable.

## Related pages

- [Cindy Lou Post-Session Automation](Post-Session-Automation.md)
- [Cindy Lou Session Scratchpad Implementation Plan](Session-Scratchpad-Implementation-Plan.md)
- [Cindy Lou Live Session Capture and Replay](Live-Session-Capture-and-Replay.md)
