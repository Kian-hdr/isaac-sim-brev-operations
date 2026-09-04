---
name: isaac-sim-brev-operations
description: Plan, scaffold, run, resume, deploy, train, evaluate, render, document, or troubleshoot NVIDIA Isaac Sim and Isaac Lab projects across robotics domains, with reproducible gates, reward-policy design, safe NVIDIA Brev lifecycle management, evidence capture, deliverable QA, and verified shutdown. Use for Isaac work whether local or remote; do not use for unrelated cloud GPU tasks or as authority for physical testing.
---

# Isaac Sim and Brev operations

Make repeat Isaac work project-neutral, context-aware, recoverable, observable, and
evidence-bounded. A plan, smoke, training run, replay, and accepted deliverable are
different states.

## Route the task

For every substantive task, read
[references/execution-standard.md](references/execution-standard.md).

Read only the additional references that apply:

- For a new robotics project, documentation pack, work breakdown, acceptance matrix,
  artifact layout, or handoff structure, read
  [references/project-documentation.md](references/project-documentation.md).
- For observations, actions, reward terms, curriculum, PPO or another optimizer,
  policy promotion, randomization, or reward-hacking review, read
  [references/reward-policy-design.md](references/reward-policy-design.md).
- For Isaac installation, compatibility, environment construction, stepping,
  lifecycle, training, or evaluator reliability, read
  [references/isaac-runtime.md](references/isaac-runtime.md).
- For Brev selection, provisioning, use, monitoring, export, or shutdown, read
  [references/brev-lifecycle.md](references/brev-lifecycle.md).
- For visible streams, recording, rendering, or video, read
  [references/isaac-media.md](references/isaac-media.md).
- For an optional project-specific overlay, read
  [references/project-overlay.md](references/project-overlay.md). Keep actual project
  records in the user's project and apply them only to that project.

## Project-neutrality rule

Discover every project's robot, task, control interface, simulator versions, safety
boundary, budget authority, artifact root, reward scale, curriculum, evaluation gates,
and deliverables from its current sources. Do not reuse any prior
project's parameters as defaults. Historical examples may suggest questions or tests,
but they are not current requirements or verified facts for the active project.

## Essential workflow

1. Discover the active project's state before asking questions. Read its instructions,
   dossier, handoff, execution ledger, controlling technical and deliverable notes,
   live task system when authorized, repository, artifact root, processes, and cloud
   inventory.
2. Turn the request into explicit deliverables and an acceptance matrix. Separate
   implementation, runtime, learning, evaluation, media, evidence, backup, and
   shutdown gates that actually apply.
3. Reconcile contradictions by source authority and date. Refresh prices, balance,
   capacity, provider lifecycle, active ownership, endpoints, and versions at use.
4. Claim one bounded mutable workstream, worktree, artifact target, and GPU owner.
   Preserve unrelated work.
5. Freeze source revision, configurations, schemas, acceptance criteria, partitions,
   seeds, artifact root, and rollback point. Pass useful local CPU gates before paid
   runtime.
6. Climb the runtime ladder: official environment smoke, project construction smoke,
   stepping and sensor smoke, dynamics validation, bounded learning, curriculum,
   frozen evaluation, visible validation, and deliverable production. Skip rungs that
   genuinely do not apply; never skip the rung that tests the current uncertainty.
7. Track substantive execution in the project acceptance matrix and execution log. Give every child
   run a stable ID. Persist manifests, logs, checkpoints, telemetry, failures, partial
   shards, and checksums before the next expensive or destructive boundary.
8. Promote only immutable results that pass the controlling evaluation, claims,
   deliverable, backup, and provider-state gates. Never weaken a frozen threshold to
   turn a failure into a pass.
9. Export essential evidence, verify the local copy, stop idle compute when supported,
   verify the final provider state directly, and update the durable project record.

Never mark the work complete because setup, one smoke, profiling, a training child, or one seed
finished. Mark it complete only after the controlling acceptance audit verifies every requested
deliverable.

## Reusable project documentation

When the user asks to initialize or standardize an Isaac robotics project, use the
bundled non-overwriting generator after reading `references/project-documentation.md`:

```bash
python3 scripts/init_project_docs.py TARGET \
  --project-name "Project Name" \
  --artifact-root "$PWD/../robotics-artifacts"
python3 scripts/validate_project_docs.py TARGET
```

Inspect the target first. Do not overwrite an existing project pack. Adapt the
generated material to the actual robot, environment, authority, evidence, and requested
deliverables; unresolved template text is not a finished plan.

## Autonomy and authority

- Resolve routine, reversible choices from evidence. Ask only when a material unknown
  could change cost, safety, architecture, legal acceptance, or completion.
- When multi-agent execution is available and explicitly allowed, use useful
  non-overlapping lanes with one mutable owner per target and one owner per GPU.
- Continue through implementation, runtime, validation, export, documentation, and
  shutdown while useful in-scope work remains. A plan is not the deliverable.
- This skill grants no spending, account, deletion, publication, or physical-test
  authority. Verify current project authority before paid use.
- Never add funds, enable auto-recharge, change billing, accept terms, delete an
  instance or storage, publish material, or begin physical testing without explicit
  authority.

## Evidence language

Distinguish planned, implemented, locally tested, runtime-smoked, dynamics-validated,
profiled, trained, promoted, frozen-evaluated, rendered, visually verified, delivered,
and deployed. A local pass is not Isaac proof. Profiling is not convergence. A partial
shard is recoverability evidence, not promotion evidence. One seed is not
generalization. An edited video is not autonomy evidence without its uninterrupted run,
telemetry, configuration, controller or policy identity, and QA.
