# Evaluation and acceptance specification

## Evaluation contract

Freeze source, environment, assets, policy or controller, checkpoint, normalization,
configuration, baselines, seeds, scenarios, partitions, randomization tuples, metrics,
thresholds, and failure taxonomy before evaluation.

## Suites

| Suite | Purpose | Episodes or trials | Metrics | Pass threshold |
|---|---|---:|---|---|
| Nominal | To define | To define | To define | To define |
| Unseen | Generalization | To define | To define | To define |
| Perturbation | Robustness | To define | To define | To define |
| Recovery | Failure handling | To define | To define | To define |

## Metrics and statistics

Report success and failure rates with suitable intervals, task-performance
distributions, constraint margins, contacts or violations by category, saturation,
interventions, recovery, numerical invalidity, and generalization gaps. Report every
exclusion and failed run.

## Baselines and policy selection

Evaluate baselines on the same frozen matrix. Select candidates using the metrics that
matter to the task, not reward or one fastest run alone. For method-level claims, use
multiple independent training seeds.

## Evidence minimum

Every result binds run ID, source-tree identity, environment lock, configuration and
asset hashes, controller and checkpoint, seed or scenario, raw telemetry, failures,
aggregate report, QA, and checksums.

## Claims boundary

Write the exact statement enabled by each passed gate. A hero run illustrates an
aggregate result but cannot replace it. A simulation evaluation is not physical
validation or deployment.

## Acceptance source

`../reproducibility/acceptance-matrix.csv` is the machine-readable completion source.
Update it only from direct evidence.
