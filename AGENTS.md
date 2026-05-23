# Literature Review Agent Instructions

This repository is a literature-review project for art-gallery problems around
orthogonal polygons, polyominoes, orthogonal polyhedra, perimeter-type bounds,
and open problems.

## Core Rule

Never translate a result across models without recording the model change.
Track at least:

- object class: simple polygon, orthogonal polygon, polyomino, integral
  orthogonal polygon, ortho-unit polygon, polycube, orthogonal polyhedron;
- holes: forbidden, allowed, bounded, or unspecified;
- guard model: point, vertex, boundary, edge, reflex edge, face, sliding camera,
  transmitter, or discrete visibility;
- parameter: vertices `n`, holes `h`, cells `m`, lattice perimeter `ell`,
  integral perimeter `N`, polyhedron edges `m`, reflex edges `r`, genus `g`;
- result status: theorem, tight theorem, conditional theorem, conjecture,
  open problem, lower bound, hardness, approximation, survey context.

## Evidence Workflow

1. Add or update the source in `literature/source_registry.json`.
2. Extract each theorem, conjecture, lower bound, hardness result, survey
   claim, or open-problem statement into `literature/claims_registry.json`.
3. Record the safe review translation in each claim's `translation_note`.
4. Update `literature/coverage_matrix.json` so every important model cell has
   a status, supporting claims, and a next action.
5. If a result is open or conditional, record the dependency in
   `literature/open_problems.json` and link it from the relevant claim and
   coverage cell.
6. Add primary URLs/DOIs when available. Use secondary pages only as discovery
   aids.
7. Record meaningful searches, including relevant-looking exclusions, in
   `literature/search_log.md`.
8. Update `orthogonal_art_gallery_lit_review.tex` only after source, claim,
   coverage, and open-problem records support the prose.

## Download Policy

Do not commit large PDFs or paywalled publisher copies. Open author PDFs,
arXiv PDFs, theses, and public book PDFs may be downloaded into
`papers/downloads/`, which is git-ignored. Record intended downloads in
`literature/download_manifest.json`.

## Search Workflow

Use a layered search:

1. primary DOI/arXiv/publisher page for each cited source;
2. author pages and public PDFs;
3. backward references from surveys, books, and theses;
4. forward searches by exact title;
5. topic searches in arXiv, DBLP, Google Scholar/Semantic Scholar, and journal
   pages.

Record reusable query strings in `literature/search_queries.md`.

## Document Architecture

The main review paper should be the readable public artifact, while the JSON
and generated Markdown files provide auditability. Use the framework templates
under `framework/templates/` for new reviews.

Every polished review should have:

1. executive summary;
2. scope and model choices;
3. result status matrix;
4. historical flow;
5. core results by model;
6. proof-technique map;
7. model separations and non-implications;
8. open problems and research directions;
9. annotated source guide;
10. evidence appendix or generated evidence-report link.

## Checks

Before finalizing changes:

```sh
python3 scripts/check_source_registry.py
python3 scripts/generate_evidence_report.py
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
git diff --check
rg -n "LaTeX Warning|Overfull|Underfull|undefined|Fatal|Error" orthogonal_art_gallery_lit_review.log
```

The log-scan command is expected to return no matches when the build is clean;
use `|| true` if running it inside a larger shell script.
