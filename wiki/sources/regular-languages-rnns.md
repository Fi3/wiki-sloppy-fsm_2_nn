---
title: "On Efficiently Representing Regular Languages as RNNs"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/regular-languages-rnns/document.txt"]
review: first-pass
---

# On Efficiently Representing Regular Languages as RNNs

## Provenance and coverage

- Attribution: Anej Svete, Robin Shing Moon Chan and Ryan Cotterell; arXiv v2, 2024-06-18.
- [Supplied URL](https://arxiv.org/html/2402.15814v2).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/regular-languages-rnns/document.txt); [capture metadata](../../raw/regular-languages-rnns/capture.json).
- Review: Abstract, introduction, preliminaries and main bounded-stack construction definitions; proof appendix not reviewed.
- Capture coverage: 315/574 browser text lines from https://arxiv.org/html/2402.15814v2. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Studies efficient RNN representations of language models using bounded pushdown automata. Compact representations require structure in the stack-update operations; arbitrary automata do not inherit the same compression. The paper separates probabilistic language-model semantics from simple accept/reject behavior and discusses activation and precision assumptions. [Evidence](../../raw/regular-languages-rnns/document.txt).

## Relevance and next question

Read the proof appendix and implement a restricted structured example before generalizing its compression to arbitrary FSMs.

## Connections

- [state encoding](../concepts/state-encoding.md).
- [Reading queue](../questions/reading-queue.md).

