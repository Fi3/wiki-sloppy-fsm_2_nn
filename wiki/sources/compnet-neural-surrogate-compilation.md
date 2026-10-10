---
title: "Learning to Compile Programs to Neural Networks"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/compnet-neural-surrogate-compilation/document.txt"]
review: first-pass
---

# Learning to Compile Programs to Neural Networks

## Provenance and coverage

- Authors: Logan Weber, Jesse Michel, Alex Renda and Michael Carbin.
- Publication: arXiv:2407.15078v1, 2024-07-21; conference status not established in this review.
- [Original source](https://arxiv.org/html/2407.15078v1). Retrieved 2026-10-07.
- [Immutable browser extraction](../../raw/compnet-neural-surrogate-compilation/document.txt); [capture metadata](../../raw/compnet-neural-surrogate-compilation/capture.json). These are extracted text, not original file bytes.
- Reviewed scope: Abstract, sections 1–4 and captured opening of evaluation methodology (section 5.1). Most evaluation, related work and appendices were not captured or audited.
- Numbered browser coverage: 263/2458 lines. Text coverage does not imply proof or figure review.

## Summary

CompNet is a learned surrogate compiler: a BERT-based encoder consumes program text and a parameter head produces the weights and biases of a smaller neural surrogate. It separates the cost of processing source code from the cost of executing the generated surrogate.

## Main claims and relevance

Sections 2–3 frame generation as producing an initialization that can be fine-tuned from program input/output examples. Section 4's ExeStack contains executable, deterministic, pointer-free numeric C functions. Section 5.1 uses a small sigmoid MLP as the target architecture. This directly addresses source-to-weights generation, in contrast to training a new function surrogate from scratch. [Captured evidence](../../raw/compnet-neural-surrogate-compilation/document.txt).

## Limits and remaining review

Upfront compiler training requires a corpus of programs and their executions. This is a restricted numeric-function setting, not support for arbitrary C programs, memory operations or exact FSM semantics. Its main objectives concern error, training data and training cost; it does not establish minimum synapse counts or a general runtime speedup.

## Connections

- [Neural surrogate compilation](../concepts/neural-surrogate-compilation.md).
- [High-level programs to approximate neural modules](../questions/high-level-programs-to-neural-surrogates.md).

