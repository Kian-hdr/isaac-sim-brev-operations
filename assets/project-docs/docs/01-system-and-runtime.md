# System and runtime specification

## Robot and task

Record embodiment, task, scene, success predicate, failure predicates, constraints, and
the boundary between simulated and physical behavior.

## Architecture and interfaces

Describe the data flow from sensors and state estimation through planning or policy,
independent safety checks, command adaptation, actuators, and simulated dynamics.
For each interface define schema, units, coordinate frame, rate, freshness, validity,
and failure behavior.

## Timing

| Layer | Rate | Hold or interpolation | Evidence |
|---|---:|---|---|
| Policy or planner | Unknown | Unknown | Pending |
| Controller | Unknown | Unknown | Pending |
| Actuator model | Unknown | Unknown | Pending |
| Physics | Unknown | Unknown | Pending |
| Sensors | Unknown | Unknown | Pending |

## Environment lock

Record OS, architecture, driver, CUDA exposure, Python, Isaac Sim, Isaac Lab, learning
framework, base image, robot and scene assets, extension revisions, and dependency
lock. Record licenses and who accepted any required terms.

## Runtime ladder

Define project-specific gates for host preflight, official smoke, import/construction,
bounded stepping, contacts and sensors, dynamics, bounded learning, frozen evaluation,
visible validation, and deliverable production. Link every gate to the acceptance
matrix and an evidence location.

## Safety and output isolation

Specify physical transports that must be absent or inhibited, command bounds, invalid
state handling, independent constraints, owner locks, and abort behavior.

## Unknowns and decisions

List assumptions separately from verified facts. Name the evidence that will resolve
each material unknown.
