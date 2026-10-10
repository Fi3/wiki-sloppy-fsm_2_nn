---
title: "Bounds on the Complexity of Recurrent Neural Network Implementations of Finite State Machines"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/fsm-rnn-complexity/document.txt"]
review: first-pass
---

# Bounds on the Complexity of Recurrent Neural Network Implementations of Finite State Machines

## Provenance and coverage

- Attribution: Bill G. Horne and Don R. Hush; NeurIPS 1993 proceedings.
- [Supplied URL](https://proceedings.neurips.cc/paper/1993/file/afda332245e2af431fb7b672a68b659d-Paper.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/fsm-rnn-complexity/document.txt); [capture metadata](../../raw/fsm-rnn-complexity/capture.json).
- Review: Abstract, introduction and main construction/bound statements; OCR-sensitive formulas and proofs not independently verified.
- Capture coverage: 295/295 browser text lines from https://proceedings.neurips.cc/paper/1993/file/afda332245e2af431fb7b672a68b659d-Paper.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Studies neuron complexity of threshold-network FSM implementations under restrictions on weights, thresholds and fan-in. It presents upper bounds and conditional matching lower bounds, with assumptions about how state is encoded. Architecture restrictions therefore belong alongside every quoted complexity bound. [Evidence](../../raw/fsm-rnn-complexity/document.txt).

## Relevance and next question

Verify formulas against the PDF: extraction corrupts several radicals/exponents. Compare state encodings and timing before relating these bounds to later constructions.

## Connections

Targeted follow-up: section 2.2 defines fan-in by nonzero weights; section 5 studies bounded fan-in. These support connection accounting via the sum of fan-ins, rather than treating neuron counts as synapse counts. See [the size analysis](../questions/fsm-size-vs-synapses.md). This follow-up does not remove the original OCR/proof-review limits.

- [state encoding](../concepts/state-encoding.md).
- [Reading queue](../questions/reading-queue.md).
