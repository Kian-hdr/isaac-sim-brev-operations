"""Behavioral regression tests; no network, GPU, credentials, or external dependencies."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


def command(script, *args):
    return subprocess.run([sys.executable, str(ROOT / 'scripts' / script), *map(str, args)],
                          capture_output=True, text=True, cwd=ROOT)


def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / 'demo with spaces'

    def generate(self, *args):
        return command('init_project_docs.py', self.project, '--project-name',
                       'Warehouse Robot Demo', '--artifact-root', self.root / 'artifacts', *args)

    def valid_pack(self):
        result = self.generate('--date', '2026-01-01')
        self.assertEqual(result.returncode, 0, result.stderr)
        return self.project / 'reproducibility/acceptance-matrix.csv'

    def rewrite_matrix(self, mutate):
        matrix = self.valid_pack()
        with matrix.open(encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            columns, rows = reader.fieldnames, list(reader)
        mutate(rows)
        with matrix.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(rows)

    def invalid(self):
        self.assertEqual(command('validate_project_docs.py', self.project).returncode, 1)

    def test_safe_pack_and_substitution(self):
        self.valid_pack()
        self.assertEqual(len(hashes(self.project)), 10)
        text = (self.project / 'PROJECT.md').read_text(encoding='utf-8')
        self.assertIn('Warehouse Robot Demo', text)
        self.assertIn('warehouse-robot-demo', text)
        self.assertIn('2026-01-01', text)
        self.assertNotIn('{{', text)
        self.assertEqual(command('validate_project_docs.py', self.project).returncode, 0)

    def test_dry_run_has_no_writes(self):
        self.assertEqual(self.generate('--dry-run').returncode, 0)
        self.assertFalse(self.project.exists())

    def test_existing_pack_unchanged(self):
        self.valid_pack()
        before = hashes(self.project)
        self.assertEqual(self.generate().returncode, 3)
        self.assertEqual(before, hashes(self.project))

    def test_one_conflict_prevents_all_writes(self):
        self.project.mkdir()
        (self.project / 'PROJECT.md').write_text('user content', encoding='utf-8')
        before = hashes(self.project)
        self.assertEqual(self.generate().returncode, 3)
        self.assertEqual(before, hashes(self.project))

    def test_unrelated_file_preserved(self):
        self.project.mkdir()
        (self.project / 'keep.txt').write_text('keep', encoding='utf-8')
        self.assertEqual(self.generate().returncode, 0)
        self.assertEqual((self.project / 'keep.txt').read_text(), 'keep')

    def symlink(self, target, link, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except (OSError, NotImplementedError):
            self.skipTest('Symlinks unavailable for this test user')

    def test_linked_output_directory_rejected(self):
        self.project.mkdir()
        outside = self.root / 'outside'
        outside.mkdir()
        self.symlink(outside, self.project / 'docs', directory=True)
        self.assertEqual(self.generate().returncode, 3)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse((self.project / 'PROJECT.md').exists())

    def test_dangling_output_symlink_rejected(self):
        self.project.mkdir()
        self.symlink(self.root / 'missing', self.project / 'PROJECT.md')
        self.assertEqual(self.generate().returncode, 3)
        self.assertFalse((self.root / 'missing').exists())

    def test_invalid_name_and_date_rejected(self):
        for args in (('--project-name', '!!!'), ('--project-name', 'bad\nname'),
                     ('--date', 'invalid'), ('--date', '2026-02-30')):
            with self.subTest(args=args):
                self.assertEqual(self.generate(*args).returncode, 2)
                self.assertFalse(self.project.exists())

    def test_unicode_name(self):
        self.assertEqual(self.generate('--project-name', 'Robot Café').returncode, 0)
        self.assertEqual(command('validate_project_docs.py', self.project).returncode, 0)

    def test_missing_file_fails(self):
        self.valid_pack()
        (self.project / 'PROJECT.md').rename(self.project / 'saved.md')
        self.invalid()

    def test_template_token_fails(self):
        self.valid_pack()
        (self.project / 'PROJECT.md').write_text('{{UNRESOLVED}}', encoding='utf-8')
        self.invalid()

    def test_empty_matrix_fails(self):
        self.rewrite_matrix(lambda rows: rows.clear())
        self.invalid()

    def test_duplicate_gate_fails(self):
        self.rewrite_matrix(lambda rows: rows.append(rows[0].copy()))
        self.invalid()

    def test_invalid_status_fails(self):
        self.rewrite_matrix(lambda rows: rows[0].update(status='DONE'))
        self.invalid()

    def test_pass_without_pointer_fails(self):
        for status in ('PASSED', ' PASSED '):
            with self.subTest(status=status):
                if not self.project.exists():
                    self.valid_pack()
                matrix = self.project / 'reproducibility/acceptance-matrix.csv'
                text = matrix.read_text().replace('PENDING', status, 1)
                if status.startswith(' '):
                    text = text.replace('PASSED', status, 1)
                matrix.write_text(text)
                self.invalid()

    def test_pointer_does_not_prove_evidence(self):
        self.rewrite_matrix(lambda rows: rows[0].update(status='PASSED', evidence_pointer='unverified-example.txt'))
        self.assertEqual(command('validate_project_docs.py', self.project).returncode, 0)

    def test_extra_csv_field_fails(self):
        matrix = self.valid_pack()
        lines = matrix.read_text().splitlines()
        lines[1] += ',extra'
        matrix.write_text('\n'.join(lines) + '\n')
        self.invalid()


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skills = Path(self.temp.name).resolve() / 'skills with spaces'
        self.target = self.skills / 'isaac-sim-brev-operations'

    def install(self, *args):
        return command('install_skill.py', '--skills-dir', self.skills, *args)

    def test_install_and_installed_validation(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        for path in self.target.rglob('*'):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (ROOT / path.relative_to(self.target)).read_bytes())
        result = command('validate_package.py', self.target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.target / '.git').exists())

    def test_install_dry_run(self):
        self.assertEqual(self.install('--dry-run').returncode, 0)
        self.assertFalse(self.skills.exists())

    def test_install_refuses_existing(self):
        self.assertEqual(self.install().returncode, 0)
        before = hashes(self.target)
        self.assertEqual(self.install().returncode, 2)
        self.assertEqual(hashes(self.target), before)

    def test_install_refuses_empty_existing_directory(self):
        self.target.mkdir(parents=True)
        self.assertEqual(self.install().returncode, 2)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_missing_resource_and_broken_link_detected(self):
        self.assertEqual(self.install().returncode, 0)
        (self.target / 'references/isaac-runtime.md').rename(self.target / 'saved.md')
        self.assertEqual(command('validate_package.py', self.target).returncode, 1)

    def test_setup_prompt_drift_detected(self):
        self.assertEqual(self.install().returncode, 0)
        prompt = self.target / 'SETUP_PROMPT.md'
        prompt.write_text(prompt.read_text().replace('Set up https:', 'Install https:'))
        self.assertEqual(command('validate_package.py', self.target).returncode, 1)

    def test_private_path_detected_without_echoing_it(self):
        self.assertEqual(self.install().returncode, 0)
        private_path = '/' + 'Users' + '/example/private'
        (self.target / 'accidental.md').write_text(private_path)
        result = command('validate_package.py', self.target)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn(private_path, result.stderr)


if __name__ == '__main__':
    unittest.main()
