#!/usr/bin/env python3
"""Validate the literature evidence layer against the LaTeX bibliography."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "literature" / "source_registry.json"
CLAIMS = ROOT / "literature" / "claims_registry.json"
COVERAGE = ROOT / "literature" / "coverage_matrix.json"
OPEN_PROBLEMS = ROOT / "literature" / "open_problems.json"
PROGRESS_TRACKER = ROOT / "literature" / "framework_progress.md"
DOCUMENT_ASSEMBLY = ROOT / "literature" / "document_assembly.md"
TEX = ROOT / "orthogonal_art_gallery_lit_review.tex"

REQUIRED_SOURCE_FIELDS = {
    "key",
    "citation",
    "links",
    "venue",
    "source_type",
    "status",
    "objects",
    "guard_models",
    "parameters",
    "relevant_result",
    "translation_note",
    "open_problem_links",
    "verification",
}

REQUIRED_OPEN_PROBLEM_FIELDS = {
    "id",
    "title",
    "question",
    "status",
    "known",
    "confirming_sources",
    "non_implications",
    "progress_paths",
}

REQUIRED_CLAIM_FIELDS = {
    "id",
    "source_key",
    "claim_type",
    "result_statement",
    "model_scope",
    "locator",
    "verification_status",
    "translation_note",
    "limitations",
    "non_implications",
    "open_problem_links",
    "coverage_cells",
    "paper_sections",
    "importance",
}

REQUIRED_COVERAGE_FIELDS = {
    "id",
    "title",
    "domain_axes",
    "coverage_status",
    "result_status",
    "summary",
    "supporting_sources",
    "supporting_claims",
    "open_problem_links",
    "paper_sections",
    "next_action",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def status_values(data: dict, field: str, errors: list[str], label: str) -> set[str]:
    values = data.get(field)
    if not isinstance(values, list) or not values:
        errors.append(f"{label} missing nonempty {field}")
        return set()
    invalid = [value for value in values if not isinstance(value, str) or not value.strip()]
    if invalid:
        errors.append(f"{label}.{field} contains non-string or empty values")
    duplicates = {value for value in values if values.count(value) > 1}
    if duplicates:
        errors.append(f"{label}.{field} contains duplicates: {sorted(duplicates)}")
    return set(values)


def bibitem_keys(tex: str) -> set[str]:
    return set(re.findall(r"\\bibitem\{([^}]+)\}", tex))


def citation_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for match in re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", tex):
        keys.update(part.strip() for part in match.split(",") if part.strip())
    return keys


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    registry = load_json(REGISTRY)
    claims_data = load_json(CLAIMS)
    coverage_data = load_json(COVERAGE)
    open_problem_data = load_json(OPEN_PROBLEMS)
    sources = registry.get("sources", [])
    claims = claims_data.get("claims", [])
    coverage_cells = coverage_data.get("coverage_cells", [])
    open_problems = open_problem_data.get("open_problems", [])
    source_status_values = status_values(registry, "status_values", errors, "source_registry")
    claim_type_values = status_values(claims_data, "claim_type_values", errors, "claims_registry")
    coverage_status_values = status_values(coverage_data, "coverage_status_values", errors, "coverage_matrix")
    result_status_values = status_values(coverage_data, "result_status_values", errors, "coverage_matrix")
    open_problem_status_values = status_values(open_problem_data, "status_values", errors, "open_problems")

    seen: set[str] = set()
    registry_keys: set[str] = set()
    for i, source in enumerate(sources):
        missing = REQUIRED_SOURCE_FIELDS - set(source)
        if missing:
            errors.append(f"source[{i}] missing fields: {sorted(missing)}")
            continue

        key = source["key"]
        if key in seen:
            errors.append(f"duplicate source key: {key}")
        seen.add(key)
        registry_keys.add(key)

        for field in ("links", "objects", "guard_models", "parameters", "open_problem_links", "verification"):
            if not isinstance(source[field], list):
                errors.append(f"{key}.{field} must be a list")

        for field in ("citation", "venue", "source_type", "status", "relevant_result", "translation_note"):
            if not isinstance(source[field], str) or not source[field].strip():
                errors.append(f"{key}.{field} must be a nonempty string")

        if source.get("status") not in source_status_values:
            errors.append(f"{key}.status has undeclared value: {source.get('status')}")

    claim_ids: set[str] = set()
    source_keys_with_claims: set[str] = set()
    for i, claim in enumerate(claims):
        missing = REQUIRED_CLAIM_FIELDS - set(claim)
        if missing:
            errors.append(f"claim[{i}] missing fields: {sorted(missing)}")
            continue

        claim_id = claim["id"]
        if claim_id in claim_ids:
            errors.append(f"duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)

        source_key = claim["source_key"]
        source_keys_with_claims.add(source_key)
        if source_key not in registry_keys:
            errors.append(f"{claim_id} links unknown source: {source_key}")

        for field in ("limitations", "non_implications", "open_problem_links", "coverage_cells", "paper_sections"):
            if not isinstance(claim[field], list):
                errors.append(f"{claim_id}.{field} must be a list")

        if not isinstance(claim["model_scope"], dict):
            errors.append(f"{claim_id}.model_scope must be an object")

        for field in ("result_statement", "locator", "verification_status", "translation_note", "importance"):
            if not isinstance(claim[field], str) or not claim[field].strip():
                errors.append(f"{claim_id}.{field} must be a nonempty string")

        if claim.get("claim_type") not in claim_type_values:
            errors.append(f"{claim_id}.claim_type has undeclared value: {claim.get('claim_type')}")

        if "tracking_issue" in claim:
            tracking_issue = claim["tracking_issue"]
            if not isinstance(tracking_issue, dict):
                errors.append(f"{claim_id}.tracking_issue must be an object")
            else:
                if not isinstance(tracking_issue.get("number"), int):
                    errors.append(f"{claim_id}.tracking_issue.number must be an integer")
                if not isinstance(tracking_issue.get("url"), str) or not tracking_issue["url"].strip():
                    errors.append(f"{claim_id}.tracking_issue.url must be a nonempty string")

        if claim["locator"] == "not_recorded":
            warnings.append(f"{claim_id} missing page/theorem locator")

    open_problem_ids: set[str] = set()
    for i, problem in enumerate(open_problems):
        missing = REQUIRED_OPEN_PROBLEM_FIELDS - set(problem)
        if missing:
            errors.append(f"open_problem[{i}] missing fields: {sorted(missing)}")
            continue

        problem_id = problem["id"]
        if problem_id in open_problem_ids:
            errors.append(f"duplicate open problem id: {problem_id}")
        open_problem_ids.add(problem_id)

        for field in ("confirming_sources", "non_implications", "progress_paths"):
            if not isinstance(problem[field], list):
                errors.append(f"{problem_id}.{field} must be a list")

        for field in ("title", "question", "status", "known"):
            if not isinstance(problem[field], str) or not problem[field].strip():
                errors.append(f"{problem_id}.{field} must be a nonempty string")

        if problem.get("status") not in open_problem_status_values:
            errors.append(f"{problem_id}.status has undeclared value: {problem.get('status')}")

    for source in sources:
        if "key" not in source:
            continue
        key = source["key"]
        for problem_id in source.get("open_problem_links", []):
            if problem_id not in open_problem_ids:
                errors.append(f"{key} links unknown open problem: {problem_id}")

    for problem in open_problems:
        if "id" not in problem:
            continue
        problem_id = problem["id"]
        for source_key in problem.get("confirming_sources", []):
            if source_key not in registry_keys:
                errors.append(f"{problem_id} confirms with unknown source: {source_key}")

    coverage_ids: set[str] = set()
    for i, cell in enumerate(coverage_cells):
        missing = REQUIRED_COVERAGE_FIELDS - set(cell)
        if missing:
            errors.append(f"coverage_cell[{i}] missing fields: {sorted(missing)}")
            continue

        cell_id = cell["id"]
        if cell_id in coverage_ids:
            errors.append(f"duplicate coverage cell id: {cell_id}")
        coverage_ids.add(cell_id)

        for field in ("supporting_sources", "supporting_claims", "open_problem_links", "paper_sections"):
            if not isinstance(cell[field], list):
                errors.append(f"{cell_id}.{field} must be a list")

        if not isinstance(cell["domain_axes"], dict):
            errors.append(f"{cell_id}.domain_axes must be an object")

        for source_key in cell.get("supporting_sources", []):
            if source_key not in registry_keys:
                errors.append(f"{cell_id} links unknown source: {source_key}")

        for claim_id in cell.get("supporting_claims", []):
            if claim_id not in claim_ids:
                errors.append(f"{cell_id} links unknown claim: {claim_id}")

        for problem_id in cell.get("open_problem_links", []):
            if problem_id not in open_problem_ids:
                errors.append(f"{cell_id} links unknown open problem: {problem_id}")

        if cell["coverage_status"] in {"unsearched", "searching"}:
            warnings.append(f"{cell_id} is not complete: {cell['coverage_status']}")

        if cell["coverage_status"].startswith("scope_excluded") and cell.get("supporting_claims"):
            errors.append(f"{cell_id} is a scope-exclusion cell but has theorem-level supporting claims")

        if cell.get("coverage_status") not in coverage_status_values:
            errors.append(f"{cell_id}.coverage_status has undeclared value: {cell.get('coverage_status')}")

        if cell.get("result_status") not in result_status_values:
            errors.append(f"{cell_id}.result_status has undeclared value: {cell.get('result_status')}")

    for claim in claims:
        if "id" not in claim:
            continue
        claim_id = claim["id"]
        for problem_id in claim.get("open_problem_links", []):
            if problem_id not in open_problem_ids:
                errors.append(f"{claim_id} links unknown open problem: {problem_id}")
        for cell_id in claim.get("coverage_cells", []):
            if cell_id not in coverage_ids:
                errors.append(f"{claim_id} links unknown coverage cell: {cell_id}")

    tex = TEX.read_text(encoding="utf-8")
    bib_keys = bibitem_keys(tex)
    cite_keys = citation_keys(tex)

    missing_from_registry = sorted(bib_keys - registry_keys)
    if missing_from_registry:
        errors.append(f"bibitems missing from registry: {missing_from_registry}")

    registry_not_in_bib = sorted(registry_keys - bib_keys)
    if registry_not_in_bib:
        errors.append(f"registry keys missing from bibliography: {registry_not_in_bib}")

    cited_without_bibitem = sorted(cite_keys - bib_keys)
    if cited_without_bibitem:
        errors.append(f"citations without bibitem: {cited_without_bibitem}")

    cited_without_claim = sorted(cite_keys - source_keys_with_claims)
    if cited_without_claim:
        errors.append(f"cited sources missing claim records: {cited_without_claim}")

    if not PROGRESS_TRACKER.exists():
        errors.append("missing framework progress tracker: literature/framework_progress.md")
    else:
        progress_text = PROGRESS_TRACKER.read_text(encoding="utf-8")
        for heading in (
            "## Framework Stage Dashboard",
            "## High-Priority Work Queue",
            "## Update Transaction Checklist",
        ):
            if heading not in progress_text:
                errors.append(f"progress tracker missing heading: {heading}")

    if not DOCUMENT_ASSEMBLY.exists():
        errors.append("missing document assembly map: literature/document_assembly.md")
    else:
        assembly_text = DOCUMENT_ASSEMBLY.read_text(encoding="utf-8")
        for heading in (
            "## Narrative Spine",
            "## Artifact Roles",
            "## Paper Flow",
            "## Update Order",
        ):
            if heading not in assembly_text:
                errors.append(f"document assembly map missing heading: {heading}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{len(registry_keys)} source records match {len(bib_keys)} bibliography entries; "
        f"{len(claim_ids)} claim records, {len(coverage_ids)} coverage cells, "
        f"and {len(open_problem_ids)} open-problem records are cross-linked."
    )
    if warnings:
        print(f"WARN: {len(warnings)} non-blocking evidence gaps.")
        for warning in warnings[:20]:
            print(f"WARN: {warning}")
        if len(warnings) > 20:
            print(f"WARN: ... {len(warnings) - 20} more warnings omitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
