---
title: "Fool's Gold: Extracting Finite State Machines from Recurrent Network Dynamics"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/fools-gold/document.txt"]
review: first-pass
---

# Fool's Gold: Extracting Finite State Machines from Recurrent Network Dynamics

## Provenance and coverage

- Attribution: John F. Kolen; NeurIPS 1993 proceedings, recovered official PDF.
- [Supplied URL](https://scispace.com/pdf/fool-s-gold-extracting-finite-state-machines-from-recurrent-4xbpf3yz7e.pdf).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/fools-gold/document.txt); [capture metadata](../../raw/fools-gold/capture.json).
- Review: Abstract and main cautionary discussion; text captured from the publisher, replacing the inaccessible SciSpace mirror. No experiments reproduced.
- Capture coverage: 271/271 browser text lines from https://proceedings.neurips.cc/paper_files/paper/1993/file/470e7a4f017a5476afb7eeb3f8b96f9b-Paper.pdf. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Warns that discretizing recurrent-network trajectories can yield misleading finite-state descriptions. Sensitivity to initial conditions and the measurement process can undermine the apparent extracted machine. Extraction quality therefore requires scrutiny beyond a plausible graph or agreement on observed trajectories. [Evidence](../../raw/fools-gold/document.txt).

## Relevance and next question

Define robustness and behavior-preservation checks before using an extracted FSM as evidence of the network's general behavior.

## Connections

- [learning vs construction](../concepts/learning-vs-construction.md).
- [Reading queue](../questions/reading-queue.md).

