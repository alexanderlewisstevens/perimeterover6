# Literature Review Scaffold

This directory holds the evidence layer for the review. The goal is to make
the prose auditable: every status claim in the paper should trace back to a
source record with the exact model and parameter stated.

## Files

- `source_registry.json`: one structured record per source in the bibliography.
- `claims_registry.json`: one structured claim/result record per theorem,
  conjecture, lower bound, hardness result, survey claim, or open-problem
  statement used by the review.
- `coverage_matrix.json`: completeness map for the main model/result cells and
  explicit scope-exclusion cells for adjacent variants that should not be
  translated into the central bounds.
- `open_problems.json`: open-problem clusters and the sources supporting their
  current status.
- `framework_progress.md`: live progress board for the review workflow, known
  framework gaps, and next update queue.
- `document_assembly.md`: map for how the ledgers, progress tracker, evidence
  report, and polished PDF fit together.
- `search_queries.md`: reusable searches for expanding the review.
- `search_log.md`: record of searches run, hits inspected, inclusion decisions,
  exclusions, and follow-up actions.
- `journals_and_venues.md`: journals, proceedings, books, and pages worth
  monitoring.
- `authors.md`: author map by topic area.
- `download_manifest.json`: open-access PDFs that can be downloaded locally
  into `papers/downloads/`.
- `evidence_report.md`: generated audit report created by
  `scripts/generate_evidence_report.py`.

## Pipeline

1. **Scope cell.** Identify the exact object class, holes assumption, guard
   model, dimension, and parameter before comparing a result with existing
   claims.
2. **Intake.** Add a source with DOI/URL, venue, bibliographic metadata, and a
   source role: primary result, survey, book, thesis, open-problem page,
   discovery source, or exclusion.
3. **Search log.** Record the search path that found the source: exact title,
   DOI/arXiv, author page, backward reference, forward citation, venue scan,
   keyword variant, or adjacent terminology.
4. **Result extraction.** Record each relevant theorem, conjecture, lower
   bound, hardness result, algorithmic result, survey role, or open-problem
   statement in `claims_registry.json`.
5. **Locator pass.** Add theorem, page, problem, conjecture, or figure
   locators whenever available. For open problems, add short source quotations
   when they help remove ambiguity.
6. **Model translation.** State what the claim does and does not imply for
   perimeter-over-six, holes, lattice versus continuous models, guard models,
   and 3D analogues.
7. **Coverage update.** Link the claim to the relevant cells in
   `coverage_matrix.json`, including a status and next action. If a
   relevant-looking variant is intentionally excluded rather than cited, record
   a scope-exclusion cell so the model decision remains auditable.
8. **Open-problem update.** Link open or conditional claims to affected
   open-problem clusters, and label them as source-stated, conditional, or
   derived.
9. **Progress update.** Update `framework_progress.md` when a stage status,
   next action, or work queue item changes.
10. **Assembly check.** Check `document_assembly.md` if the paper structure or
   artifact roles changed.
11. **Paper update.** Only then update `orthogonal_art_gallery_lit_review.tex`.
12. **Audit.** Run `python3 scripts/check_source_registry.py`, generate the
   evidence report, rebuild the PDF, and inspect the LaTeX log.

## Completeness Checklist

Use this checklist before claiming that a result is known, missing,
conditional, or open.

- The model cell is explicit: object class, holes, guard type, parameter, and
  dimension are all recorded.
- The source is primary for the mathematical claim, or the review clearly says
  when a survey, book, or thesis is being used for synthesis.
- The claim appears in `claims_registry.json` with a status and locator, or the
  evidence report makes the missing locator visible as follow-up work.
- The translation note says which nearby statements do not follow.
- The relevant coverage cells link back to the claim.
- Any open-problem entry states whether the problem is source-stated,
  conditional on an unproved hypothesis, or derived from the coverage matrix.
- The search log records at least one seed path, one backward or forward path,
  and any plausible exclusions for the model cell.
- The progress tracker reflects the current stage status and next action.
- The paper prose is updated after the evidence files, not before.

## Status Labels

The ledgers declare their allowed status vocabularies at the top level. The
validator rejects undeclared values, so add a vocabulary entry before using a
new status in a source, claim, coverage cell, result-status field, or
open-problem record.

- `theorem`: proved but not necessarily tight.
- `tight_theorem`: proved and accompanied by matching examples/lower bounds.
- `conditional`: follows from a stated unproved conjecture or hypothesis.
- `conjecture`: explicitly proposed but not proved in the source.
- `open_problem`: explicitly identified as open, or derived from the source map.
- `hardness`: computational complexity result.
- `survey`: background, terminology, or historical synthesis.
