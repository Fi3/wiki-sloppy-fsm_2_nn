---
title: "Current synthesis"
type: overview
created: 2026-10-07
updated: 2026-10-09
status: active
sources: ["raw/reading-list-original-order.md", "raw/mit-fsm-design/document.txt", "raw/efficient-fsm-simulation/document.txt", "raw/verilog2nn/document.txt", "raw/differentiable-fsm/document.txt", "raw/spectral-wfa-rnn/document.txt", "raw/fools-gold/document.txt"]
---

# Current synthesis

## Current understanding

The first batch has 30 first-pass source summaries. Four supplied resources remain unreadable or inaccessible. The [reading queue](questions/reading-queue.md) accounts for every URL and the scope of completed reading.

The material suggests three routes worth comparing. This grouping is our interpretation, not a claim that the constructions are interchangeable:

| Route | Evidence | Main contract to check |
| --- | --- | --- |
| Direct tensor recurrence | [Differentiable FSM](sources/differentiable-fsm.md), [weighted automata / second-order RNNs](sources/spectral-wfa-rnn.md) | Input/state encoding, emissions and deterministic versus probabilistic behavior |
| Recurrent threshold construction | [Alon–Dewdney–Ott](sources/efficient-fsm-simulation.md) | Activation, initialization, network restrictions and output latency |
| Neuralized next-state/output circuit | [MIT FSM design](sources/mit-fsm-design.md), [verilog2nn](sources/verilog2nn.md) | Combinational gate correctness plus a sequential state/reset wrapper |

Our proposed next step is a small, fully specified machine with a trusted symbolic runner, followed by one construction and a step-equivalence check. See the [research roadmap](questions/research-roadmap.md). No FSM-to-network code or performance experiment has been implemented yet.

For the user's synapse-count objective, compare compact state encoding plus shared next-state/output logic with a one-hot baseline. [Efficient methods and matrix mapping](questions/efficient-methods-and-matrix-mapping.md) distinguishes sparse gate construction, local LUT/threshold optimization and symbol-selected tensor recurrence. Its explicit matrices clarify that dependency depth, local activation requirements and affine fusion determine layers; there is no general one-layer-per-function rule. This is a proposed comparison, not a measured efficiency ranking.

The user subsequently proposed high-level bounded-memory code with pure functions and permitted lossy replacement. This opens a separate approximate route: [neural surrogate compilation](concepts/neural-surrogate-compilation.md). Five new first-pass sources identify function replacement (Parrot), workflow definitions, path-guided sampling (Turaco), learned source-to-weights initialization (CompNet), and a restricted compile-plus-learn alternative (Cajal). [High-level program analysis](questions/high-level-programs-to-neural-surrogates.md) proposes minimizing connections under a whole-program error target. Function boundaries are useful candidates, but model partition, repeated-step error and actual speed remain unresolved. No approximate model has been trained here.

The [2026-10-09 recap correction](questions/efficient-methods-and-matrix-mapping.md) separates constructing an exact network from finding a globally smallest one in polynomial time. The collected results do not prove a blanket “minimum FSM-to-NN implies P=NP” claim, training is not a universal efficiency winner, and explicit Boolean lowering is one exact route rather than a requirement. A direct one-unit ReLU toggle provides a compact exact example; arbitrary-machine size and runtime remain separate questions.

A further [size-versus-time analysis](questions/smallest-networks-fastest-algorithms-and-p-vs-np.md) uses Cook's official description and circuit lectures to identify the genuine P-versus-NP connection. Efficient uniform construction and bit-cost evaluation of exact SAT networks would imply P=NP; sufficiently general superpolynomial circuit lower bounds would imply P≠NP. A finite minimization procedure alone supplies neither conclusion. Fixed finite-state stream processing, nonuniform input-length families, recurrence and weight precision must be distinguished.

## Disagreements and uncertainty

- Different size bounds use different network models, state encodings and resource restrictions. Reconcile these assumptions before interpreting them as contradictions. Older mathematical extractions contain OCR errors. [State encoding](concepts/state-encoding.md).
- Learning relaxed tables from examples and extracting states from recurrent trajectories do not automatically preserve all sequence behavior. [Construction, learning and extraction](concepts/learning-vs-construction.md), [Kolen](sources/fools-gold.md).
- The source collection includes complexity, quantum and cryptographic background; its relevance requires explicit problem definitions or reductions. [Complexity scope](concepts/complexity-limits.md).
- Compiler documentation supplies possible deployment components. Supported operators, compatible versions and speed on the intended workload remain untested. [Compiler pipeline](concepts/compiler-pipeline.md).
- First-pass summaries identify useful claims, not independently verified proofs or reproduced experiments. Complete text capture does not imply complete visual or technical review.
- The BYU and Caltech PDFs, ScienceDirect resource and GGM PDF still need readable copies. TENSORIZE currently has an abstract-level summary rather than a full-paper review. [Queue](questions/reading-queue.md).

## Open questions

- Which finite state machine model and target network architecture should be investigated first?
- Is the objective exact sequence behavior, compact representation, runtime speed, learnability, or some combination?
- Are outputs Mealy or Moore, and what latency/reset convention is acceptable?
- Which activation, precision and legal-input assumptions should the construction preserve?
- Which representation gives a useful tradeoff against a direct transition-table baseline?
- The user defines NN size as synapse count. [FSM size versus synapses](questions/fsm-size-vs-synapses.md) derives example method-specific bounds; connection count, neuron count and allocated matrix entries must be kept distinct.
- Which remaining full-paper sections or original equations should be read before implementing the chosen route?

## Related pages

- [Overview](overview.md)
- [Index](index.md)
- [Boolean circuits as neural networks](concepts/boolean-circuit-compilation.md)
- [Weighted automata](concepts/weighted-automata.md)
