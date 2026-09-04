# Project documentation and deliverable architecture

Read this reference when starting a new Isaac robotics project, repairing its planning
structure, defining deliverables, or creating a reusable handoff.

## Build from the active project

The bundled pack is a neutral starting structure, not a source of project facts. Before
filling it, inspect the active repository and current instructions. Discover or label
unknown:

- robot, embodiment, task, scene, control boundary, and physical-output boundary
- owners, repositories, worktrees, cloud environments, GPU ownership, and artifact root
- source and dependency versions, assets, datasets, checkpoints, and licenses
- budget and account authority, legal acceptances, publication scope, and safety gates
- requested outputs, audiences, exact formats, and evidence needed for each claim

Do not copy values, versions, permissions, or thresholds from a previous project. An
unknown stays `Unknown` until resolved; a proposal stays `Proposed` until accepted.

## Documentation pack

Generate the pack with `scripts/init_project_docs.py`. It creates:

```text
PROJECT.md
docs/
  01-system-and-runtime.md
  02-reward-and-policy.md
  03-training-and-curriculum.md
  04-evaluation-and-acceptance.md
  05-deliverables-and-media.md
operations/
  EXECUTION_LOG.md
  HANDOFF.md
reproducibility/
  acceptance-matrix.csv
  artifact-contract.md
```

Keep this structure only when the files have distinct owners or retrieval purposes.
For a small project, merge documents rather than maintaining empty files. Preserve an
existing project structure and add only missing contracts.

## What each document controls

- `PROJECT.md`: objective, non-goals, current status, authority, owners, and source
  precedence.
- `01-system-and-runtime.md`: architecture, interfaces, coordinate frames, rates,
  simulator and dependency locks, assets, sensors, actuators, safety boundary, and
  runtime ladder.
- `02-reward-and-policy.md`: MDP, observation, action, reward, termination, exploit
  analysis, and policy/export boundary.
- `03-training-and-curriculum.md`: algorithm choice, partitions, randomization,
  curriculum, compute budget, checkpoints, breakers, and promotion rules.
- `04-evaluation-and-acceptance.md`: frozen suites, baselines, statistical reporting,
  failure taxonomy, evidence schema, and claims boundary.
- `05-deliverables-and-media.md`: exact final files, audiences, formats, story or
  operator need, provenance, technical and visual QA, backup, and promotion.
- `EXECUTION_LOG.md`: append-only material state changes, run IDs, ownership, evidence,
  costs, blockers, and provider transitions. Do not put per-second progress here.
- `HANDOFF.md`: latest verified checkpoint, current state, failures, restart order,
  provider state, and smallest next action.
- `acceptance-matrix.csv`: one row per independently auditable gate.
- `artifact-contract.md`: non-overwriting external artifact layout, manifest minimum,
  checksums, retention, and backup.

## Acceptance matrix design

Use stable IDs and the status vocabulary `PENDING`, `PASSED`, `FAILED`, `BLOCKED`, and
`UNAVAILABLE`. A row needs:

- gate ID and domain
- one objectively testable requirement
- required direct evidence and artifact location
- current status and evidence pointer
- owner and last-checked date
- claim enabled by a pass

Split broad goals. Useful gate families include:

- `BASE`: repository, artifact root, versions, assets, and ownership reconciled
- `CPU`: schemas, invariants, deterministic tests, lint, and configuration validation
- `RUNTIME`: official smoke, project construction, stepping, contacts, sensors, and
  physical-output inhibition
- `DYNAMICS`: controller, actuator, timing, saturation, recovery, and deterministic
  replay
- `TRAIN`: bounded learning signal, checkpoints, curriculum stages, and breakers
- `EVAL`: frozen baselines, multiple seeds, unseen conditions, failures, and selection
- `MEDIA`: source run, synchronized views, encoding, visual QA, and claims
- `EVID`: identity, manifests, raw telemetry, failures, checksums, and backup
- `OPS`: export, provider shutdown, storage state, balance, and handoff

Do not let a narrow gate satisfy a broader row. A construction smoke cannot pass
learning; throughput profiling cannot pass convergence; one replay cannot pass
generalization; a candidate cannot pass certified delivery.

## Deliverable contract

For every requested output record:

1. exact filename or naming rule
2. audience and decision it must support
3. content and behavioral acceptance criteria
4. controller or policy identity and source run
5. technical format and QA
6. supporting raw evidence
7. claims it permits and does not permit
8. promotion location and backup verification

Treat source evidence, candidates, and certified deliverables as separate classes.
Never overwrite a promoted master. Retain rejected candidates with their rejection
reason when they are material evidence.

## Artifact root

Large repositories, datasets, checkpoints, telemetry, frame sequences, and media belong
outside the knowledge base. Give the project one canonical external artifact root and
non-overwriting run IDs. The pack proposes a useful layout, but adapt it to the actual
outputs. Bind promoted artifacts to source revision, configuration, environment,
assets, seed or scenario, controller or checkpoint, QA, and checksum.

## Update discipline

- Update the execution log after material state changes and before handoff.
- Update the acceptance matrix only from direct evidence.
- Preserve failed runs and frozen thresholds.
- When a newer decision supersedes a plan, retain the history and name the superseding
  source and date.
- End work with outcome, changes, validation, evidence paths, limitations, provider
  state, and next action.
