# Final Status Pass Template

Use this pass before publishing a review, after adding a central source, or
after reopening a status claim. Its job is not to prove that the literature is
complete. Its job is to make the latest status claim auditable.

## Trigger

Run this pass when any of these are true:

- the paper says a result is open, conditional, recently proved, or not known;
- a central source, theorem, conjecture, or open problem was added;
- the review is about to be pushed, released, submitted, or shared publicly;
- a reader is likely to ask whether a newer paper changes a status row.

## Source Set

List the central records whose status could change.

- Central theorem or conjecture sources:
- Open-problem pages, theses, surveys, or books:
- Adjacent-model sources that readers may confuse with the central model:
- Venues, authors, and keywords most likely to contain follow-up work:

## Search Recipe

For each central source, record the exact searches in `search_log.md` and add
reusable query strings to `search_queries.md`.

1. DOI/arXiv/publisher lookup for the source itself.
2. Forward-citation lookup from OpenAlex, Semantic Scholar, Google Scholar,
   DBLP, MathSciNet, zbMATH, or field-specific indexes.
3. Exact-title web search for the source and for the central theorem/problem
   phrase.
4. Author-page and coauthor-page scan for follow-up papers, preprints, slides,
   theses, and errata.
5. Venue scan for the field's main journals, conferences, and workshops since
   the last checked date.
6. Topic search using the most likely synonyms, older names, parameter names,
   and adjacent-model terminology.
7. Adjacent-model search for plausible but non-comparable results that need
   explicit exclusion or separate coverage cells.

## Evidence Updates

After the searches, update the evidence layer before editing prose.

- Add new theorem-level sources to `source_registry.json`.
- Add one claim record per theorem, conjecture, lower bound, hardness result,
  survey claim, or open-problem statement.
- Create a theorem-level coverage cell for a comparable result.
- Create a scope-exclusion cell for a relevant-looking but non-comparable
  adjacent model when it affects reader interpretation.
- Update open-problem records with the search date and the exact reason the
  status did or did not change.
- Update `framework_progress.md` and `document_assembly.md` if the review's
  release readiness or paper flow changed.

## Status Outcomes

Use one of these outcomes in the search log and coverage matrix.

- `status_changed`: a new source proves, disproves, sharpens, or reframes the
  central claim.
- `status_preserved`: searches found no tracked source changing the central
  claim.
- `adjacent_source_added`: a source is relevant for orientation but belongs to
  a different model cell.
- `scope_exclusion_added`: a tempting source or model was excluded with a
  recorded rationale.
- `blocked_by_access`: a source looks important, but the primary text or
  locator is not available yet.

## Language Rules

- Say "no tracked source found in this pass" rather than "no source exists."
- Give the pass date and the search route when preserving an open or
  conditional status.
- Do not cite a forward-search result count as proof of openness by itself.
- If an adjacent result is added, state the changed model axis before
  discussing the theorem.
- If a central status changes, update the executive summary, status matrix,
  open-problem section, annotated source guide, and evidence trail together.

## Release Gate

Before committing or publishing, run the repository's validation commands and
record failures as next actions instead of smoothing them over in prose.

```sh
python3 scripts/check_source_registry.py
python3 scripts/generate_evidence_report.py
pdflatex -interaction=nonstopmode -halt-on-error REVIEW_SOURCE.tex
pdflatex -interaction=nonstopmode -halt-on-error REVIEW_SOURCE.tex
git diff --check
rg -n "LaTeX Warning|Overfull|Underfull|undefined|Fatal|Error" REVIEW_SOURCE.log
```

If the review is not LaTeX-based, replace the build and log-scan commands with
the equivalent renderer, link checker, notebook execution, test suite, or
artifact-generation command.
