---
title: "torch.export IR Specification"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/pytorch-export-ir/document.txt"]
review: first-pass
---

# torch.export IR Specification

## Provenance and coverage

- Attribution: PyTorch official documentation; main/development branch captured 2026-10-07.
- [Supplied URL](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/export/ir_spec.html).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/pytorch-export-ir/document.txt); [capture metadata](../../raw/pytorch-export-ir/capture.json).
- Review: IR overview and operator/node contract sections; this is a documentation reading, not a compatibility test.
- Capture coverage: 765/765 browser text lines from https://docs.pytorch.org/docs/main/user_guide/torch_compiler/export/ir_spec.html. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Defines an export representation built on FX with a stronger contract for operators, inputs, outputs and metadata. It specifies restricted call targets and explicit handling of parameters/buffers. This is useful for preserving a constructed tensor program across compilation stages. [Evidence](../../raw/pytorch-export-ir/document.txt).

## Relevance and next question

Choose a pinned PyTorch version and test operator/control-flow support for a state-transition step. The main-branch specification may differ from stable releases.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

