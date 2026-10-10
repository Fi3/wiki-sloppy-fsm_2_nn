---
title: "Exact FSM construction"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/mit-fsm-design/document.txt", "raw/efficient-fsm-simulation/document.txt", "raw/verilog2nn/document.txt"]
---

# Exact FSM construction

## Define the behavior first

A clocked machine combines state storage with next-state/output logic. Specify initialization, input sampling, the transition function, and whether outputs depend on state alone or also on the current input. [MIT FSM design](../sources/mit-fsm-design.md).

For a Mealy machine, write the target contract as

$$q_{t+1}=\delta(q_t,x_t),\qquad y_t=\lambda(q_t,x_t).$$

## Candidate constructions

- **Recurrent threshold network:** a classical route with explicit state/input neurons. The Alon–Dewdney–Ott construction includes an output delay; timing is part of the simulation contract. [Source](../sources/efficient-fsm-simulation.md).
- **Combinational neural step plus state storage:** compile next-state/output Boolean logic, then feed the computed next state into the following step. The supplied verilog2nn repository covers combinational logic. The sequential wrapper is a proposed extension for this project. [Source](../sources/verilog2nn.md).

## Proposed correctness obligation

Let $E$ encode symbolic states and $D$ decode outputs. Show that for every reachable state and legal input,

$$F(E(q),x)=(E(\delta(q,x)),\widetilde y),\qquad D(\widetilde y)=\lambda(q,x).$$

Correct initialization and the same timing convention then extend step correctness to traces by induction. This is our verification plan, not a completed proof for an implementation. Invalid encodings, reset and any latency must have explicit contracts.

## Related pages

- [State encoding](state-encoding.md)
- [Boolean-circuit compilation](boolean-circuit-compilation.md)
- [Research roadmap](../questions/research-roadmap.md)
