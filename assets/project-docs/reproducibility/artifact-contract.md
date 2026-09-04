# Artifact contract

Canonical external root: `{{ARTIFACT_ROOT}}`

The root must be verified before execution. Never infer it from another project.

## Recommended non-overwriting layout

```text
baselines/
source-environment-references/
frozen-configurations/
manifests/
logs/
training-runs/
policies-and-checkpoints/
evaluation-runs/
telemetry/
raw-source-evidence/
rendered-or-exported-candidates/
final-deliverables/
qa/technical/
qa/visual/
checksums/
reproducibility/
```

Adapt unused categories to the project, but keep candidates separate from promoted
outputs. Use stable, unique run IDs and never overwrite immutable evidence.

## Run manifest minimum

Record run ID, timestamps, owner, source revision and dirty state, source-tree identity,
environment and dependency lock, hardware, asset and configuration hashes, seed or
scenario, controller or policy and checkpoint identity, requested budget, actual work,
result status, failure taxonomy, artifact inventory, QA, and checksums.

## Persistence and recovery

Write host-readable atomic partial shards before expensive boundaries. Verify file
presence and hashes outside the child process or container. Partial shards are
non-promotable until finalization proves completeness and ordering.

## Retention and backup

Retain accepted and rejected checkpoints or candidates required to explain selection,
all material failures, raw support evidence, final manifests, and checksum ledgers.
Verify a separate backup of essential evidence and final deliverables before operational
closure. Never treat cloud synchronization as verified backup without a read or hash
check.
