---
title: "DnD: A Cross-Architecture Deep Neural Network Decompiler"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/dnd-decompiler/document.txt"]
review: first-pass
---

# DnD: A Cross-Architecture Deep Neural Network Decompiler

## Provenance and coverage

- Attribution: Ruoyu Wu, Taegyu Kim, Dave (Jing) Tian, Antonio Bianchi and Dongyan Xu; publication date not verified from reviewed extract.
- [Supplied URL](https://wuruoyu.github.io/assets/pdf/dnd.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/dnd-decompiler/document.txt); [capture metadata](../../raw/dnd-decompiler/capture.json).
- Review: Abstract and introduction/early system material; evaluation and complete recovery guarantees not reviewed.
- Capture coverage: 378/1674 browser text lines from https://wuruoyu.github.io/assets/pdf/dnd.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Recovers high-level DNN representations from compiled binaries using symbolic execution, loop analysis and operator-template matching. The paper reports evaluations across selected compilers and instruction sets. It concerns reversing compiled neural programs, rather than compiling arbitrary programs into neural networks. [Evidence](../../raw/dnd-decompiler/document.txt).

## Relevance and next question

Inspect operation coverage and assumptions before applying its lifting ideas to a new compiler or to state-machine logic.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

