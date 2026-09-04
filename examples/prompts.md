# Generic example prompts

These are proposed workflows, not recorded projects or verified simulation results.
Use the setup prompt in the repository root before first use.

## New simulation-only project

```text
Use $isaac-sim-brev-operations to scaffold a warehouse robot documentation pack.
Use a fresh directory and a separate artifact root. Propose runtime, reward, and
acceptance contracts. Leave unverified values explicit and do not start paid compute.
```

## Reward and evaluation review

```text
Use $isaac-sim-brev-operations to review this simulated pick-and-place reward.
Inspect the actual implementation and observation/action contracts. Identify possible
reward exploits, terminal ordering issues, data leakage, and missing evaluation
coverage. Report findings with evidence; do not change the frozen thresholds.
```

## Resume an authorized run

```text
Use $isaac-sim-brev-operations to inspect this project's handoff and latest evidence.
Reconcile the repository and artifacts, identify the next unpassed gate, and prepare
a bounded runtime plan. Verify current cloud state only with authorized access.
Do not start paid resources until this project's budget and authority are explicit.
```
