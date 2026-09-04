# Isaac runtime and lifecycle

Read this reference for Isaac Sim or Isaac Lab environment setup, construction,
stepping, training, evaluation, recovery, or runtime troubleshooting.

## Freeze a compatibility lane

Record operating system, architecture, NVIDIA driver, CUDA exposure, Python, Isaac Sim,
Isaac Lab, learning library, robot asset, extension revisions, container or VM image,
and dependency lock. Treat a previously working combination as historical until the
current host reproduces it.

Do not repair an unsuitable paid host by replacing its driver or base operating system
without a specific recovery plan. Prefer a compatible host or image. Record undeclared
dependencies and packaging repairs in the environment lock and evidence, not only in
shell history. License or EULA acceptance is a user boundary unless already authorized.

## Runtime ladder

Use distinct run IDs and evidence for:

1. GPU, disk, memory, driver, and persistent-path preflight
2. official or known-good Isaac smoke
3. project import and environment construction
4. reset and bounded stepping with finite observations and actions
5. contacts, sensors, cameras, timing, and physical-output inhibition
6. scripted dynamics, saturation, recovery, and deterministic replay
7. bounded learning and checkpoint-resume smoke
8. curriculum training and frozen evaluation
9. visible policy and camera validation
10. certified render or other deliverable production

Passing one rung permits the next bounded attempt. It does not promote later claims.

## Environment and process lifecycle

- Give one process or supervisor explicit ownership of the SimulatorApp, environment,
  GPU, output root, and child run IDs.
- Do not create multiple fresh environments sequentially inside one long-lived
  SimulatorApp until teardown and recreation have a bounded, observed pass. A stalled
  second construction can leave CPU active and GPU idle without usable evidence.
- Prefer one constructed environment with vectorized lanes and explicit full resets
  between controller, seed, or partition batches when that matches the task.
- If sequential fresh environments are necessary, test a two-environment lifecycle
  smoke first with bounded construction, teardown, GPU-memory, and process-exit checks.
- Supervisors must not block indefinitely on a child wait. Poll with a bounded interval,
  check deadline, budget, stop request, owner lock, progress, and partial artifacts
  between polls.
- Treat exit `137` as a termination symptom, not automatic proof of OOM. Record OOM
  state, last logs, partial artifacts, supervisor action, and container state.

## Vectorized training

Use one shared policy and optimizer unless the experiment explicitly studies another
architecture. Record environment count, rollout length, transition count, seeds, lane
layout, and whether cameras or rendering are disabled. Training lanes must reset to
identical starting conditions when comparing controllers.

Profile environment counts through a fixed ladder. Select from measured throughput,
stability, deterministic behavior, and memory headroom using a rule frozen before the
profile. Do not select on GPU utilization alone. Label profile checkpoints and one-
update runs `profiling only` unless they independently meet a learning gate.

## Determinism and identity

Bind evidence to source revision and source-tree identity, configuration content hash,
asset hash, environment lock, seed schedule, controller or policy identity, checkpoint
bundle, and baseline producer. Use one documented seed algorithm. Do not mix linear,
hash-derived, or ad hoc schedules inside one acceptance suite.

Compare deterministic replays only at the scope actually tested. Same-process,
fresh-process, same-lane, and spatially offset comparisons prove different things.

## Persist before expensive boundaries

Write atomic, host-readable result shards, manifests, checksums, and latest recoverable
checkpoints after each controller and partition, before environment reconstruction,
container removal, provider stop, or balance exhaustion. Fsync when loss would invalidate
the run. Verify the files from the host side before destroying a container.

Partial shards are non-promotable until finalization validates completeness, ordering,
identity, and checksums. Keep them because they make recovery and diagnosis possible.

## Physics, contacts, and sensors

- Assert control-to-physics substep ratios and log requested versus applied commands.
- Validate frames, units, contact classes, collision geometry, actuator saturation,
  reset state, and maximum displacement at physics cadence.
- Keep collision and constraint truth independent of rendered perception so an actor
  cannot exploit hidden geometry.
- Distinguish sensor configuration from observed sensor output. A configured camera or
  randomization field is not proof that valid data arrived or the variation was applied.
- Keep training without cameras or rendering unless the policy or current gate needs
  them. Validate asynchronous sensor arrival with bounded waits and preserved frames.

## Failure handling

Preserve failing telemetry and unchanged thresholds. Diagnose implementation, model,
timing, scene, and configuration before retuning. A diagnostic probe is non-promotable
unless the acceptance matrix explicitly defines it as a gate. After a diagnostic
identifies a candidate correction, freeze a new source/configuration identity and rerun
the complete original gate.

Never infer physical validity from simulation. Physical outputs remain absent or hard-
inhibited unless a separately authorized project safety process permits them.
