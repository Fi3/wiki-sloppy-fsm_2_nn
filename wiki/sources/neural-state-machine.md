---
title: "Learning by Abstraction: The Neural State Machine"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/neural-state-machine/document.txt"]
review: first-pass
---

# Learning by Abstraction: The Neural State Machine

## Provenance and coverage

- Attribution: Drew A. Hudson and Christopher D. Manning; NeurIPS 2019, arXiv PDF snapshot v4 dated 2019-11-25.
- [Supplied URL](https://arxiv.org/pdf/1907.03950).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/neural-state-machine/document.txt); [capture metadata](../../raw/neural-state-machine/capture.json).
- Review: Abstract, introduction and beginning of related work; full architecture/evaluation not reviewed.
- Capture coverage: 114/883 browser text lines from https://arxiv.org/pdf/1907.03950. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Proposes a visual-reasoning model that predicts a probabilistic scene graph and traverses it using question-derived soft instructions. Its states represent objects in a learned graph. The term neural state machine here does not establish a general exact compiler for a supplied symbolic FSM. [Evidence](../../raw/neural-state-machine/document.txt).

## Relevance and next question

Read the architecture/evaluation if learned semantic graph traversal is relevant; keep its task and state semantics separate from deterministic transducers.

## Connections

- [learning vs construction](../concepts/learning-vs-construction.md).
- [Reading queue](../questions/reading-queue.md).

