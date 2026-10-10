---
title: "Auto-Vectorization in LLVM"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/llvm-vectorizers/document.txt"]
review: first-pass
---

# Auto-Vectorization in LLVM

## Provenance and coverage

- Attribution: LLVM official documentation; rolling version captured 2026-10-07.
- [Supplied URL](https://llvm.org/docs/Vectorizers.html).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/llvm-vectorizers/document.txt); [capture metadata](../../raw/llvm-vectorizers/capture.json).
- Review: Vectorizer overview, usage, cost model and limitations; generated code not inspected.
- Capture coverage: 593/593 browser text lines from https://llvm.org/docs/Vectorizers.html. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Describes loop vectorization and SLP vectorization. One combines work across loop iterations; the other groups scalar operations. Cost models and dependence checks constrain applicability. Having a tensor expression does not by itself establish vectorized machine code or a speedup. [Evidence](../../raw/llvm-vectorizers/document.txt).

## Relevance and next question

Inspect generated code and benchmark representative batches; determine which dimension offers independent work.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

