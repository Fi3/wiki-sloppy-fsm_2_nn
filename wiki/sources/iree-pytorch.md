---
title: "IREE PyTorch Integration"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/iree-pytorch/document.txt"]
review: first-pass
---

# IREE PyTorch Integration

## Provenance and coverage

- Attribution: IREE official framework guide; rolling documentation captured 2026-10-07.
- [Supplied URL](https://iree.dev/guides/ml-frameworks/pytorch/).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/iree-pytorch/document.txt); [capture metadata](../../raw/iree-pytorch/capture.json).
- Review: Framework workflow, prerequisites, JIT/AOT overview; examples not executed.
- Capture coverage: 612/612 browser text lines from https://iree.dev/guides/ml-frameworks/pytorch/. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Documents PyTorch integration through IREE Turbine, with JIT and ahead-of-time workflows. The paths connect PyTorch graph capture to native deployment, including compiled VMFB artifacts. It provides an integration route, not evidence of exactness or speed for an FSM implementation. [Evidence](../../raw/iree-pytorch/document.txt).

## Relevance and next question

Verify supported operators and exported state/input signatures for a small transition module before adopting this route.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

