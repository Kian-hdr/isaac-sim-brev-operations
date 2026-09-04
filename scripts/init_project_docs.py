#!/usr/bin/env python3
"""Create a non-overwriting, project-neutral Isaac robotics documentation pack."""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

TEMPLATE_ROOT = Path(__file__).resolve().parent.parent / "assets" / "project-docs"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("project name must contain at least one letter or digit")
    return slug


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", text)))
    if unresolved:
        raise ValueError(f"unresolved template tokens: {', '.join(unresolved)}")
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Project root to populate")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--artifact-root", default="TO_BE_DEFINED_EXTERNAL_ARTIFACT_ROOT")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not TEMPLATE_ROOT.is_dir():
        print(f"Template root is missing: {TEMPLATE_ROOT}", file=sys.stderr)
        return 2
    try:
        project_slug = slugify(args.project_name)
        if date.fromisoformat(args.date).isoformat() != args.date:
            raise ValueError("date must be YYYY-MM-DD")
        for value in (args.project_name, args.artifact_root):
            if any(c in value for c in ("\n", "\r", "\0", "`", "|", "{{", "}}")):
                raise ValueError("name and artifact root must be single-line text without template or Markdown delimiters")
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    files = sorted(path for path in TEMPLATE_ROOT.rglob("*") if path.is_file())
    if not files:
        print("No project templates found", file=sys.stderr)
        return 2
    target = args.target.expanduser().resolve()
    destinations = [(source, target / source.relative_to(TEMPLATE_ROOT)) for source in files]
    conflicts = [destination for _, destination in destinations if os.path.lexists(destination)]
    for _, destination in destinations:
        for parent in destination.parents:
            if parent == target:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                conflicts.append(parent)
    if conflicts:
        print("Refusing to overwrite existing project documentation:", file=sys.stderr)
        for path in conflicts:
            print(f"  {path}", file=sys.stderr)
        return 3
    values = {
        "PROJECT_NAME": args.project_name,
        "PROJECT_SLUG": project_slug,
        "DATE": args.date,
        "ARTIFACT_ROOT": args.artifact_root,
    }
    rendered = [(destination, render(source.read_text(encoding="utf-8"), values)) for source, destination in destinations]
    if args.dry_run:
        for destination, _ in rendered:
            print(destination)
        return 0
    for destination, content in rendered:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("x", encoding="utf-8") as handle:
            handle.write(content)
        print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
