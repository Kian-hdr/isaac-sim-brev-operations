# Training and curriculum plan

## Algorithm and rationale

Choose learning or optimization method from the task and baselines. Pin framework,
network, optimizer, precision, rollout, batching, discount, entropy, clipping,
normalization, stopping, and checkpoint settings. Label proposed values as proposed.

## Dataset and scenario partitions

Define training, validation, sealed test, and challenge partitions by base asset,
layout, generator seed, scenario family, or dataset subject. Keep variants of one base
case in one partition. Record content hashes and a leakage test.

## Curriculum

| Stage | Task distribution | Authority and randomization | Frozen promotion gate | Rollback |
|---|---|---|---|---|
| 0 | To define | To define | To define with sample count | Last passing checkpoint |

Promotion uses frozen weights, normalization, configuration, and evaluation. Training
return alone cannot promote a stage. A failed stage does not weaken the threshold.

## Domain randomization

For each parameter record units, distribution, correlation, ramp, sampling frequency,
physical justification, training application, and deterministic evaluation cases.
Distinguish sampled from actually applied randomization.

## Compute and budget

Define local gates, scale-profile ladder, environment-count selection rule, transition
or wall-time ceiling, evaluation and export buffer, and provider authority. Charge
accepted, rejected, and breaker rollouts to the cumulative budget.

## Checkpoints and recovery

Define latest, immutable periodic, stage-passing, and Pareto candidate retention.
Checkpoint policy, optimizer, normalization, curriculum, configuration, source, seeds,
budget ledger, and hashes. Persist host-readable partial shards before expensive
boundaries; mark incomplete shards non-promotable.

## Circuit breakers

Stop on nonfinite values, invariant failure, unacceptable constraint regression,
stalled progress, deadline, owner loss, insufficient safe budget, or exhausted approved
ceiling. Record failure evidence and the restart authority.
