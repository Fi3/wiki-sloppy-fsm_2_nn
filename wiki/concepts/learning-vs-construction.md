---
title: "Construction, learning and extraction"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/differentiable-fsm/document.txt", "raw/fools-gold/document.txt", "raw/neural-state-machine/document.txt", "raw/relu-membership-query-extraction/document.txt"]
---

# Construction, learning and extraction

## Separate the tasks

| Task | Given | Desired artifact | Main obligation |
| --- | --- | --- | --- |
| Construction | A specified machine | A network implementing it | Preserve the declared behavior |
| Learning | Observations/examples | A fitted machine or network | Establish generalization beyond observations |
| Extraction | An existing network or query oracle | An interpretable/recovered representation | Preserve behavior under the extraction assumptions |
| Surrogate compilation | An executable program, source and/or observed examples | A deployable neural replacement | Meet a declared application error target on a specified workload |

These are working distinctions for this wiki; success at one does not automatically solve another.

## Evidence

The differentiable FSM tutorial learns relaxed transition tables and shows that fitting an observed sequence can yield unintended behavior elsewhere. [Source](../sources/differentiable-fsm.md).

Kolen warns that trajectory discretization and initial-condition sensitivity can make extracted finite-state descriptions misleading. [Fool's Gold](../sources/fools-gold.md).

Exact ReLU query reconstruction uses specific oracle and regularity assumptions. [Daniely–Granot](../sources/relu-membership-query-extraction.md).

Hudson–Manning's neural state machine is a learned scene-graph reasoning model. Its task and notion of state differ from compiling a specified deterministic transducer. [Source](../sources/neural-state-machine.md).

The user's proposed lossy transformation of high-level pure functions falls under [neural surrogate compilation](neural-surrogate-compilation.md). Parrot learns function replacements from executions, while CompNet generates initial surrogate weights from source text. This relaxes exact behavior preservation and introduces workload, error-budget and composition questions. [Saved comparison](../questions/high-level-programs-to-neural-surrogates.md).

## Questions for future experiments

Record the known specification, observed training coverage, held-out sequences, unvisited transitions, decoding rules and robustness checks. A successful example or plausible diagram alone is insufficient evidence of global behavior preservation.

## Related pages

- [Exact FSM construction](exact-fsm-construction.md)
- [Weighted automata](weighted-automata.md)
- [Complexity limits](complexity-limits.md)
