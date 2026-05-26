# Final Status Outcome Table Template

Use this table after a final status pass when the paper preserves, changes, or
clarifies a central status claim. It is a reader-facing summary, not a
replacement for the search log or coverage matrix.

## When to Include

Include a compact outcome table when any of these are true:

- the paper says a central problem remains open, conditional, or unresolved;
- recent searches found adjacent results that readers may confuse with the
  central model;
- a source was added but does not close the central model cell;
- the status did not change, but the review needs to show why that conclusion
  is auditable.

## Required Columns

Use these columns in the paper or generated evidence appendix.

| Cell checked | Outcome | Reader-facing consequence |
| --- | --- | --- |
| Exact model cell: object, assumptions, guard/model/method, parameter, and setting. | `status_changed`, `status_preserved`, `adjacent_source_added`, `scope_exclusion_added`, or `blocked_by_access`. | One cautious sentence saying what the review may now say, including any non-transfer warning. |

## Optional Columns

Add these only when the table remains readable.

- Status before pass.
- Search-log section and pass date.
- Source, claim, coverage, or open-problem records changed.
- Main adjacent hits excluded and the changed model axis.
- Next action if the pass was blocked or incomplete.

## Writing Rules

- Do not use the table to prove nonexistence of a result.
- Say "no tracked source in this pass changes the status" when preserving a
  claim.
- Name the model axis that blocks transfer for every adjacent result.
- Keep raw query strings and hit lists in `search_log.md` or
  `search_queries.md`, not in the paper table.
- If the status changes, update the executive summary, status matrix, open
  problems, annotated source guide, evidence report, and conclusion together.
