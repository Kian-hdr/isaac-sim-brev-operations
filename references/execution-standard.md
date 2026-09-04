# Execution standard

Read this reference for every substantive Isaac Sim or Isaac Lab task.

## Source precedence

Use this order unless the current project explicitly defines another:

1. Current user request and approval boundaries
2. Current project AI guide and controlling workstream specification
3. Live task system and execution ledger for current state
4. Cross-project operating standard
5. Historical tutorials, results, and remembered provider behavior

This bundled reference is the reusable operating standard. No private knowledge base,
cloud account, task database, external dashboard, or creator-specific file is required.
Use project-local instructions, `operations/EXECUTION_LOG.md`, and the acceptance
matrix when shared systems are absent. A dashboard is optional, not a prerequisite.
Tool-specific goal APIs are optional and may only be used under the host's rules.

## Baseline discovery

Before mutation, determine and record:

- requested outcome and acceptance evidence
- repository, branch or worktree, source commit, and dirty state
- dependency lock, Python, CUDA, driver, Isaac Sim, and Isaac Lab versions
- robot, scene, controller, policy, checkpoint, and dataset identities
- canonical external artifact root and prior evidence inventory
- active local processes, task owners, GPU owners, and cloud environments
- live task database state when authorized
- project spending authority and current safety boundary

For a new project, create or repair the documentation and acceptance structure only
after this discovery. Read `project-documentation.md`; never populate a new project
with parameters, permissions, paths, or thresholds from a historical project.

Do not start with a generic questionnaire. Ask a bounded question only if the answer
cannot be discovered and a wrong default could materially alter cost, safety,
architecture, or acceptance.

## Local-first gate

- Use an isolated worktree or branch from a verified source commit.
- Preserve unrelated changes and maintain a known-good rollback point.
- Freeze schemas, configurations, and acceptance gates before paid runtime.
- Run useful unit, invariant, lint, type, compile, configuration, and deterministic
  replay checks locally.
- A local pass authorizes only the next bounded runtime attempt. It is not proof of
  simulator behavior, training, rendering, deployment, or physical validity.

## Parallel execution

When permitted and useful:

- Divide inspection, CPU implementation, tests, schemas, documentation, media
  preparation, evaluation, and independent QA into non-overlapping lanes.
- Give every lane a concrete deliverable, exact inputs, one mutable owner, output path,
  validation criteria, and evidence handoff.
- Keep one owner per file set, worktree, experiment, environment, and GPU.
- Do not run competing Isaac renderers or training jobs on one GPU.
- Reassign idle capacity to the next unblocked task.
- Integrate and rerun the relevant gate before accepting lane output.

## Runtime ladder

Use the narrowest rung that can answer the current uncertainty:

1. CPU contract and deterministic tests
2. Official or known-good Isaac environment smoke
3. Small project integration smoke
4. Dynamics, sensor, timing, and failure validation
5. Bounded training smoke
6. Curriculum or full training
7. Frozen multi-seed and unseen-condition evaluation
8. Visible camera and presentation validation
9. Certified render or deliverable production

Read `isaac-runtime.md` before rungs 2 through 7. A throughput ladder, one optimizer
update, or a generated checkpoint is profiling or plumbing evidence unless the
controlling learning gate explicitly says otherwise.

Preserve failed runs. Do not weaken gates or cherry-pick results to make progress look
better.

## Artifact and evidence contract

Each project owns one canonical external artifact root. Use stable run IDs and a
non-overwriting structure for:

- baseline inventories and manifests
- environment locks and configurations
- checkpoints and controller or policy identities
- training, evaluation, telemetry, and failure records
- raw footage, rendered frames, and candidates
- technical and visual QA
- certified deliverables, checksums, and verified backups

For every promoted result retain source revision, dirty state, versions, asset IDs,
configuration, seed or course, checkpoint hash, raw telemetry, failures, unedited
support evidence, QA, and final hashes.

Keep large artifacts outside the documentation repository. Record durable summaries and exact
pointers in the project notes. Update the execution ledger after material state changes
and at handoff.

Persist host-readable partial shards and checksums before environment recreation,
container removal, provider stop, or another expensive boundary. Partial output supports
recovery and diagnosis but remains non-promotable until complete finalization passes.

## Completion audit

Before claiming completion, map every requested deliverable and gate to direct current
evidence. Verify files, tests, runtime output, manifests, media, provider state, and
documentation at the scope each requirement needs. Missing, indirect, stale, or merely
consistent evidence is not a pass.

Finish with outcome, changes, validation, evidence, limitations, final provider state,
and the smallest useful next action.
