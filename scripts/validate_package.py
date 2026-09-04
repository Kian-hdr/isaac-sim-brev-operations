#!/usr/bin/env python3
"""Validate this distribution offline using only the Python standard library."""
from __future__ import annotations

import argparse
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    'SKILL.md', 'README.md', 'SETUP_PROMPT.md', 'LICENSE', 'NOTICE.md', 'VERSION',
    'VALIDATION.md', 'agents/openai.yaml', 'examples/prompts.md',
    'scripts/init_project_docs.py', 'scripts/validate_project_docs.py',
    'scripts/install_skill.py', 'scripts/validate_package.py', 'scripts/setup_smoke.py',
    'tests/test_package.py',
)
REFERENCES = ('execution-standard', 'project-documentation', 'reward-policy-design',
              'isaac-runtime', 'brev-lifecycle', 'isaac-media', 'project-overlay')
TEMPLATES = ('PROJECT.md', 'docs/01-system-and-runtime.md', 'docs/02-reward-and-policy.md',
             'docs/03-training-and-curriculum.md', 'docs/04-evaluation-and-acceptance.md',
             'docs/05-deliverables-and-media.md', 'operations/EXECUTION_LOG.md',
             'operations/HANDOFF.md', 'reproducibility/acceptance-matrix.csv',
             'reproducibility/artifact-contract.md')
IGNORED = {'.git', '__pycache__', '.venv'}
# Heuristics only. Never print the matching text, which might contain a secret.
PRIVATE_PATTERNS = (
    r'/Users/[A-Za-z0-9_.-]+/', r'/Volumes/[A-Za-z0-9_. -]+/', r'[A-Z]:\\Users\\[^\\\s]+\\',
    r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
    r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}',
    r'AKIA[A-Z0-9]{16}', r'sk-[A-Za-z0-9_-]{32,}',
)


def validate(root):
    errors = []
    required = list(REQUIRED_FILES)
    required += [f'references/{name}.md' for name in REFERENCES]
    required += [f'assets/project-docs/{name}' for name in TEMPLATES]
    for name in required:
        path = root / name
        if not path.is_file() or path.is_symlink():
            errors.append(f'Missing or linked resource: {name}')
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if any(part in IGNORED for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f'Symlink is not a distributable resource: {relative}')
            continue
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'Unexpected non-text resource: {relative}')
            continue
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, text):
                errors.append(f'Potential private content in {relative}; inspect locally')
                break
        if path.suffix == '.py':
            try:
                ast.parse(text)
            except SyntaxError:
                errors.append(f'Invalid Python syntax: {relative}')
        if path.suffix == '.md':
            for link in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
                url = urlsplit(link.strip('<>'))
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (path.parent / unquote(url.path)).resolve()
                if root.resolve() not in target.parents or not target.exists():
                    errors.append(f'Broken or external local link in {relative}: {url.path}')
    skill = root / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        if not match:
            errors.append('Missing skill frontmatter')
        else:
            # This package uses two scalar fields; this is not a general YAML parser.
            fields = dict(line.split(': ', 1) for line in match[1].splitlines() if ': ' in line)
            if fields.get('name') != 'isaac-sim-brev-operations':
                errors.append('Incorrect skill name')
            if not 1 <= len(fields.get('description', '')) <= 1024:
                errors.append('Missing or oversized skill description')
    readme, prompt = root / 'README.md', root / 'SETUP_PROMPT.md'
    if readme.is_file() and prompt.is_file():
        blocks = []
        for path in (readme, prompt):
            match = re.search(r'```text\n(.*?)\n```', path.read_text(encoding='utf-8'), re.S)
            blocks.append(match[1] if match else None)
        if not blocks[0] or blocks[0] != blocks[1]:
            errors.append('README and SETUP_PROMPT setup blocks differ or are absent')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    if not errors:
        print('Package validation passed (structure, links, syntax, prompt parity, privacy heuristics).')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
