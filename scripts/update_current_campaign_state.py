#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = REPO_ROOT / "index.md"
CURRENT_STATE_PATH = REPO_ROOT / "Current-State.md"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def read_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError(f"Expected JSON object in {path}")
    return data


def today_iso() -> str:
    return date.today().isoformat()


def update_frontmatter_date(text: str, updated: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("Markdown file is missing YAML frontmatter")

    frontmatter = match.group(1)
    if not re.search(r"^updated:\s*.*$", frontmatter, flags=re.MULTILINE):
        raise ValueError("Markdown frontmatter is missing an updated field")

    frontmatter = re.sub(r"^updated:\s*.*$", f"updated: {updated}", frontmatter, flags=re.MULTILINE)
    return f"---\n{frontmatter}\n---\n" + text[match.end():]


def replace_h2_section(text: str, heading: str, body: str) -> str:
    heading_pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.MULTILINE)
    match = heading_pattern.search(text)
    if not match:
        raise ValueError(f"Missing section heading: ## {heading}")

    next_heading = re.search(r"^##\s+.+$", text[match.end():], flags=re.MULTILINE)
    section_end = match.end() + next_heading.start() if next_heading else len(text)
    replacement = f"## {heading}\n\n{body.strip()}\n\n"
    return text[:match.start()] + replacement + text[section_end:].lstrip("\n")


def as_paragraphs(value: Any, label: str) -> str:
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError(f"{label} cannot be blank")
        return text
    if isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value):
        return "\n\n".join(item.strip() for item in value)
    raise TypeError(f"{label} must be a non-empty string or list of non-empty strings")


def as_bullets(value: Any, label: str) -> str:
    if not isinstance(value, list) or not value:
        raise TypeError(f"{label} must be a non-empty list of strings")
    lines: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise TypeError(f"{label} must contain only non-empty strings")
        stripped = item.strip()
        lines.append(stripped if stripped.startswith("-") else f"- {stripped}")
    return "\n".join(lines)


def apply_updates(payload: dict[str, Any], updated: str, dry_run: bool) -> list[Path]:
    changed: list[Path] = []

    if "current_situation" in payload:
        text = INDEX_PATH.read_text(encoding="utf-8")
        original = text
        text = update_frontmatter_date(text, updated)
        text = replace_h2_section(text, "Current Situation", as_paragraphs(payload["current_situation"], "current_situation"))
        if text != original:
            changed.append(INDEX_PATH)
            if not dry_run:
                INDEX_PATH.write_text(text, encoding="utf-8")

    current_state = payload.get("current_state")
    if current_state is not None:
        if not isinstance(current_state, dict):
            raise TypeError("current_state must be an object")
        section_map = {
            "current_focus": ("Current Focus", as_paragraphs),
            "recent_runs": ("Recent Runs / Follow-ups", as_bullets),
            "in_world_date": ("In-World Date", as_bullets),
            "immediate_leads": ("Immediate Leads", as_bullets),
            "open_questions": ("Open Questions", as_bullets),
        }
        text = CURRENT_STATE_PATH.read_text(encoding="utf-8")
        original = text
        text = update_frontmatter_date(text, updated)
        for key, (heading, renderer) in section_map.items():
            if key in current_state:
                text = replace_h2_section(text, heading, renderer(current_state[key], f"current_state.{key}"))
        if text != original:
            changed.append(CURRENT_STATE_PATH)
            if not dry_run:
                CURRENT_STATE_PATH.write_text(text, encoding="utf-8")

    if not changed:
        raise ValueError("No campaign-state updates supplied")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch front-page Current Situation and Current State sections after a session closeout.")
    parser.add_argument("payload", type=Path, help="JSON file containing current_situation and/or current_state updates")
    parser.add_argument("--updated", default=today_iso(), help="ISO date to write into page frontmatter; defaults to today")
    parser.add_argument("--dry-run", action="store_true", help="Validate and report changed pages without writing files")
    args = parser.parse_args()

    changed = apply_updates(read_json(args.payload), args.updated, args.dry_run)
    action = "would update" if args.dry_run else "updated"
    for path in changed:
        print(f"{action}: {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
