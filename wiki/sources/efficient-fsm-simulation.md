---
title: "Efficient Simulation of Finite Automata by Neural Nets"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/efficient-fsm-simulation/document.txt"]
review: first-pass
---

# Efficient Simulation of Finite Automata by Neural Nets

## Provenance and coverage

- Attribution: Noga Alon, A. K. Dewdney and Teunis J. Ott; Journal of the ACM 38(2), April 1991.
- [Supplied URL](https://www.cs.tau.ac.il/~nogaa/PDFS/Publications/Efficient%20simulations%20of%20finite%20automata%20by%20neural%20nets.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/efficient-fsm-simulation/document.txt); [capture metadata](../../raw/efficient-fsm-simulation/capture.json).
- Review: Abstract, model definitions, theorem statements and Section 5 construction text; full extracted text captured, proofs/figures not independently verified.
- Capture coverage: 797/797 browser text lines from https://www.cs.tau.ac.il/~nogaa/PDFS/Publications/Efficient%20simulations%20of%20finite%20automata%20by%20neural%20nets.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Studies Mealy-machine simulation by recurrent threshold machines. Construction size depends on permitted weights, thresholds and connectivity. The straightforward construction uses state/input-pair neurons; its outputs lag the original machine by one step. Smaller constructions and counting lower bounds use specific models. [Evidence](../../raw/efficient-fsm-simulation/document.txt).

## Relevance and next question

Translate Section 5 while preserving valid initialization and output latency. Check equations visually before reproducing OCR-sensitive bounds.

## Connections

- [exact fsm construction](../concepts/exact-fsm-construction.md).
- [Reading queue](../questions/reading-queue.md).

