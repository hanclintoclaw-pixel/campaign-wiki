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
from decimal import Decimal
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

ASSET_DISPLAY_NAMES = {
    "belmont": "Belmont",
    "buzz": "Buzz",
    "mr. clean": "Mr. Clean",
    "mr clean": "Mr. Clean",
    "the finisher": "The Finisher",
    "finisher": "The Finisher",
    "waddles": "Waddles",
}


class IngestError(RuntimeError):
    pass


@dataclass(frozen=True)
class Report:
    kind: str
    job: str
    asset_line: str
    asset_name: str
    nuyen_delta: int
    quality_label: str
    quality_score: int
    work_notes: tuple[str, ...]
    followups: tuple[str, ...]
    raw: str
    project_track: str = ""
    work_order: str = ""
    lane: str = ""
    player_choice: str = ""
    roll: str = ""
    outcome: str = ""
    result: str = ""
    rigger_note: str = ""

    @property
    def legacy_tutorial_number(self) -> int | None:
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
    normalized = name.lower()
    for key in sorted(ASSET_DISPLAY_NAMES, key=len, reverse=True):
        pattern = rf"(?<![a-z0-9]){re.escape(key)}(?:'s|s')?(?![a-z0-9])"
        if re.search(pattern, normalized):
            return ASSET_DISPLAY_NAMES[key]
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
    if "CURTIS MORNING GARAGE REPORT" in text.upper():
        return parse_morning_garage_report(text)

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
        kind="drone_shift",
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


def parse_morning_garage_report(text: str) -> Report:
    project_track = extract_field(text, "Project track")
    work_order = extract_field(text, "Work Order")
    lane = extract_field(text, "Lane")
    if lane.lower() not in {"rigger school", "project"}:
        raise IngestError(f"Only routine Rigger School or Project Morning Garage reports can be auto-ingested; got lane {lane!r}.")

    asset_line = extract_field(text, "Asset")
    player_choice = extract_field(text, "Player choice")
    roll = extract_field(text, "Roll")
    outcome = extract_field(text, "Outcome")
    if outcome.lower() != "success":
        raise IngestError(f"Only successful Morning Garage reports can be auto-ingested; got outcome {outcome!r}.")

    result = extract_field(text, "Result")
    nuyen_delta = parse_nuyen_delta(extract_field(text, "Nuyen delta"))
    if abs(nuyen_delta) > SAFE_DELTA_LIMIT:
        raise IngestError(f"Nuyen delta {nuyen_delta:+d}¥ exceeds routine auto-ingest limit of {SAFE_DELTA_LIMIT}¥.")

    quality_score = int(extract_field(text, "Quality delta").replace("+", "").strip())
    rigger_note = extract_field(text, "Rigger note")
    ingest_note = extract_field(text, "Cindy ingest/closeout note")
    if "apply the nuyen delta" not in ingest_note.lower() or "record the explicit player choice" not in ingest_note.lower():
        raise IngestError("Morning Garage ingest note does not authorize the routine nuyen and continuity updates.")

    sheet_change = extract_field(text, "Sheet change")
    if "no permanent" not in sheet_change.lower():
        raise IngestError("Morning Garage sheet change does not explicitly block permanent changes.")

    day_match = re.search(r"\bday\s+(\d+)\s*/\s*(\d+)\b", project_track, flags=re.IGNORECASE)
    if not day_match:
        raise IngestError(f"Could not parse Morning Garage project day from: {project_track!r}")
    day_number = int(day_match.group(1))
    total_days = int(day_match.group(2))
    job = f"Morning Garage Advanced Drone Pilot retrieval Day {day_number}: {work_order}"
    return Report(
        kind="morning_garage",
        job=job,
        asset_line=asset_line,
        asset_name=normalize_asset_name(asset_line),
        nuyen_delta=nuyen_delta,
        quality_label="Quality",
        quality_score=quality_score,
        work_notes=(result,),
        followups=(rigger_note,),
        raw=text,
        project_track=f"Advanced Drone Pilot retrieval Day {day_number}/{total_days}",
        work_order=work_order,
        lane=lane,
        player_choice=player_choice,
        roll=roll,
        outcome=outcome,
        result=result,
        rigger_note=rigger_note,
    )


YEN_AMOUNT_PATTERN = r"[+-]?[\d,]+(?:\.\d+)?"


def parse_yen_amount(raw: str) -> Decimal:
    return Decimal(raw.replace(",", ""))


def format_yen(value: int | Decimal, *, signed: bool = False) -> str:
    amount = Decimal(value)
    sign = ""
    if signed:
        sign = "+" if amount >= 0 else "-"
        amount = abs(amount)
    if amount == amount.to_integral_value():
        body = f"{int(amount):,d}"
    else:
        body = f"{amount:,.2f}".rstrip("0").rstrip(".")
    return f"{sign}{body}¥"


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
    if report.kind == "morning_garage":
        choice = report.player_choice[:1].lower() + report.player_choice[1:]
        result = re.sub(r"^Curtis\s+", "", report.result).rstrip(".")
        result = result[:1].lower() + result[1:]
        return (
            f"- **{day.isoformat()} — {report.job}**: Curtis completed the "
            f"{report.project_track} work order as a {report.outcome.lower()}. Final report logged "
            f"**{format_yen(report.nuyen_delta, signed=True)}** project spend and "
            f"**Quality {format_yen(report.quality_score, signed=True).removesuffix('¥')}** after choosing "
            f"{choice} and rolling **{report.roll}**. Result: {report.result.rstrip('.')}. "
            f"Follow-up note: {report.rigger_note} "
            "No permanent gear, drone, vehicle, combat, or stat change applies today unless the GM separately approves it."
        )

    work = sentence_join(report.work_notes)
    return (
        f"- **{day.isoformat()} — {report.job}**: Curtis completed Taco's {report.asset_name} ticket as "
        f"{article(report.quality_label)} {report.quality_label.lower()}. Final report logged "
        f"**{format_yen(report.nuyen_delta, signed=True)}** net shift result and "
        f"**Maintenance Quality {report.quality_score}** after {work}."
        f"{followup_sentence(report)}"
    )


def vehicle_note_line(report: Report, day: date) -> str:
    work = sentence_join(report.work_notes)
    return (
        f"- **{day.isoformat()} — Curtis Drone Shift {report.job}:** Curtis completed "
        f"{article(report.quality_label)} {report.quality_label.lower()} on {report.asset_name}. "
        f"The work included {work}. Final report logged "
        f"**{format_yen(report.nuyen_delta, signed=True)}** net shift result and "
        f"**Maintenance Quality {report.quality_score}**."
        f"{followup_sentence(report)}"
    )


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise IngestError(f"Expected text block not found: {old[:80]!r}")
    return text.replace(old, new, 1)


def update_funds_note(text: str, report: Report, day: date) -> str:
    ledger_text = update_current_nuyen_ledger(text, report, day)
    if ledger_text != text:
        return ledger_text

    pattern = re.compile(
        rf"Current funds note preserved in dossier: \*\*(?P<balance>{YEN_AMOUNT_PATTERN})¥\*\* current nuyen balance "
        r"\((?P<body>.*?)\)",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise IngestError("Could not find Curtis current funds Drone Shift note.")

    drone_pattern = re.compile(
        r"\*\*(?P<drone_delta>[+-][\d,]+)¥\*\* net from completed Curtis Drone Shift(?: / Morning Garage)? Work Orders"
        r"(?P<label>[^,)]*)"
    )
    drone_match = drone_pattern.search(match.group("body"))
    if not drone_match:
        raise IngestError("Could not find Curtis Drone Shift subtotal in current funds note.")

    old_balance = parse_yen_amount(match.group("balance"))
    old_drone_delta = int(drone_match.group("drone_delta").replace(",", ""))
    new_balance = old_balance + report.nuyen_delta
    new_drone_delta = old_drone_delta + report.nuyen_delta
    old_label = drone_match.group("label")
    legacy_range = re.search(r"Tutorial (?P<start>\d+)-(?P<end>\d+)", old_label, flags=re.IGNORECASE)
    if report.legacy_tutorial_number is not None and legacy_range:
        start = int(legacy_range.group("start"))
        end = report.legacy_tutorial_number or int(legacy_range.group("end"))
        new_label = f" legacy Tutorial {start}-{end}"
    elif legacy_range:
        start = int(legacy_range.group("start"))
        end = int(legacy_range.group("end"))
        new_label = f" including legacy Tutorial {start}-{end} and later named shifts"
    else:
        new_label = old_label

    new_body = drone_pattern.sub(
        f"**{format_yen(new_drone_delta, signed=True)}** net from completed Curtis Drone Shift Work Orders{new_label}",
        match.group("body"),
        count=1,
    )

    replacement = (
        f"Current funds note preserved in dossier: **{format_yen(new_balance)}** current nuyen balance "
        f"({new_body})"
    )
    return text[: match.start()] + replacement + text[match.end() :]


def update_current_nuyen_ledger(text: str, report: Report, day: date) -> str:
    tracked_pattern = re.compile(rf"- Current tracked nuyen: \*\*(?P<balance>{YEN_AMOUNT_PATTERN})¥\*\*(?P<tail>[^\n]*)")
    current_pattern = re.compile(rf"- \*\*Known current nuyen:\*\* \*\*(?P<balance>{YEN_AMOUNT_PATTERN})¥\*\*(?P<tail>[^\n]*)")
    tracked_match = tracked_pattern.search(text)
    current_match = current_pattern.search(text)
    history_pattern = re.compile(
        r"\*\*(?P<drone_delta>[+-][\d,]+)¥\*\* net from completed Curtis Drone Shift / Morning Garage Work Orders"
    )
    history_match = history_pattern.search(text)
    if not current_match or not history_match:
        return text

    old_balance = parse_yen_amount(current_match.group("balance"))
    old_drone_delta = int(history_match.group("drone_delta").replace(",", ""))
    new_text = current_pattern.sub(
        f"- **Known current nuyen:** **{format_yen(old_balance + report.nuyen_delta)}**{current_match.group('tail')}",
        text,
        count=1,
    )
    if tracked_match:
        new_text = tracked_pattern.sub(
            f"- Current tracked nuyen: **{format_yen(parse_yen_amount(tracked_match.group('balance')) + report.nuyen_delta)}**{tracked_match.group('tail')}",
            new_text,
            count=1,
        )
    new_text = history_pattern.sub(
        f"**{format_yen(old_drone_delta + report.nuyen_delta, signed=True)}** net from completed Curtis Drone Shift / Morning Garage Work Orders",
        new_text,
        count=1,
    )
    if report.kind == "morning_garage":
        history_entry = (
            f", and **{format_yen(report.nuyen_delta, signed=True)}** {report.job} project spend on "
            f"{day.isoformat()}"
        )
        history_line_start = new_text.find("- **Current nuyen history:**")
        if history_line_start == -1:
            raise IngestError("Could not find Curtis nuyen history line.")
        history_line_end = new_text.find("\n", history_line_start)
        if history_line_end == -1:
            history_line_end = len(new_text)
        period = new_text.rfind(".", history_line_start, history_line_end)
        if period == -1:
            raise IngestError("Could not find Curtis nuyen history sentence end.")
        new_text = new_text[:period] + history_entry + new_text[period:]
    return new_text


def report_already_recorded(text: str, report: Report) -> bool:
    if report.job in text:
        return True
    return report.legacy_tutorial_number is not None and re.search(
        rf"\b(?:Curtis Drone Shift\s+)?Tutorial\s+{report.legacy_tutorial_number}\b",
        text,
        flags=re.IGNORECASE,
    ) is not None


def update_curtis(report: Report, day: date) -> bool:
    text = CURTIS_PATH.read_text(encoding="utf-8")
    if report_already_recorded(text, report):
        return False

    text = update_funds_note(text, report, day)
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
    if report.kind == "morning_garage":
        return False
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
    run(["git", "add", "PCs/Curtis.md", "Vehicles", "scripts/ingest_curtis_drone_shift_report.py"])
    status = run(["git", "status", "--short"])
    if not status.strip():
        return
    run([
        "git",
        "commit",
        "-m",
        f"Ingest Curtis {report.job}",
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
