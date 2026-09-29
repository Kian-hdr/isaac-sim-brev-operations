# Isaac Sim and Brev Operations

A reusable AI coding assistant skill for planning and operating NVIDIA Isaac Sim and
Isaac Lab projects, locally or on NVIDIA Brev. It combines execution guidance with
Python tools that generate and validate a project documentation pack.

Use it to define reward and policy contracts, freeze evaluation gates, manage bounded
GPU runs, preserve evidence, review media, and verify shutdown. It is a workflow and
documentation toolkit, not a simulator, robot controller, training implementation,
cloud provisioner, or automated dashboard.

**Start here:** copy the setup prompt below into your AI coding assistant.
[Download v1.1.0 ZIP](https://github.com/Kian-hdr/isaac-sim-brev-operations/archive/refs/tags/v1.1.0.zip)
• [Dedicated setup prompt](SETUP_PROMPT.md) • [Validation scope](VALIDATION.md)

## Copy-ready setup prompt

```text
Set up https://github.com/Kian-hdr/isaac-sim-brev-operations on this machine.
Complete the safe local setup, rather than only giving me instructions.

1. Detect my OS, shell, Python version, Git availability, and coding assistant's
   supported skill directory. Use Python 3.9 or newer. If a prerequisite is missing,
   install it using an appropriate trusted method when authorized; otherwise explain
   the exact manual step. Never change system Python or security settings.
2. Download release v1.1.0 into a new, uniquely named directory. Prefer:
   git clone --branch v1.1.0 --depth 1 https://github.com/Kian-hdr/isaac-sim-brev-operations.git
   If Git is unavailable, download and extract:
   https://github.com/Kian-hdr/isaac-sim-brev-operations/archive/refs/tags/v1.1.0.zip
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

## Requirements

For the bundled tools: **Python 3.9+**, a writable workspace, and no third-party Python
packages. Git is optional if using the ZIP. The command examples use a POSIX shell;
on Windows use `py -3` and equivalent PowerShell paths. The tools use `pathlib` and
are tested separately from any simulator installation.

For agent use: an assistant capable of reading local files and executing commands.
Codex skill discovery is optional; another assistant can read [SKILL.md](SKILL.md)
and follow its linked references. No private knowledge base, proprietary helper,
creator account, fixed volume, or external task database is required.

For actual simulation, separately install a compatible Isaac Sim/Isaac Lab release,
GPU driver, assets, and dependencies. Check the release-specific
[Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)
and [Isaac Lab installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html).
Local documentation setup does not establish GPU compatibility. A Mac can prepare
project documents without being the simulator host.

Brev is optional. Cloud use requires your own account, authentication, available
capacity, explicit budget authority, and an approved compatibility lane. Use
[NVIDIA's CLI setup guide](https://docs.nvidia.com/brev/latest/cli/getting-started),
then inspect the installed CLI's `--help` before using version-dependent commands.
The scripts in this repository never invoke Brev or start paid compute.

## Manual installation

Clone into a new directory, or extract the ZIP and open a terminal in its root:

```sh
git clone --branch v1.1.0 --depth 1 https://github.com/Kian-hdr/isaac-sim-brev-operations.git
cd isaac-sim-brev-operations
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 scripts/setup_smoke.py
python3 scripts/install_skill.py --dry-run
python3 scripts/install_skill.py
```

The default is `~/.agents/skills/isaac-sim-brev-operations`, following
[OpenAI's local skill documentation](https://learn.chatgpt.com/docs/build-skills).
If the host uses another location, provide its **parent skills directory**:

```sh
python3 scripts/install_skill.py --skills-dir "$HOME/.codex/skills"
```

That command is an alternative for hosts configured to use that location, not a
second installation step. The installer refuses an existing destination, verifies
copied bytes, and does not edit assistant configuration. It copies the skill, all
references and templates, scripts, tests, examples, documentation, and license;
Git metadata and CI files stay in the checkout. Restart the assistant if discovery
is stale. Discovery in every assistant/version is not guaranteed.

Without native skills support, ask your assistant to read the checkout's `SKILL.md`
and follow its references. All Python commands also work without an AI assistant.

## Quick start

From the repository root, create a new documentation pack:

```sh
python3 scripts/init_project_docs.py ../warehouse-robot-demo \
  --project-name "Warehouse Robot Demo" \
  --artifact-root "$PWD/../warehouse-robot-artifacts"
python3 scripts/validate_project_docs.py ../warehouse-robot-demo
```

The same commands work from the installed skill directory. Ten files are created:
project overview; runtime, reward/policy, curriculum, evaluation, and media documents;
execution log; handoff; acceptance matrix; and artifact contract. The artifact-root
argument records a path; the generator does not create storage or run simulation.
Use `--dry-run` to preview paths, or `--date YYYY-MM-DD` for reproducible generation.
Generation refuses conflicting output files. A partial failure may leave new files;
inspect and preserve them, then use a fresh target.

Ask your agent:

```text
Use $isaac-sim-brev-operations to plan a simulation-only warehouse robot project.
Inspect this workspace, generate a documentation pack in a new directory, and define
acceptance evidence. Label proposed values and unknowns. Do not provision compute.
```

A successful validator result means the documentation structure is valid. It does
not mean the proposed plan is complete or any acceptance gate passed. Adapt the
unknowns to your project before runtime. See [example prompts](examples/prompts.md).

## What is included

| Location | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent entrypoint and reference routing |
| `agents/openai.yaml` | Optional Codex interface metadata |
| `references/` | Execution, runtime, rewards, Brev, media, documentation, generic overlay |
| `assets/project-docs/` | Ten text/CSV templates, no private project records or robot assets |
| `scripts/` | Generator, project validator, installer, package validator, isolated setup smoke |
| `tests/` | CPU regression tests, no cloud or credentials |
| [SETUP_PROMPT.md](SETUP_PROMPT.md) | Complete agent setup instructions |
| [NOTICE.md](NOTICE.md) | Provenance, attribution, and third-party boundaries |

## Limitations

- Operational references guide an agent; they do not implement a trainer, evaluator,
  simulator installer, budget meter, secret store, progress UI, or shutdown service.
- The acceptance matrix and execution log replace any need for a private dashboard.
  Project overlays are optional and must remain in the relevant project.
- Project validation checks required files, template tokens, CSV structure, unique
  gate IDs, allowed statuses, and evidence pointers for PASSED rows. It does **not**
  inspect the evidence behind a pointer, certify scientific validity, or prove safety.
- Templates intentionally contain `Unknown`, `To define`, and `PENDING` entries.
  Merge or adapt the documents if useful; the supplied structural validator expects
  the original ten-file layout and must be adapted if you change it.
- No GPU execution, learning convergence, streaming, real robot behavior, or live
  Brev lifecycle result is implied by this package's tests. Exact runtime versions,
  prices, capacity, and license acceptance must be checked for each project.
- The Brev reference now guides session recovery, reuse of Launchables, runtime
  readiness, and authorized cleanup after verified export. It does not grant paid
  compute or deletion authority, perform login, deploy an instance, or verify a
  Launchable automatically.
- Installer/generator conflict checks protect normal use, not hostile concurrent
  filesystem changes. Do not run them in a directory another process is mutating.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| `python3` not found | Install Python 3.9+ from a trusted distribution; on Windows try `py -3`. No pip packages are needed. |
| Existing installation | Compare versions and local changes. Preserve the old copy outside active skill directories before a deliberate replacement. |
| Skill not visible | Verify the assistant's actual skill directory and restart. You can always request direct reading of `SKILL.md`. |
| Generator refuses target | Use a new target or reconcile existing documents manually. It will not overwrite the ten named outputs. |
| Validator reports an error | Repair the stated file or CSV row. Keep gates PENDING until direct evidence exists. |
| Interrupted install | Inspect the partial destination, move it to a recovery location, then retry. Do not delete unrelated files. |
| No GPU or Brev access | Use documentation tools locally. Follow official runtime setup only when separately authorized. |
| Runtime or stream fails | Use the runtime/media references, preserve logs, and separate headless job health from viewer health. |

## Updates and maintenance

`VERSION` identifies the distribution. `v1.0.0` was the initial public tag; `main` may
contain later work. To update, download a desired tagged version into a new checkout,
review changes and notices, run validation/tests/smoke, compare local modifications,
and move the old installed copy to a recovery directory outside active skill discovery.
Install the reviewed version, then restart the assistant if needed. Updates are manual;
there is no background updater and no automatic overwrite.

Maintainers must keep the setup prompt identical here and in `SETUP_PROMPT.md`, use
real release URLs, preserve notices, and keep private data out of examples. Run the
three validation commands above before tagging. The CI workflow runs package checks,
regression tests, and the isolated setup smoke across its declared Python/OS matrix.
Report reproducible issues without credentials, private endpoints, or project records.

## License

Original material is available under the [MIT License](LICENSE). Third-party products,
assets, services, and their names remain subject to their own licenses and terms.
This project is not affiliated with or endorsed by NVIDIA or OpenAI. See
[NOTICE.md](NOTICE.md).
