# Validation scope

The reproducible checks are:

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 scripts/setup_smoke.py
```

Package validation checks required resources, UTF-8 content, Python syntax, entrypoint
metadata, relative Markdown links, and setup-prompt parity. It includes heuristic
checks for credential-shaped text and local machine paths; this is not an exhaustive
secret scanner. Release preparation also includes manual review of the complete payload.

The regression suite tests document generation, non-overwrite and symlink behavior,
malformed acceptance matrices, template substitutions, installer copying, and invalid
package detection. The setup smoke installs into a temporary skills directory, checks
byte parity, generates a safe example from the installed copy, validates it, verifies
all gates remain PENDING, and confirms a second generation cannot overwrite it.
It uses no credentials, network, cloud resources, simulator, or physical hardware.

## Release evidence

Local release preparation on 2026-09-04 passed package validation, all 24 regression
tests, and the isolated setup smoke on macOS using Python 3.9.6 and Python 3.13.
The original skill's complete 21-file hash inventory was checked and unchanged.
The public payload was manually inspected for private records and dependencies.

An additional development-only validation used OpenAI's installed skill validator
with PyYAML in a temporary virtual environment. The published tools do not depend
on that environment or on PyYAML. Public download and CI results will be linked
from the release notes after verification. See GitHub Actions for the status of the
exact revision you download.

## Not established by these checks

- Assistant discovery or autonomous decision quality across every client/model.
- Fully unattended prerequisite installation, authentication, or external account setup.
- Isaac Sim/Isaac Lab runtime compatibility, GPU stepping, learning, rendering,
  streaming, live Brev provisioning, costs, export, or shutdown.
- Truth or scientific adequacy of evidence referenced by a PASSED acceptance row.
- Physical safety, sim-to-real transfer, or hardware readiness.

The setup prompt's executable local steps can be replayed in isolation. Passing those
steps does not prove every AI assistant will follow the prompt identically. Unsupported
hardware, authentication, licensing, and paid resources still require user involvement.
