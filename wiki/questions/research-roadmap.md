---
title: "How should we start an FSM-to-network implementation?"
type: question
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/mit-fsm-design/document.txt", "raw/verilog2nn/document.txt", "raw/differentiable-fsm/document.txt", "raw/efficient-fsm-simulation/document.txt", "raw/spectral-wfa-rnn/document.txt"]
---

# How should we start an FSM-to-network implementation?

## Question

Which first experiment would turn this reading list into a reproducible construction, while keeping exactness, learning and performance distinct?

## Proposed answer

Start with a fully specified small deterministic machine and a trusted symbolic runner. Treat each construction route as a separate experiment with the same observable contract. This is a research proposal; no FSM compiler or neural implementation has been built or tested yet.

| Route | Starting material | Main issue to resolve |
| --- | --- | --- |
| Direct transition/emission tensors | [Differentiable FSM](../sources/differentiable-fsm.md), [linear second-order recurrence](../sources/spectral-wfa-rnn.md) | Deterministic tables versus learned distributions; tensor axis conventions |
| Threshold-network construction | [Alon–Dewdney–Ott](../sources/efficient-fsm-simulation.md) | Valid initialization, activation assumptions and latency |
| Neuralized Boolean step plus stored state | [MIT FSM design](../sources/mit-fsm-design.md), [verilog2nn](../sources/verilog2nn.md) | Compile the combinational step and define the sequential wrapper |

## Proposed sequence

1. Define state/input/output sets, complete transitions, initial/reset state and output timing. A small parity or sequence-detector machine is a possible example; no particular example has been selected.
2. Implement a direct symbolic transition-table reference and enumerate all reachable state/input pairs.
3. Choose one route, construct parameters from the known machine, and check step equivalence. Include reset, empty input, repeated inputs and invalid-encoding policy.
4. Compare traces on exhaustive short sequences and longer randomized/adversarial sequences. Trace testing supplements the step argument; it does not by itself prove arbitrary-length equivalence.
5. Only after behavior agrees, investigate encoding/connection reductions and [compiler deployment](../concepts/compiler-pipeline.md). Record compilation overhead, inference time and memory separately.
6. If studying learned machines, use a separate experiment with explicit training/held-out coverage and [extraction caveats](../concepts/learning-vs-construction.md).

## Assumptions and unresolved points

- The user's preferred machine type, activation family, target hardware and acceptable latency are not yet specified.
- A conventional recurrent network and a tensorized second-order update may satisfy different architectural requirements.
- The classical papers' equations need visual checking before reproducing exact complexity bounds.
- A compact construction or a successful compilation is not evidence of faster execution on the target workload.

## Related pages

- [Reading queue and access status](reading-queue.md)
- [Exact FSM construction](../concepts/exact-fsm-construction.md)
- [Current synthesis](../synthesis.md)
