#!/usr/bin/env python3
"""Generate a Markdown evidence report from the literature ledgers."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LITERATURE = ROOT / "literature"
SOURCES = LITERATURE / "source_registry.json"
CLAIMS = LITERATURE / "claims_registry.json"
COVERAGE = LITERATURE / "coverage_matrix.json"
OPEN_PROBLEMS = LITERATURE / "open_problems.json"
SEARCH_LOG = LITERATURE / "search_log.md"
PROGRESS_TRACKER = LITERATURE / "framework_progress.md"
DOCUMENT_ASSEMBLY = LITERATURE / "document_assembly.md"
OUTPUT = LITERATURE / "evidence_report.md"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None recorded.\n"
    return "".join(f"- {item}\n" for item in items)


def main() -> int:
    source_data = load_json(SOURCES)
    claim_data = load_json(CLAIMS)
    coverage_data = load_json(COVERAGE)
    open_problem_data = load_json(OPEN_PROBLEMS)

    sources = source_data.get("sources", [])
    claims = claim_data.get("claims", [])
    coverage_cells = coverage_data.get("coverage_cells", [])
    open_problems = open_problem_data.get("open_problems", [])

    source_by_key = {source["key"]: source for source in sources}
    claim_by_id = {claim["id"]: claim for claim in claims}

    source_statuses = Counter(source["status"] for source in sources)
    claim_types = Counter(claim["claim_type"] for claim in claims)
    coverage_statuses = Counter(cell["coverage_status"] for cell in coverage_cells)
    open_problem_statuses = Counter(problem["status"] for problem in open_problems)

    major_results = [
        claim
        for claim in claims
        if claim["importance"] == "central"
        and claim["claim_type"] in {"theorem", "tight_theorem"}
    ]
    conditional_or_open_claims = [
        claim
        for claim in claims
        if claim["claim_type"] in {"conditional", "conjecture", "open_problem"}
    ]
    missing_locators = [
        claim
        for claim in claims
        if claim["locator"] == "not_recorded"
    ]
    unsearched_cells = [
        cell
        for cell in coverage_cells
        if cell["coverage_status"] in {"unsearched", "searching"}
    ]
    scope_exclusion_cells = [
        cell
        for cell in coverage_cells
        if cell["coverage_status"].startswith("scope_excluded")
    ]
    next_actions = [
        f"{cell['title']}: {cell['next_action']}"
        for cell in coverage_cells
        if cell.get("next_action")
    ]

    lines: list[str] = []
    lines.append("# Evidence Report\n\n")
    lines.append(
        "Generated from the structured literature ledgers. This report is an "
        "audit companion for the review paper, not a substitute for the prose.\n\n"
    )

    lines.append("## Summary\n\n")
    lines.append(f"- Sources: {len(sources)}\n")
    lines.append(f"- Claims: {len(claims)}\n")
    lines.append(f"- Coverage cells: {len(coverage_cells)}\n")
    lines.append(f"- Scope-exclusion cells: {len(scope_exclusion_cells)}\n")
    lines.append(f"- Open-problem clusters: {len(open_problems)}\n")
    lines.append(f"- Claims missing page/theorem locators: {len(missing_locators)}\n")
    lines.append(f"- Coverage cells still unsearched/searching: {len(unsearched_cells)}\n\n")

    lines.append("## Status Counts\n\n")
    lines.append("### Source Statuses\n\n")
    lines.append(bullet_list([f"`{key}`: {value}" for key, value in sorted(source_statuses.items())]))
    lines.append("\n### Claim Types\n\n")
    lines.append(bullet_list([f"`{key}`: {value}" for key, value in sorted(claim_types.items())]))
    lines.append("\n### Coverage Statuses\n\n")
    lines.append(bullet_list([f"`{key}`: {value}" for key, value in sorted(coverage_statuses.items())]))
    lines.append("\n### Open-Problem Statuses\n\n")
    lines.append(bullet_list([f"`{key}`: {value}" for key, value in sorted(open_problem_statuses.items())]))
    lines.append("\n")

    lines.append("## Declared Status Vocabularies\n\n")
    lines.append("### Source Status Values\n\n")
    lines.append(bullet_list([f"`{value}`" for value in source_data.get("status_values", [])]))
    lines.append("\n### Claim Type Values\n\n")
    lines.append(bullet_list([f"`{value}`" for value in claim_data.get("claim_type_values", [])]))
    lines.append("\n### Coverage Status Values\n\n")
    lines.append(bullet_list([f"`{value}`" for value in coverage_data.get("coverage_status_values", [])]))
    lines.append("\n### Result Status Values\n\n")
    lines.append(bullet_list([f"`{value}`" for value in coverage_data.get("result_status_values", [])]))
    lines.append("\n### Open-Problem Status Values\n\n")
    lines.append(bullet_list([f"`{value}`" for value in open_problem_data.get("status_values", [])]))
    lines.append("\n")

    lines.append("## Major Proven Results\n\n")
    for claim in major_results:
        source = source_by_key.get(claim["source_key"], {})
        lines.append(f"### `{claim['id']}`\n\n")
        lines.append(f"- Source: `{claim['source_key']}`")
        if source.get("venue"):
            lines.append(f" ({source['venue']})")
        lines.append("\n")
        lines.append(f"- Status: `{claim['claim_type']}`\n")
        lines.append(f"- Result: {claim['result_statement']}\n")
        lines.append(f"- Translation note: {claim['translation_note']}\n")
        lines.append(f"- Locator: {claim['locator']}\n\n")
        if claim.get("tracking_issue"):
            issue = claim["tracking_issue"]
            lines.append(f"- Tracking issue: [#{issue['number']}]({issue['url']})\n\n")

    lines.append("## Open and Conditional Problems\n\n")
    for problem in open_problems:
        lines.append(f"### `{problem['id']}`\n\n")
        lines.append(f"- Title: {problem['title']}\n")
        lines.append(f"- Status: `{problem['status']}`\n")
        lines.append(f"- Question: {problem['question']}\n")
        lines.append(f"- Known: {problem['known']}\n")
        lines.append(f"- Confirming sources: {', '.join(problem['confirming_sources'])}\n")
        lines.append(f"- Progress paths: {'; '.join(problem['progress_paths'])}\n\n")

    if conditional_or_open_claims:
        lines.append("## Conditional or Open Claim Records\n\n")
        for claim in conditional_or_open_claims:
            lines.append(f"- `{claim['id']}` (`{claim['claim_type']}`): {claim['result_statement']}\n")
        lines.append("\n")

    lines.append("## Coverage Matrix\n\n")
    for cell in coverage_cells:
        lines.append(f"### `{cell['id']}`\n\n")
        lines.append(f"- Title: {cell['title']}\n")
        lines.append(f"- Coverage status: `{cell['coverage_status']}`\n")
        lines.append(f"- Result status: `{cell['result_status']}`\n")
        lines.append(f"- Summary: {cell['summary']}\n")
        if cell in scope_exclusion_cells:
            lines.append(
                "- Evidence role: Scope-exclusion cell; this records a model "
                "decision, not a theorem-level claim.\n"
            )
            supporting_claims = ", ".join(cell["supporting_claims"]) or (
                "None recorded; this is expected for a scope-exclusion cell."
            )
            lines.append(f"- Supporting theorem claims: {supporting_claims}\n")
        else:
            supporting_claims = ", ".join(cell["supporting_claims"]) or "None recorded."
            lines.append(f"- Supporting claims: {supporting_claims}\n")
        lines.append(f"- Next action: {cell['next_action']}\n\n")

    lines.append("## Verification Gaps\n\n")
    if missing_locators:
        for claim in missing_locators:
            if claim.get("tracking_issue"):
                issue = claim["tracking_issue"]
                lines.append(
                    f"- `{claim['id']}` needs page/theorem locator "
                    f"([#{issue['number']}]({issue['url']})).\n"
                )
            else:
                lines.append(f"- `{claim['id']}` needs page/theorem locator.\n")
    else:
        lines.append("- No missing locators recorded.\n")
    lines.append("\n")

    lines.append("## Search and Completeness Gaps\n\n")
    if unsearched_cells:
        for cell in unsearched_cells:
            lines.append(f"- `{cell['id']}` is `{cell['coverage_status']}`.\n")
    else:
        lines.append("- No coverage cells are currently marked `unsearched` or `searching`.\n")
    if scope_exclusion_cells:
        excluded_ids = ", ".join(f"`{cell['id']}`" for cell in scope_exclusion_cells)
        lines.append(f"- Scope-exclusion cells tracked: {excluded_ids}.\n")
    if SEARCH_LOG.exists():
        lines.append(f"- Search log present: `{SEARCH_LOG.relative_to(ROOT)}`.\n")
    else:
        lines.append("- Search log missing.\n")
    if PROGRESS_TRACKER.exists():
        lines.append(f"- Progress tracker present: `{PROGRESS_TRACKER.relative_to(ROOT)}`.\n")
    else:
        lines.append("- Progress tracker missing.\n")
    if DOCUMENT_ASSEMBLY.exists():
        lines.append(f"- Document assembly map present: `{DOCUMENT_ASSEMBLY.relative_to(ROOT)}`.\n")
    else:
        lines.append("- Document assembly map missing.\n")
    lines.append("\n")

    lines.append("## Next Actions\n\n")
    lines.append(bullet_list(next_actions))
    if PROGRESS_TRACKER.exists():
        lines.append(f"\nSee `{PROGRESS_TRACKER.relative_to(ROOT)}` for the framework-stage work queue.\n")
    if DOCUMENT_ASSEMBLY.exists():
        lines.append(f"See `{DOCUMENT_ASSEMBLY.relative_to(ROOT)}` for the reader-facing document flow.\n")

    OUTPUT.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
