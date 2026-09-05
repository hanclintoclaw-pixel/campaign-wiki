#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


DEFAULT_OUTPUT_ROOT = Path("/Volumes/carbonite/claw/data/cindylou/runtime/session-closeout")
DEFAULT_LIVE_SESSION_CANDIDATES = [
    Path(os.environ.get("LIVE_SESSION_DIR", "")).expanduser() if os.environ.get("LIVE_SESSION_DIR") else None,
    Path("/Volumes/carbonite/claw/data/cindylou/runtime/live-session"),
    Path.home() / ".openclaw/workspace-cindylou/runtime/live-session",
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


def first_existing_live_session_dir() -> Path:
    for candidate in DEFAULT_LIVE_SESSION_CANDIDATES:
        if candidate and candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError("No live-session directory found; pass --session-dir or --transcript")


def latest_archived_session(live_session_dir: Path) -> Path:
    sessions_dir = live_session_dir / "sessions"
    if not sessions_dir.exists():
        raise FileNotFoundError(f"No archived sessions directory found at {sessions_dir}")
    candidates = [path for path in sessions_dir.iterdir() if (path / "transcript.jsonl").exists()]
    if not candidates:
        raise FileNotFoundError(f"No archived session transcript found under {sessions_dir}")
    return max(candidates, key=lambda path: (path / "transcript.jsonl").stat().st_mtime).resolve()


def resolve_session(args: argparse.Namespace) -> tuple[Path, Path]:
    if args.transcript:
        transcript = args.transcript.expanduser().resolve()
        return transcript.parent, transcript
    if args.session_dir:
        session_dir = args.session_dir.expanduser().resolve()
        return session_dir, session_dir / "transcript.jsonl"
    live_session_dir = first_existing_live_session_dir()
    if args.current:
        return live_session_dir, live_session_dir / "transcript.jsonl"
    session_dir = latest_archived_session(live_session_dir)
    return session_dir, session_dir / "transcript.jsonl"


def display_line(row: dict[str, Any]) -> str:
    timestamp = str(row.get("timestamp") or "").strip()
    speaker = str(row.get("speaker") or row.get("author") or "Unknown").strip()
    text = " ".join(str(row.get("text") or row.get("content") or "").split())
    return f"- {timestamp} | {speaker}: {text}"


def matching_rows(rows: Iterable[dict[str, Any]], pattern: re.Pattern[str], limit: int) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for row in rows:
        text = str(row.get("text") or row.get("content") or "")
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


def build_packet(args: argparse.Namespace) -> tuple[str, Path]:
    session_dir, transcript_path = resolve_session(args)
    if not transcript_path.exists():
        raise FileNotFoundError(f"Transcript not found: {transcript_path}")

    rows = read_jsonl(transcript_path)
    if not rows:
        raise ValueError(f"Transcript is empty: {transcript_path}")

    timestamps = [ts for ts in (parse_timestamp(row.get("timestamp")) for row in rows) if ts]
    speakers = Counter(str(row.get("speaker") or row.get("author") or "Unknown").strip() for row in rows)
    text_rows = [row for row in rows if str(row.get("text") or row.get("content") or "").strip()]
    authentic_hits = sum(1 for row in text_rows if AUTHENTIC_RE.search(str(row.get("text") or row.get("content") or "")))
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

    packet = f"""# Cindy session closeout packet: {session_id}

## Deterministic source facts

- Session id: `{session_id}`
- Transcript: `{transcript_path}`
- Transcript rows: {len(rows)} total / {len(text_rows)} with text
- First transcript timestamp: {first_ts}
- Last transcript timestamp / likely stopped-at time: {last_ts}
- Discord channel ids: {channel_text}
- Discord thread ids: {thread_text}
- Authentic-session signal rows: {authentic_hits}
- Candidate wiki session page: `Sessions/{session_date}.md`
- Closeout packet path: `{out_path}`

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
    return packet, out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a compact local closeout packet from a Cindy live-session transcript."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--session-dir", type=Path, help="Archived live-session directory containing transcript.jsonl")
    source.add_argument("--transcript", type=Path, help="Specific transcript.jsonl path")
    source.add_argument("--current", action="store_true", help="Use the current live-session transcript instead of latest archive")
    parser.add_argument("--out-dir", type=Path, help="Directory for closeout-packet.md")
    parser.add_argument("--transcript-lines", type=int, default=70, help="Compact transcript sample line budget")
    parser.add_argument("--evidence-limit", type=int, default=18, help="Max evidence lines per evidence class")
    parser.add_argument("--tail-limit", type=int, default=12, help="Last transcript lines to include")
    parser.add_argument("--marker-limit", type=int, default=20, help="Max GM panel markers to include")
    parser.add_argument("--print", action="store_true", help="Print the packet to stdout instead of writing it")
    args = parser.parse_args()

    packet, out_path = build_packet(args)
    if args.print:
        print(packet)
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(packet, encoding="utf-8")
    print(f"wrote: {out_path}")


if __name__ == "__main__":
    main()
