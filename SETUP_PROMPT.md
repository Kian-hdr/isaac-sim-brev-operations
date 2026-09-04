# Copy-ready setup prompt

Paste the entire block into an AI coding assistant with local filesystem, terminal,
and internet access. This installs the skill and validates its local tools. An assistant
without those capabilities can explain the manual steps but cannot execute them.

```text
Set up https://github.com/Kian-hdr/isaac-sim-brev-operations on this machine.
Complete the safe local setup, rather than only giving me instructions.

1. Detect my OS, shell, Python version, Git availability, and coding assistant's
   supported skill directory. Use Python 3.9 or newer. If a prerequisite is missing,
   install it using an appropriate trusted method when authorized; otherwise explain
   the exact manual step. Never change system Python or security settings.
2. Download release v1.0.0 into a new, uniquely named directory. Prefer:
   git clone --branch v1.0.0 --depth 1 https://github.com/Kian-hdr/isaac-sim-brev-operations.git
   If Git is unavailable, download and extract:
   https://github.com/Kian-hdr/isaac-sim-brev-operations/archive/refs/tags/v1.0.0.zip
   Do not overwrite an existing checkout. Record the source URL and version.
3. Read README.md, SKILL.md, SETUP_PROMPT.md, NOTICE.md, and
   references/execution-standard.md before executing the downloaded scripts.
   Follow my current instructions and your host's permission rules.
4. From the downloaded repository, using the detected Python interpreter, run:
   python3 scripts/validate_package.py
   python3 -m unittest discover -s tests -v
   python3 scripts/setup_smoke.py
   On Windows use the equivalent Python command, such as py -3. Stop and report
   failures; do not label a failed check successful.
5. Inspect existing skill installations before installing. For current Codex, the
   default is ~/.agents/skills. Honor a configured directory or another assistant's
   documented location using --skills-dir. Run scripts/install_skill.py --dry-run,
   then scripts/install_skill.py with the same destination. Preserve existing skills
   and configuration. If this skill already exists, compare it and report whether
   it can be reused; never overwrite or activate a duplicate silently. If no native
   skill support exists, keep the checkout and explain how to read SKILL.md directly.
6. In a new workspace outside the repository, use the installed copy's
   scripts/init_project_docs.py with --project-name "Warehouse Robot Demo" and an
   absolute --artifact-root in that workspace. Validate it with
   scripts/validate_project_docs.py. This is a documentation-only example; leave
   all simulation, training, evaluation, and provider gates PENDING.
7. Show the installed location, version, checks actually passed, example location,
   and how to invoke $isaac-sim-brev-operations. If skill discovery needs a restart,
   say so. Separate verified local setup from untested assistant or GPU behavior.

I authorize reversible local setup in new directories. Ask only when a missing
choice or permission materially blocks progress. Do not collect credentials,
create external accounts, accept third-party terms, provision paid resources,
change billing, or operate hardware. Isaac Sim, Isaac Lab, Brev login, GPU drivers,
and cloud compute are optional later steps requiring compatible hardware and my
specific authorization. Explain any such manual steps and remaining limitations.
```
