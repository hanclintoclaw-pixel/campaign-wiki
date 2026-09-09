#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_ROOT = Path("/Volumes/carbonite/claw/data/cindylou/runtime/session-closeout")
DEFAULT_LIVE_SESSION_CANDIDATES = [
    Path(os.environ.get("LIVE_SESSION_DIR", "")).expanduser() if os.environ.get("LIVE_SESSION_DIR") else None,
    Path("/Volumes/carbonite/claw/data/cindylou/runtime/live-session"),
    Path.home() / ".openclaw/workspace-cindylou/runtime/live-session",
]
REQUIRED_SWEEP_PATHS = [
    "Sessions/",
    "index.md",
    "Current-State.md",
    "Timeline/Session-Chronology.md",
    "Clues/README.md",
    "Arcs/README.md",
    "NPCs/README.md",
    "PCs/README.md",
    "Locations/README.md",
    "Factions/README.md",
    "Organizations/README.md",
]

DATE_RE = re.compile(
    r"\b(?:20\d{2}-\d{2}-\d{2}|206\d(?:[-/ ]\d{1,2}[-/ ]\d{1,2})?|"
    r"(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)|"
    r"(?:tonight|tomorrow|next day|next morning|this evening|that evening|court next day))\b",
    re.IGNORECASE,
)
REWARD_RE = re.compile(
    r"\b(?:karma|nuyen|\u00a5|yen|payout|pay(?:day|ment|s|ing|ed)?|paid|reward|fee|bonus|"
    r"expense|cost|spent|spend|ledger|gear|loot|damage|favor|contact|heat|reputation|rep)\b",
    re.IGNORECASE,
)
STOP_RE = re.compile(
    r"\b(?:session|closeout|wrap|wrapped|done|stop(?:ped)?|end(?:ed)?|hard out|next week|next thursday|"
    r"thank you for joining|enjoyed yourself|same time)\b",
    re.IGNORECASE,
)
AUTHENTIC_RE = re.compile(
    r"\b(?:roll|test|target number|karma|nuyen|johnson|run|crew|judge|court|bodyguard|"
    r"matrix|spell|combat|initiative|legwork|stakeout|contact|npc|shadowrun)\b",
    re.IGNORECASE,
)
SESSION_CLOSEOUT_INTENT_RE = re.compile(
    r"\b(?:summari[sz]e|recap|close\s*out|closeout|ingest|wiki\s*update|session\s*update|"
    r"update\s*(?:the\s*)?wiki|last\s*night|yesterday|latest\s*(?:game|session)|after\s*session)\b",
    re.IGNORECASE,
)


def parse_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                row = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on {path}:{line_no}: {exc}") from exc
            if isinstance(row, dict):
                rows.append(row)
    return rows


def row_text(row: dict[str, Any]) -> str:
    return str(row.get("text") or row.get("content") or "")


def read_text_if_exists(path: Path, max_chars: int) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n\n[truncated]"


def read_markdown_context(path: Path, max_chars: int, *, tail_chars: int = 3500) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if len(text) <= max_chars:
        return text
    tail_budget = min(tail_chars, max(1000, max_chars // 3))
    head_budget = max_chars - tail_budget
    return (
        text[:head_budget].rstrip()
        + "\n\n[truncated middle; preserving latest/lower-page context]\n\n"
        + text[-tail_budget:].lstrip()
    )


def first_existing_live_session_dir() -> Path:
    for candidate in DEFAULT_LIVE_SESSION_CANDIDATES:
        if candidate and candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError("No live-session directory found; pass --session-dir or --transcript")


def transcript_authenticity(
    rows: list[dict[str, Any]],
    *,
    min_rows: int,
    min_hits: int,
    min_duration_s: int,
) -> dict[str, Any]:
    timestamps = [ts for ts in (parse_timestamp(row.get("timestamp")) for row in rows) if ts]
    text_rows = [row for row in rows if row_text(row).strip()]
    authentic_hits = sum(1 for row in text_rows if AUTHENTIC_RE.search(row_text(row)))
    duration_s = 0
    if timestamps:
        duration_s = int(max(0.0, (max(timestamps) - min(timestamps)).total_seconds()))

    has_rows = len(text_rows) >= min_rows
    has_hits = authentic_hits >= min_hits
    has_duration = duration_s >= min_duration_s if timestamps else True
    dense_hits = authentic_hits >= max(min_hits * 2, 10) and len(text_rows) >= max(12, min_rows // 3)

    if (has_rows and has_hits and has_duration) or dense_hits:
        verdict = "authentic"
    elif has_hits or (has_rows and authentic_hits >= max(2, min_hits // 2)):
        verdict = "provisional"
    else:
        verdict = "not_authentic"
    return {
        "verdict": verdict,
        "text_rows": len(text_rows),
        "authentic_hits": authentic_hits,
        "duration_s": duration_s,
        "has_timestamps": bool(timestamps),
        "min_rows": min_rows,
        "min_hits": min_hits,
        "min_duration_s": min_duration_s,
    }


def candidate_session_score(info: dict[str, Any]) -> tuple[int, int, int, float]:
    auth = info.get("authenticity", {})
    verdict_rank = {"authentic": 2, "provisional": 1, "not_authentic": 0}.get(str(auth.get("verdict")), 0)
    return (
        verdict_rank,
        int(auth.get("authentic_hits", 0) or 0),
        int(auth.get("text_rows", 0) or 0),
        float(info.get("mtime", 0.0) or 0.0),
    )


def archived_session_candidates(live_session_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    sessions_dir = live_session_dir / "sessions"
    if not sessions_dir.exists():
        raise FileNotFoundError(f"No archived sessions directory found at {sessions_dir}")
    paths = [path for path in sessions_dir.iterdir() if (path / "transcript.jsonl").exists()]
    if not paths:
        raise FileNotFoundError(f"No archived session transcript found under {sessions_dir}")
    cutoff = datetime.now().timestamp() - max(1, int(args.source_window_hours * 3600))
    candidates: list[dict[str, Any]] = []
    for path in paths:
        transcript = path / "transcript.jsonl"
        mtime = transcript.stat().st_mtime
        if args.source_window_hours > 0 and mtime < cutoff:
            continue
        try:
            rows = read_jsonl(transcript)
            authenticity = transcript_authenticity(
                rows,
                min_rows=args.authentic_min_rows,
                min_hits=args.authentic_min_hits,
                min_duration_s=args.authentic_min_duration_s,
            )
        except Exception as exc:
            authenticity = {
                "verdict": "not_authentic",
                "error": str(exc),
                "text_rows": 0,
                "authentic_hits": 0,
                "duration_s": 0,
            }
        candidates.append({
            "session_dir": path.resolve(),
            "transcript_path": transcript.resolve(),
            "mtime": mtime,
            "authenticity": authenticity,
        })
    if not candidates and args.source_window_hours > 0:
        original_window = args.source_window_hours
        args.source_window_hours = 0
        candidates = archived_session_candidates(live_session_dir, args)
        for candidate in candidates:
            candidate.setdefault("resolver_notes", []).append(f"no candidates found inside {original_window:g}h window; widened to all archives")
    return sorted(candidates, key=candidate_session_score, reverse=True)


def resolve_session(args: argparse.Namespace) -> dict[str, Any]:
    if args.transcript:
        transcript = args.transcript.expanduser().resolve()
        return {"session_dir": transcript.parent, "transcript_path": transcript, "resolver_notes": ["explicit transcript path"]}
    if args.session_dir:
        session_dir = args.session_dir.expanduser().resolve()
        return {"session_dir": session_dir, "transcript_path": session_dir / "transcript.jsonl", "resolver_notes": ["explicit session directory"]}
    live_session_dir = first_existing_live_session_dir()
    if args.current:
        return {"session_dir": live_session_dir, "transcript_path": live_session_dir / "transcript.jsonl", "resolver_notes": ["current live-session transcript requested"]}
    candidates = archived_session_candidates(live_session_dir, args)
    selected = candidates[0]
    notes = selected.setdefault("resolver_notes", [])
    notes.extend([
        f"selected best archived transcript from {len(candidates)} candidate(s)",
        f"source window hours: {args.source_window_hours:g}",
    ])
    if selected["authenticity"].get("verdict") != "authentic":
        notes.append("no fully authentic recent session candidate found; selected highest-scoring candidate for preservation/review")
    selected["candidate_count"] = len(candidates)
    return selected


def display_line(row: dict[str, Any]) -> str:
    timestamp = str(row.get("timestamp") or "").strip()
    speaker = str(row.get("speaker") or row.get("author") or "Unknown").strip()
    text = " ".join(row_text(row).split())
    return f"- {timestamp} | {speaker}: {text}"


def matching_rows(rows: Iterable[dict[str, Any]], pattern: re.Pattern[str], limit: int) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for row in rows:
        text = row_text(row)
        if pattern.search(text):
            matches.append(row)
    return matches[-limit:]


def unique_ordered(values: Iterable[Any], limit: int) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
        if len(out) >= limit:
            break
    return out


def infer_session_date(rows: list[dict[str, Any]], session_dir: Path) -> str:
    match = re.match(r"(20\d{2}-\d{2}-\d{2})", session_dir.name)
    if match:
        return match.group(1)
    for row in rows:
        ts = parse_timestamp(row.get("timestamp"))
        if ts:
            return ts.date().isoformat()
    return "YYYY-MM-DD"


def compact_excerpt(rows: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if len(rows) <= limit:
        return rows
    head_count = max(3, limit // 5)
    tail_count = max(6, limit // 5)
    middle_count = max(0, limit - head_count - tail_count)
    step = max(1, (len(rows) - head_count - tail_count) // max(1, middle_count))
    middle = rows[head_count : len(rows) - tail_count : step][:middle_count]
    return rows[:head_count] + middle + rows[-tail_count:]


def load_markers(session_dir: Path, limit: int) -> list[str]:
    path = session_dir / "gm-control-panel-markers.jsonl"
    if not path.exists():
        return []
    markers = read_jsonl(path)
    lines: list[str] = []
    for marker in markers[-limit:]:
        marker_type = str(marker.get("marker_type") or "marker").strip()
        label = str(marker.get("label") or "").strip()
        note = str(marker.get("note") or "").strip()
        timestamp = str(marker.get("timestamp") or marker.get("created_at") or "").strip()
        if note:
            label_text = f" ({label})" if label else ""
            lines.append(f"- {timestamp} | {marker_type}{label_text}: {note}")
    return lines


def render_lines(rows: Iterable[dict[str, Any]]) -> str:
    lines = [display_line(row) for row in rows]
    return "\n".join(lines) if lines else "- None found in transcript packet."


def infer_intent(args: argparse.Namespace) -> dict[str, Any]:
    phrase = " ".join(args.intent or []).strip()
    recognized = bool(SESSION_CLOSEOUT_INTENT_RE.search(phrase)) if phrase else True
    lowered = phrase.lower()
    if phrase and not any([args.current, args.session_dir, args.transcript]):
        if any(token in lowered for token in ["current", "live", "right now", "ongoing"]):
            args.current = True
    if phrase and any(token in lowered for token in ["preview", "show packet", "print packet"]):
        args.print = True
    return {
        "phrase": phrase,
        "recognized": recognized,
        "source_hint": "current" if args.current else ("explicit" if args.session_dir or args.transcript else "latest-authentic-archive"),
        "requested_operation": "wiki-closeout" if recognized else "unknown",
    }


def git(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=check,
    )


def porcelain_paths() -> list[str]:
    result = git(["status", "--porcelain"], check=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def require_clean_worktree(allow_dirty: bool) -> None:
    dirty = porcelain_paths()
    if dirty and not allow_dirty:
        joined = "\n".join(dirty)
        raise RuntimeError(
            "Refusing to run a mutating closeout with a dirty campaign-wiki worktree. "
            "Commit/stash unrelated changes or pass --allow-dirty.\n" + joined
        )


def build_packet(args: argparse.Namespace) -> dict[str, Any]:
    intent = infer_intent(args)
    resolved = resolve_session(args)
    session_dir = resolved["session_dir"]
    transcript_path = resolved["transcript_path"]
    if not transcript_path.exists():
        raise FileNotFoundError(f"Transcript not found: {transcript_path}")

    rows = read_jsonl(transcript_path)
    if not rows:
        raise ValueError(f"Transcript is empty: {transcript_path}")

    timestamps = [ts for ts in (parse_timestamp(row.get("timestamp")) for row in rows) if ts]
    speakers = Counter(str(row.get("speaker") or row.get("author") or "Unknown").strip() for row in rows)
    text_rows = [row for row in rows if row_text(row).strip()]
    authenticity = transcript_authenticity(
        rows,
        min_rows=args.authentic_min_rows,
        min_hits=args.authentic_min_hits,
        min_duration_s=args.authentic_min_duration_s,
    )
    authentic_hits = int(authenticity.get("authentic_hits", 0) or 0)
    session_date = infer_session_date(rows, session_dir)
    session_id = session_dir.name
    first_ts = min(timestamps).isoformat() if timestamps else "unknown"
    last_ts = max(timestamps).isoformat() if timestamps else "unknown"
    thread_ids = unique_ordered((row.get("thread_id") for row in rows), 6)
    channel_ids = unique_ordered((row.get("channel_id") for row in rows), 6)
    markers = load_markers(session_dir, args.marker_limit)

    date_rows = matching_rows(text_rows, DATE_RE, args.evidence_limit)
    reward_rows = matching_rows(text_rows, REWARD_RE, args.evidence_limit)
    stop_rows = matching_rows(text_rows, STOP_RE, args.evidence_limit)
    tail_rows = text_rows[-args.tail_limit :]
    sampled_rows = compact_excerpt(text_rows, args.transcript_lines)

    out_dir = (args.out_dir or DEFAULT_OUTPUT_ROOT / session_id).expanduser().resolve()
    out_path = out_dir / "closeout-packet.md"

    speaker_lines = "\n".join(f"- {speaker}: {count} transcript rows" for speaker, count in speakers.most_common())
    marker_text = "\n".join(markers) if markers else "- None found."
    thread_text = ", ".join(thread_ids) if thread_ids else "unknown"
    channel_text = ", ".join(channel_ids) if channel_ids else "unknown"
    resolver_text = "\n".join(f"- {note}" for note in resolved.get("resolver_notes", [])) or "- None."
    authenticity_verdict = str(authenticity.get("verdict") or "unknown")
    clarification_flags = []
    if not date_rows:
        clarification_flags.append("in-world date/time not found in evidence packet")
    if not reward_rows:
        clarification_flags.append("final rewards/ledger changes not found in evidence packet")
    if authenticity_verdict != "authentic":
        clarification_flags.append(f"transcript authenticity is {authenticity_verdict}")
    clarification_text = "\n".join(f"- {flag}" for flag in clarification_flags) if clarification_flags else "- None from deterministic preflight."

    packet = f"""# Cindy session closeout packet: {session_id}

## Deterministic source facts

- Invoked intent phrase: `{intent['phrase'] or 'default closeout'}`
- Intent recognized as closeout: {intent['recognized']}
- Session id: `{session_id}`
- Transcript: `{transcript_path}`
- Transcript rows: {len(rows)} total / {len(text_rows)} with text
- First transcript timestamp: {first_ts}
- Last transcript timestamp / likely stopped-at time: {last_ts}
- Discord channel ids: {channel_text}
- Discord thread ids: {thread_text}
- Authentic-session verdict: {authenticity_verdict}
- Authentic-session signal rows: {authentic_hits}
- Transcript duration seconds: {authenticity.get('duration_s', 0)}
- Candidate wiki session page: `Sessions/{session_date}.md`
- Closeout packet path: `{out_path}`

## Source resolver notes

{resolver_text}

## Preflight clarification flags

{clarification_text}

## Attendance evidence

{speaker_lines}

## GM panel closeout markers

{marker_text}

## Candidate in-world date / time evidence

Use these transcript lines first. Infer the in-world date/time from table statements when possible. If they conflict or are absent, mark the session provisional and ask one compact clarification.

{render_lines(date_rows)}

## Reward / ledger / character-state evidence

Use transcript evidence for rewards and ledgers first. Extract Karma, nuyen, gear, damage, favors, contacts, heat, reputation, expenses, and unresolved accounting. If no final award is present, write that no final award was recorded yet.

{render_lines(reward_rows)}

## Session stop / closeout evidence

Use the transcript stop time above as the default session end unless this evidence says otherwise.

{render_lines(stop_rows)}

## Last transcript lines

{render_lines(tail_rows)}

## Minimal agent instructions

Run the closeout as a wiki maintenance sweep, not as a generic summary.

1. Read this packet, then inspect only the linked/current wiki surfaces needed for the changed entities and active leads.
2. Create or update `Sessions/{session_date}.md` using the session template sections: Summary, Major Scenes, NPCs Introduced / In Play, Clues Gained, Decisions Made, Rewards / Ledgers, Changes to Campaign State, Open Threads, Sources.
3. Pull in-world date/time, rewards, and stopped-at time from transcript evidence before asking the GM. Ask only about facts that remain ambiguous.
4. Sweep the wiki for required consistency changes: `index.md` Current Situation, `Current-State.md`, `Timeline/Session-Chronology.md`, `Clues/README.md` lead board, relevant PC/NPC/Location/Faction/Organization/Arc pages and indexes.
5. Keep player-visible pages player-safe. Preserve GM-only marker notes only in private/local notes unless the GM explicitly approves them for public canon.
6. Use `scripts/update_current_campaign_state.py` for approved front-page/current-state section replacement when practical.
7. Finish only when session page, Current Situation, Current State, chronology, and lead board either agree or have an explicit "unchanged / needs clarification" note.

## Closeout outcome contract

Return exactly one operational outcome in the final report:

- publish-ready ingest: wiki pages are updated, linked, committed, and ready/deployed if appropriate;
- draft/provisional ingest: wiki pages are updated but date/reward/canon status needs GM confirmation;
- needs GM clarification: no public publish because one or more concrete blockers remain;
- no authentic session found: transcript did not contain enough campaign-play evidence.

## Compact transcript sample

This is only for orientation. Prefer the evidence sections above, then inspect the full transcript only for disputed or missing facts.

{render_lines(sampled_rows)}
"""
    return {
        "intent": intent,
        "session_dir": session_dir,
        "transcript_path": transcript_path,
        "session_id": session_id,
        "session_date": session_date,
        "first_timestamp": first_ts,
        "last_timestamp": last_ts,
        "rows": len(rows),
        "text_rows": len(text_rows),
        "authenticity": authenticity,
        "authentic_hits": authentic_hits,
        "clarification_flags": clarification_flags,
        "resolver_notes": resolved.get("resolver_notes", []),
        "packet": packet,
        "out_dir": out_dir,
        "packet_path": out_path,
    }


def build_wiki_context(session_date: str) -> str:
    session_path = REPO_ROOT / "Sessions" / f"{session_date}.md"
    existing_session = read_markdown_context(session_path, 8000)
    current_state = read_markdown_context(REPO_ROOT / "Current-State.md", 9000)
    index_page = read_markdown_context(REPO_ROOT / "index.md", 5000)
    chronology = read_markdown_context(REPO_ROOT / "Timeline" / "Session-Chronology.md", 10000)
    clues = read_markdown_context(REPO_ROOT / "Clues" / "README.md", 10000)
    template = read_text_if_exists(REPO_ROOT / "meta" / "TEMPLATE.session.md", 4000)
    path_list = "\n".join(f"- `{path}`" for path in REQUIRED_SWEEP_PATHS)
    existing_text = existing_session or "No existing candidate session page found. Create it if the transcript is authentic."
    return f"""# Compact wiki context for session closeout

## Required sweep surfaces

{path_list}

## Candidate session template

```markdown
{template}
```

## Existing candidate session page

```markdown
{existing_text}
```

## Current front page snapshot

```markdown
{index_page}
```

## Current State snapshot

```markdown
{current_state}
```

## Session Chronology snapshot

```markdown
{chronology}
```

## Lead Board snapshot

```markdown
{clues}
```
"""


def build_agent_prompt(packet_path: Path, wiki_context_path: Path, manifest_path: Path, facts_path: Path, plan_path: Path, session_date: str) -> str:
    return f"""You are running Cindy Lou's local post-session closeout workflow inside the campaign-wiki repository.

Objective: summarize the session transcript and perform the full player-safe wiki closeout while minimizing broad context reads.

Start with these local files:
- Closeout evidence packet: `{packet_path}`
- Structured facts: `{facts_path}`
- Workflow plan/contract: `{plan_path}`
- Compact wiki context: `{wiki_context_path}`
- Run manifest/checklist: `{manifest_path}`

Required behavior:
1. Read the closeout packet, structured facts, and workflow plan first. Use their evidence sections before opening the full transcript.
2. Use the transcript path from the packet for targeted follow-up searches only when the packet is insufficient.
3. If structured facts say authenticity is not `authentic`, stop with `no authentic session found` or `needs GM clarification` unless the GM explicitly approved provisional ingest.
4. Infer in-world date/time, rewards/ledgers, and stopped-at time from transcript evidence first. Ask the GM only when evidence is absent or contradictory.
5. Create or update `Sessions/{session_date}.md` with Summary, Major Scenes, NPCs Introduced / In Play, Clues Gained, Decisions Made, Rewards / Ledgers, Changes to Campaign State, Open Threads, and Sources.
6. Create new pages for newly introduced NPCs, PCs, locations, factions, organizations, arcs, vehicles, Matrix hosts, or other durable entities that need wiki records. Update existing PC/NPC/location/faction/org/arc records when the transcript changes their state.
7. Update cross-links and relevant indexes so the new pages are reachable.
8. Update `index.md` Current Situation, `Current-State.md`, `Timeline/Session-Chronology.md`, and `Clues/README.md` if the session changes them. If one is unchanged, leave a clear reason in the final report.
9. Keep public pages player-safe. Do not publish GM-only marker content unless the GM explicitly marked it public-safe.
10. Preserve uncertainty honestly: provisional canon status is better than confident wrong canon.
11. Run available repository checks such as `git diff --check`; do not invent new build tooling.

Do not stop after drafting a summary. The expected output is the wiki mutation itself plus a concise final report with exactly one closeout outcome: publish-ready ingest, draft/provisional ingest, needs GM clarification, or no authentic session found.
"""


def write_workspace(packet_info: dict[str, Any]) -> dict[str, Path]:
    out_dir = packet_info["out_dir"]
    packet_path = packet_info["packet_path"]
    wiki_context_path = out_dir / "wiki-context.md"
    prompt_path = out_dir / "agent-prompt.md"
    manifest_path = out_dir / "manifest.json"
    facts_path = out_dir / "closeout-facts.json"
    plan_path = out_dir / "closeout-plan.json"

    out_dir.mkdir(parents=True, exist_ok=True)
    packet_path.write_text(packet_info["packet"], encoding="utf-8")
    wiki_context_path.write_text(build_wiki_context(packet_info["session_date"]), encoding="utf-8")
    source_artifacts = {
        "event_ledger": str(packet_info["session_dir"] / "event-ledger.jsonl"),
        "scene_scratchpad": str(packet_info["session_dir"] / "scene-scratchpad.json"),
        "prompt_view": str(packet_info["session_dir"] / "prompt-view.json"),
        "recent_delta": str(packet_info["session_dir"] / "recent-delta.json"),
        "gm_markers": str(packet_info["session_dir"] / "gm-control-panel-markers.jsonl"),
    }
    facts = {
        "schema": "cindylou.session-closeout-facts/v1",
        "intent": packet_info["intent"],
        "session_id": packet_info["session_id"],
        "session_date": packet_info["session_date"],
        "first_timestamp": packet_info["first_timestamp"],
        "last_timestamp": packet_info["last_timestamp"],
        "transcript_path": str(packet_info["transcript_path"]),
        "row_counts": {
            "total": packet_info["rows"],
            "text": packet_info["text_rows"],
        },
        "authenticity": packet_info["authenticity"],
        "resolver_notes": packet_info["resolver_notes"],
        "clarification_flags": packet_info["clarification_flags"],
        "source_artifacts": {
            name: {"path": path, "exists": Path(path).exists()}
            for name, path in source_artifacts.items()
        },
        "candidate_public_outputs": {
            "session_page": f"Sessions/{packet_info['session_date']}.md",
            "front_page": "index.md",
            "current_state": "Current-State.md",
            "chronology": "Timeline/Session-Chronology.md",
            "lead_board": "Clues/README.md",
        },
    }
    facts_path.write_text(json.dumps(facts, indent=2) + "\n", encoding="utf-8")

    plan = {
        "schema": "cindylou.session-closeout-plan/v1",
        "outcome_contract": [
            "publish-ready ingest",
            "draft/provisional ingest",
            "needs GM clarification",
            "no authentic session found",
        ],
        "phases": [
            "preflight/authenticate",
            "extract structured facts",
            "draft or update session page",
            "sweep current situation/current state/chronology/lead board",
            "update changed entity pages and indexes",
            "validate public safety, links, and required sections",
        ],
        "model_context_order": [
            str(prompt_path),
            str(packet_path),
            str(facts_path),
            str(plan_path),
            str(wiki_context_path),
            "targeted transcript/source artifact lookups only when needed",
        ],
        "hard_stops": [
            "Do not publish if authenticity.verdict is not authentic unless GM explicitly approves provisional ingest.",
            "Do not publish GM-only marker text to player-visible pages.",
            "Do not invent date, rewards, or ledger outcomes when transcript evidence is absent.",
        ],
    }
    plan_path.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "schema": "cindylou.session-closeout/v2",
        "session_id": packet_info["session_id"],
        "session_date": packet_info["session_date"],
        "repo_root": str(REPO_ROOT),
        "session_dir": str(packet_info["session_dir"]),
        "transcript_path": str(packet_info["transcript_path"]),
        "packet_path": str(packet_path),
        "facts_path": str(facts_path),
        "plan_path": str(plan_path),
        "wiki_context_path": str(wiki_context_path),
        "prompt_path": str(prompt_path),
        "candidate_session_page": f"Sessions/{packet_info['session_date']}.md",
        "authenticity": packet_info["authenticity"],
        "clarification_flags": packet_info["clarification_flags"],
        "required_sweep_paths": REQUIRED_SWEEP_PATHS,
        "acceptance": [
            "session page created or updated",
            "Current Situation explicitly changed or reported unchanged",
            "Current-State explicitly changed or reported unchanged",
            "Session Chronology explicitly changed or reported unchanged",
            "Lead Board explicitly changed or reported unchanged",
            "changed entities/pages linked from an index or parent page",
            "date/reward/ledger uncertainty either resolved from transcript or reported as GM clarification",
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    prompt_path.write_text(
        build_agent_prompt(packet_path, wiki_context_path, manifest_path, facts_path, plan_path, packet_info["session_date"]),
        encoding="utf-8",
    )
    return {
        "packet": packet_path,
        "wiki_context": wiki_context_path,
        "prompt": prompt_path,
        "manifest": manifest_path,
        "facts": facts_path,
        "plan": plan_path,
    }


def run_agent(command: str, prompt_path: Path, log_path: Path) -> None:
    prompt_text = prompt_path.read_text(encoding="utf-8")
    if "{prompt}" in command or "{prompt_path}" in command:
        rendered = command.format(prompt=shlex.quote(str(prompt_path)), prompt_path=shlex.quote(str(prompt_path)))
        stdin_text = None
    else:
        rendered = command
        stdin_text = prompt_text
    with log_path.open("w", encoding="utf-8") as log:
        result = subprocess.run(
            rendered,
            cwd=REPO_ROOT,
            shell=True,
            input=stdin_text,
            text=True,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
    if result.returncode != 0:
        raise RuntimeError(f"Agent command failed with exit code {result.returncode}; see {log_path}")


def validate_closeout(session_date: str) -> list[str]:
    issues: list[str] = []
    changed = porcelain_paths()
    if not changed:
        issues.append("No campaign-wiki file changes detected after closeout run.")
    session_path = REPO_ROOT / "Sessions" / f"{session_date}.md"
    if not session_path.exists():
        issues.append(f"Candidate session page is missing: Sessions/{session_date}.md")
    for path in ["index.md", "Current-State.md", "Timeline/Session-Chronology.md", "Clues/README.md"]:
        if not (REPO_ROOT / path).exists():
            issues.append(f"Required sweep surface is missing: {path}")
    diff_check = git(["diff", "--check"], check=False)
    if diff_check.returncode != 0:
        issues.append("git diff --check failed:\n" + diff_check.stdout.strip())
    return issues


def commit_and_push(args: argparse.Namespace, session_date: str) -> None:
    if not args.commit and not args.push:
        return
    allowed_paths = [
        "Sessions",
        "index.md",
        "Current-State.md",
        "Timeline",
        "Clues",
        "Arcs",
        "NPCs",
        "PCs",
        "Locations",
        "Factions",
        "Organizations",
        "Vehicles",
        "Tech",
        "Documentation",
    ]
    git(["add", "--", *[path for path in allowed_paths if (REPO_ROOT / path).exists()]])
    if args.commit:
        message = args.commit_message or f"Close out session {session_date}"
        git(["commit", "-m", message, "-m", "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"])
    if args.push:
        git(["push"])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build or run Cindy's low-token local post-session closeout workflow."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--session-dir", type=Path, help="Archived live-session directory containing transcript.jsonl")
    source.add_argument("--transcript", type=Path, help="Specific transcript.jsonl path")
    source.add_argument("--current", action="store_true", help="Use the current live-session transcript instead of latest archive")
    parser.add_argument("intent", nargs="*", help="Optional fuzzy request phrase, e.g. 'summarize last night' or 'update the wiki from the latest game'")
    parser.add_argument("--out-dir", type=Path, help="Directory for closeout-packet.md and run artifacts")
    parser.add_argument("--transcript-lines", type=int, default=70, help="Compact transcript sample line budget")
    parser.add_argument("--evidence-limit", type=int, default=18, help="Max evidence lines per evidence class")
    parser.add_argument("--tail-limit", type=int, default=12, help="Last transcript lines to include")
    parser.add_argument("--marker-limit", type=int, default=20, help="Max GM panel markers to include")
    parser.add_argument("--source-window-hours", type=float, default=36, help="Recent archive window for fuzzy/latest session selection; 0 means all archives")
    parser.add_argument("--authentic-min-rows", type=int, default=40, help="Minimum text transcript rows for a normal authentic-session verdict")
    parser.add_argument("--authentic-min-hits", type=int, default=6, help="Minimum campaign-play keyword hits for a normal authentic-session verdict")
    parser.add_argument("--authentic-min-duration-s", type=int, default=900, help="Minimum transcript duration for a normal authentic-session verdict when timestamps exist")
    parser.add_argument("--allow-inauthentic", action="store_true", help="Allow mutating model runs even if deterministic preflight does not mark the transcript authentic")
    parser.add_argument("--print", action="store_true", help="Print the packet to stdout instead of writing artifacts")
    parser.add_argument("--run-agent", action="store_true", help="Run the configured local model/coding agent on the generated prompt")
    parser.add_argument("--agent-command", default=os.environ.get("CINDY_CLOSEOUT_AGENT"), help="Shell command for the local agent; stdin receives the prompt unless {prompt} is present")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow mutating runs when campaign-wiki already has uncommitted changes")
    parser.add_argument("--commit", action="store_true", help="Commit resulting wiki changes after a successful agent run")
    parser.add_argument("--push", action="store_true", help="Push after commit; implies no extra validation beyond git push")
    parser.add_argument("--commit-message", help="Commit message for --commit")
    args = parser.parse_args()

    mutating = args.run_agent or args.commit or args.push
    if mutating:
        require_clean_worktree(args.allow_dirty)

    packet_info = build_packet(args)
    auth_verdict = str(packet_info["authenticity"].get("verdict") or "unknown")
    if mutating and auth_verdict != "authentic" and not args.allow_inauthentic:
        raise RuntimeError(
            f"Refusing mutating closeout because transcript authenticity is {auth_verdict}. "
            "Review the generated packet or pass --allow-inauthentic for an explicit provisional run."
        )
    if args.print and not mutating:
        print(packet_info["packet"])
        return

    paths = write_workspace(packet_info)
    print(f"wrote packet: {paths['packet']}")
    print(f"wrote facts: {paths['facts']}")
    print(f"wrote plan: {paths['plan']}")
    print(f"wrote prompt: {paths['prompt']}")
    print(f"wrote manifest: {paths['manifest']}")

    if not args.run_agent:
        print("prepared closeout workspace only; pass --run-agent with --agent-command or CINDY_CLOSEOUT_AGENT to mutate the wiki")
        return
    if not args.agent_command:
        raise RuntimeError("--run-agent requires --agent-command or CINDY_CLOSEOUT_AGENT")

    log_path = packet_info["out_dir"] / "agent-run.log"
    run_agent(args.agent_command, paths["prompt"], log_path)
    print(f"agent log: {log_path}")

    issues = validate_closeout(packet_info["session_date"])
    if issues:
        for issue in issues:
            print(f"validation issue: {issue}")
        raise SystemExit(2)
    print("closeout validation passed")
    commit_and_push(args, packet_info["session_date"])


if __name__ == "__main__":
    main()
