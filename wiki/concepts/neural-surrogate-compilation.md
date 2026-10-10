---
title: "Neural surrogate compilation of high-level programs"
type: concept
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/parrot-neural-acceleration/document.txt", "raw/neural-surrogate-programming/document.txt", "raw/turaco-complexity-guided-sampling/document.txt", "raw/compnet-neural-surrogate-compilation/document.txt", "raw/cajal-compiling-to-linear-neurons/document.txt"]
---

# Neural surrogate compilation of high-level programs

## Contract

Replace selected program behavior with a neural approximation evaluated under a declared workload distribution and error metric. The original executable supplies labels. This differs from [exact FSM construction](exact-fsm-construction.md): acceptable output error, rather than complete transition equivalence, becomes the main contract.

The [surrogate programming taxonomy](../sources/neural-surrogate-programming.md) separates deployment in place of a program (compilation), retraining for another task (adaptation), and using the surrogate to optimize inputs to the original program (optimization).

## Evidence and routes

- [Parrot, MICRO 2012](../sources/parrot-neural-acceleration.md): instrument selected pure, fixed-interface functions, gather examples, train/search MLPs and substitute accelerator calls. Internal loops and function calls are allowed in a replaced region.
- [CompNet, 2024 preprint](../sources/compnet-neural-surrogate-compilation.md): encode C source, generate surrogate weights with a hypernetwork, and fine-tune the resulting small model on program executions. Its corpus is restricted to deterministic executable numeric functions without pointer interfaces.
- [Turaco, OOPSLA 2023](../sources/turaco-complexity-guided-sampling.md): use program paths and learning-complexity estimates to allocate samples to separate path surrogates; preserve the path conditions used for selection.
- [Cajal, POPL 2026](../sources/cajal-compiling-to-linear-neurons.md): an adjacent hybrid approach that compiles restricted typed linear programs to linear neurons and links them with learned networks. Ordinary purity alone does not establish its typing conditions.

These first-pass readings do not establish a universal compiler or minimum-size model.

## Design implications

Function boundaries expose reusable interfaces and are sensible initial candidate boundaries, but need not be the optimal partition. Compare per-function models with models of fused regions or entire loop computations. Preserve explicit data/state interfaces first; learned latent interfaces require joint training and sequence validation.

Model size, execution cost and learning cost are separate: a reused network does not acquire new weights on each loop iteration, but every invocation still executes it. Approximations can change the inputs seen by downstream modules and compound over repeated steps. Evaluate the composed program on complete held-out runs, not only isolated functions.

## Related pages

- [High-level programs to neural surrogates](../questions/high-level-programs-to-neural-surrogates.md)
- [Construction, learning and extraction](learning-vs-construction.md)
- [Compiler pipeline](compiler-pipeline.md)
- [Efficient methods and matrix mapping](../questions/efficient-methods-and-matrix-mapping.md)
