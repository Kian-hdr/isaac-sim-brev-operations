#!/usr/bin/env python3
"""Install a complete local skill copy, without overwriting an existing installation."""
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
NAME = 'isaac-sim-brev-operations'
FILES = ('SKILL.md', 'README.md', 'SETUP_PROMPT.md', 'LICENSE', 'NOTICE.md',
         'VERSION', 'VALIDATION.md')
DIRECTORIES = ('agents', 'assets', 'references', 'scripts', 'examples', 'tests')


def payload():
    paths = [ROOT / name for name in FILES]
    for name in DIRECTORIES:
        directory = ROOT / name
        if not directory.is_dir() or directory.is_symlink():
            raise ValueError(f'Missing or linked directory: {name}')
        paths.extend(p for p in directory.rglob('*')
                     if '__pycache__' not in p.parts and p.suffix != '.pyc'
                     and (p.is_file() or p.is_symlink()))
    for path in paths:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Missing or linked payload file: {path.relative_to(ROOT)}')
    return sorted(paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', type=Path, default=Path.home() / '.agents' / 'skills',
                        help='Parent skills directory (default: ~/.agents/skills)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        sources = payload()
        parent = args.skills_dir.expanduser().resolve()
        target = parent / NAME
        if os.path.lexists(target):
            raise ValueError(f'Refusing to overwrite existing installation: {target}')
        if target == ROOT or ROOT in target.parents:
            raise ValueError('Installation must be outside the source package')
        if args.dry_run:
            print(f'Would install {len(sources)} files to {target}')
            return 0
        parent.mkdir(parents=True, exist_ok=True)
        target.mkdir()  # Exclusive creation also protects against concurrent installers.
        for source in sources:
            destination = target / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open('xb') as handle:
                handle.write(source.read_bytes())
            if hashlib.sha256(destination.read_bytes()).digest() != hashlib.sha256(source.read_bytes()).digest():
                raise OSError(f'Copy verification failed: {destination}')
        print(f'Installed and hash-verified {len(sources)} files: {target}')
        print('Invoke $isaac-sim-brev-operations in your agent. Restart it if discovery is stale.')
        return 0
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        print('An interrupted installation may remain; inspect it before moving it aside and retrying.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
