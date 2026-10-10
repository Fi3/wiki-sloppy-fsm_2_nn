---
title: "MIT 6.004: Finite State Machines — 6.1 Annotated Slides"
type: source
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/mit-fsm-design/document.txt"]
review: first-pass
---

# MIT 6.004: Finite State Machines — 6.1 Annotated Slides

## Provenance and coverage

- Attribution: MIT OpenCourseWare, 6.004 Computation Structures, Spring 2017; section 6.1.
- [Supplied URL](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/).
- Retrieved: 2026-10-07.
- [Immutable extracted text](../../raw/mit-fsm-design/document.txt); [capture metadata](../../raw/mit-fsm-design/capture.json).
- Review: Text accompanying the annotated FSM slides, including transition and implementation explanations; image diagrams not independently inspected.
- Capture coverage: 819/819 browser text lines from https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/. Capture coverage is distinct from review coverage; original file bytes and linked assets were not downloaded. Text extraction can lose equations and figures.

## Summary

Explains clocked finite-state design as state storage plus combinational next-state/output logic. The transition specification must cover state/input combinations; output behavior may depend on state alone or state and current inputs. Examples show state diagrams, encoding choices and implementation concerns. [Evidence](../../raw/mit-fsm-design/document.txt).

## Relevance and next question

Write the reset, input-sampling and output-timing convention for the first machine before translating its combinational logic.

## Connections

- [exact fsm construction](../concepts/exact-fsm-construction.md).
- [Reading queue](../questions/reading-queue.md).

