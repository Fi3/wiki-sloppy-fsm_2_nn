---
title: "Complexity claims and their scope"
type: concept
created: 2026-10-07
updated: 2026-10-09
status: active
sources: ["raw/multi-output-circuit-minimization/document.txt", "raw/relu-training-hardness/document.txt", "raw/quantized-network-training/document.txt", "raw/relu-membership-query-extraction/document.txt", "raw/p-vs-np/document.txt", "raw/quantum-lower-bounds/document.txt", "raw/hill-pseudorandom-generators/document.txt", "raw/cook-p-vs-np/document.txt", "raw/circuits-and-nonuniform-computation/document.txt"]
---

# Complexity claims and their scope

## Distinguish the computational problems

| Problem | Evidence and limitation |
| --- | --- |
| Minimize a multi-output Boolean circuit | NP-hardness result uses randomized many-one reductions. Do not silently substitute single-output minimization. [Source](../sources/multi-output-circuit-minimization.md) |
| Fit a depth-two ReLU network | Worst-case training results concern squared-loss fitting; finer bounds use stated hypotheses. [Source](../sources/relu-training-hardness.md) |
| Train fully quantized ReLU networks | Hard cases coexist with tractability for specified parameter combinations. [Source](../sources/quantized-network-training.md) |
| Recover a network from queries | Polynomial guarantees require oracle access and regularity conditions. [Source](../sources/relu-membership-query-extraction.md) |

Construction cost, minimal representation, learning cost, extraction cost and inference cost are different questions. This distinction prevents apparent disagreements between results with different inputs and guarantees.

## When a minimizer would imply P = NP

Merely finding or asking for a smallest network does not imply $P=NP$. The relevant claim would require a **polynomial-time algorithm guaranteed to find a global optimum on every instance** of a precisely defined optimization problem, together with a matching hardness reduction.

For a problem NP-hard under deterministic polynomial-time reductions, such an exact polynomial-time optimizer would imply $P=NP$ if its result solves the associated hard decision question. That conditional principle does not establish hardness of our unspecified FSM-to-minimum-synapse-network problem. Define the source representation, activations, architecture, weight encoding, state/output semantics and equivalence domain first. A truth table can be exponentially larger than a source program describing its function, so the input-size convention matters too.

The multi-output circuit result in this collection uses **randomized** reductions. A deterministic polynomial-time solver for its target problem would provide randomized polynomial-time algorithms for NP problems (in particular, $NP\subseteq BPP$); this result alone is not the deterministic implication $P=NP$. Nor does circuit minimization immediately transfer to neural synapse minimization: a more expressive target might use smaller representations that invalidate a size-preserving reduction. [Source, abstract](../sources/multi-output-circuit-minimization.md).

Training does not remove worst-case optimization difficulty. Goel et al. prove NP-hardness for globally minimizing squared training loss even with a single ReLU, and other results depend on stated hypotheses. Practical gradient-based fitting is a heuristic approach to a declared loss, not a universal optimal compiler. These results do not show that every useful training run is difficult. [Source, abstract](../sources/relu-training-hardness.md).

See the [corrected efficiency recap](../questions/efficient-methods-and-matrix-mapping.md) for why exact construction need not be minimal, Boolean lowering is optional, and approximation need not be the most efficient route.

## Circuit size, time and uniformity

Connection count does not include recurrence steps, arithmetic precision or the cost of constructing a model. Size and depth are distinct even for feedforward circuits. P versus NP concerns worst-case bit-cost time as input length grows, not just the optimum for one fixed-size FSM.

[Cook's official description](../sources/cook-p-vs-np.md), sections 1–3, gives the relevant connection: a polynomial-time SAT algorithm implies P=NP; a superpolynomial general Boolean-circuit-size lower bound for an NP-complete problem implies P≠NP because every P computation has polynomial-size circuits. The latter is an asymptotic lower bound, not a consequence of merely computing each finite minimum.

Separately chosen small circuits for each input length describe nonuniform computation (P/poly). To infer P membership from a family, supply an efficient uniform construction and evaluation algorithm. [Blais's lectures](../sources/circuits-and-nonuniform-computation.md). A neural application also needs a stated simulation/precision model. See [smallest networks versus fastest algorithms](../questions/smallest-networks-fastest-algorithms-and-p-vs-np.md) for conditions, an exhaustive-minimization example and the fixed-FSM distinction.

## Background with narrower relevance

- [P versus NP](../sources/p-vs-np.md) remains an unsolved complexity question in the captured institutional overview.
- [Quantum polynomial lower bounds](../sources/quantum-lower-bounds.md) concern oracle-query complexity.
- [HILL](../sources/hill-pseudorandom-generators.md) links one-way functions and pseudorandom generators.

These sources do not directly establish hardness or speedups for the proposed FSM compiler. Any application requires a matching problem definition, resource model and reduction.

## Related pages

- [State encoding](state-encoding.md)
- [Learning versus construction](learning-vs-construction.md)
- [Boolean-circuit compilation](boolean-circuit-compilation.md)
