---
title: Wiki Editor Persistence
type: meta
visibility: player-safe
updated: 2026-07-09
---

# Wiki Editor Persistence

Goal: let players or Cindy edit campaign pages in a browser-friendly WYSIWYG flow without adding a backend or bypassing Git review.

## Current workflow

1. Open a wiki page and click **Edit** in the static editor bar.
2. The browser fetches raw Markdown for the page from the wiki source commit that built the site.
3. Edit the Markdown in the page-local editor.
4. **Save changes** stays disabled until the Markdown differs from the fetched source.
5. On **Save changes**, the editor opens a prefilled GitHub Issue against `campaign-wiki`.
6. The issue body includes a human summary plus a fenced JSON request containing the source commit, page path, source hash, and a `line-patch/v1` Markdown diff. If the URL would be too long, the JSON request downloads as an attachment file instead.
7. Cindy validates author permission from GitHub issue metadata, checks the source commit/hash against the current repo state, applies the patch in git, pushes, waits for GitHub Pages, closes the issue, and posts the result in Discord.

## Required issue JSON fields

```json
{
  "schemaVersion": "campaign-wiki-edit/v1",
  "appId": "campaign-wiki-editor",
  "appName": "Campaign Wiki Editor",
  "sourceRepository": "hanclintoclaw-pixel/campaign-wiki",
  "sourceCommit": "commit-sha-used-to-generate-this-request",
  "sourceRef": "commit-or-branch-used-to-fetch-raw-markdown",
  "pagePath": "NPCs/Example.md",
  "originalSha256": "sha256-of-source-markdown",
  "summary": "Short description of the requested page edit.",
  "requestedChanges": [
    {
      "type": "patch_markdown_file",
      "targetPath": "NPCs/Example.md",
      "baseSnapshot": "commit:path",
      "baseSha256": "sha256-of-source-markdown",
      "format": "line-patch/v1",
      "payload": {
        "hunks": [],
        "originalLineCount": 0,
        "resultingLineCount": 0,
        "changedLineCount": 0
      }
    }
  ]
}
```

## Ingestion script

`scripts/ingest_wiki_edit_issues.py` validates and optionally applies editor issues. GitHub logins allowed to submit edits without per-repo collaborator status live in `.github/wiki-edit-allowlist.txt`; keep one GitHub login per line.

Dry-run a specific issue:

```sh
python3 scripts/ingest_wiki_edit_issues.py --issue 1
```

Apply, commit, push, and close after review:

```sh
python3 scripts/ingest_wiki_edit_issues.py --issue 1 --apply --commit --push --close
```

Default batch mode scans open issues labeled `wiki-edit` and unlabeled issues whose title starts with `Edit wiki page:`. Dry-run is the default; file writes require `--apply`, commits require `--commit`, pushes require `--push`, and closing/commenting on issues requires `--close`. For one-off approvals, use `--trusted-user <GitHubLogin>` or the comma-separated `WIKI_EDIT_TRUSTED_USERS` environment variable.

## Security expectations

- Treat issues as requests, not direct writes.
- Validate the issue author's GitHub `authorAssociation`; do not trust request-body text as permission.
- Do not act on public drive-by issues without repo-member approval.
- Verify `sourceCommit`/`baseSha256` before applying the patch; if the page has moved on, rebase or ask for resubmission.
- Preserve YAML frontmatter unless the edit explicitly changes it.
- Resolve conflicts against the current wiki page before committing.
- Keep generated/editor-only state out of the repository.
