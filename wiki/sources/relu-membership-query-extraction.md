---
title: "An Exact Poly-Time Membership-Queries Algorithm for Extracting a Three-Layer ReLU Network"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/relu-membership-query-extraction/document.txt"]
review: first-pass
---

# An Exact Poly-Time Membership-Queries Algorithm for Extracting a Three-Layer ReLU Network

## Provenance and coverage

- Attribution: Amit Daniely and Elad Granot; arXiv v5, 2023-03-04.
- [Supplied URL](https://arxiv.org/html/2105.09673v5).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/relu-membership-query-extraction/document.txt); [capture metadata](../../raw/relu-membership-query-extraction/capture.json).
- Review: Abstract, introduction, results and assumptions; later proofs/appendices not reviewed.
- Capture coverage: 164/820 browser text lines from https://arxiv.org/html/2105.09673v5. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Studies reconstructing ReLU networks using black-box queries. Polynomial-time guarantees depend on general-position assumptions, with additional restrictions for depth-three networks. The reconstruction works through changes in piecewise-affine behavior. It addresses recovering a network's function, rather than compiling a supplied FSM. [Evidence](../../raw/relu-membership-query-extraction/document.txt).

## Relevance and next question

Compare the oracle model and regularity conditions with any proposed inverse extraction task; do not transfer these guarantees to ordinary sample-based training.

## Connections

- [complexity limits](../concepts/complexity-limits.md).
- [Reading queue](../questions/reading-queue.md).

