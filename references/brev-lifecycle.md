# Brev lifecycle and budget

Read this reference before any Brev selection, provisioning, paid runtime, monitoring,
restart, replacement, export, or shutdown action.

## CLI discovery and authentication

Follow [NVIDIA's CLI installation and login guide](https://docs.nvidia.com/brev/latest/cli/getting-started).
Inspect `brev --version`, `brev --help`, and the installed help for each intended
subcommand before use. Use search and a creation dry run when supported; verify exact
flags in installed help. Record the selected version and command.

Try an inventory read with the existing session before starting a new login. If it
has expired and the task authorizes Brev use, start the official `brev login` flow and
continue after verifying the intended account and organization. The documented
`--skip-browser` flag prints a URL; it does not bypass browser authentication. Do not
mistake connectivity errors for an expired session or repeatedly log out and log in.
Stop for a password, MFA, CAPTCHA, new terms, or another human-only challenge when
the host cannot complete it under the user's instructions. Keep credentials out of
shell history, setup recipes, logs, and project records. Do not assume another
provider's token works with Brev's `--token` login mode.

## Reusable environments and Launchables

Before provisioning, inspect existing compatible instances, environment recipes,
and [Launchables](https://docs.nvidia.com/brev/concepts/launchables). A Launchable
is a deployable configuration, not a running instance or an immutable version lock.
Reuse a suitable one when its software, GPU, storage, network, source, and terms fit
the project. A provider default or an old recipe ID is not a project version pin.

When repeated project setup justifies a custom Launchable, define restart-safe setup
with pinned source and dependencies, persistent storage, minimal network exposure,
and a runtime smoke. Use the currently supported Brev Console builder or documented
interface, select access no broader than the task authorizes, and keep secrets out of
recipe defaults and source files. Verify the built recipe by deploying it only within
the approved compute budget. Record the recipe ID and configuration in the project's
private record. A saved recipe is not runtime proof.

Inspect installed CLI help before using a Launchable deployment flag; CLI versions
may differ from the web documentation. Preview when supported, then separately
refresh current capacity, cost, license requirements, and project version fit. If a
create command times out or gives an uncertain result, reconcile live inventory
before retrying so it cannot silently create duplicate paid instances. A reachable
shell is not Isaac readiness: verify GPU and driver, pinned Isaac versions, storage,
stepping, sensors, and any viewing path required by the task. After repeated failure
at the same setup step, diagnose or switch to a compatible supported path within
the budget instead of repeating that method.

## Refresh before selection

Inspect the signed-in live provider state and record:

- available prepaid balance
- all relevant instances and their lifecycle states
- GPU, CPU, RAM, storage, provider, and region
- running and stopped-storage prices
- stoppable, restartable, or deletion-only behavior
- capacity and compatibility with the required workload

Never rely on an older project snapshot for current billing, balance, inventory, capacity,
or lifecycle behavior.

Also identify the runtime layer: VM mode, provider container, user container, or a
combination. Verify which path is persistent from the host and from every container.
Discover persistent workspace paths and mounts; do not inherit stop or deletion
behavior from another instance or provider.

## Select for accepted-result time

Choose the fastest credible path to an accepted result whose technical requirements and
buffered total cost fit the authorized balance. Do not automatically choose the
cheapest or most expensive instance.

Unless the project specifies another rule, reserve the greater of 25 percent of the
estimated runtime or 15 minutes, plus expected storage and export cost.

Prefer a stoppable instance when its performance is adequate. Treat a deletion-only
provider as a material constraint. Deletion requires explicit authorization and is not
a routine shutdown mechanism.

Record the selection rationale and the live configuration and price before starting.

## Authorization matrix

The current project or user must explicitly authorize paid use. When standing authority
exists, routine creation, start, stop, restart, replacement, or reuse may proceed within
that scope without repeat confirmation.

Standing compute authority alone does not imply authority to:

- add funds or enable auto-recharge
- change billing or account settings
- accept new commercial terms
- purchase a separate plan
- delete instances or persistent storage beyond the user's task or standing authority
- use the account for unrelated work

## Runtime observability

Assign one GPU owner. Give every run a stable ID and write logs, checkpoints, and
artifacts to persistent storage.

Give the supervisor a bounded polling loop. It must recheck child progress, deadline,
budget, owner state, stop requests, and persisted partial evidence rather than block
indefinitely on a container or process wait.

Keep a persistent acceptance matrix and execution log from substantive work until
the accepted deliverables are verified and delivered. Use the controlling acceptance
matrix or fixed weighted goal phases as its authoritative total. Synchronize it after
material evidence changes.

Track intermediate jobs under separate explicit run IDs. A completed setup, smoke,
training seed, evaluation batch, render, or transfer must not replace or close the
goal dashboard. Use authoritative child-job units:

- tests completed
- training iterations or timesteps
- evaluation seeds or trials
- rendered frames
- transferred bytes
- fixed weighted phases

Update after meaningful units, phase changes, retries, or blockers. Use `Unknown` when
no trustworthy percentage or ETA exists. Do not manufacture progress.

When a goal has passed at least one acceptance gate, its dashboard may forecast ETA
from measured average gate throughput since the recorded goal start. Mark the duration
and finish time as approximate because acceptance gates can differ greatly in effort.
Hold the predicted finish steady between updates so the ETA counts down, then
recalculate on each goal synchronization so stalls or new passes refine the forecast.

Use the project acceptance matrix and execution log as the persistent tracker.
An existing dashboard may present them; no dashboard implementation is bundled.

If a terminal dashboard is used, keep it bounded to fixed terminal rows. Redraw those rows in
place, truncate task text to the terminal width, and never append a new status block
on each refresh. Prefer the terminal alternate screen so the original shell view is
restored when the watcher exits.

A blocker is non-terminal at goal scope. Keep the goal open, display the blocker, save
recoverable work, and resume the same goal tracker when work can continue. Goal
completion requires an explicit completion audit against the current acceptance source.

## Budget exhaustion

Warn when projected completion exceeds the available balance or less than one hour of
the current compute remains, unless the project defines a stricter threshold.

Before requesting a top-up:

1. Save the newest recoverable checkpoint and material logs.
2. Export essential evidence.
3. Stop avoidable compute when supported.
4. Refresh the live balance and prices.
5. Estimate the remaining accepted-result cost honestly.
6. Ask for the smallest practical amount the user needs to add.

Never add the funds independently.

Do not assume deletion-only prepaid capacity is durable storage. Export continuously
and reserve enough balance for evaluation, evidence finalization, export, and recovery,
not only the expected training body.

## Export and shutdown

1. Preserve the newest recoverable state and stop output writers.
2. Export required outputs, logs, checkpoints, and recovery inputs to the project's
   approved destination outside the instance.
3. Verify the destination inventory, hashes or equivalent integrity, and usability
   of the copy. A queued upload or unverified sync is not a backup. A verified local
   copy in a synced folder proves the local copy; check cloud receipt separately.
4. Delete only a task-owned temporary instance and its disposable attached storage
   when the user has authorized that cleanup and the job and export checks are done.
   Preserve shared resources, source files, destination copies, backups, and the only
   recoverable copy of unfinished work. Record instance identity, authorization,
   destination, and verification evidence before deletion.
5. Otherwise stop idle compute when supported and preserve required storage.
6. Refresh and record final instance state, retained storage, current prices, and
   remaining balance. Do not report shutdown until provider state is directly
   verified. Do not ask again when an existing authorization covers the exact cleanup.

Provider failure, capacity loss, or a broken stream does not justify hiding status.
Preserve the last verified progress, mark the exact blocker, and continue other useful
work where possible.
