# Framework Progress Tracker

Last updated: YYYY-MM-DD

This file is the live progress board for a literature review. It tracks the
state of the review process itself: which framework stages are current, which
artifacts have been updated, and which stage should be handled next.

## Status Labels

- `done`: complete for the current scope, but revisited when new literature or
  scope cells are added.
- `active`: usable now, with known follow-up work.
- `needs_work`: important framework work remains before the review should be
  treated as polished.
- `blocked`: waiting on source access, discovery, or a scope decision.
- `recurring`: should be repeated during every substantial literature pass.

## Framework Stage Dashboard

| Stage | Status | Primary artifacts | Current state | Next update |
| --- | --- | --- | --- | --- |
| Scope and model cells | `active` | `coverage_matrix.json`, scope section |  | Track theorem-level cells and explicit scope-exclusion cells. |
| Source intake | `active` | `source_registry.json`, bibliography |  |  |
| Search tracking | `needs_work` | `search_log.md`, query list |  |  |
| Claim extraction | `active` | `claims_registry.json` |  |  |
| Locator pass | `needs_work` | `claims_registry.json`, `evidence_report.md` |  |  |
| Translation audit | `active` | claim records, model-separation prose |  |  |
| Coverage update | `active` | `coverage_matrix.json`, status tables |  |  |
| Open-problem update | `active` | `open_problems.json`, open-problem section |  |  |
| Final status pass | `recurring` | `search_log.md`, `search_queries.md`, coverage next actions |  | Repeat before release or after central status changes. |
| Document assembly | `active` | `document_assembly.md`, paper outline |  |  |
| Paper synchronization | `active` | review source, compiled paper |  |  |
| Audit and build | `recurring` | scripts, generated reports, build logs |  |  |

## High-Priority Work Queue

1.
2.
3.

## Update Transaction Checklist

Use this checklist whenever adding literature, changing a status claim, or
editing an open problem.

- Identify the scope cell or create a new one.
- If the variant is adjacent but intentionally excluded, create or update a
  scope-exclusion cell and record the reason.
- Add or update the source registry record.
- Record the search path and any relevant exclusions.
- Extract each theorem, conjecture, hardness result, lower bound, survey claim,
  or open-problem statement into a claim record.
- Add locator information when available.
- Write the translation note and non-implications.
- Link the claim to coverage cells.
- Link conditional or open claims to open-problem records.
- Update this progress tracker if the stage status or next action changed.
- Update the document assembly map if the paper structure or artifact roles
  changed.
- Run the final status pass for central open, conditional, or recent-status
  claims before publishing or pushing.
- Regenerate the evidence report.
- Update the paper prose and rebuild the deliverable.
- Run validation checks before publishing or pushing.
