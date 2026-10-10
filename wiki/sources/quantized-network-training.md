---
title: "Tractability via Low Dimensionality: The Parameterized Complexity of Training Quantized Neural Networks"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/quantized-network-training/document.txt"]
review: first-pass
---

# Tractability via Low Dimensionality: The Parameterized Complexity of Training Quantized Neural Networks

## Provenance and coverage

- Attribution: Robert Ganian, Frank Sommer and Manuel Sorge; ICLR 2026.
- [Supplied URL](https://proceedings.iclr.cc/paper_files/paper/2026/file/bf1b3f86d67feecdc22c1abea2c6127c-Paper-Conference.pdf); [alternate supplied URL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bf1b3f86d67feecdc22c1abea2c6127c-Abstract-Conference.html).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/quantized-network-training/document.txt); [capture metadata](../../raw/quantized-network-training/capture.json).
- Review: Abstract, introduction and opening results; later proofs not reviewed. The supplied PDF and abstract are one work.
- Capture coverage: 258/680 browser text lines from https://proceedings.iclr.cc/paper_files/paper/2026/file/bf1b3f86d67feecdc22c1abea2c6127c-Paper-Conference.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Studies ReLU training with parameters and data restricted to finite integer domains. It reports hardness even under restrictive settings and tractable parameterized cases involving input dimension together with additional architecture/output/error parameters. Quantization alone does not remove worst-case training difficulty. [Evidence](../../raw/quantized-network-training/document.txt).

## Relevance and next question

Review the exact quantization mode and parameter combinations; distinguish constructing fixed weights from solving a training optimization problem.

## Connections

- [complexity limits](../concepts/complexity-limits.md).
- [Reading queue](../questions/reading-queue.md).

