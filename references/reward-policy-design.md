# Reward and policy design

Read this reference for reinforcement-learning objectives, observations, actions,
rewards, terminations, curriculum, randomization, training, policy selection, or
reward-exploit review in any Isaac robotics domain.

## Start from the task contract

Do not begin by tuning weights. Define:

- success predicate and invalid terminal predicates
- task horizon, control and physics rates, reset distribution, and constraints
- ordered or continuous progress measure, if any
- deployable observation boundary and privileged critic or evidence boundary
- action semantics and the independent lower-level controller or actuator model
- required baselines, validation distributions, and accepted deliverables

Decide whether learning is actually needed. Retain a scripted, optimization-based, or
classical-control baseline when it can expose environment or reward defects.

## Policy and control stack

Document every rate and interface from policy to physics:

```text
policy action
  -> delay, jitter, clipping, and slew
  -> independent controller or command adapter
  -> actuator allocation, saturation, and dynamics
  -> simulated robot dynamics and contacts
```

Assert integer substep relationships when required. Log requested and applied actions,
saturation, actuator state, and reset state. Keep high-authority research profiles
isolated from conservative or physical-output paths. Simulation parameters are not
physical operating limits.

## Observation contract

For every field specify source, coordinate frame, units, normalization, clipping,
latency, noise, dropout, missing-value encoding, history, and export availability.

- The actor receives only information available in the intended deployment boundary,
  or a clearly labeled state-policy surrogate passed through the future perception
  adapter.
- Privileged state may go to the critic and evidence only. Test tensor separation and
  inspect exported policy inputs.
- Include actuator state or history when delay and lag make the process partially
  observable.
- Fit normalization only on training data. Checkpoint it and freeze it for validation
  and test.

## Action contract

Define semantic units before normalization. Record limits, scaling, rate, clipping,
slew, latency, controller mapping, saturation priority, invalid-action behavior, and
reset behavior. Test signs, frames, bounds, NaN and Inf rejection, actuator lag, and
whether the task remains controllable under the proposed authority.

## Reward specification

Write the reward mathematically before implementation. For every term record:

- name and task rationale
- equation, units, normalization, coefficient, and bound
- dense, sparse, event, constraint, or terminal class
- when it is active and mutually exclusive events
- raw per-step telemetry and episodic sum
- plausible exploit and corresponding test

Prefer task progress, valid completion, constraint satisfaction, and elapsed cost over
direct rewards for a visually desired maneuver. If a behavior should emerge only when
useful, make the task geometry require it rather than paying for the behavior itself.

### Terminal dominance

Prove that an invalid early termination cannot outscore the slowest valid completion.
One reusable pattern is:

1. Bound accumulated dense shaping to `[L, U]`, either analytically or with a bounded
   episodic ledger.
2. Choose valid terminal reward `F` and invalid terminal penalty `X` so
   `L + F > U + X` with a documented margin.
3. Ensure only the exact success predicate can receive `F` and invalid terminal
   precedence is deterministic.
4. Property-test the inequality across randomized trajectories, horizons, term
   combinations, and terminal paths.

The values are project decisions. Do not reuse a prior project's numeric coefficients.
Log pre-clipped terms and ledger clipping. Frequent clipping means the reward scale is
miscalibrated, even if the invariant still holds.

## Reward-exploit threat model

Test applicable failures explicitly:

| Exploit class | Typical mitigation |
|---|---|
| early failure saves time | terminal-dominance proof |
| event farming | monotonic identity and one-shot event tests |
| wrong order or direction | signed swept event and terminal precedence |
| shortcutting | constraint-aware progress, cut planes, and independent geometry |
| tunneling | swept body checks and physics-substep displacement bounds |
| hovering or inactivity | elapsed cost and success-only terminal reward |
| useless oscillation | no direct behavior bonus, action-change telemetry, time cost |
| boundary skimming | continuous margin term plus exact contact truth |
| permanent saturation | actuator observation, grace window, penalty, promotion cap |
| sensor gaming | confidence gating and task-progress dominance |
| privileged leakage | separate schemas, tensor tests, and export inspection |
| finish spoofing | complete success predicate and mutually exclusive terminals |
| reset farming | zero pre-action reward and reset property tests |

Add project-specific exploits. Preserve exploit failures as evidence rather than tuning
around them invisibly.

## Curriculum

Each stage defines task distribution, randomized reset, action authority, learning
focus, fixed evaluation suite, promotion metrics, sample count, and rollback rule.
Promote with frozen weights and normalization, not training return. A failed stage
returns to the last passing checkpoint and adds failure-specific training cases without
weakening the gate.

Partition generator seeds, base layouts, assets, and scenario families before
training. Keep variants of one base scenario in one partition. Validation may select
checkpoints; sealed test may not. Record content hashes and test for leakage.

## Randomization

Version distributions, units, correlations, ramp schedule, sampling frequency, and
physical justification. Training may sample stochastically; evaluation uses a fixed
manifest of seeds and parameter tuples. Separate sampled from actually applied
randomization. A field in a manifest is not proof that the simulator used it.

Do not call proposed simulation ranges physical tolerances. Calibrate from measurements
when transfer matters.

## Training and profiling

Pin algorithm, library, network, optimizer, precision, rollout, batch, update, entropy,
discount, stopping, and checkpoint settings. Give every paid run a transition or
wall-time budget and pre-launch budget reservation. Charge accepted, rejected, and
breaker rollouts so failed work does not disappear from the ceiling.

Use scale profiling to select a stable environment count from throughput, stability,
and memory headroom. Keep profiling independent of learning promotion. High GPU use,
one update, or a checkpoint file does not prove learning or convergence. Keep
PPO-sensitive loss math in the validated precision; treat compilation and mixed
precision as optional optimizations that must preserve the numerical contract.

Persist immutable periodic checkpoints, latest recoverable state, optimizer and
normalization state, configuration, budget ledger, and failure inventory. Select policy
candidates using a Pareto view of success, task performance, constraint margin,
saturation, recovery, and other project metrics, not return alone.

## Evaluation

Use frozen policy, normalization, configuration, baselines, seeds, scenarios, and
software identity. Evaluate multiple independent training seeds when the claim is about
the method rather than one checkpoint. Report distributions and confidence intervals,
failure categories, constraint margins, saturation, intervention, generalization gaps,
and all exclusions.

A hero run may illustrate a passed policy. It must not replace aggregate evaluation or
hide failures. Bind deliverables to the exact checkpoint and source evaluation.
