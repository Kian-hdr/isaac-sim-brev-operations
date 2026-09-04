#!/usr/bin/env python3
"""Replay safe setup in temporary directories; never install into the real user profile."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

from install_skill import NAME, ROOT, payload


def run(*args, expected=0):
    result = subprocess.run([sys.executable, *map(str, args)], cwd=ROOT,
                            capture_output=True, text=True)
    if result.returncode != expected:
        raise RuntimeError(f'Unexpected exit {result.returncode}: {result.stdout}\n{result.stderr}')
    return result


def main():
    with tempfile.TemporaryDirectory(prefix='isaac-skill-setup-') as temp:
        workspace = Path(temp).resolve()
        skills = workspace / 'agent skills'
        run(ROOT / 'scripts/validate_package.py')
        run(ROOT / 'scripts/install_skill.py', '--skills-dir', skills, '--dry-run')
        if skills.exists():
            raise RuntimeError('Dry run wrote files')
        run(ROOT / 'scripts/install_skill.py', '--skills-dir', skills)
        installed = skills / NAME
        for source in payload():
            if source.read_bytes() != (installed / source.relative_to(ROOT)).read_bytes():
                raise RuntimeError('Installed content differs')
        run(installed / 'scripts/validate_package.py')
        project = workspace / 'warehouse demo'
        command = (installed / 'scripts/init_project_docs.py', project, '--project-name',
                   'Warehouse Robot Demo', '--artifact-root', workspace / 'artifacts')
        run(*command)
        run(installed / 'scripts/validate_project_docs.py', project)
        before = {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in project.rglob('*') if p.is_file()}
        if len(before) != 10:
            raise RuntimeError('Expected ten generated documents')
        with (project / 'reproducibility/acceptance-matrix.csv').open(encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(f))
        if not rows or any(row['status'] != 'PENDING' for row in rows):
            raise RuntimeError('Safe example must leave every gate PENDING')
        run(*command, expected=3)
        after = {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in project.rglob('*') if p.is_file()}
        if before != after:
            raise RuntimeError('Refused generation altered existing files')
        run(ROOT / 'scripts/install_skill.py', '--skills-dir', skills, expected=2)
        print('Setup smoke passed: isolated install, byte parity, installed validation,')
        print('ten-file safe example, PENDING gates, and non-overwrite behavior.')
        print('Temporary test workspace cleaned. No GPU, network, or account operations performed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
