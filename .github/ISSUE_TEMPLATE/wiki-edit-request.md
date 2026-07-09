---
name: Wiki edit request
about: Request a canonical Markdown page edit from the static wiki editor
title: "Edit wiki page: <path>"
labels: [wiki-edit, needs-review]
assignees: []
---

## Human summary

Who made the change, what changed, and why should it become campaign canon?

## Machine-readable request

```json
{
  "schemaVersion": "campaign-wiki-edit/v1",
  "appId": "campaign-wiki-editor",
  "appName": "Campaign Wiki Editor",
  "createdAt": "YYYY-MM-DDTHH:mm:ss.sssZ",
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
