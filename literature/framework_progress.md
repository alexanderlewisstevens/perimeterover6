# Framework Progress Tracker

Last updated: 2026-05-26

This file is the live progress board for the literature-review framework. It
tracks whether each framework stage has been updated for the current review and
which artifact needs attention next. The evidence report says what the ledgers
currently contain; this file says where the review process stands.

## Status Labels

- `done`: complete for the current scope, but still revisited when new sources
  or model cells are added.
- `active`: usable now, with known follow-up work.
- `needs_work`: important framework work remains before the review should be
  treated as polished.
- `blocked`: waiting on access, source discovery, or a decision about scope.
- `recurring`: should be repeated during every substantial literature pass.

## Framework Stage Dashboard

| Stage | Status | Primary artifacts | Current state | Next update |
| --- | --- | --- | --- | --- |
| Scope and model cells | `active` | `coverage_matrix.json`, paper scope sections | The main 2D, polyomino, integral-polygon, 3D orthogonal-polyhedron, cited adjacent-model cells, and current adjacent-model exclusions are represented. | Add a new coverage cell or scope-exclusion cell before adding prose for any newly discovered variant. |
| Source intake | `active` | `source_registry.json`, bibliography | The bibliography and source registry are aligned. | Mark discovery-only and exclusion sources more explicitly as searches expand. |
| Search tracking | `active` | `search_log.md`, `search_queries.md` | Major seed searches, the first forward/adjacent-model sweep, and the final OpenAlex/web status pass are recorded. | Repeat forward-citation, venue-scan, author-page, and exclusion entries after new central sources appear or before a future release. |
| Claim extraction | `active` | `claims_registry.json` | Every cited source has at least one claim record. | Split any source that supports multiple distinct theorems/open problems into separate claim records when needed. |
| Locator pass | `active` | `claims_registry.json`, `evidence_report.md` | Central, foundational 2D, holes, 3D baseline, and restricted-visibility locator batches are complete for the current cited-source set. | Keep locator checks recurring as new sources are added or adjacent models are split into separate cells. |
| Translation audit | `active` | `claims_registry.json`, model-separation section | The main non-implications around holes, lattice scale, guard type, and 3D analogues are recorded. | Recheck translation notes whenever a new result is added to a neighboring model cell. |
| Coverage update | `active` | `coverage_matrix.json`, status tables | No coverage cells are currently marked unsearched/searching; the adjacent-model split, explicit scope-exclusion pass, and limited-field edge-guard cell are complete. | Keep `next_action` fields current as searches or locators change. |
| Open-problem update | `active` | `open_problems.json`, open-problem section | Eight open-problem clusters are tracked. | Label any new cluster as source-stated, conditional, or derived before using it in the paper. |
| Document assembly | `active` | `document_assembly.md`, paper section order, framework templates | The paper now has a front executive synthesis and an explicit map from ledgers to reader-facing sections; the reusable templates now include scope-exclusion cells and a final-status-pass template. | Recheck the assembly map and templates whenever the paper structure, artifact roles, or release gate changes. |
| Paper synchronization | `active` | `orthogonal_art_gallery_lit_review.tex`, PDF | The paper includes the current synthesis, completeness protocol, final-status-pass outcome table, and evidence audit trail. | Update prose only after source, claim, coverage, open-problem, progress, and assembly records support the change. |
| Audit and build | `recurring` | `scripts/`, `evidence_report.md`, PDF | Registry checks now validate cross-links, scope-exclusion cells, and declared status vocabularies. | Run checks after every substantive evidence or prose edit. |

## High-Priority Work Queue

1. Repeat forward-citation, venue, and author-page scans after any new central
   source is added or before the next public release.
2. Promote floodlight, half-plane, dispersive, contiguous, mobile, or
   point-boundary variants to source and claim records only if the paper later
   cites a specific theorem-level result from one of those adjacent models.
3. Extract theorem-level subclaims for face guards, sliding cameras,
   transmitters, k-hop visibility, and discrete polyforms only if the review
   expands beyond the current extremal-bound focus.
4. Keep the coverage matrix `next_action` fields synchronized with this board
   and the document assembly map.
5. Keep reusable framework templates synchronized with any process rule learned
   from this review.
6. Add new source, claim, coverage, result, or open-problem statuses to the
   appropriate declared vocabulary before using them in records.
7. Regenerate `evidence_report.md` and rebuild the PDF after each batch of
   source or claim updates.

## Update Transaction Checklist

Use this checklist whenever adding literature, changing a status claim, or
editing an open problem.

- Identify the scope cell or create a new one.
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
- Run or update the final status pass for central open, conditional, or
  recent-status claims before publishing or pushing.
- Regenerate the evidence report.
- Update the paper prose and rebuild the PDF.
- Run validation checks before publishing or pushing.

## Recurring Check Commands

```sh
python3 scripts/check_source_registry.py
python3 scripts/generate_evidence_report.py
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
pdflatex -interaction=nonstopmode -halt-on-error orthogonal_art_gallery_lit_review.tex
git diff --check
```
