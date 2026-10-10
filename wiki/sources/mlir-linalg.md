---
title: "Linalg Dialect Rationale: The Case For Compiler-Friendly Custom Operations"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/mlir-linalg/document.txt"]
review: first-pass
---

# Linalg Dialect Rationale: The Case For Compiler-Friendly Custom Operations

## Provenance and coverage

- Attribution: MLIR official design rationale; rolling documentation captured 2026-10-07.
- [Supplied URL](https://mlir.llvm.org/docs/Rationale/RationaleLinalgDialect/).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/mlir-linalg/document.txt); [capture metadata](../../raw/mlir-linalg/capture.json).
- Review: Design principles and structured-operation rationale; compiler behavior not tested.
- Capture coverage: 402/402 browser text lines from https://mlir.llvm.org/docs/Rationale/RationaleLinalgDialect/. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Motivates structured operations that retain iteration and data-access information so transformations can be applied systematically. Linalg represents parallel and reduction structure; the rationale separates transformation validity from profitability. Preserving high-level structure is useful when lowering transition computations. [Evidence](../../raw/mlir-linalg/document.txt).

## Relevance and next question

Identify which dense or sparse operations actually represent the chosen FSM and compare lowering costs, rather than assuming every loop becomes a profitable matrix multiplication.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

