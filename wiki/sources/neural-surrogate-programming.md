---
title: "Programming with Neural Surrogates of Programs"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/neural-surrogate-programming/document.txt"]
review: first-pass
---

# Programming with Neural Surrogates of Programs

## Provenance and coverage

- Authors: Alex Renda, Yi Ding and Michael Carbin.
- Publication: Onward! 2021; arXiv submission 2021-12-12.
- [Original source](https://arxiv.org/abs/2112.06148). Retrieved 2026-10-07.
- [Immutable browser extraction](../../raw/neural-surrogate-programming/document.txt); [capture metadata](../../raw/neural-surrogate-programming/capture.json). These are extracted text, not original file bytes.
- Reviewed scope: arXiv abstract and bibliographic metadata only; the full paper and simulator implementation were not reviewed.
- Numbered browser coverage: 171/171 lines. Text coverage does not imply proof or figure review.

## Summary

Organizes programming with neural surrogates into three patterns: compilation deploys a model in place of the original program; adaptation retrains that model for a different task; optimization uses the differentiable model to find inputs that are then run through the original program.

## Main claims and relevance

The abstract describes case studies on a CPU simulator and a shared methodology for these workflows. Surrogate compilation is the category most directly matching the user's request. [Captured evidence](../../raw/neural-surrogate-programming/document.txt).

## Limits and remaining review

This abstract does not establish a general efficient mapping for all bounded-memory programs. Reported case-study results have not been reproduced, and details of model partitioning and composition need full-paper review.

## Connections

- [Neural surrogate compilation](../concepts/neural-surrogate-compilation.md).
- [High-level programs to approximate neural modules](../questions/high-level-programs-to-neural-surrogates.md).

