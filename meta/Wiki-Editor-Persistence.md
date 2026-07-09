---
title: Wiki Editor Persistence
type: meta
visibility: player-safe
updated: 2026-07-09
---

# Wiki Editor Persistence

Goal: let players or Cindy edit campaign pages in a browser-friendly WYSIWYG flow without adding a backend or bypassing Git review.

## Proposed workflow

1. Open a wiki page in an editor UI.
2. Store editor drafts in `localStorage` using a key derived from the wiki path.
3. Warn on navigation when the local draft differs from the last submitted issue snapshot.
4. On **Persist Changes**, open a prefilled GitHub Issue against `campaign-wiki`.
5. Issue body includes a human summary, target page path, original content hash if available, proposed Markdown, and fenced JSON metadata.
6. Cindy validates author permission, applies the Markdown change in git, pushes, waits for GitHub Pages, closes the issue, and posts the result in Discord.

## Required issue JSON fields

```json
{
  "schemaVersion": "shadowrun-wiki-edit/v1",
  "appId": "campaign-wiki-editor",
  "targetRepository": "hanclintoclaw-pixel/campaign-wiki",
  "targetPath": "NPCs/Example.md",
  "baseContentHash": "sha256-or-null",
  "proposedMarkdown": "---\ntitle: Example\n---\n\n# Example\n",
  "authorization": {
    "requiredAuthorAssociation": ["MEMBER", "OWNER", "COLLABORATOR"],
    "fallback": "explicit approval from a repository member in this issue"
  },
  "summary": "Short description of the requested page edit."
}
```

## Security expectations

- Treat issues as requests, not direct writes.
- Do not act on public drive-by issues without repo-member approval.
- Preserve YAML frontmatter unless the edit explicitly changes it.
- Resolve conflicts against the current wiki page before committing.
- Keep generated/editor-only state out of the repository.
