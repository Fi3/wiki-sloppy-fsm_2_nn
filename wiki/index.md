# Wiki index

Research focus: **finite state machines → neural networks**. The first intake contains 35 URLs / 34 catalog entries after one confirmed duplicate pair was merged: 30 first-pass source summaries and four unresolved access/extraction cases. Review scope is recorded on every source page.

A subsequent query added five first-pass sources on neural surrogate programming, function replacement and source-to-network compilation.

Two further source notes cover Cook's official P-versus-NP description and circuit/nonuniform computation lectures.

## Navigation

- [Overview](overview.md) — Scope and research goals.
- [Current synthesis](synthesis.md) — Candidate routes, limits and unresolved questions.
- [Activity log](log.md) — Chronological history of changes.

## Questions and analyses

- [Reading queue and access status](questions/reading-queue.md) — Every supplied URL, priorities and remaining review work.
- [Research roadmap](questions/research-roadmap.md) — Proposed first equivalence experiment; no implementation yet.
- [FSM size versus synapse count](questions/fsm-size-vs-synapses.md) — Method-dependent connection bounds, an explicit linear construction and a compact counter example.
- [Efficient methods and matrix mapping](questions/efficient-methods-and-matrix-mapping.md) — Synapse-oriented candidates, explicit matrices, layers and corrections about exactness versus optimality.
- [High-level programs to neural surrogates](questions/high-level-programs-to-neural-surrogates.md) — Lossy function/module replacement, related research, loop choices and composition error.
- [Smallest networks versus fastest algorithms](questions/smallest-networks-fastest-algorithms-and-p-vs-np.md) — Circuit size, runtime, uniformity and what would actually settle P versus NP.

## Concepts

- [Exact FSM construction](concepts/exact-fsm-construction.md) — Behavior, timing and a proposed step-equivalence obligation.
- [State encoding and construction cost](concepts/state-encoding.md) — Separate storage size from transition complexity and compare assumptions.
- [Weighted automata and second-order recurrence](concepts/weighted-automata.md) — Matrix semantics, tensor updates and architecture restrictions.
- [Boolean circuits as neural networks](concepts/boolean-circuit-compilation.md) — Gate mappings, synthesis objectives and the sequential-wrapper gap.
- [Construction, learning and extraction](concepts/learning-vs-construction.md) — Keep task definitions and guarantees distinct.
- [Neural surrogate compilation](concepts/neural-surrogate-compilation.md) — Train or generate function replacements from executions and source code.
- [Tensor-program capture, lowering and deployment](concepts/compiler-pipeline.md) — Map tool roles and define performance checks.
- [Complexity claims and their scope](concepts/complexity-limits.md) — Interpret hardness and tractability under their actual models.

## Sources

All summaries below are first-pass notes. Capture completeness does not imply full proof, figure or experimental review.

### Program surrogates and hybrid compilation

- [Neural Acceleration / Parrot](sources/parrot-neural-acceleration.md) — Trains replacements for selected pure, fixed-interface functions, including regions with loops and calls.
- [Programming with Neural Surrogates](sources/neural-surrogate-programming.md) — Classifies surrogate compilation, adaptation and optimization workflows.
- [Turaco](sources/turaco-complexity-guided-sampling.md) — Uses execution-path complexity and frequency to guide training-data allocation for stratified surrogates.
- [Learning to Compile Programs / CompNet](sources/compnet-neural-surrogate-compilation.md) — Generates surrogate weights from numeric C source using a hypernetwork, followed by fine-tuning.
- [Compiling to Linear Neurons / Cajal](sources/cajal-compiling-to-linear-neurons.md) — Compiles a restricted typed linear language and combines its neurons with learned models.

### Weighted/tensor recurrence

- [Notes on Equivalence and Minimization of Weighted Automata](sources/weighted-automata-equivalence.md) — Presents weighted automata over a field through linear algebra.
- [Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning](sources/spectral-wfa-rnn.md) — Connects weighted finite automata to second-order recurrent networks with linear activations on discrete-symbol sequences.

### Complexity background

- [The P versus NP Problem — Cook's official description](sources/cook-p-vs-np.md) — Formal time complexity, NP-completeness and the circuit-lower-bound approach.
- [Boolean circuits and nonuniform computation — Blais lectures](sources/circuits-and-nonuniform-computation.md) — Size versus depth, polynomial-size families and P/poly.
- [An Exact Poly-Time Membership-Queries Algorithm for Extracting a Three-Layer ReLU Network](sources/relu-membership-query-extraction.md) — Studies reconstructing ReLU networks using black-box queries.
- [Quantum Lower Bounds by Polynomials](sources/quantum-lower-bounds.md) — Uses polynomial methods to bound quantum query complexity of Boolean functions, distinguishing total functions from promise problems.
- [NP-Hardness of Circuit Minimization for Multi-Output Functions](sources/multi-output-circuit-minimization.md) — The proceedings abstract reports NP-hardness of minimizing general multi-output Boolean circuits under polynomial-time randomized many-one reductions.
- [Tight Hardness Results for Training Depth-2 ReLU Networks](sources/relu-training-hardness.md) — The abstract establishes worst-case hardness for fitting depth-two ReLU networks under squared loss, including a single-ReLU case.
- [Tractability via Low Dimensionality: The Parameterized Complexity of Training Quantized Neural Networks](sources/quantized-network-training.md) — Studies ReLU training with parameters and data restricted to finite integer domains.
- [P vs NP](sources/p-vs-np.md) — Introduces the distinction between efficiently checking a proposed solution and efficiently finding one, and lists P versus NP as unsolved.
- [A Pseudorandom Generator from Any One-Way Function](sources/hill-pseudorandom-generators.md) — Shows how to construct a pseudorandom generator from any one-way function, linking the existence of the two primitives.

### Representation and encoding

- [On Efficiently Representing Regular Languages as RNNs](sources/regular-languages-rnns.md) — Studies efficient RNN representations of language models using bounded pushdown automata.
- [Bounds on the Complexity of Recurrent Neural Network Implementations of Finite State Machines](sources/fsm-rnn-complexity.md) — Studies neuron complexity of threshold-network FSM implementations under restrictions on weights, thresholds and fan-in.

### Boolean/threshold synthesis

- [Disjoint-Support Decomposition and Extraction for Interconnect-Driven Threshold Logic Synthesis](sources/threshold-interconnect-synthesis.md) — Develops disjoint-support decomposition and extraction for threshold logic synthesis, targeting interconnects as well as weight and threshold costs.
- [Effective Logic Synthesis for Threshold Logic Circuit Design](sources/threshold-logic-synthesis.md) — Proposes identifying threshold functions during technology mapping, including redundant cuts and cost models based on gate counts, fan-in and weight/threshold values.
- [Optimizing Neural Network Representations of Boolean Networks](sources/boolean-network-optimization.md) — Proposes deterministic optimization of neural representations of Boolean networks while preserving functional equivalence.
- [verilog2nn](sources/verilog2nn.md) — Describes a combinational Verilog-to-PyTorch flow using Yosys, AND/NOT netlists, topological layers and sparse linear/ReLU operations.

### Compilation and deployment

- [torch.export IR Specification](sources/pytorch-export-ir.md) — Defines an export representation built on FX with a stronger contract for operators, inputs, outputs and metadata.
- [torch.fx](sources/pytorch-fx.md) — FX supplies symbolic tracing, a graph intermediate representation and Python code generation for transforming modules.
- [torch.compiler](sources/pytorch-compiler.md) — Explains torch.compile and its graph-capture/compiler stack: TorchDynamo, a backend such as TorchInductor, and AOT Autograd.
- [Torch-MLIR Architecture](sources/torch-mlir-architecture.md) — Describes a frontend/backend split joined by a backend contract in the torch dialect.
- [IREE CPU Deployment](sources/iree-cpu.md) — Describes CPU compilation targets, executable formats and runtime devices.
- [IREE PyTorch Integration](sources/iree-pytorch.md) — Documents PyTorch integration through IREE Turbine, with JIT and ahead-of-time workflows.
- [Auto-Vectorization in LLVM](sources/llvm-vectorizers.md) — Describes loop vectorization and SLP vectorization.
- [Linalg Dialect Rationale: The Case For Compiler-Friendly Custom Operations](sources/mlir-linalg.md) — Motivates structured operations that retain iteration and data-access information so transformations can be applied systematically.
- [DnD: A Cross-Architecture Deep Neural Network Decompiler](sources/dnd-decompiler.md) — Recovers high-level DNN representations from compiled binaries using symbolic execution, loop analysis and operator-template matching.
- [TENSORIZE: Fast Synthesis of Tensor Programs from Legacy Code using Symbolic Tracing, Sketching and Solving](sources/tensorize.md) — The university abstract describes lifting legacy loop code into tensor DSLs through symbolic tracing, sketches and algebraic solving.

### Direct construction

- [MIT 6.004: Finite State Machines — 6.1 Annotated Slides](sources/mit-fsm-design.md) — Explains clocked finite-state design as state storage plus combinational next-state/output logic.
- [Efficient Simulation of Finite Automata by Neural Nets](sources/efficient-fsm-simulation.md) — Studies Mealy-machine simulation by recurrent threshold machines.

### Learning and extraction

- [Differentiable Finite State Machines](sources/differentiable-fsm.md) — Represents Mealy-machine transitions and emissions as tensors acting on one-hot input/state vectors.
- [Learning by Abstraction: The Neural State Machine](sources/neural-state-machine.md) — Proposes a visual-reasoning model that predicts a probabilistic scene graph and traverses it using question-derived soft instructions.
- [Fool's Gold: Extracting Finite State Machines from Recurrent Network Dynamics](sources/fools-gold.md) — Warns that discretizing recurrent-network trajectories can yield misleading finite-state descriptions.

## Entities

No separate entity pages are needed yet; attribution is recorded in the source summaries.
