# Activity log

Append entries in chronological order. Preserve existing entries.

## [2026-10-07] setup | Initialize the local LLM wiki

- Created immutable-source and compiled-wiki directories, agent instructions, page templates, and local bookkeeping tools.
- Added the [index](index.md), [overview](overview.md), and [synthesis](synthesis.md).
- The user set the focus to finite state machines to neural networks; tailored the overview and ingestion guidance accordingly.
- No domain sources have been ingested. The first source and specific machine/network models remain open.

## [2026-10-07] ingest | First pass of the user's 35-URL reading batch

- Preserved the [canonical user list](../raw/reading-list-original-order.md) and created the [complete reading queue](questions/reading-queue.md). The initial raw capture grouped URLs despite its original-order label; preserved it unchanged and added a corrected canonical copy.
- Merged the confirmed ICLR 2026 PDF/abstract pair into one catalog entry. Unknown documents may contain further duplicates; no assumption made about their identity.
- Captured browser-extracted text for 30 sources, each with checksum and line-coverage metadata. Direct shell downloading was unavailable, so these are extracted snapshots rather than original PDF/HTML bytes.
- Added 30 source summaries with explicit first-pass review scopes. Recovered the Fool's Gold paper from the official publisher, PyTorch documentation through resolved paths, and TENSORIZE's abstract from the university publication page.
- Recorded four unresolved access/extraction cases in the [retrieval report](../raw/retrieval-report-2026-10-07.md): BYU, Caltech, ScienceDirect, and the unreadable GGM text layer.
- Integrated evidence into [exact construction](concepts/exact-fsm-construction.md), [state encoding](concepts/state-encoding.md), [weighted automata](concepts/weighted-automata.md), [Boolean compilation](concepts/boolean-circuit-compilation.md), [learning/extraction](concepts/learning-vs-construction.md), [compiler deployment](concepts/compiler-pipeline.md), and [complexity scope](concepts/complexity-limits.md).
- Updated the [overview](overview.md), [synthesis](synthesis.md), and [index](index.md); saved a proposed [research roadmap](questions/research-roadmap.md).
- Remaining work includes full-paper/proof/figure review, access recovery, selecting an example machine, and reproducing a construction. No project neural implementation or benchmark has been executed.

## [2026-10-07] lint | Validate the first reading batch

- Structural lint checked 43 pages, imported-source checksums, required metadata, local links, catalog coverage, and content-page incoming links: zero errors and zero warnings.
- Reviewed claims for scope: separate construction, training and extraction; restrict gate identities to Boolean inputs; retain timing, architecture and precision caveats; distinguish source-reported tests from reproduced project results.
- Helper regression tests passed. This maintenance pass does not establish source theorem correctness or experimental reproducibility.

## [2026-10-07] query | FSM size versus neural-network synapse count

- The user defined neural-network size as the number of synapses. Saved a [size analysis](questions/fsm-size-vs-synapses.md), distinguishing fixed-method bounds, optimal representations and statistical correlation.
- Derived a sparse one-hot Mealy step network with $4nk$ nonzero weighted connections, excluding biases and separately counted state-copy wiring. Derived a structured unary cyclic-counter example with $O(\log n)$ connections when combinational depth may grow within a machine step.
- Checked the first equations exhaustively over 256 two-state binary Mealy tables (1,024 step cases) and checked ripple increment over all states for bit widths 1–8. These validate formulas, not a deployed compiler or optimality/performance claims.
- Rechecked source definitions for nonzero weights, fan-in and network-model restrictions; preserved original proof/OCR caveats. Updated [state encoding](concepts/state-encoding.md), the [synthesis](synthesis.md), and [index](index.md).

## [2026-10-07] query | Efficient methods, function matrices and network layers

- Saved [efficient methods and matrix mapping](questions/efficient-methods-and-matrix-mapping.md), comparing synapse-oriented Boolean/threshold construction with direct matrix/tensor recurrence without claiming a universal efficiency winner.
- Rechecked the official ICLR 2025 paper's sections 2.1–2.2 and opening of 3.1. Recorded its Heaviside activation, local linear readouts, parallel scheduling, relay requirement and $2d$ versus $d+1$ depth formulas; retained first-pass proof/experiment limits.
- Derived explicit matrices for parallel/dependent AND functions, XOR, parity transitions and the fixed-weight one-hot FSM cell. Exhaustive checks passed for 1,024 FSM step cases and every binary input to the gate examples.
- Updated Boolean compilation, weighted automata, the synthesis, source review scope and index. No deployed compiler, global optimality result or hardware benchmark was produced.
- Structural lint checked 45 wiki pages with zero errors and zero warnings.

## [2026-10-07] query | High-level pure programs to approximate neural modules

- The user permitted a lossy transformation from bounded-memory high-level code, suggesting reusable networks per function. Saved [the analysis](questions/high-level-programs-to-neural-surrogates.md) and a [surrogate-compilation concept](concepts/neural-surrogate-compilation.md), keeping this error-based contract distinct from prior exact constructions.
- Researched and imported five new immutable browser snapshots with checksums and coverage metadata: Parrot, Programming with Neural Surrogates, Turaco, CompNet and Cajal. Added explicitly scoped first-pass summaries; complete arXiv abstract pages do not imply full-paper review.
- Recovered Parrot's author-hosted PDF and Turaco's PDF after its HTML retrieval failed. Direct Cajal publisher opens failed; its arXiv abstract and primary publisher bibliographic excerpt surfaced in search support the limited notes. No missing paper content was inferred.
- Compared training from executable examples with learned source-to-weights generation, function versus region partitioning, whole-loop versus body replacement, shared weights and composed/sequence error. Updated the learning distinction, synthesis and index. No model training, deployed compiler or new performance experiment was performed.
- Structural lint checked 52 wiki pages with zero errors and zero warnings; imported snapshot integrity and local links passed.

## [2026-10-09] query | Correct the recap on minimum size, training and exact compilation

- Extended the existing [methods analysis](questions/efficient-methods-and-matrix-mapping.md) with a corrected recap rather than creating a duplicate question page.
- Rechecked primary abstracts for multi-output circuit minimization, ReLU training hardness and Cajal, plus the direct FSM tensor formulation. Preserved proof-review limitations; no new full-paper audit was claimed.
- Clarified the polynomial-time/global-optimum condition and the need for a matching reduction. Recorded why the collection's randomized circuit-minimization reduction alone does not establish P=NP, or automatically transfer to neural synapse minimization.
- Distinguished training as a practical approximate route from a universal optimal method. Added a direct exact one-unit ReLU toggle derivation and the assumptions for its connection count.
- Updated [complexity scope](concepts/complexity-limits.md), the surrogate analysis, synthesis and index; retained original raw snapshots unchanged. No model training or performance benchmark was performed.
- Structural lint checked 52 wiki pages with zero errors and zero warnings.

## [2026-10-09] query | Smallest neural network versus fastest algorithm and P versus NP

- Saved [the follow-up analysis](questions/smallest-networks-fastest-algorithms-and-p-vs-np.md), distinguishing synapses from depth, recurrent steps, bit cost and construction time; separated FSM state count from growing input-instance length.
- Imported Cook's official problem description and two Blais circuit lectures as two new immutable source records with checksums and coverage metadata. Cook's 566 numbered text lines and both lecture text extractions were captured completely; text completeness does not imply independent proof or figure verification.
- Recorded the actual complexity connection: uniform polynomial-time SAT construction/evaluation would imply P=NP, while a sufficiently general superpolynomial circuit-size lower bound for an NP-complete problem would imply P≠NP. Kept these conditional statements separate from finite exact minimization and from the collection's randomized circuit-minimization reduction.
- Added an elementary circuit enumeration argument to show why an optimizer's existence alone does not decide asymptotic growth. Updated complexity scope, the earlier methods note, synthesis and index; no new minimizer, benchmark or complexity theorem was produced.
- Structural lint checked 55 wiki pages with zero errors and zero warnings; source checksums and links passed.

## [2026-10-10] setup | Prepare the initial portable Git snapshot

- Updated the [README](../README.md) to identify this as a test wiki for the user's website, with nothing interesting expected, and added instructions for cloning and using it on another PC.
- Defined the snapshot to include sources and provenance, wiki pages, agent instructions, templates, helper scripts, tests, and shared Obsidian settings. Added Git attributes to preserve source bytes and checksums across operating systems, and ignored local agent directories and the exported bundle.
- Direct initialization in the workspace was blocked because `.git/` is read-only in this environment. Initialized a separate temporary repository for exporting the first commit as `rsm-2-nn.bundle`; the README explains how to clone the bundle into a normal working repository.
- Structural lint checked 55 wiki pages with zero errors and zero warnings. All nine existing helper tests passed.
