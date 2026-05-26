# Document Assembly Map

Last updated: 2026-05-23

This map explains how the review artifacts combine into the reader-facing
paper. The goal is to keep the final document readable while preserving an
auditable path from every result and open problem back to the evidence layer.

## Narrative Spine

The paper should answer four questions in order:

1. What is the main result map for orthogonal art-gallery problems?
2. Which perimeter-over-six readings are already proven, and why?
3. Which nearby statements do not follow because of holes, scale, guard type,
   dimension, or parameter changes?
4. Which problems remain genuinely open, conditional, or derived from the
   coverage matrix?

The short answer belongs near the front of the paper. The technical survey,
proof techniques, and evidence audit then justify that short answer.

## Artifact Roles

| Artifact | Reader-facing role | Maintenance role |
| --- | --- | --- |
| `orthogonal_art_gallery_lit_review.tex` | Main polished literature-review paper. | Presents only claims supported by the evidence layer. |
| `orthogonal_art_gallery_lit_review.pdf` | Compiled public deliverable. | Rebuilt after prose or evidence changes. |
| `source_registry.json` | Bibliographic ground truth. | Records each source, role, links, and verification state. |
| `claims_registry.json` | Extracted theorem/problem ledger. | One claim per theorem, conjecture, hardness result, survey claim, or open-problem statement. |
| `coverage_matrix.json` | Result-status map by model cell. | Prevents model changes from being hidden in prose. |
| `open_problems.json` | Open-problem ledger. | Separates source-stated, conditional, and derived open directions. |
| `search_log.md` | Search audit trail. | Records searches, inclusions, exclusions, and follow-up paths. |
| `framework_progress.md` | Workflow progress board. | Tracks which framework stage needs attention next. |
| `evidence_report.md` | Generated audit companion. | Summarizes counts, gaps, coverage cells, and next actions. |

## Paper Flow

1. **Abstract.** One-paragraph short answer.
2. **Executive synthesis.** Reader-facing result map and the main open
   directions.
3. **Introduction and scope.** Why the models must be separated.
4. **Conventions and terminology.** Definitions used once, then reused.
5. **Historical flow.** How the main result lines developed.
6. **Status overview and 2D coverage chart.** Compact proven/open/conditional
   map.
7. **Model separations and proof techniques.** Why tempting implications fail
   and where proof methods break.
8. **Status by model.** More detailed 2D, polyomino, integral, and 3D survey.
9. **Open problems and research directions.** Source-stated problems first,
   then conditional gaps, then derived directions.
10. **Annotated source guide.** Role of each central paper.
11. **Completeness protocol and evidence trail.** How the review was checked
   and what still needs verification.
12. **Conclusion.** Concise list of the main statuses.

## Update Order

When a new source or result is added, update artifacts in this order:

1. `coverage_matrix.json` if a new model cell is needed.
2. `source_registry.json`.
3. `search_log.md`.
4. `claims_registry.json`.
5. `open_problems.json` if the result is open, conditional, or gap-forming.
6. `framework_progress.md`.
7. Final status pass records in `search_log.md` and `search_queries.md` for
   central open, conditional, or recent-status claims.
8. `evidence_report.md` by running the generator.
9. `orthogonal_art_gallery_lit_review.tex`.
10. `orthogonal_art_gallery_lit_review.pdf`.

The paper should not be the first place where a new result appears.

## Status Display Rules

- Put the most important proven results in the executive synthesis.
- Put exact model distinctions in the status matrix or coverage chart.
- Put limitations and non-implications before the detailed model survey.
- Put open problems in three groups: source-stated, conditional, and derived.
- Put remaining evidence gaps in the completeness/evidence sections rather
  than smoothing them into the prose.

## Current Assembly Assessment

The paper now has the required reader-facing layers: short answer, synthesis
table, scope definitions, status matrix, coverage chart, model separations,
proof-technique map, model-by-model survey, open problems, annotated sources,
and evidence protocol. The first forward/adjacent-model sweep and final
OpenAlex/web status pass for the central open clusters are logged, the
currently cited adjacent models have their own coverage cells, and the
currently excluded adjacent models have explicit scope-exclusion cells. The
main remaining assembly work is recurring rather than structural: repeat
forward-citation and venue scans after new central sources appear, and add
either a theorem-level coverage cell or a scope-exclusion cell before adding
prose about any newly discovered visibility or guard variant.
