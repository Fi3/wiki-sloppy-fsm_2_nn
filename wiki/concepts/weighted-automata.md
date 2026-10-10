---
title: "Weighted automata and second-order recurrence"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/weighted-automata-equivalence/document.txt", "raw/spectral-wfa-rnn/document.txt", "raw/differentiable-fsm/document.txt"]
---

# Weighted automata and second-order recurrence

## Algebraic representation

Using row-vector state, a weighted automaton assigns a matrix $M(a)$ to each input symbol and evaluates

$$f(a_1\cdots a_k)=\alpha M(a_1)\cdots M(a_k)\eta.$$

The empty word uses the identity matrix. Forward/backward spaces provide the setting for equivalence and minimization over a field. [Kiefer, preliminaries and equivalence section](../sources/weighted-automata-equivalence.md).

## Neural connection

For one-hot inputs, a symbol-selected matrix update can be written as a contraction of input, state and a transition tensor. Rabusseau–Li–Precup's equivalence concerns **linear second-order RNNs**, not every ordinary RNN architecture. [Source](../sources/spectral-wfa-rnn.md).

A practical Mealy-machine tensor formulation also includes an emission tensor and a starting state. Its deterministic and probabilistic interpretations have different contracts. [Differentiable FSM tutorial](../sources/differentiable-fsm.md).

With column-vector state, an equivalent convention is $h'=T_a h$, where $(T_a)_{r,q}=1$ exactly when the deterministic transition sends state $q$ to $r$ on symbol $a$. Selecting $T_a$ by input is bilinear when expressed jointly in one-hot input and state; it is not a single fixed affine map of their concatenation. See [matrix mapping](../questions/efficient-methods-and-matrix-mapping.md) for the parity example and an ordinary fixed-weight ReLU realization.

## Open questions

- Which orientation and tensor axes will the first implementation use?
- Is the output an acceptance score, a weighted series, or a per-step emitted symbol?
- Are exact field arithmetic or approximate floating-point rank decisions required?

## Related pages

- [Learning versus construction](learning-vs-construction.md)
- [State encoding](state-encoding.md)
- [Research roadmap](../questions/research-roadmap.md)
