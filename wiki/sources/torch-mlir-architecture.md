---
title: "Torch-MLIR Architecture"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/torch-mlir-architecture/document.txt"]
review: first-pass
---

# Torch-MLIR Architecture

## Provenance and coverage

- Attribution: Torch-MLIR project documentation; main branch, commit not pinned.
- [Supplied URL](https://github.com/llvm/torch-mlir/blob/main/docs/architecture.md).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/torch-mlir-architecture/document.txt); [capture metadata](../../raw/torch-mlir-architecture/capture.json).
- Review: Architecture overview, backend contract and lowering sections; linked architecture image not inspected.
- Capture coverage: 389/389 browser text lines from https://raw.githubusercontent.com/llvm/torch-mlir/main/docs/architecture.md. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Describes a frontend/backend split joined by a backend contract in the torch dialect. Frontends normalize PyTorch programs into that contract; backends lower supported operations into target dialects. Torch-MLIR is a component for building a flow, rather than a production end-to-end compiler by itself. [Evidence](../../raw/torch-mlir-architecture/document.txt).

## Relevance and next question

Check the current supported frontend and required operators before selecting a lowering route; do not assume all PyTorch graphs meet the backend contract.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

