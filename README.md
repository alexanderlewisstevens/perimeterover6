# Orthogonal Art Gallery Literature Review

Literature review for art-gallery problems related to orthogonal polygons,
polyominoes, and 3D orthogonal polyhedra.

The review focuses on perimeter-type guard bounds, especially the question of
whether orthogonal lattice objects can be guarded with at most perimeter over
six guards. It also records source-confirmed open problems and separates proven
results from conditional or conjectural statements.

## Contents

- Definitions for the 2D and 3D objects, guard models, and common parameters
  used in the review.
- A status overview separating 2D orthogonal polygons, polyominoes,
  ortho-unit polygons, integral orthogonal polygons, and 3D orthogonal
  polyhedra.
- A coverage chart showing which 2D classes are included in the principal
  bounds and which are not.
- A model-separation section explaining which results do not imply each other
  because of scale, holes, guard type, or dimension.
- A proof-technique map explaining where coloring, quadrilateralization,
  rectangle packing, area arguments, and 3D edge-guard methods apply.
- Focused survey sections for 2D orthogonal polygons, polyomino perimeter
  results, and 3D orthogonal polyhedra.
- Algorithmic and optimization context for hardness, approximation, sliding
  cameras, transmitters, and discrete visibility variants.
- A research-facing open-problem table, a concise problem list, and an
  annotated source guide.

## Files

- `orthogonal_art_gallery_lit_review.tex`: LaTeX source.
- `orthogonal_art_gallery_lit_review.pdf`: compiled review.
- `AGENTS.md`: working instructions for future literature-review agents.
- `framework/templates/`: reusable templates for CS literature-review papers,
  result cards, open-problem cards, and evidence reports.
- `literature/source_registry.json`: structured source-by-source evidence
  ledger.
- `literature/claims_registry.json`: one result/claim record per extracted
  theorem, conjecture, hardness result, survey claim, or open-problem statement.
- `literature/coverage_matrix.json`: completeness map for the model/result
  cells covered by the review.
- `literature/open_problems.json`: open-problem clusters and their supporting
  sources.
- `literature/search_log.md`: search audit log for included and excluded
  literature.
- `literature/search_queries.md`: reusable search strings for follow-up
  arXiv, DOI, venue, and author searches.
- `literature/journals_and_venues.md`: journals, proceedings, books, and pages
  to monitor.
- `literature/authors.md`: author map by subtopic.
- `literature/download_manifest.json`: open-access PDFs worth downloading
  locally into `papers/downloads/`.
- `scripts/check_source_registry.py`: consistency check between the LaTeX
  bibliography, source registry, claim registry, coverage matrix, and open
  problems.
- `scripts/generate_evidence_report.py`: generates the Markdown evidence audit.
- `papers/`: local paper-cache instructions. Downloaded PDFs are intentionally
  git-ignored.

## Review Workflow

The paper is now backed by an auditable evidence layer. Add each source to
`literature/source_registry.json`, extract each result into
`literature/claims_registry.json`, update the relevant cells in
`literature/coverage_matrix.json`, link any affected open problem in
`literature/open_problems.json`, and only then update the LaTeX prose.

Run these checks before publishing changes:

```sh
python3 scripts/check_source_registry.py
python3 scripts/generate_evidence_report.py
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
git diff --check
```

## Main Status Summary

- The perimeter-over-six theorem is proven for hole-free polyominoes.
- Hole-free integral orthogonal polygons overlap exactly with the hole-free
  polyomino theorem after unit-grid subdivision, so their `floor(N/6)` bound is
  not a separate open problem.
- The polyomino-with-holes version is conditional/open.
- The Diaz-Banez integral `floor(N/6)` wording remains open only under a
  broader reading that allows holes or another lattice-domain convention not
  reduced to a hole-free polyomino.
- In 3D, the standard terminology is orthogonal polyhedron or orthogonal
  polytope, and point guards do not give a direct planar analogue.

The most direct open directions are the polyomino-with-holes perimeter bound,
Massberg's maximal-rectangle packing conjecture, the holes/broader-domain
`floor(N/6)` extension, and Urrutia-type edge-guard conjectures for
orthogonal polyhedra.
