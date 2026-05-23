# CS Literature Review Framework

This directory contains reusable templates for building an auditable literature
review in computer science. The core idea is to separate bibliographic truth,
claim truth, coverage/completeness state, open-problem state, and final prose.

## Core Artifacts

- `source_registry.json`: what each source is.
- `claims_registry.json`: what each source proves, conjectures, surveys, or
  leaves open.
- `coverage_matrix.json`: which model/problem cells are covered, open,
  conditional, unknown, or out of scope.
- `open_problems.json`: unresolved questions and their supporting evidence.
- `search_log.md`: searches performed and why sources were included or
  excluded.
- `evidence_report.md`: generated audit companion for the paper.

## Standard Workflow

1. Define scope as a coverage matrix.
2. Seed the review with canonical surveys, books, open-problem pages, and
   central papers.
3. Run backward citation, forward citation, venue, author, and keyword sweeps.
4. Add source records.
5. Extract claim records.
6. Update coverage and open-problem records.
7. Generate the evidence report.
8. Write or revise the paper only after evidence records support the prose.

The templates in `framework/templates/` define the paper architecture and the
record shapes for results, open problems, and evidence reports.
