---
title: "Differentiable Finite State Machines"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/differentiable-fsm/document.txt"]
review: first-pass
---

# Differentiable Finite State Machines

## Provenance and coverage

- Attribution: Google Research Self-Organising Systems tutorial; URL under 2022. Individual byline/date not recovered.
- [Supplied URL](https://google-research.github.io/self-organising-systems/2022/diff-fsm/).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/differentiable-fsm/document.txt); [capture metadata](../../raw/differentiable-fsm/capture.json).
- Review: Text, equations, code and toy-task discussion reviewed; diagrams and linked notebooks were not independently inspected/executed.
- Capture coverage: 231/231 browser text lines from https://google-research.github.io/self-organising-systems/2022/diff-fsm/. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Represents Mealy-machine transitions and emissions as tensors acting on one-hot input/state vectors. Softmax relaxes the tables into distributions for gradient-based fitting; hard decoding returns discrete tables. Entropy regularization and initialization biases affect discovered machines. The tutorial demonstrates that fitting one sequence can still produce the wrong general behavior. [Evidence](../../raw/differentiable-fsm/document.txt).

## Relevance and next question

Compare directly constructing deterministic tensors from a known table with learning them from examples; test unobserved transitions and longer sequences.

## Connections

- [learning vs construction](../concepts/learning-vs-construction.md).
- [Reading queue](../questions/reading-queue.md).

