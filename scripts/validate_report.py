#!/usr/bin/env python3
"""Validate generated Markdown reports before commit."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DATE_SUFFIX = re.compile(r"-\d{4}-\d{2}-\d{2}\.md$")


def validate(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    try:
        relative = path.resolve().relative_to(root.resolve())
    except ValueError:
        return [f"Report is outside the repository: {path}"]

    if relative.parts[:1] != ("reports",):
        errors.append(f"Report must be under reports/: {relative}")
    if path.suffix.lower() != ".md":
        errors.append(f"Report must be Markdown: {relative}")
    if not DATE_SUFFIX.search(path.name):
        errors.append(f"Filename must end with -YYYY-MM-DD.md: {relative}")
    if not path.is_file():
        errors.append(f"Report does not exist: {relative}")
        return errors

    content = path.read_text(encoding="utf-8")
    if not content.strip():
        errors.append(f"Report is empty: {relative}")
    if not any(line.startswith("# ") for line in content.splitlines()):
        errors.append(f"Report has no H1 heading: {relative}")
    if "read.readwise.io/" in content:
        errors.append(f"Report contains a Readwise reader URL instead of an original source URL: {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs="+", type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    errors = [error for report in args.reports for error in validate(report, root)]
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(args.reports)} report(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

