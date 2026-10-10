---
title: "Disjoint-Support Decomposition and Extraction for Interconnect-Driven Threshold Logic Synthesis"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/threshold-interconnect-synthesis/document.txt"]
review: first-pass
---

# Disjoint-Support Decomposition and Extraction for Interconnect-Driven Threshold Logic Synthesis

## Provenance and coverage

- Attribution: Hao Chen, Shao-Chun Hung and Jie-Hong R. Jiang; DAC 2019.
- [Supplied URL](https://baloneymath.github.io/files/DAC19_thre.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/threshold-interconnect-synthesis/document.txt); [capture metadata](../../raw/threshold-interconnect-synthesis/capture.json).
- Review: Abstract, introduction and initial definitions/method sections; full evaluation not reviewed.
- Capture coverage: 362/618 browser text lines from https://baloneymath.github.io/files/DAC19_thre.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Develops disjoint-support decomposition and extraction for threshold logic synthesis, targeting interconnects as well as weight and threshold costs. It treats binary-output threshold circuits as a hardware model. Its optimization objectives may be relevant after constructing a transition circuit, but do not establish a particular runtime advantage. [Evidence](../../raw/threshold-interconnect-synthesis/document.txt).

## Relevance and next question

Inspect supported decomposition cases and benchmark costs; compare their gate model with the intended ReLU or threshold-network implementation.

## Connections

- [boolean circuit compilation](../concepts/boolean-circuit-compilation.md).
- [Reading queue](../questions/reading-queue.md).

