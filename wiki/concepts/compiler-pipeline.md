---
title: "Tensor-program capture, lowering and deployment"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/pytorch-fx/document.txt", "raw/pytorch-export-ir/document.txt", "raw/pytorch-compiler/document.txt", "raw/torch-mlir-architecture/document.txt", "raw/iree-pytorch/document.txt", "raw/iree-cpu/document.txt", "raw/mlir-linalg/document.txt", "raw/llvm-vectorizers/document.txt", "raw/tensorize/document.txt", "raw/dnd-decompiler/document.txt"]
---

# Tensor-program capture, lowering and deployment

## Roles of the supplied tools

| Component | Role in the reviewed material | Source |
| --- | --- | --- |
| FX | Module tracing, graph transformations and generated Python | [FX](../sources/pytorch-fx.md) |
| torch.export IR | A stronger operator/input/metadata contract on an FX representation | [Specification](../sources/pytorch-export-ir.md) |
| torch.compile | Graph capture and compilation through a backend | [Compiler guide](../sources/pytorch-compiler.md) |
| Torch-MLIR | Normalize to a backend contract and lower to target dialects | [Architecture](../sources/torch-mlir-architecture.md) |
| IREE Turbine | PyTorch JIT/AOT integration with IREE | [Framework guide](../sources/iree-pytorch.md) |
| IREE CPU | Executable formats, targets and runtime device choices | [Deployment](../sources/iree-cpu.md) |
| MLIR Linalg | Retain structured iteration/access information for transformations | [Rationale](../sources/mlir-linalg.md) |
| LLVM vectorizers | Loop/SLP vectorization subject to dependence and cost checks | [Guide](../sources/llvm-vectorizers.md) |

These are components and possible routes. They are not a verified single interchangeable pipeline. Pin compatible versions and test required operators before combining them.

## Lifting and reversing

TENSORIZE's abstract describes synthesizing tensor DSL programs from symbolic traces of legacy code; its full paper still needs review. [Source](../sources/tensorize.md).

DnD works in the reverse direction, recovering neural structure from compiled binaries through symbolic analysis and templates. That scope does not establish arbitrary-program-to-network conversion. [Source](../sources/dnd-decompiler.md).

## Proposed benchmark protocol

Verify behavior before measuring speed. Separate compilation time, warm-up, steady-state execution, state handling, batching and memory cost. Compare against a direct transition-table implementation. No tool installation, compilation experiment or benchmark has been performed yet.

## Related pages

- [Boolean-circuit compilation](boolean-circuit-compilation.md)
- [Research roadmap](../questions/research-roadmap.md)
