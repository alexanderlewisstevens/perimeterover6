# Review Paper Outline

Use this outline for a literature review whose prose is backed by structured
evidence files. The goal is a readable paper first, with enough traceability
that every result and open problem can be audited.

## 1. Executive Summary

- State the field, the main axes of variation, and the result map in one page.
- Highlight the most important proven results.
- Highlight the genuinely open directions and distinguish source-stated open
  problems from derived gaps.
- Make this section agree with the document assembly map.

## 2. Scope and Model Choices

- Define the problem classes, models, parameters, and assumptions once.
- State excluded variants and boundary cases.
- State whether excluded variants are informal background or formal
  scope-exclusion cells in the evidence layer.
- Identify terms that are commonly confused across the literature.

## 3. Result Status Matrix

- Give a compact table of model cells versus theorem/open/conditional status.
- Include the primary source for each central status claim.
- Include adjacent-but-excluded model cells only when they prevent a likely
  misreading of the status table.
- Make the status matrix agree with `coverage_matrix.json`.

## 4. Historical Flow

- Explain how the literature developed.
- Keep this narrative short; it should orient the reader before technical
  sections, not replace the result map.

## 5. Core Results by Model

- Group the main body by model, object class, problem family, or other natural
  axes from the coverage matrix.
- For each important result, use the result-card fields: model, assumptions,
  parameter, exact conclusion, status, primary source, and non-implications.

## 6. Proof-Technique Map

- Explain which techniques prove which result families.
- Explain where each technique breaks or requires additional hypotheses.

## 7. Model Separations and Non-Implications

- List tempting but invalid transfers across assumptions, problem variants,
  dimensions, benchmark settings, datasets, complexity classes, or parameters.
- When a tempting transfer comes from a searched but excluded variant, name the
  evidence-layer exclusion cell instead of treating the absence as implicit.

## 8. Open Problems and Research Directions

- Put source-stated open problems first.
- Then list conditional gaps.
- Then list derived research directions identified by comparing known results.

## 9. Annotated Source Guide

- Give short source notes for central papers, surveys, books, theses, and
  open-problem pages.
- Prefer role-oriented annotations over full abstracts.

## 10. Completeness and Evidence Protocol

- State that completeness means auditability, not proof that no paper was
  missed.
- Describe the review workflow: scope cells, source intake, layered searches,
  claim extraction, translation notes, coverage updates, open-problem updates,
  progress tracking, document assembly, locator pass, final status pass, and
  paper synchronization.
- List the remaining evidence gaps, such as missing locators, unsearched
  coverage cells, outdated forward-citation sweeps, progress-board items, or
  unrecorded exclusions.
- Distinguish theorem-level coverage cells from scope-exclusion cells, which
  support model separation but do not themselves assert mathematical results.

## 11. Evidence Appendix or Generated Report Link

- Link to the generated evidence report.
- Summarize remaining verification gaps, coverage gaps, and search gaps.
