# Evidence Report Outline

The evidence report is generated from the review's JSON ledgers. It is a
supporting artifact for auditability, not a replacement for the paper.

## Summary

- Source count.
- Claim count.
- Open-problem count.
- Coverage-cell count.
- Scope-exclusion cell count.
- Progress-stage count by status.
- Document assembly map status.
- Current warning count.

## Major Proven Results

- Central claims whose status is theorem or tight theorem.

## Open and Conditional Problems

- Open-problem records grouped by type/status.

## Coverage Matrix

- Each model cell, its status, supporting claims, and next action.
- Scope-exclusion cells should render with an explicit "no supporting theorem
  claims" note and the reason the adjacent variant is not being used as
  evidence.

## Verification Gaps

- Claims without page/theorem locators.
- Claims needing primary checks.
- Sources without DOI/URL or weak verification.

## Search and Completeness Gaps

- Coverage cells still unsearched or searching.
- Adjacent variants mentioned in prose or search logs but lacking either a
  theorem-level coverage cell or a scope-exclusion cell.
- Search-log sections that still need entries.
- Progress-board stages marked `needs_work` or `blocked`.
- Missing or stale document assembly map.

## Next Actions

- Highest-priority actions implied by coverage and verification gaps.
- Highest-priority progress-board items.
