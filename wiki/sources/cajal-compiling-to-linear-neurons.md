---
title: "Compiling to Linear Neurons"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/cajal-compiling-to-linear-neurons/document.txt"]
review: first-pass
---

# Compiling to Linear Neurons

## Provenance and coverage

- Authors: Joey Velez-Ginorio, Nada Amin, Konrad Kording and Steve Zdancewic.
- Publication: arXiv submission 2025-11-14; primary publisher bibliographic excerpt lists PACMPL 10, POPL, article 35, published 2026-01-08, DOI 10.1145/3776677.
- [Original source](https://arxiv.org/abs/2511.13769). Retrieved 2026-10-07.
- [Immutable browser extraction](../../raw/cajal-compiling-to-linear-neurons/document.txt); [capture metadata](../../raw/cajal-compiling-to-linear-neurons/capture.json). These are extracted text, not original file bytes.
- Reviewed scope: arXiv abstract and metadata, plus publisher bibliographic/opening excerpt surfaced in search. Direct publisher opens failed; the compiler proof and full experiments were not audited.
- Numbered browser coverage: 164/164 lines. Text coverage does not imply proof or figure review.

## Summary

Introduces Cajal, a restricted typed, higher-order linear programming language, and states a correctness result for compiling its programs to linear neurons. It links compiled components with learned networks to specify part of a model's behavior before training.

## Main claims and relevance

The abstract motivates combining discrete programmed structure with differentiable learning, and reports improvements in learning and data efficiency in its experiments. This is an adjacent hybrid route, rather than lossy replacement of every ordinary-language function. [Captured evidence](../../raw/cajal-compiling-to-linear-neurons/document.txt).

## Limits and remaining review

Linear typing imposes restrictions beyond ordinary purity. The abstract does not justify compiling arbitrary loops, mutable arrays or an unrestricted bounded-memory language. Claims about proofs and learning improvements remain source-reported here.

## Connections

- [Neural surrogate compilation](../concepts/neural-surrogate-compilation.md).
- [High-level programs to approximate neural modules](../questions/high-level-programs-to-neural-surrogates.md).

