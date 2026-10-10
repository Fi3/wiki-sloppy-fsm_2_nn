---
title: "Optimizing Neural Network Representations of Boolean Networks"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/boolean-network-optimization/document.txt"]
review: first-pass
---

# Optimizing Neural Network Representations of Boolean Networks

## Provenance and coverage

- Attribution: Joshua Russell, Ignacio Gavier, Devdhar Patel, Edward Rietman and Hava Siegelmann; ICLR 2025.
- [Supplied URL](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f67852b3910e3aba21c951849b4531a6-Abstract-Conference.html).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/boolean-network-optimization/document.txt); [capture metadata](../../raw/boolean-network-optimization/capture.json).
- Review: Official abstract and opening paper sections, with targeted follow-up on sections 2.1–2.2 and the opening of 3.1 for activation, matrix mapping, depth and connection objectives. The 52-page paper and supplementary material were only partially captured; later proofs and experiments have not been audited.
- Capture coverage: 20/20 browser text lines from https://proceedings.iclr.cc/paper_files/paper/2025/hash/f67852b3910e3aba21c951849b4531a6-Abstract-Conference.html; 501/5500 browser text lines from https://proceedings.iclr.cc/paper_files/paper/2025/file/f67852b3910e3aba21c951849b4531a6-Paper-Conference.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Proposes deterministic optimization of neural representations of Boolean networks while preserving functional equivalence. The authors report reductions in neurons/connections and an objective-aware approach that shares work across subproblems. This is directly relevant to reducing constructed transition networks. [Evidence](../../raw/boolean-network-optimization/document.txt).

## Relevance and next question

Section 2.2 reviews bounded-input LUT mapping, truth-table-to-multilinear-polynomial conversion, two-affine-stage local networks with Heaviside hidden units and linear readouts, parallelization by Boolean DAG depth, and affine layer merging. For LUT depth $d$, its unmerged depth is $2d$ and merged depth is $d+1$. Identity vertices remove skip connections. The opening of section 3.1 relates hidden units to nonconstant monomials and first-stage connections to their degree sum. [Printed pages 3–5, extracted text](../../raw/boolean-network-optimization/document.txt).

These details support the [matrix/layer analysis](../questions/efficient-methods-and-matrix-mapping.md). This is a threshold-network construction, not an assertion that all gates use one ReLU layer.

Examine algorithm guarantees, activation model and remaining evaluation before reproducing results. Lossless reduction does not automatically establish global minimality or faster execution.

## Connections

- [boolean circuit compilation](../concepts/boolean-circuit-compilation.md).
- [Reading queue](../questions/reading-queue.md).
