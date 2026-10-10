---
title: "The P versus NP Problem — Official Problem Description"
type: source
created: 2026-10-09
updated: 2026-10-09
status: active
sources: ["raw/cook-p-vs-np/document.txt"]
review: first-pass
---

# The P versus NP Problem — Official Problem Description

## Provenance and coverage

- Author: Stephen Cook. Publisher/host: Clay Mathematics Institute.
- [Official PDF](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf); linked from the [CMI problem page](https://www.claymath.org/millennium/p-vs-np/).
- Retrieved 2026-10-09. Publication date not established from the reviewed metadata; the upload path is not a reliable publication date.
- [Immutable browser text](../../raw/cook-p-vs-np/document.txt); [capture metadata](../../raw/cook-p-vs-np/capture.json). Numbered text coverage is 566/566 lines across two overlapping tool responses, not original PDF bytes.
- Review: definitions and principal implications in sections 1–3, especially printed pages 1–2, 4–5 and 8. Historical discussion and appendix captured/read for context; proofs and cited research were not independently audited.

## Summary and evidence

Defines P through worst-case running time bounded by a fixed polynomial in input length. Section 2, Proposition 1(c), states that putting an NP-complete language in P implies P=NP; SAT is an example. Section 3 explains why a superpolynomial Boolean-circuit-size lower bound for an NP-complete problem suffices to prove P≠NP: every language in P has a polynomial-size circuit family. These are stable definitions and conditional implications used in the wiki. [Evidence](../../raw/cook-p-vs-np/document.txt).

## Caveats

The document includes historical state-of-the-art remarks, which are not current survey evidence. In particular, it states primality is in P in section 2 while a later section retains an older contrary remark. Do not repeat those remarks as present-day facts. The circuit statement concerns sufficiently expressive Boolean circuits, not a lower bound for any chosen small neural architecture, and is not an algorithm for determining the asymptotic minimum.

## Connections and next question

- [Complexity scope](../concepts/complexity-limits.md).
- [Smallest networks, fastest algorithms and P versus NP](../questions/smallest-networks-fastest-algorithms-and-p-vs-np.md).
- [CMI overview](p-vs-np.md).

For a neural application, establish the circuit-to-network simulation and count weight precision, evaluation steps and uniform construction cost.

