# Completeness Protocol Template

Use this protocol as the review's audit checklist. Adapt the scope axes and
search layers to the field, but keep the separation between sources, claims,
coverage, open problems, and prose.

## Scope Axes

Define the axes that determine whether two results are comparable.

- Object or problem class:
- Assumptions and variants:
- Model or method:
- Parameter, metric, or benchmark:
- Dimension, domain, dataset, or setting:
- Declared source, claim, coverage, result, and open-problem status labels:

## Inclusion Workflow

1. Identify the exact scope cell before comparing the result with existing
   literature.
2. Add the source with DOI/URL, venue, year, authors, and source role.
3. Record how the source was found: seed source, exact-title search, DOI/arXiv
   lookup, author page, backward reference, forward citation, venue scan,
   keyword variant, adjacent terminology, or exclusion pass.
4. Extract one claim record per theorem, conjecture, lower bound, hardness
   result, algorithmic result, benchmark result, survey claim, or open-problem
   statement.
5. Add locators: theorem, page, problem, conjecture, figure, dataset, table,
   or appendix references. Mark missing locators explicitly.
6. Write the translation note: what the claim safely implies for the review
   and what nearby statements it does not imply.
7. Update the coverage matrix with status, supporting claims, and next action.
   If the source or model is relevant-looking but deliberately excluded, add a
   scope-exclusion cell or equivalent exclusion record with no theorem-level
   supporting claim.
8. Update the open-problem ledger when the claim is open, conditional, or
   exposes a derived gap.
9. Update the progress tracker when a framework stage, next action, or work
   queue item changes.
10. Check the document assembly map when the reader-facing structure or
    artifact roles change.
11. Add or update prose only after the evidence records support the statement.
12. Regenerate the evidence report and run validation checks.

## Open-Problem Classification

- `source_stated_open_problem`: a source explicitly states that the problem is
  open, conjectural, or unresolved.
- `conditional_gap`: the desired result follows from an unproved hypothesis or
  conjecture.
- `derived_research_direction`: the review identifies the gap by comparing
  searched coverage cells.
- `scope_exclusion`: the review has searched or encountered an adjacent model
  and records why it is not evidence for the central claim.

## Search Layers

1. Exact lookup: title, DOI, arXiv, publisher page, DBLP, and author PDF.
2. Seed expansion: books, surveys, theses, tutorials, and open-problem pages.
3. Backward citation expansion from every central source.
4. Forward citation expansion from every central source.
5. Venue expansion in the journals, conferences, workshops, and books where
   the field regularly publishes.
6. Author expansion through recurring authors, coauthors, students, and
   follow-up papers.
7. Terminology expansion through synonyms, older names, adjacent models, and
   benchmark terminology.
8. Exclusion pass for plausible but out-of-scope sources.

## Completeness Gate

Before stating that a result is known, missing, conditional, or open, verify:

- the scope cell is explicit;
- every status value in the affected records is declared in the relevant
  ledger vocabulary;
- the source is primary for the claim or clearly labeled as synthesis;
- the claim record has a status, locator, and translation note;
- non-implications across nearby models are recorded;
- affected coverage cells link back to the claim;
- excluded adjacent variants have a scope-exclusion cell or search-log
  exclusion before they are cited as non-implications;
- affected open-problem records are classified correctly;
- search-log entries support the conclusion;
- the progress tracker reflects the current work queue;
- the document assembly map still describes the paper structure;
- remaining gaps are visible in the evidence report.

## Paper Language Rules

- Say "source-stated open problem" only when a source says it directly.
- Say "conditional" when an implication depends on an unproved hypothesis.
- Say "derived gap" or "research direction" when the review infers the gap
  from searched coverage cells.
- Avoid saying a result is absent from the literature unless the search log
  makes the basis for that statement clear.
- Do not cite a scope-exclusion cell as a theorem. It records a model decision,
  not a mathematical result.
