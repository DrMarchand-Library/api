#!/usr/bin/env python3
"""
Public Privacy Lint

This linter protects the public DrMarchand-Library/api repository from private
address records, identity proof, credentials, and sensitive business records.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".yml", ".yaml", ".py", ".js", ".ts",
    ".tsx", ".jsx", ".html", ".css", ".xml"
}

SKIP_DIRS = {
    ".git", ".venv", "node_modules", "vendor", "dist", "build", "__pycache__"
}

@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str

RULES: List[Rule] = [
    Rule(
        "private_address_terms",
        re.compile(r"\b(?:home address|apartment|apt\.?|driver license|address proof|residence proof)\b", re.IGNORECASE),
        "Private address/license proof language does not belong in the public API repo.",
    ),
    Rule(
        "specific_address_markers",
        re.compile(r"\b(?:pine meadows|fort myers|routing number|bank account|ssn|social security|passport)\b", re.IGNORECASE),
        "Potential specific private identity/address/banking marker found.",
    ),
    Rule(
        "private_financial_records",
        re.compile(r"\b(?:tax return|w-9|ein certificate|bank statement|payroll|irs transcript)\b", re.IGNORECASE),
        "Private tax, banking, payroll, or IRS materials do not belong in the public API repo.",
    ),
    Rule(
        "credentials",
        re.compile(r"\b(?:service_account|private_key|client_secret|api[_-]?key|access_token|refresh_token)\b", re.IGNORECASE),
        "Credential-like material must never be committed to the public API repo.",
    ),
]

ALLOWLIST = [
    re.compile(r"PUBLIC_DATA_BOUNDARY\.md"),
    re.compile(r"public_privacy_lint\.py"),
]


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def is_allowlisted(path: Path) -> bool:
    path_text = path.as_posix()
    return any(pattern.search(path_text) for pattern in ALLOWLIST)


def scan_file(path: Path) -> List[str]:
    if is_allowlisted(path):
        return []

    findings: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings

    for line_no, line in enumerate(text.splitlines(), start=1):
        for rule in RULES:
            if rule.pattern.search(line):
                findings.append(
                    f"ERROR: {path}:{line_no}: {rule.name}: {rule.message}\n"
                    f"  -> {line.strip()}"
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Protect public repo from private data leakage.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    findings: List[str] = []
    for path in iter_files(Path(args.root).resolve()):
        findings.extend(scan_file(path))

    if findings:
        print("\n".join(findings))
        return 1

    print("Public privacy lint passed. No private address/proof/credential markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
