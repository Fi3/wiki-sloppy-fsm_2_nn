---
title: "Boolean circuits as neural networks"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/verilog2nn/document.txt", "raw/boolean-network-optimization/document.txt", "raw/threshold-logic-synthesis/document.txt", "raw/threshold-interconnect-synthesis/document.txt"]
---

# Boolean circuits as neural networks

## Constructive gate mapping

The verilog2nn README describes synthesis to an AND/NOT netlist, topological layering and sparse linear/ReLU operations. For Boolean inputs $a,b\in\{0,1\}$,

$$a\land b=\operatorname{ReLU}(a+b-1),\qquad \neg a=1-a.$$

The input-domain restriction matters: these identities do not assert Boolean behavior for arbitrary real values. Repository verification claims have not been reproduced here. [Source](../sources/verilog2nn.md).

## Optimization evidence

- The ICLR 2025 work studies lossless optimization of neural representations of Boolean networks. Reported size reductions need reproduction before becoming project results. [Source](../sources/boolean-network-optimization.md).
- Threshold synthesis considers costs including fan-in, weights and gate coverage. [TCAD source](../sources/threshold-logic-synthesis.md).
- Disjoint-support work also targets interconnect cost. [DAC source](../sources/threshold-interconnect-synthesis.md).

## Project interpretation

An FSM step can expose current state and input as circuit inputs and next state and output as circuit outputs. This is a proposed application of the combinational route. State retention, resets and timing still require a sequential wrapper and verification.

Do not equate fewer neurons, fewer wires, smaller hardware area and faster tensor inference; they are different objectives.

Layers collect operations that can run in parallel; named functions do not determine layer count. The ICLR 2025 construction maps local LUTs to threshold-hidden/linear-output subnetworks, parallelizes by DAG depth and merges adjacent affine stages. For LUT depth $d$, section 2.2 gives $2d$ unmerged stages versus $d+1$ merged stages, with identity relays where needed. Matrix fusion can change sparsity. [Source](../sources/boolean-network-optimization.md).

See [efficient methods and matrix mapping](../questions/efficient-methods-and-matrix-mapping.md) for explicit AND/XOR matrices, a two-matrix exact FSM step, and a synapse-oriented comparison.

## Related pages

- [Exact FSM construction](exact-fsm-construction.md)
- [Compiler pipeline](compiler-pipeline.md)
- [Complexity limits](complexity-limits.md)
