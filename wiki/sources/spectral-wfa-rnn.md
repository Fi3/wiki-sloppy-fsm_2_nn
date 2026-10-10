---
title: "Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/spectral-wfa-rnn/document.txt"]
review: first-pass
---

# Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning

## Provenance and coverage

- Attribution: Guillaume Rabusseau, Tianyu Li and Doina Precup; AISTATS/PMLR 89, 2019.
- [Supplied URL](https://proceedings.mlr.press/v89/rabusseau19a.html).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/spectral-wfa-rnn/document.txt); [capture metadata](../../raw/spectral-wfa-rnn/capture.json).
- Review: Official abstract and beginning of the full paper; complete proofs and simulation study not reviewed.
- Capture coverage: 47/47 browser text lines from https://proceedings.mlr.press/v89/rabusseau19a.html; 433/1290 browser text lines from https://proceedings.mlr.press/v89/rabusseau19a/rabusseau19a.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Connects weighted finite automata to second-order recurrent networks with linear activations on discrete-symbol sequences. It extends spectral-learning ideas through low-rank Hankel tensors toward continuous-input linear second-order RNNs. The architecture and linearity restrictions are essential. [Evidence](../../raw/spectral-wfa-rnn/document.txt).

## Relevance and next question

Derive the symbol/state bilinear update with explicit tensor axes, then inspect rank and sampling assumptions before implementing spectral recovery.

## Connections

- [weighted automata](../concepts/weighted-automata.md).
- [Reading queue](../questions/reading-queue.md).

