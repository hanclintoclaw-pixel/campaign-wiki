#!/usr/bin/env python3
"""Ingest a routine Curtis Drone Shift final report into campaign-wiki.

The script intentionally handles only the safe, routine path: completed Curtis
Drone Shift reports with small nuyen deltas and no permanent drone stat edits.
Ambiguous reports should be left for Cindy/GM review.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURTIS_PATH = ROOT / "PCs" / "Curtis.md"
VEHICLE_DIR = ROOT / "Vehicles"
SAFE_DELTA_LIMIT = 200

ASSET_PAGES = {
    "belmont": "Belmont.md",
    "buzz": "Buzz.md",
    "mr. clean": "Mr-Clean.md",
    "mr clean": "Mr-Clean.md",
    "the finisher": "The-Finisher.md",
    "finisher": "The-Finisher.md",
    "waddles": "Waddles.md",
}


class IngestError(RuntimeError):
    pass


@dataclass(frozen=True)
class Report:
    job: str
    asset_line: str
    asset_name: str
    nuyen_delta: int
    quality_label: str
    quality_score: int
    work_notes: tuple[str, ...]
    followups: tuple[str, ...]
    raw: str

    @property
    def tutorial_number(self) -> int | None:
        match = re.search(r"\bTutorial\s+(\d+)\b", self.job, flags=re.IGNORECASE)
        return int(match.group(1)) if match else None


def run(command: list[str], *, cwd: Path = ROOT) -> str:
    result = subprocess.run(command, cwd=cwd, check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise IngestError(f"Command failed ({' '.join(command)}): {detail}")
    return result.stdout


def extract_field(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, flags=re.IGNORECASE | re.MULTILINE)
    if not match:
        raise IngestError(f"Missing required field: {label}")
    return match.group(1).strip()


def parse_nuyen_delta(raw: str) -> int:
    cleaned = raw.replace("¥", "").replace(",", "").strip()
    match = re.search(r"([+-]?\d+)", cleaned)
    if not match:
        raise IngestError(f"Could not parse nuyen delta: {raw!r}")
    return int(match.group(1))


def parse_quality(raw: str) -> tuple[str, int]:
    match = re.search(r"^(.*?)\s*\(([-+]?\d+)\)\s*$", raw)
    if not match:
        raise IngestError(f"Could not parse maintenance quality: {raw!r}")
    return match.group(1).strip(), int(match.group(2))


def normalize_asset_name(asset_line: str) -> str:
    name = asset_line.split(" - ", 1)[0].strip()
    return re.sub(r"\s+", " ", name)


def parse_work_notes(text: str) -> tuple[str, ...]:
    notes: list[str] = []
    pattern = r"^\d+\.\s+.+?;\s*(success|failure);\s*[+-]?¥?\d+;\s*(.+)$"
    for match in re.finditer(pattern, text, flags=re.MULTILINE):
        note = match.group(2).strip()
        if note:
            notes.append(note.rstrip("."))
    return tuple(notes)


def parse_followups(text: str) -> tuple[str, ...]:
    followups: list[str] = []
    capture = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if re.match(r"Selected tradeoffs / follow-up effects:", line, flags=re.IGNORECASE):
            capture = True
            continue
        if capture and re.match(r"Cindy ingest/closeout note:", line, flags=re.IGNORECASE):
            break
        if capture and line.startswith("-"):
            followup = re.sub(r":\s*Follow-up:\s*", ": ", line[1:].strip(), flags=re.IGNORECASE)
            followups.append(followup.rstrip("."))
    return tuple(followups)


def parse_report(text: str) -> Report:
    if "CURTIS DRONE SHIFT REPORT" not in text.upper():
        raise IngestError("Report marker not found.")

    status = extract_field(text, "Status")
    if status.lower() != "complete":
        raise IngestError(f"Only completed reports can be auto-ingested; got status {status!r}.")

    job = extract_field(text, "Job")
    asset_line = extract_field(text, "Asset")
    nuyen_delta = parse_nuyen_delta(extract_field(text, "Nuyen delta"))
    if abs(nuyen_delta) > SAFE_DELTA_LIMIT:
        raise IngestError(f"Nuyen delta {nuyen_delta:+d}¥ exceeds routine auto-ingest limit of {SAFE_DELTA_LIMIT}¥.")

    quality_label, quality_score = parse_quality(extract_field(text, "Maintenance quality"))
    ingest_note = extract_field(text, "Cindy ingest/closeout note")
    if "do not apply permanent" not in ingest_note.lower():
        raise IngestError("Ingest note does not explicitly block permanent stat changes.")

    return Report(
        job=job,
        asset_line=asset_line,
        asset_name=normalize_asset_name(asset_line),
        nuyen_delta=nuyen_delta,
        quality_label=quality_label,
        quality_score=quality_score,
        work_notes=parse_work_notes(text),
        followups=parse_followups(text),
        raw=text,
    )


def format_yen(value: int, *, signed: bool = False) -> str:
    if signed:
        return f"{value:+,d}¥"
    return f"{value:,d}¥"


def sentence_join(parts: tuple[str, ...], limit: int = 4) -> str:
    selected = [p.rstrip(".") for p in parts if p.strip()][:limit]
    if not selected:
        return "closing the routine work order"
    if len(selected) == 1:
        return selected[0]
    return ", ".join(selected[:-1]) + ", and " + selected[-1]


def followup_sentence(report: Report) -> str:
    if not report.followups:
        return ""
    detail = "; ".join(followup.rstrip(".") for followup in report.followups)
    return f" Follow-up note: {detail}."


def article(text: str) -> str:
    return "an" if text[:1].lower() in {"a", "e", "i", "o", "u"} else "a"


def completed_work_order_line(report: Report, day: date) -> str:
    work = sentence_join(report.work_notes)
    return (
        f"- **{day.isoformat()} — {report.job}**: Curtis completed Taco's {report.asset_name} ticket as "
        f"{article(report.quality_label)} {report.quality_label.lower()}. Final report logged "
        f"**{format_yen(report.nuyen_delta, signed=True)}** net shift result and "
        f"**Maintenance Quality {report.quality_score}** after {work}."
        f"{followup_sentence(report)} No permanent {report.asset_name}/drone stat changes apply unless the GM confirms them."
    )


def vehicle_note_line(report: Report, day: date) -> str:
    work = sentence_join(report.work_notes)
    return (
        f"- **{day.isoformat()} — Curtis Drone Shift {report.job}:** Curtis completed "
        f"{article(report.quality_label)} {report.quality_label.lower()} on {report.asset_name}. "
        f"The work included {work}. Final report logged "
        f"**{format_yen(report.nuyen_delta, signed=True)}** net shift result and "
        f"**Maintenance Quality {report.quality_score}**."
        f"{followup_sentence(report)} No permanent {report.asset_name} stat changes apply unless the GM confirms them."
    )


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise IngestError(f"Expected text block not found: {old[:80]!r}")
    return text.replace(old, new, 1)


def update_funds_note(text: str, report: Report) -> str:
    pattern = re.compile(
        r"Current funds note preserved in dossier: \*\*(?P<balance>[\d,]+)¥\*\* current nuyen balance "
        r"\((?P<body>.*?)\)",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise IngestError("Could not find Curtis current funds Drone Shift note.")

    drone_pattern = re.compile(
        r"\*\*(?P<drone_delta>[+-][\d,]+)¥\*\* net from completed Curtis Drone Shift Work Orders "
        r"Tutorial (?P<start>\d+)-(?P<end>\d+)"
    )
    drone_match = drone_pattern.search(match.group("body"))
    if not drone_match:
        raise IngestError("Could not find Curtis Drone Shift subtotal in current funds note.")

    old_balance = int(match.group("balance").replace(",", ""))
    old_drone_delta = int(drone_match.group("drone_delta").replace(",", ""))
    new_balance = old_balance + report.nuyen_delta
    new_drone_delta = old_drone_delta + report.nuyen_delta
    start = int(drone_match.group("start"))
    end = report.tutorial_number or int(drone_match.group("end"))

    new_body = drone_pattern.sub(
        f"**{format_yen(new_drone_delta, signed=True)}** net from completed Curtis Drone Shift Work Orders "
        f"Tutorial {start}-{end}",
        match.group("body"),
        count=1,
    )

    replacement = (
        f"Current funds note preserved in dossier: **{format_yen(new_balance)}** current nuyen balance "
        f"({new_body})"
    )
    return text[: match.start()] + replacement + text[match.end() :]


def report_already_recorded(text: str, report: Report) -> bool:
    if report.job in text:
        return True
    return report.tutorial_number is not None and re.search(
        rf"\b(?:Curtis Drone Shift\s+)?Tutorial\s+{report.tutorial_number}\b",
        text,
        flags=re.IGNORECASE,
    ) is not None


def update_curtis(report: Report, day: date) -> bool:
    text = CURTIS_PATH.read_text(encoding="utf-8")
    if report_already_recorded(text, report):
        return False

    text = update_funds_note(text, report)
    marker = "## Relevant Sessions"
    line = completed_work_order_line(report, day)
    text = replace_once(text, marker, f"{line}\n\n{marker}")
    CURTIS_PATH.write_text(text, encoding="utf-8")
    return True


def vehicle_path(report: Report) -> Path | None:
    key = report.asset_name.lower()
    filename = ASSET_PAGES.get(key)
    return VEHICLE_DIR / filename if filename else None


def update_vehicle(report: Report, day: date) -> bool:
    path = vehicle_path(report)
    if path is None or not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if report_already_recorded(text, report):
        return False

    line = vehicle_note_line(report, day)
    if "## Notes\n" in text:
        text = replace_once(text, "## Notes\n", f"## Notes\n\n{line}\n")
    else:
        text = replace_once(text, "## Sources", f"## Notes\n\n{line}\n\n## Sources")
    path.write_text(text, encoding="utf-8")
    return True


def ensure_clean_worktree() -> None:
    status = run(["git", "status", "--short"])
    if status.strip():
        raise IngestError(f"campaign-wiki has uncommitted changes; refusing auto-ingest:\n{status}")


def commit_and_push(report: Report, *, push: bool) -> None:
    run(["git", "add", "PCs/Curtis.md", "Vehicles"])
    status = run(["git", "status", "--short"])
    if not status.strip():
        return
    run([
        "git",
        "commit",
        "-m",
        f"Ingest Curtis Drone Shift {report.job}",
        "-m",
        "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>",
    ])
    if push:
        run(["git", "push"])


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, help="Read report text from a file instead of stdin.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Ingest date, YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--apply", action="store_true", help="Write wiki changes. Default is dry-run parse only.")
    parser.add_argument("--commit", action="store_true", help="Commit changes after applying.")
    parser.add_argument("--push", action="store_true", help="Push the commit after committing.")
    args = parser.parse_args(argv)

    raw = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    report = parse_report(raw)
    ingest_day = date.fromisoformat(args.date)

    if args.apply:
        ensure_clean_worktree()
        changed_curtis = update_curtis(report, ingest_day)
        changed_vehicle = update_vehicle(report, ingest_day)
        if args.commit:
            commit_and_push(report, push=args.push)
        if not changed_curtis and not changed_vehicle:
            print(f"Already ingested: {report.job}")
        else:
            print(
                f"Ingested {report.job}: {format_yen(report.nuyen_delta, signed=True)}, "
                f"Maintenance Quality {report.quality_score}."
            )
    else:
        print(
            f"DRY RUN: {report.job}; asset {report.asset_name}; "
            f"delta {format_yen(report.nuyen_delta, signed=True)}; quality {report.quality_score}."
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except IngestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
