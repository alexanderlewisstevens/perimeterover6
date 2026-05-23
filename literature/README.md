# Literature Review Scaffold

This directory holds the evidence layer for the review. The goal is to make
the prose auditable: every status claim in the paper should trace back to a
source record with the exact model and parameter stated.

## Files

- `source_registry.json`: one structured record per source in the bibliography.
- `claims_registry.json`: one structured claim/result record per theorem,
  conjecture, lower bound, hardness result, survey claim, or open-problem
  statement used by the review.
- `coverage_matrix.json`: completeness map for the main model/result cells.
- `open_problems.json`: open-problem clusters and the sources supporting their
  current status.
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

1. **Intake.** Add a source with DOI/URL, venue, and bibliographic metadata.
2. **Result extraction.** Record each relevant theorem, conjecture, lower
   bound, hardness result, or survey role in `claims_registry.json`.
3. **Model translation.** State what the claim does and does not imply for
   perimeter-over-six, holes, and 3D analogues.
4. **Coverage update.** Link the claim to the relevant cells in
   `coverage_matrix.json`.
5. **Open-problem update.** Link open or conditional claims to affected
   open-problem clusters.
6. **Paper update.** Only then update `orthogonal_art_gallery_lit_review.tex`.
7. **Audit.** Run `python3 scripts/check_source_registry.py`, generate the
   evidence report, and rebuild the PDF.

## Status Labels

- `theorem`: proved but not necessarily tight.
- `tight_theorem`: proved and accompanied by matching examples/lower bounds.
- `conditional`: follows from a stated unproved conjecture or hypothesis.
- `conjecture`: explicitly proposed but not proved in the source.
- `open_problem`: explicitly identified as open, or derived from the source map.
- `hardness`: computational complexity result.
- `survey`: background, terminology, or historical synthesis.
