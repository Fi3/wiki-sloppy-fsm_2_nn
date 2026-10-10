---
title: "Notes on Equivalence and Minimization of Weighted Automata"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/weighted-automata-equivalence/document.txt"]
review: first-pass
---

# Notes on Equivalence and Minimization of Weighted Automata

## Provenance and coverage

- Attribution: Stefan Kiefer; arXiv v1, 2020-09-02.
- [Supplied URL](https://arxiv.org/html/2009.01217v1).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/weighted-automata-equivalence/document.txt); [capture metadata](../../raw/weighted-automata-equivalence/capture.json).
- Review: Abstract, definitions, equivalence algorithm and principal minimization statements; proofs not independently verified.
- Capture coverage: 405/405 browser text lines from https://arxiv.org/html/2009.01217v1. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Presents weighted automata over a field through linear algebra. A word is evaluated by composing symbol-specific matrices between initial and final vectors. Forward/backward spaces support equivalence tests and minimization; the Hankel representation connects behavior to rank. These are algebraic results, not a claim about training arbitrary nonlinear RNNs. [Evidence](../../raw/weighted-automata-equivalence/document.txt).

## Relevance and next question

Translate the evaluation convention consistently into a tensor recurrence; verify field assumptions and numeric rank decisions before implementing minimization.

## Connections

- [weighted automata](../concepts/weighted-automata.md).
- [Reading queue](../questions/reading-queue.md).

