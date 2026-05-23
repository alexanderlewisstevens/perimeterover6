# Result Card Template

Use one card per theorem, conjecture, lower bound, hardness result,
approximation result, survey claim, or open-problem statement.

```json
{
  "id": "claim_short_source_or_result_name",
  "source_key": "BibliographyKey",
  "claim_type": "theorem | tight_theorem | conditional | conjecture | open_problem | lower_bound | hardness | approximation | survey",
  "result_statement": "Exact result as needed by the review.",
  "model_scope": {
    "objects": [],
    "variants": [],
    "parameters": [],
    "assumptions": []
  },
  "locator": "page/theorem/conjecture number, or not_recorded",
  "verification_status": "primary_checked | secondary_checked | needs_page_or_theorem_locator | needs_primary_check",
  "translation_note": "Safe prose translation for the review.",
  "limitations": [],
  "non_implications": [],
  "open_problem_links": [],
  "coverage_cells": [],
  "paper_sections": [],
  "importance": "central | supporting | background"
}
```

## Writing Rules

- Do not merge multiple unrelated theorems into one claim.
- Do not translate across models without recording the changed assumption.
- Do not create a claim record just to justify an exclusion. Use a
  scope-exclusion coverage cell or search-log exclusion unless a specific
  theorem, conjecture, lower bound, hardness result, survey claim, or
  open-problem statement is being used.
- Record missing page/theorem locators as `not_recorded`; the evidence report
  will surface them as verification gaps.
