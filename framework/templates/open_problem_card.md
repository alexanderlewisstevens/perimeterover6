# Open Problem Card Template

Use this for unresolved questions, conditional gaps, and derived research
directions.

```json
{
  "id": "stable_open_problem_id",
  "title": "Readable title",
  "problem_type": "source_stated_open_problem | conditional_gap | derived_research_direction",
  "question": "Precise question.",
  "status": "open | open_with_partial_results | open_or_conditional | active_research_direction",
  "known": "What is already known.",
  "confirming_sources": [],
  "supporting_claims": [],
  "non_implications": [],
  "progress_paths": [],
  "coverage_cells": []
}
```

## Classification Rules

- `source_stated_open_problem`: the source explicitly states the problem is
  open or conjectural.
- `conditional_gap`: a desired result follows from an unproved conjecture or
  hypothesis.
- `derived_research_direction`: the review identifies the gap by comparing
  known results.
