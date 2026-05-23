# CS Literature Review Framework

This directory contains reusable templates for building an auditable literature
review in computer science. The core idea is to separate bibliographic truth,
claim truth, coverage/completeness state, open-problem state, and final prose.

## Core Artifacts

- `source_registry.json`: what each source is.
- `claims_registry.json`: what each source proves, conjectures, surveys, or
  leaves open.
- `coverage_matrix.json`: which model/problem cells are covered, open,
  conditional, unknown, or out of scope, including explicit scope-exclusion
  cells for adjacent variants that should not be translated into central
  results.
- `open_problems.json`: unresolved questions and their supporting evidence.
- `framework_progress.md`: live progress board for workflow stage status,
  review gaps, and next update queue.
- `document_assembly.md`: map showing how the evidence artifacts become a
  readable literature-review paper.
- `search_log.md`: searches performed and why sources were included or
  excluded.
- `evidence_report.md`: generated audit companion for the paper.
- `templates/completeness_protocol.md`: reusable checklist for
  deciding when a review can responsibly say a result is known, missing,
  conditional, or open.
- `templates/progress_tracker.md`: reusable dashboard for tracking which
  framework stages are done, active, blocked, or recurring.

## Standard Workflow

1. Define scope as a coverage matrix. Use explicit axes such as object class,
   assumptions, model, parameter, dimension, dataset, benchmark, or complexity
   setting. Declare allowed status vocabularies before relying on them in
   records or prose.
2. Seed the review with canonical surveys, books, theses, open-problem pages,
   and central theorem papers.
3. Run layered searches: exact title and DOI/arXiv lookup, author pages,
   backward references, forward citation searches, venue scans, keyword
   variants, and adjacent terminology.
4. Add source records. Mark whether each source is primary evidence for a
   claim, a survey source, a discovery source, or an exclusion.
5. Extract claim records. Each theorem, conjecture, lower bound, hardness
   result, algorithmic result, benchmark result, survey claim, or open problem
   gets its own record.
6. Record translation notes. State what the claim does and does not imply
   across nearby models or assumptions before using it in prose.
7. Update coverage records. Every important cell should have a status,
   supporting claim identifiers, and a next action. For adjacent sources or
   model variants that are deliberately not part of the review, add a
   scope-exclusion cell or equivalent exclusion record instead of leaving the
   decision only in prose.
8. Update open-problem records. Separate source-stated open problems,
   conditional gaps, and derived gaps.
9. Add locators and quotations where useful. Prefer theorem numbers, page
   numbers, problem numbers, figure numbers, and short quotes from the primary
   source for open-problem statements.
10. Update the progress tracker. Record which framework stage changed, what is
    still incomplete, and which artifact should be updated next.
11. Check the document assembly map when the structure, artifact roles, or
    reader-facing flow changes.
12. Generate the evidence report and run validation checks.
13. Write or revise the paper only after evidence records support the prose.

## Completeness Criteria

The framework does not treat completeness as proof that no relevant paper was
missed. It treats completeness as an auditable state. A review is in good
shape when:

- every central prose claim has a source record and claim record;
- every result comparison names the model axes being compared;
- every status value used by the ledgers is declared and validated;
- every open-problem statement is labeled as source-stated, conditional, or
  derived from the coverage matrix;
- every in-scope coverage cell has a status and next action;
- every important adjacent-but-excluded variant has a recorded exclusion
  rationale before it is used as negative evidence;
- every important search path has a search-log entry, including plausible
  exclusions;
- the progress tracker agrees with the coverage matrix, evidence report, and
  current work queue;
- the document assembly map explains how the evidence artifacts support the
  reader-facing paper;
- every missing locator is visible in the evidence report instead of hidden in
  prose;
- the generated evidence report, registry validator, paper build, and
  formatting checks have been run after the last substantive edit.

## Search Layers

Use multiple search layers because literature reviews usually miss results at
model boundaries rather than at obvious title matches.

1. Exact source lookup: title, DOI, arXiv identifier, publisher page, DBLP, and
   author-hosted PDF.
2. Seed expansion: references from books, surveys, theses, and open-problem
   lists.
3. Forward expansion: papers citing each seed source, especially recent survey
   and thesis citations.
4. Venue expansion: proceedings and journals where the area regularly appears.
5. Author expansion: recurring authors, coauthors, students, and follow-up
   papers.
6. Terminology expansion: synonyms, older terminology, adjacent models, and
   benchmark names.
7. Exclusion pass: record sources that look relevant but are not in scope, with
   the reason.

The templates in `framework/templates/` define the paper architecture and the
record shapes for results, open problems, and evidence reports.
