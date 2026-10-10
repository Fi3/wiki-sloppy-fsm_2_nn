---
title: "IREE CPU Deployment"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/iree-cpu/document.txt"]
review: first-pass
---

# IREE CPU Deployment

## Provenance and coverage

- Attribution: IREE official deployment guide; rolling documentation captured 2026-10-07.
- [Supplied URL](https://iree.dev/guides/deployment-configurations/cpu/).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/iree-cpu/document.txt); [capture metadata](../../raw/iree-cpu/capture.json).
- Review: CPU overview, executable formats, runtime devices and workflow; examples not executed.
- Capture coverage: 435/435 browser text lines from https://iree.dev/guides/deployment-configurations/cpu/. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Describes CPU compilation targets, executable formats and runtime devices. The guide distinguishes asynchronous multithreaded local-task execution from synchronous local-sync execution, and documents compiler/runtime steps. Target settings and scheduling choices affect deployment behavior. [Evidence](../../raw/iree-cpu/document.txt).

## Relevance and next question

Benchmark both compilation and runtime configurations on the intended CPU and workload; the guide provides no performance measurement for this wiki's FSMs.

## Connections

- [compiler pipeline](../concepts/compiler-pipeline.md).
- [Reading queue](../questions/reading-queue.md).

