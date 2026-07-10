#!/usr/bin/env python3
"""Ingest campaign-wiki edit issues produced by the static wiki editor.

Dry-run is the default. Use --apply to edit files, then optionally --commit,
--push, and --close after review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ACCEPTED_SCHEMA = "campaign-wiki-edit/v1"
ACCEPTED_APP_ID = "campaign-wiki-editor"
ACCEPTED_ASSOCIATIONS = {"MEMBER", "OWNER", "COLLABORATOR"}
DEFAULT_LABEL = "wiki-edit"
DEFAULT_ALLOWLIST = Path(".github/wiki-edit-allowlist.txt")
TITLE_PREFIX = "Edit wiki page:"


class IngestError(RuntimeError):
    pass


@dataclass(frozen=True)
class Issue:
    number: int
    title: str
    author: str
    author_association: str
    body: str
    labels: tuple[str, ...]
    url: str


@dataclass(frozen=True)
class ChangeResult:
    issue: Issue
    path: Path
    summary: str
    changed_line_count: int


def run(command: list[str], *, cwd: Path, capture: bool = True) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise IngestError(f"Command failed ({' '.join(command)}): {detail}")
    return result.stdout if capture else ""


def repo_root() -> Path:
    return Path(run(["git", "rev-parse", "--show-toplevel"], cwd=Path.cwd()).strip())


def default_repo(root: Path) -> str:
    remote = run(["git", "remote", "get-url", "origin"], cwd=root).strip()
    ssh_match = re.search(r"github.com[:/]([^/]+/[^/.]+)(?:\.git)?$", remote)
    if not ssh_match:
        raise IngestError(f"Could not infer GitHub owner/repo from origin URL: {remote}")
    return ssh_match.group(1)


def gh_api(root: Path, repo: str, path: str) -> Any:
    payload = run(["gh", "api", f"repos/{repo}{path}"], cwd=root)
    return json.loads(payload)


def issue_from_api(data: dict[str, Any]) -> Issue:
    return Issue(
        number=int(data["number"]),
        title=str(data.get("title") or ""),
        author=str((data.get("user") or {}).get("login") or ""),
        author_association=str(data.get("author_association") or ""),
        body=str(data.get("body") or ""),
        labels=tuple(str(label.get("name") or "") for label in data.get("labels") or []),
        url=str(data.get("html_url") or ""),
    )


def fetch_issue(root: Path, repo: str, number: int) -> Issue:
    return issue_from_api(gh_api(root, repo, f"/issues/{number}"))


def list_candidate_issues(root: Path, repo: str, label: str, scan_title_prefix: bool) -> list[Issue]:
    issues = [issue_from_api(item) for item in gh_api(root, repo, "/issues?state=open&per_page=100")]
    candidates: list[Issue] = []
    for issue in issues:
        if label in issue.labels or (scan_title_prefix and issue.title.startswith(TITLE_PREFIX)):
            candidates.append(issue)
    return candidates


def extract_request(body: str) -> dict[str, Any]:
    blocks = re.findall(r"```(?:json)?\s*(.*?)```", body, flags=re.IGNORECASE | re.DOTALL)
    errors: list[str] = []
    for block in blocks:
        try:
            value = json.loads(block)
        except json.JSONDecodeError as exc:
            errors.append(str(exc))
            continue
        if isinstance(value, dict):
            return value
    if errors:
        raise IngestError(f"Could not parse fenced JSON request: {'; '.join(errors)}")
    raise IngestError("Issue body has no fenced JSON request. Attachment fallback ingestion is not implemented yet; attach or paste the JSON block.")


def safe_repo_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute() or ".." in path.parts:
        raise IngestError(f"Unsafe target path: {raw_path}")
    if path.suffix != ".md":
        raise IngestError(f"Only Markdown files can be patched: {raw_path}")
    return path


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_show_text(root: Path, commit: str, path: str) -> str:
    return run(["git", "show", f"{commit}:{path}"], cwd=root)


def normalize_login(login: str) -> str:
    return login.strip().lower()


def read_allowlist(path: Path) -> set[str]:
    if not path.exists():
        return set()

    trusted: set[str] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        candidate = line.split("#", 1)[0].strip()
        if not candidate:
            continue
        if "@" in candidate:
            raise IngestError(f"Allowlist {path}:{line_number} must contain GitHub logins, not email addresses.")
        trusted.add(normalize_login(candidate))
    return trusted


def ensure_author_allowed(issue: Issue, trusted_users: set[str]) -> None:
    if issue.author_association in ACCEPTED_ASSOCIATIONS:
        return
    if normalize_login(issue.author) in trusted_users:
        return
    raise IngestError(
        f"Issue #{issue.number} author {issue.author!r} has association {issue.author_association!r}; "
        f"add their GitHub login to {DEFAULT_ALLOWLIST} or rerun with --trusted-user after explicit repo-member approval."
    )


def validate_request(root: Path, repo: str, request: dict[str, Any]) -> tuple[Path, dict[str, Any]]:
    if request.get("schemaVersion") != ACCEPTED_SCHEMA:
        raise IngestError(f"Unsupported schemaVersion: {request.get('schemaVersion')!r}")
    if request.get("appId") != ACCEPTED_APP_ID:
        raise IngestError(f"Unsupported appId: {request.get('appId')!r}")
    if request.get("sourceRepository") != repo:
        raise IngestError(f"Request repository {request.get('sourceRepository')!r} does not match {repo!r}")

    page_path = safe_repo_path(str(request.get("pagePath") or ""))
    changes = request.get("requestedChanges")
    if not isinstance(changes, list) or len(changes) != 1 or not isinstance(changes[0], dict):
        raise IngestError("Expected exactly one requestedChanges[] entry.")

    change = changes[0]
    if change.get("type") != "patch_markdown_file":
        raise IngestError(f"Unsupported change type: {change.get('type')!r}")
    if change.get("format") != "line-patch/v1":
        raise IngestError(f"Unsupported patch format: {change.get('format')!r}")
    target_path = safe_repo_path(str(change.get("targetPath") or ""))
    if target_path != page_path:
        raise IngestError(f"pagePath {page_path} does not match targetPath {target_path}")

    source_commit = str(request.get("sourceCommit") or "")
    if not re.fullmatch(r"[0-9a-fA-F]{7,40}", source_commit):
        raise IngestError(f"Invalid sourceCommit: {source_commit!r}")
    run(["git", "cat-file", "-e", f"{source_commit}^{{commit}}"], cwd=root)

    base_text = git_show_text(root, source_commit, page_path.as_posix())
    base_sha = str(change.get("baseSha256") or request.get("originalSha256") or "")
    actual_base_sha = sha256_text(base_text)
    if base_sha != actual_base_sha:
        raise IngestError(f"Base SHA mismatch for {page_path}: request {base_sha}, git {actual_base_sha}")

    return page_path, change


def ensure_target_not_dirty(root: Path, path: Path) -> None:
    status = run(["git", "status", "--porcelain", "--", path.as_posix()], cwd=root).strip()
    if status:
        raise IngestError(f"Target file has uncommitted changes; refusing to patch: {status}")


def apply_line_patch(original_text: str, payload: dict[str, Any]) -> str:
    lines = original_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    hunks = payload.get("hunks")
    if not isinstance(hunks, list):
        raise IngestError("Patch payload is missing hunks[].")

    offset = 0
    for hunk in hunks:
        if not isinstance(hunk, dict):
            raise IngestError("Patch hunk must be an object.")
        start_line = int(hunk.get("startLine"))
        delete_count = int(hunk.get("deleteCount"))
        insert_lines = hunk.get("insertLines")
        if start_line < 1 or delete_count < 0 or not isinstance(insert_lines, list):
            raise IngestError(f"Invalid patch hunk: {hunk!r}")
        index = start_line - 1 + offset
        if index < 0 or index > len(lines):
            raise IngestError(f"Patch hunk startLine out of range: {start_line}")
        lines[index : index + delete_count] = [str(item) for item in insert_lines]
        offset += len(insert_lines) - delete_count

    resulting_line_count = payload.get("resultingLineCount")
    if isinstance(resulting_line_count, int) and resulting_line_count != len(lines):
        raise IngestError(f"Resulting line count mismatch: patch {resulting_line_count}, actual {len(lines)}")
    return "\n".join(lines)


def process_issue(root: Path, repo: str, issue: Issue, args: argparse.Namespace, trusted_users: set[str]) -> ChangeResult:
    ensure_author_allowed(issue, trusted_users)
    request = extract_request(issue.body)
    target_path, change = validate_request(root, repo, request)
    ensure_target_not_dirty(root, target_path)

    current_text = target_path.read_text(encoding="utf-8")
    current_sha = sha256_text(current_text)
    base_sha = str(change.get("baseSha256") or "")
    if current_sha != base_sha:
        raise IngestError(f"Current {target_path} SHA {current_sha} does not match request base {base_sha}; manual rebase needed.")

    payload = change.get("payload")
    if not isinstance(payload, dict):
        raise IngestError("Patch payload must be an object.")
    new_text = apply_line_patch(current_text, payload)
    if new_text == current_text:
        raise IngestError("Patch does not change the target file.")

    if args.apply:
        target_path.write_text(new_text, encoding="utf-8")

    return ChangeResult(
        issue=issue,
        path=target_path,
        summary=str(request.get("summary") or issue.title),
        changed_line_count=int(payload.get("changedLineCount") or 0),
    )


def commit_changes(root: Path, results: list[ChangeResult]) -> str:
    paths = sorted({result.path.as_posix() for result in results})
    run(["git", "add", *paths], cwd=root)
    issue_list = ", ".join(f"#{result.issue.number}" for result in results)
    first_path = paths[0] if len(paths) == 1 else f"{len(paths)} wiki pages"
    message = f"Apply wiki edit request {issue_list}\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
    run(["git", "commit", "-m", message], cwd=root, capture=True)
    return run(["git", "rev-parse", "--short", "HEAD"], cwd=root).strip()


def post_close(root: Path, results: list[ChangeResult], commit_sha: str, *, push: bool, close: bool) -> None:
    for result in results:
        body = f"Applied in `{commit_sha}`."
        if push:
            body += " GitHub Pages will redeploy from the pushed commit."
        run(["gh", "issue", "comment", str(result.issue.number), "--body", body], cwd=root, capture=True)
        if close:
            run(["gh", "issue", "close", str(result.issue.number), "--reason", "completed"], cwd=root, capture=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingest campaign-wiki edit issues.")
    parser.add_argument("--repo", help="GitHub owner/repo. Defaults to origin remote.")
    parser.add_argument("--issue", type=int, action="append", help="Issue number to ingest. May be repeated.")
    parser.add_argument("--label", default=DEFAULT_LABEL, help="Label to scan in batch mode.")
    parser.add_argument("--no-title-scan", action="store_true", help="Do not scan unlabeled open issues with the editor title prefix.")
    parser.add_argument("--allowlist", type=Path, default=DEFAULT_ALLOWLIST, help="Text file of trusted GitHub logins. Default: .github/wiki-edit-allowlist.txt")
    parser.add_argument("--trusted-user", action="append", default=[], help="Allow a GitHub login whose author_association is not accepted. May be repeated.")
    parser.add_argument("--apply", action="store_true", help="Write patched files. Default is dry-run only.")
    parser.add_argument("--commit", action="store_true", help="Commit applied changes.")
    parser.add_argument("--push", action="store_true", help="Push committed changes.")
    parser.add_argument("--close", action="store_true", help="Comment on and close applied issues after commit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    os.chdir(root)
    repo = args.repo or default_repo(root)
    trusted_users = read_allowlist(root / args.allowlist)
    trusted_users.update(normalize_login(user) for user in args.trusted_user)
    trusted_users.update(normalize_login(user) for user in os.environ.get("WIKI_EDIT_TRUSTED_USERS", "").split(",") if user.strip())

    if args.commit and not args.apply:
        raise IngestError("--commit requires --apply")
    if args.push and not args.commit:
        raise IngestError("--push requires --commit")
    if args.close and not args.commit:
        raise IngestError("--close requires --commit")

    issues = [fetch_issue(root, repo, number) for number in args.issue] if args.issue else list_candidate_issues(root, repo, args.label, not args.no_title_scan)
    if not issues:
        print("No candidate wiki edit issues found.")
        return 0

    results: list[ChangeResult] = []
    failures = 0
    for issue in issues:
        try:
            result = process_issue(root, repo, issue, args, trusted_users)
            results.append(result)
            mode = "applied" if args.apply else "validated"
            print(f"{mode}: issue #{issue.number} -> {result.path} ({result.changed_line_count} changed patch line entries)")
        except IngestError as exc:
            failures += 1
            print(f"skipped: issue #{issue.number}: {exc}", file=sys.stderr)

    if failures and not results:
        return 1

    commit_sha = ""
    if args.commit and results:
        commit_sha = commit_changes(root, results)
        print(f"committed: {commit_sha}")
    if args.push and results:
        run(["git", "push"], cwd=root, capture=False)
        print("pushed")
    if args.close and results:
        post_close(root, results, commit_sha, push=args.push, close=args.close)
        print("commented/closed issues")

    if not args.apply and results:
        print("dry-run only; rerun with --apply to write files.")
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except IngestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
