---
title: "Boolean Circuits and Non-Uniform Computation — CS 365"
type: source
created: 2026-10-09
updated: 2026-10-09
status: active
sources: ["raw/circuits-and-nonuniform-computation/document.txt"]
review: first-pass
---

# Boolean Circuits and Non-Uniform Computation — CS 365

## Provenance and coverage

- Author: Eric Blais, University of Waterloo, CS 365 winter 2026. Both pages list last edit 2026-01-07.
- [Lecture 10: Boolean Circuits](https://cs.uwaterloo.ca/~eblais/cs365/w26/circuits); [Lecture 11: Non-Uniform Computation](https://cs.uwaterloo.ca/~eblais/cs365/w26/nonuniform).
- Retrieved 2026-10-09. [Immutable browser text](../../raw/circuits-and-nonuniform-computation/document.txt); [capture metadata](../../raw/circuits-and-nonuniform-computation/capture.json).
- Coverage: 109/109 and 68/68 numbered browser lines. Reviewed the textual definitions, parity example, simulation lemma and nonuniform complexity statements. Figures not inspected; proofs not independently audited.

## Summary and evidence

Lecture 10 distinguishes circuit size from depth and describes a balanced parity circuit with linear size and logarithmic depth. A circuit handles one input length; a family handles varying lengths. Lecture 11 shows how time-bounded Turing computations can be represented by circuits, then characterizes P/poly through polynomial-size circuit families and polynomial-time computation with advice. Arbitrary small circuit families need not supply a single efficient construction algorithm. [Evidence](../../raw/circuits-and-nonuniform-computation/document.txt).

## Caveats

The lecture's size convention counts AND/OR gates with unbounded fan-in; it is not the user's nonzero-connection metric. Translate wire counts and allowed operations explicitly when applying it to neural networks. Its general simulation and nonuniformity arguments do not prove neural minimization hardness or a separation of P from NP. We rely on the stated definitions and implications rather than claiming a full technical review of every historical comment.

## Connections and next question

- [Complexity scope](../concepts/complexity-limits.md).
- [Smallest networks, fastest algorithms and P versus NP](../questions/smallest-networks-fastest-algorithms-and-p-vs-np.md).

Which network family has a polynomial-cost uniform generator and a polynomial bit-cost evaluator, and which circuit model can it simulate?

