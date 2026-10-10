---
title: "Reading queue and access status"
type: question
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/reading-list-original-order.md", "raw/retrieval-report-2026-10-07.md"]
---

# Reading queue and access status

## Intake

The user supplied **35 URLs, cataloged as 34 entries after merging one confirmed duplicate pair**: the ICLR 2026 PDF and abstract are one work. **30 entries have first-pass summaries; four remain unresolved.** The unresolved documents could contain additional duplicates, so their identity is not assumed. Every supplied URL appears below, in its original order. [Canonical supplied list](../../raw/reading-list-original-order.md), [access report](../../raw/retrieval-report-2026-10-07.md).

“First pass” means initial claims, relevance and limitations have been filed. It does not mean every page, proof, figure, linked notebook or experiment was reviewed. Each source summary states its review scope. Original PDFs/HTML bytes could not be downloaded through the local shell; raw evidence is preserved as browser-extracted text, with checksums and explicit coverage metadata.

## Suggested reading order

This prioritization is our interpretation of relevance to the user's goal:

1. [MIT's FSM design](../sources/mit-fsm-design.md): specify behavior and timing.
2. [Differentiable FSM](../sources/differentiable-fsm.md) and [verilog2nn](../sources/verilog2nn.md): compare concrete tensor and Boolean-circuit routes.
3. [Alon–Dewdney–Ott](../sources/efficient-fsm-simulation.md) and [Horne–Hush](../sources/fsm-rnn-complexity.md): inspect recurrent constructions, assumptions and size bounds.
4. [Rabusseau–Li–Precup](../sources/spectral-wfa-rnn.md) and [Kiefer](../sources/weighted-automata-equivalence.md): formalize weighted/tensor recurrence and equivalence.
5. [Svete–Chan–Cotterell](../sources/regular-languages-rnns.md): investigate when structured state compression applies.
6. Study [Boolean/threshold optimization](../concepts/boolean-circuit-compilation.md), then [deployment](../concepts/compiler-pipeline.md) once the target construction is specified.
7. Use [learning/extraction](../concepts/learning-vs-construction.md) and [complexity background](../concepts/complexity-limits.md) to bound claims and develop validation.

## Complete supplied inventory

| # | Resource and supplied URL | Track | Review/access status |
| --- | --- | --- | --- |
| 1 | [Notes on Equivalence and Minimization of Weighted Automata](../sources/weighted-automata-equivalence.md) · [URL](https://arxiv.org/html/2009.01217v1) | Weighted/tensor recurrence | First pass: text captured; review scope in summary |
| 2 | [An Exact Poly-Time Membership-Queries Algorithm for Extracting a Three-Layer ReLU Network](../sources/relu-membership-query-extraction.md) · [URL](https://arxiv.org/html/2105.09673v5) | Complexity background | First pass: partial capture/review |
| 3 | [On Efficiently Representing Regular Languages as RNNs](../sources/regular-languages-rnns.md) · [URL](https://arxiv.org/html/2402.15814v2) | Representation and encoding | First pass: partial capture/review |
| 4 | [Quantum Lower Bounds by Polynomials](../sources/quantum-lower-bounds.md) · [URL](https://arxiv.org/pdf/quant-ph/9802049) | Complexity background | First pass: partial capture/review |
| 5 | [BYU vanhorn_6.pdf — title unverified](https://axon.cs.byu.edu/papers/vanhorn_6.pdf) | Unclassified until readable | Unresolved: 502; needs accessible copy |
| 6 | [Disjoint-Support Decomposition and Extraction for Interconnect-Driven Threshold Logic Synthesis](../sources/threshold-interconnect-synthesis.md) · [URL](https://baloneymath.github.io/files/DAC19_thre.pdf) | Boolean/threshold synthesis | First pass: partial capture/review |
| 7 | [torch.export IR Specification](../sources/pytorch-export-ir.md) · [URL](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/export/ir_spec.html) | Compilation and deployment | First pass: text captured; review scope in summary |
| 8 | [torch.fx](../sources/pytorch-fx.md) · [URL](https://docs.pytorch.org/docs/stable/fx.html) | Compilation and deployment | First pass: resolved documentation |
| 9 | [torch.compiler](../sources/pytorch-compiler.md) · [URL](https://docs.pytorch.org/docs/stable/torch.compiler.html) | Compilation and deployment | First pass: resolved documentation |
| 10 | [NP-Hardness of Circuit Minimization for Multi-Output Functions](../sources/multi-output-circuit-minimization.md) · [URL](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2020.22) | Complexity background | First pass: text captured; review scope in summary |
| 11 | [Tight Hardness Results for Training Depth-2 ReLU Networks](../sources/relu-training-hardness.md) · [URL](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.22) | Complexity background | First pass: text captured; review scope in summary |
| 12 | [Torch-MLIR Architecture](../sources/torch-mlir-architecture.md) · [URL](https://github.com/llvm/torch-mlir/blob/main/docs/architecture.md) | Compilation and deployment | First pass: text captured; review scope in summary |
| 13 | [IREE CPU Deployment](../sources/iree-cpu.md) · [URL](https://iree.dev/guides/deployment-configurations/cpu/) | Compilation and deployment | First pass: text captured; review scope in summary |
| 14 | [IREE PyTorch Integration](../sources/iree-pytorch.md) · [URL](https://iree.dev/guides/ml-frameworks/pytorch/) | Compilation and deployment | First pass: text captured; review scope in summary |
| 15 | [Auto-Vectorization in LLVM](../sources/llvm-vectorizers.md) · [URL](https://llvm.org/docs/Vectorizers.html) | Compilation and deployment | First pass: text captured; review scope in summary |
| 16 | [Linalg Dialect Rationale: The Case For Compiler-Friendly Custom Operations](../sources/mlir-linalg.md) · [URL](https://mlir.llvm.org/docs/Rationale/RationaleLinalgDialect/) | Compilation and deployment | First pass: text captured; review scope in summary |
| 17 | [MIT 6.004: Finite State Machines — 6.1 Annotated Slides](../sources/mit-fsm-design.md) · [URL](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/) | Direct construction | First pass: text captured; review scope in summary |
| 18 | [Effective Logic Synthesis for Threshold Logic Circuit Design](../sources/threshold-logic-synthesis.md) · [URL](https://people.eecs.berkeley.edu/~alanmi/publications/2019/tcad19_thresh.pdf) | Boolean/threshold synthesis | First pass: partial capture/review |
| 19 | [Optimizing Neural Network Representations of Boolean Networks](../sources/boolean-network-optimization.md) · [URL](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f67852b3910e3aba21c951849b4531a6-Abstract-Conference.html) | Boolean/threshold synthesis | First pass: partial capture/review |
| 20 | [Tractability via Low Dimensionality: The Parameterized Complexity of Training Quantized Neural Networks](../sources/quantized-network-training.md) · [URL](https://proceedings.iclr.cc/paper_files/paper/2026/file/bf1b3f86d67feecdc22c1abea2c6127c-Paper-Conference.pdf) | Complexity background | First pass: partial capture/review |
| 21 | [Tractability via Low Dimensionality: The Parameterized Complexity of Training Quantized Neural Networks](../sources/quantized-network-training.md) · [URL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bf1b3f86d67feecdc22c1abea2c6127c-Abstract-Conference.html) | Complexity background | Duplicate URL — see #20 |
| 22 | [Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning](../sources/spectral-wfa-rnn.md) · [URL](https://proceedings.mlr.press/v89/rabusseau19a.html) | Weighted/tensor recurrence | First pass: partial capture/review |
| 23 | [Bounds on the Complexity of Recurrent Neural Network Implementations of Finite State Machines](../sources/fsm-rnn-complexity.md) · [URL](https://proceedings.neurips.cc/paper/1993/file/afda332245e2af431fb7b672a68b659d-Paper.pdf) | Representation and encoding | First pass: text captured; review scope in summary |
| 24 | [Caltech 070708.pdf — title unverified](https://users.cms.caltech.edu/~dave/presentations/070708.pdf) | Unclassified until readable | Unresolved: timeout; needs accessible copy |
| 25 | [DnD: A Cross-Architecture Deep Neural Network Decompiler](../sources/dnd-decompiler.md) · [URL](https://wuruoyu.github.io/assets/pdf/dnd.pdf) | Compilation and deployment | First pass: partial capture/review |
| 26 | [P vs NP](../sources/p-vs-np.md) · [URL](https://www.claymath.org/millennium/p-vs-np/) | Complexity background | First pass: text captured; review scope in summary |
| 27 | [A Pseudorandom Generator from Any One-Way Function](../sources/hill-pseudorandom-generators.md) · [URL](https://www.cs.bu.edu/fac/lnd/pdf/hill.pdf) | Complexity background | First pass: partial capture/review |
| 28 | [Efficient Simulation of Finite Automata by Neural Nets](../sources/efficient-fsm-simulation.md) · [URL](https://www.cs.tau.ac.il/~nogaa/PDFS/Publications/Efficient%20simulations%20of%20finite%20automata%20by%20neural%20nets.pdf) | Direct construction | First pass: text captured; review scope in summary |
| 29 | [TENSORIZE: Fast Synthesis of Tensor Programs from Legacy Code using Symbolic Tracing, Sketching and Solving](../sources/tensorize.md) · [URL](https://www.pure.ed.ac.uk/ws/portalfiles/portal/493345271/BrauckmannEtalCGO2025TENSORIZEFastSynthesisofTensorPrograms.pdf) | Compilation and deployment | First pass: university abstract; PDF pending |
| 30 | [ScienceDirect PII 0893608094900825 — title unverified](https://www.sciencedirect.com/science/article/abs/pii/0893608094900825) | Unclassified until readable | Unresolved: access failure / 403 |
| 31 | [GGM PDF — title/content not verified](https://www.wisdom.weizmann.ac.il/~oded/X/ggm.pdf) | Unclassified until readable | Unresolved: zero extracted lines; needs OCR/copy |
| 32 | [Differentiable Finite State Machines](../sources/differentiable-fsm.md) · [URL](https://google-research.github.io/self-organising-systems/2022/diff-fsm/) | Learning and extraction | First pass: text captured; review scope in summary |
| 33 | [Learning by Abstraction: The Neural State Machine](../sources/neural-state-machine.md) · [URL](https://arxiv.org/pdf/1907.03950) | Learning and extraction | First pass: partial capture/review |
| 34 | [Fool's Gold: Extracting Finite State Machines from Recurrent Network Dynamics](../sources/fools-gold.md) · [URL](https://scispace.com/pdf/fool-s-gold-extracting-finite-state-machines-from-recurrent-4xbpf3yz7e.pdf) | Learning and extraction | First pass: recovered publisher PDF |
| 35 | [verilog2nn](../sources/verilog2nn.md) · [URL](https://github.com/Enter-tainer/verilog2nn) | Boolean/threshold synthesis | First pass: text captured; review scope in summary |

## Unresolved access

- BYU: exact title and contents still unknown after failed retrieval/search.
- Caltech: exact title and contents still unknown after repeated timeouts.
- ScienceDirect: access failure; no title or abstract verified.
- GGM: PDF recognized, but no extractable text or inspectable screenshot was returned. OCR or an extractable copy is needed.

Do not mark these four ingested based on filenames or secondary citations. Recover their content before drawing conclusions.

## Next substantive work

Choose a first machine and construction route using the [research roadmap](research-roadmap.md). Deep-read the relevant construction/proof sections, fill incomplete captures, and reproduce an equivalence experiment. This queue tracks remaining work; first-pass summaries are useful starting points rather than completed technical audits.
