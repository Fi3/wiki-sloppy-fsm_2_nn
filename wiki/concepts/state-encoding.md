---
title: "State encoding and construction cost"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/mit-fsm-design/document.txt", "raw/efficient-fsm-simulation/document.txt", "raw/fsm-rnn-complexity/document.txt", "raw/regular-languages-rnns/document.txt"]
---

# State encoding and construction cost

## What is being measured?

The cost of storing state and the cost of computing transitions are distinct. MIT's design discussion treats state-bit count and combinational logic as a tradeoff. [Source](../sources/mit-fsm-design.md).

Compare one-hot, binary and structured encodings using the same machine, timing and cost model. Record state dimension, transition neurons/operators, nonzero connections, parameter precision and execution work.

## Evidence and limits

- Threshold-network bounds change with permitted weights, thresholds, fan-in, and encoding assumptions. Different model restrictions can explain different bounds. [Alon–Dewdney–Ott](../sources/efficient-fsm-simulation.md), [Horne–Hush](../sources/fsm-rnn-complexity.md).
- Structured bounded-stack language models can admit compact RNN representations; the construction restricts the update functions. This is not a universal compression claim for arbitrary FSMs. [Svete–Chan–Cotterell](../sources/regular-languages-rnns.md).

## Unresolved points

The user's requested NN size metric is **synapse count**. A [saved analysis](../questions/fsm-size-vs-synapses.md) derives $4nk$ weighted step-network connections for an explicit one-hot Mealy construction, and an $O(\log n)$ construction for a structured cyclic-counter family under a different within-step depth model. These are original derivations with explicit counting conventions, not universal optimality claims. Evaluate transition logic and connectivity alongside state count.

Several older PDFs have corrupted mathematical extraction. Check original equations visually before entering exact asymptotic formulas. Compare activation, precision, input alphabet, output behavior and steps per transition before calling two results inconsistent.

## Related pages

- [Exact FSM construction](exact-fsm-construction.md)
- [Weighted automata](weighted-automata.md)
- [Complexity limits](complexity-limits.md)
- [FSM size versus synapse count](../questions/fsm-size-vs-synapses.md)
