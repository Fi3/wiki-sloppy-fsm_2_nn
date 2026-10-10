---
title: "verilog2nn"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/verilog2nn/document.txt"]
review: first-pass
---

# verilog2nn

## Provenance and coverage

- Attribution: Enter-tainer/verilog2nn GitHub repository; README snapshot, commit not pinned.
- [Supplied URL](https://github.com/Enter-tainer/verilog2nn).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/verilog2nn/document.txt); [capture metadata](../../raw/verilog2nn/capture.json).
- Review: README pipeline, gate equations and test descriptions; claims are reported by the repository, not independently reproduced.
- Capture coverage: 276/276 browser text lines from https://github.com/Enter-tainer/verilog2nn. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Describes a combinational Verilog-to-PyTorch flow using Yosys, AND/NOT netlists, topological layers and sparse linear/ReLU operations. Gate identities are intended for Boolean inputs. The README reports equivalence tests, including an exhaustive small adder. Sequential state, reset and cycle timing require additional design. [Evidence](../../raw/verilog2nn/document.txt).

## Relevance and next question

Inspect source and tests before adoption; develop a state-register wrapper separately. No repository code has been installed or executed in this wiki.

## Connections

- [boolean circuit compilation](../concepts/boolean-circuit-compilation.md).
- [Reading queue](../questions/reading-queue.md).

