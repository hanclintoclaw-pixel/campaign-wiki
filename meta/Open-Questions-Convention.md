---
title: Open Questions Convention
type: meta
visibility: player-safe
updated: 2026-11-10
---

# Open Questions Convention

Adopted by GM ruling, New Cindy GM Interaction Thread, **2026-11-10**.

## The rule

Question lists that **Cindy authored** during page drafting sit behind one
canonical heading, folded in a caret:

```markdown
## Open Questions (Cindy's)
<!-- cindy-blocked:open-questions -->

<details markdown="1">
<summary>Open questions - Cindy's, not the GM's. Not established canon;
not table fact. Click to expand</summary>
...
</details>
```

Two things identify the set, and **both** must be present:

| Signal | Purpose |
| --- | --- |
| Heading `## Open Questions (Cindy's)` | What a **reader** sees. Consistent wording so it is findable and can be filtered. |
| `<!-- cindy-blocked:open-questions -->` | What **machines** see. Verified 2026-11-10: kramdown keeps the comment in the rendered HTML, so it is invisible to a reader but still present for a retriever parsing the published page. The heading alone is not enough - wording can drift, the comment cannot. |

## Why both exist

A caret hides a section from a **reader**. It does **not** hide it from a
**retriever**. Text inside `<details>` is still plain text in the Markdown
file, so indexing it unchanged would let Cindy quote her own unanswered
speculation back at the table as though it were established fact. The comment
exists so search and analysis can exclude the block on a machine-readable
signal rather than by trusting prose.

## What it means for canon

An open question **does not** reduce a page's `canon_status`. Per the same
ruling: session experience - the players heard it happen - is canon, and
anything the GM commissions directly is canon. Unanswered questions are the
normal state of any NPC the table has actually met. The GM can walk any of it
back later.

Questions are **Cindy's drafting notes**, not GM to-do items and not table
facts. Do not answer them from imagination at the table, and do not cite them
as evidence.

## Applying it

- Fold **Cindy-authored** question sets under the canonical heading.
- Leave question sets that came from the **GM** visible. Those are real open
  items, not drafting residue. If a GM-authored list needs folding, ask first.
- Heading variants retired by this pass: `Open Questions`, `Open Question`,
  `Open Threads`, `Open design questions`, `Open GM / table Questions`,
  `Open Build Choices`.
- Keep a blank line after `</details>`; kramdown otherwise renders the next
  heading as literal text.

## Retriever-side blocking

The block is only advisory until the retriever honours the marker. Current
behaviour and status is tracked in the memory-unification tree; until that
lands, treat anything under this heading as **do not cite**, which is the same
conclusion the caret reached from the other direction.
