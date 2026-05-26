# Document Assembly Map

Last updated: YYYY-MM-DD

This map explains how a literature review's artifacts combine into the
reader-facing paper. Use it to keep the final document readable while
preserving an auditable path from every result and open problem back to the
evidence layer.

## Narrative Spine

The paper should answer these questions in order:

1. What is the main result map?
2. Which results are already proven, and under which exact assumptions?
3. Which nearby statements do not follow because the model changes?
4. Which problems remain source-stated open problems, conditional gaps, or
   derived research directions?

## Artifact Roles

| Artifact | Reader-facing role | Maintenance role |
| --- | --- | --- |
| Main paper source | Polished literature-review paper. | Presents only claims supported by the evidence layer. |
| Compiled deliverable | Public PDF or rendered document. | Rebuilt after prose or evidence changes. |
| `source_registry.json` | Bibliographic ground truth. | Records sources, roles, links, and verification state. |
| `claims_registry.json` | Extracted theorem/problem ledger. | One claim per theorem, conjecture, hardness result, survey claim, or open-problem statement. |
| `coverage_matrix.json` | Result-status and scope-exclusion map by model cell. | Prevents model changes and exclusion decisions from being hidden in prose. |
| `open_problems.json` | Open-problem ledger. | Separates source-stated, conditional, and derived open directions. |
| `search_log.md` | Search audit trail. | Records searches, inclusions, exclusions, and follow-up paths. |
| `search_queries.md` | Reusable search strings and index URLs. | Makes final status passes repeatable. |
| `framework_progress.md` | Workflow progress board. | Tracks which framework stage needs attention next. |
| `evidence_report.md` | Generated audit companion. | Summarizes counts, gaps, coverage cells, and next actions. |

## Paper Flow

1. Abstract or short answer.
2. Executive synthesis.
3. Scope and terminology.
4. Historical flow.
5. Result status matrix.
6. Model separations and non-implications.
7. Proof-technique map.
8. Core results by model.
9. Open problems and research directions.
10. Annotated source guide.
11. Completeness protocol and evidence trail.
12. Conclusion.

## Update Order

When a new source or result is added, update artifacts in this order:

1. Coverage matrix if a new theorem-level model cell or scope-exclusion cell
   is needed.
2. Source registry.
3. Search log.
4. Claims registry.
5. Open-problem ledger when relevant.
6. Framework progress tracker.
7. Final status pass records for central open, conditional, or recently changed
   claims.
8. Generated evidence report.
9. Main paper source.
10. Compiled deliverable.

## Status Display Rules

- Put the most important proven results in the executive synthesis.
- Put exact model distinctions in the status matrix or coverage chart.
- Put limitations and non-implications before the detailed model survey.
- Keep scope-exclusion cells visible in the model-separation or evidence
  sections, not in the theorem-result rows unless they are needed to prevent a
  common misreading.
- Put open problems in three groups: source-stated, conditional, and derived.
- Put remaining evidence gaps in the completeness/evidence sections.
- Put the most recent final-status-pass date in the completeness/evidence
  section when the paper preserves an open or conditional conclusion.
