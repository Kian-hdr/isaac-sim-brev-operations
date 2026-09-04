# Reward and policy specification

## Status

Status: Proposed. No numeric value or behavior in this file is implemented or verified
until linked evidence says so.

## MDP and baselines

Define state, observation, action, transition cadence, reset distribution, horizon,
success, invalid terminals, constraints, and classical, scripted, optimization-based,
or random baselines.

## Control stack

Document normalized policy action, semantic command, delay and jitter, clipping and
slew, independent controller, actuator allocation, saturation, actuator dynamics, and
physics. Identify simulation-only profiles and physical-output inhibition.

## Observation schema

| Field | Actor or critic | Source | Frame and units | Normalize and clip | Delay, noise, missing value |
|---|---|---|---|---|---|
| To define | To define | To define | To define | To define | To define |

Prove that actor inputs contain no privileged-only truth. Define history or recurrence,
normalization fitting, checkpointing, and frozen evaluation behavior.

## Action schema

| Field | Semantic range and units | Policy mapping | Rate | Invalid behavior |
|---|---|---|---:|---|
| To define | To define | To define | Unknown | Terminate or reject as specified |

## Reward equation

Write the complete per-step and terminal equation. For each term record units,
normalization, coefficient, analytic or measured bound, activation, telemetry, rationale,
and exploit test. Do not copy coefficients from another project.

## Terminal-dominance proof

Bound total dense shaping to `[L, U]`. Choose project-specific valid terminal reward
`F` and invalid penalty `X`. Prove with margin that `L + F > U + X`, and test every
terminal path. Only the exact success predicate may receive `F`.

## Termination precedence

Define mutually exclusive ordering for success, collision, constraint violation,
invalid state or action, wrong event, unrecoverable state, and timeout.

## Reward-exploit threat model

Cover early failure, event farming, wrong order or direction, shortcutting, tunneling,
inactivity, oscillation, boundary skimming, saturation, sensor gaming, privileged
leakage, finish spoofing, and reset farming where applicable. Add task-specific exploits
and corresponding property or integration tests.

## Claims boundary

State what a passing training run, aggregate evaluation, and demonstration can and
cannot prove. Simulation results do not set physical operating limits.
