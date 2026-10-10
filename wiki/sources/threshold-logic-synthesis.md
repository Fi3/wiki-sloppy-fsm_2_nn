---
title: "Effective Logic Synthesis for Threshold Logic Circuit Design"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/threshold-logic-synthesis/document.txt"]
review: first-pass
---

# Effective Logic Synthesis for Threshold Logic Circuit Design

## Provenance and coverage

- Attribution: Augusto Neutzling, Jody Maick Matos, Alan Mishchenko, Andre Reis and Renato P. Ribas; IEEE TCAD, May 2019.
- [Supplied URL](https://people.eecs.berkeley.edu/~alanmi/publications/2019/tcad19_thresh.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/threshold-logic-synthesis/document.txt); [capture metadata](../../raw/threshold-logic-synthesis/capture.json).
- Review: Abstract, introduction and early method sections; complete evaluation not reviewed.
- Capture coverage: 389/894 browser text lines from https://people.eecs.berkeley.edu/~alanmi/publications/2019/tcad19_thresh.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Proposes identifying threshold functions during technology mapping, including redundant cuts and cost models based on gate counts, fan-in and weight/threshold values. Reported area/depth reductions concern the evaluated synthesis flow. Those hardware costs cannot be assumed to equal software neural-inference costs. [Evidence](../../raw/threshold-logic-synthesis/document.txt).

## Relevance and next question

Compare gate-library assumptions and cost models with the intended network before reusing this optimization approach.

## Connections

- [boolean circuit compilation](../concepts/boolean-circuit-compilation.md).
- [Reading queue](../questions/reading-queue.md).

