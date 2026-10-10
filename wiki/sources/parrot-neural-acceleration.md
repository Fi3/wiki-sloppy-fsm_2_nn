---
title: "Neural Acceleration for General-Purpose Approximate Programs"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/parrot-neural-acceleration/document.txt"]
review: first-pass
---

# Neural Acceleration for General-Purpose Approximate Programs

## Provenance and coverage

- Authors: Hadi Esmaeilzadeh, Adrian Sampson, Luis Ceze and Doug Burger.
- Publication: MICRO 2012.
- [Original source](https://www.cs.cornell.edu/~asampson/media/papers/npu-micro2012.pdf). Retrieved 2026-10-07.
- [Immutable browser extraction](../../raw/parrot-neural-acceleration/document.txt); [capture metadata](../../raw/parrot-neural-acceleration/capture.json). These are extracted text, not original file bytes.
- Reviewed scope: Abstract, introduction, programming model and compilation workflow through the captured portion of section 4.2 (PDF pages 1–4). Remaining architecture and evaluation sections were not audited.
- Numbered browser coverage: 387/1642 lines. Text coverage does not imply proof or figure review.

## Summary

Parrot replaces selected regions of imperative code with trained neural networks. Its implemented annotation boundary is an entire function. Candidate functions must be frequently executed, tolerate approximation, have compile-time fixed-size inputs and outputs, and be pure: all observed inputs and effects must be explicit in the interface.

## Main claims and relevance

Section 3.1 explicitly allows calls, loops and complex control flow inside a candidate region. Section 4 instruments executions to gather input/output examples, searches MLP topologies, trains weights and replaces calls with accelerator invocations. These are close to the user's proposed function-level transformation. The introduction reports benchmark speed/energy improvements on its NPU architecture; those are source reports, not measurements here. [Captured evidence](../../raw/parrot-neural-acceleration/document.txt).

## Limits and remaining review

Purity and bounded interfaces make replacement possible; they do not guarantee a function is easy to approximate. Speedups depend on the accelerator and invocation overhead. The source discusses keeping address computations precise and selecting only successfully approximated functions.

## Connections

- [Neural surrogate compilation](../concepts/neural-surrogate-compilation.md).
- [High-level programs to approximate neural modules](../questions/high-level-programs-to-neural-surrogates.md).

