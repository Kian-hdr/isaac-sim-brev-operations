#!/usr/bin/env python3
"""Validate a generated Isaac robotics documentation pack."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED = (
    "PROJECT.md", "docs/01-system-and-runtime.md", "docs/02-reward-and-policy.md",
    "docs/03-training-and-curriculum.md", "docs/04-evaluation-and-acceptance.md",
    "docs/05-deliverables-and-media.md", "operations/EXECUTION_LOG.md",
    "operations/HANDOFF.md", "reproducibility/acceptance-matrix.csv",
    "reproducibility/artifact-contract.md",
)
ALLOWED_STATUS = {"PENDING", "PASSED", "FAILED", "BLOCKED", "UNAVAILABLE"}
CSV_COLUMNS = (
    "gate_id", "domain", "requirement", "required_evidence", "status",
    "evidence_pointer", "owner", "last_checked", "claim_enabled",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    root = parser.parse_args().target.expanduser().resolve()
    errors: list[str] = []
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\{\{[A-Z0-9_]+\}\}", text):
            errors.append(f"unresolved template token: {relative}")
        if not text.strip():
            errors.append(f"empty required file: {relative}")
    matrix = root / "reproducibility/acceptance-matrix.csv"
    if matrix.is_file():
        with matrix.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != CSV_COLUMNS:
                errors.append("acceptance matrix columns do not match the contract")
            seen: set[str] = set()
            row_count = 0
            for line_number, row in enumerate(reader, start=2):
                row_count += 1
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"acceptance matrix line {line_number}: malformed row")
                if (row.get("status") or "").strip() == "PASSED" and not (row.get("evidence_pointer") or "").strip():
                    errors.append(f"acceptance matrix line {line_number}: PASSED requires an evidence pointer")
                gate_id = (row.get("gate_id") or "").strip()
                if not gate_id:
                    errors.append(f"acceptance matrix line {line_number}: missing gate_id")
                elif gate_id in seen:
                    errors.append(f"acceptance matrix line {line_number}: duplicate gate_id {gate_id}")
                seen.add(gate_id)
                status = (row.get("status") or "").strip()
                if status not in ALLOWED_STATUS:
                    errors.append(f"acceptance matrix line {line_number}: invalid status {status!r}")
            if row_count == 0:
                errors.append("acceptance matrix must contain at least one gate")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Project documentation pack valid: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
