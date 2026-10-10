---
title: "Turaco: Complexity-Guided Data Sampling for Training Neural Surrogates of Programs"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/turaco-complexity-guided-sampling/document.txt"]
review: first-pass
---

# Turaco: Complexity-Guided Data Sampling for Training Neural Surrogates of Programs

## Provenance and coverage

- Authors: Alex Renda, Yi Ding and Michael Carbin.
- Publication: OOPSLA2 2023, PACMPL 7, article 280.
- [Original source](https://arxiv.org/pdf/2309.11726). Retrieved 2026-10-07.
- [Immutable browser extraction](../../raw/turaco-complexity-guided-sampling/document.txt); [capture metadata](../../raw/turaco-complexity-guided-sampling/capture.json). These are extracted text, not original file bytes.
- Reviewed scope: Abstract, introduction and worked example (sections 1–2), plus the captured opening definitions of section 3.1. Later analysis proofs, language details, evaluation and appendices were not audited.
- Numbered browser coverage: 343/4169 lines. Text coverage does not imply proof or figure review.

## Summary

Uses source-program execution paths to guide training-data allocation. It models a program as a stratified function and trains a separate surrogate for each stratum; runtime uses the original path conditions to choose the appropriate surrogate.

## Main claims and relevance

Sections 1.3 and 2 combine path frequency with a bound on path learning complexity to allocate samples. Their analysis targets stratified analytic functions. This supplies a concrete alternative to one neural network per named function: preserve branch selection and learn the numerical behavior within paths. [Captured evidence](../../raw/turaco-complexity-guided-sampling/document.txt).

## Limits and remaining review

Its language and theoretical assumptions restrict the applicable functions. The introduction reports both successful experiments and classes where the sampling policy worsens error. It is not a universal sample-selection or program-compression guarantee.

## Connections

- [Neural surrogate compilation](../concepts/neural-surrogate-compilation.md).
- [High-level programs to approximate neural modules](../questions/high-level-programs-to-neural-surrogates.md).

