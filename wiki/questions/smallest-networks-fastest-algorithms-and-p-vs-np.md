---
title: "Would the smallest neural network give the fastest algorithm or settle P versus NP?"
type: question
created: 2026-10-09
updated: 2026-10-09
status: active
sources: ["raw/cook-p-vs-np/document.txt", "raw/circuits-and-nonuniform-computation/document.txt", "raw/multi-output-circuit-minimization/document.txt", "raw/mit-fsm-design/document.txt"]
---

# Would the smallest neural network give the fastest algorithm or settle P versus NP?

## Answer and scope

The user asks whether finding the smallest neural network is equivalent to finding the fastest algorithm, and whether the ability to minimize networks would at least determine whether P=NP.

There is a real connection through circuit complexity, but the claimed equivalence does not follow. Synapse count is a representation/work measure. Running time also depends on evaluation depth, repeated recurrence, arithmetic precision, input access and the time required to construct the network. An exact minimizer for each finite problem size does not automatically provide an asymptotic upper or lower bound for SAT.

Here $n$ means the number of bits in an input instance, not the number of states in an FSM. P versus NP concerns a single algorithm's worst-case time across arbitrarily large input instances. [Cook, section 1, printed pages 1–2](../sources/cook-p-vs-np.md).

## Network size and execution time

For a sparse feedforward network evaluated once, with $E$ nonzero weighted connections and $V$ units, straightforward sequential evaluation uses $O(E+V)$ scalar operations. This is our operation count under constant-cost primitive arithmetic/activations, not a hardware benchmark. Parallel latency depends on dependencies and available processors; large fan-in must not be treated as free on a finite machine. For a recurrent cell reused for $T$ steps, the same scheme uses $O(T(E+V))$ scalar operations while retaining the same stored network.

Thus a small recurrent network can perform a long computation. Minimizing its connections does not minimize its number of steps. Even among feedforward graphs, equal connection counts need not give equal depth: an AND chain and a balanced AND tree on $n$ Boolean inputs both have $n-1$ binary gates and $2(n-1)$ incoming gate connections, while their depths are $n-1$ and $\lceil\log_2 n\rceil$. Mapping each gate to $\operatorname{ReLU}(a+b-1)$ preserves this example on Boolean inputs. This is our derivation for a DAG allowing skip connections; an adjacent-layer-only MLP may require relays and a different edge count. [Earlier matrix/gate identities](efficient-methods-and-matrix-mapping.md).

The [circuit lectures](../sources/circuits-and-nonuniform-computation.md), lecture 10, separately define size and depth and give a balanced parity construction. Their unbounded-fan-in gate-count convention differs from synapse counting and must be translated explicitly.

Classical P versus NP uses bit-cost computation. A weight containing an enormous number of bits, or a real primitive treated as a unit-cost oracle, can hide resources excluded by a connection-only metric. Specify how weights and intermediates are represented and what their arithmetic costs.

## A fixed FSM is not an arbitrary SAT solver

A fixed deterministic FSM with constant-time transition lookup makes one update per input symbol, so its membership/output computation takes linear time in stream length. This is the direct consequence of the ordinary clocked-state model described in [MIT's FSM notes](../sources/mit-fsm-design.md). Optimizing its neural representation can matter practically, but this alone does not address general SAT at unbounded sizes.

A high-level program has finitely many internal configurations when all storage, values and address/control state have fixed finite domains. To study general complexity, allow the problem size and resource bounds to grow. Cook's Turing-machine appendix distinguishes finite control from its unbounded tape. [Printed pages 9–10](../sources/cook-p-vs-np.md). A compiler polynomial in the size of an explicitly supplied FSM can still cost exponential time in SAT input length if constructing that FSM already requires exponentially many states.

## What would prove P = NP?

Suppose a deterministic procedure takes $1^n$ and constructs a network $N_n$ that exactly decides SAT on every valid formula encoding of length $n$, with a declared convention for invalid encodings. If construction takes polynomial time in $n$, the complete description has polynomial length, and exact evaluation has polynomial bit-cost on every such input, then constructing and evaluating $N_n$ gives a polynomial-time SAT algorithm. Because SAT is NP-complete, this would prove P=NP. Global minimality is not required. This is our application of [Cook's Proposition 1(c), printed pages 4–5](../sources/cook-p-vs-np.md).

Merely having a small separately chosen network for every input length does not establish that efficient construction procedure. In the Boolean-circuit model, polynomial-size families define P/poly, which does not by itself establish membership in P. This distinction is uniform versus nonuniform computation. [Blais, lecture 11](../sources/circuits-and-nonuniform-computation.md).

## What would prove P ≠ NP?

Cook's section 3 explains an established route: prove that an NP-complete problem such as SAT has no polynomial-size Boolean circuit family. Every polynomial-time algorithm can be simulated with a polynomial-size circuit family, so this circuit lower bound would imply P≠NP. [Printed page 8](../sources/cook-p-vs-np.md).

A neural lower bound could play that role only after proving that the target network class can simulate every relevant polynomial-size Boolean circuit with polynomial overhead under the declared resource metric. The elementary bounded-fan-in Boolean/ReLU constructions show why such a simulation is plausible for a permissive feedforward model. A bound for a restricted architecture, fixed depth, selected state encoding or chosen compiler output does not automatically rule out every polynomial-time algorithm. A particular exact compiler producing a huge network supplies an upper bound for its construction, not a lower bound on every possible implementation.

Failure to find an efficient network, or an inefficient minimization procedure, does not prove P≠NP. The hard lower-bound proof is the essential additional result.

## Why an exact minimizer alone is insufficient

For finite Boolean truth tables and a fixed finite gate basis, there is already a conceptual exhaustive minimizer: enumerate circuits in increasing size, test their outputs on every input, and stop at the first match. It terminates because every finite Boolean function has a finite circuit. This is our consequence of the circuit universality construction in [Blais, lecture 10](../sources/circuits-and-nonuniform-computation.md), not a proposed practical implementation.

For this model one can therefore determine the exact minimum separately at each $n$, at enormous cost. This does not decide whether the sequence of minima is bounded by some polynomial for all input lengths, nor provide an efficient uniform generator. A neural version needs finite/decidable candidate and equivalence conditions before making the analogous enumeration claim. No unrestricted exact real-weight neural minimizer is asserted here.

Even an optimizer polynomial in an explicitly supplied truth table's length may be exponential in $n$, because that table contains $2^n$ output entries for a one-output Boolean function. Conversely, a polynomial-time solver for a problem already proved NP-hard under an appropriate reduction could imply a collapse; that is a different claim from a slow optimizer's existence. See [complexity scope](../concepts/complexity-limits.md) for the randomized-reduction limitation of the circuit-minimization paper in this collection.

## Consequence for this project

Track connection count, depth, recurrent steps, precision, construction cost and inference cost separately. Network minimization is a useful optimization target. Settling P versus NP additionally requires a uniform polynomial-time construction/evaluation result or a sufficiently general asymptotic lower bound, not just optimal results on finitely many machine sizes.

No minimizer, circuit lower bound or new complexity result has been implemented/proved here. The examples and conditional implications above are explanatory derivations backed by the cited definitions; source proofs were not independently audited.

## Related pages

- [Complexity claims and their scope](../concepts/complexity-limits.md)
- [FSM size versus synapse count](fsm-size-vs-synapses.md)
- [Efficient methods and matrix mapping](efficient-methods-and-matrix-mapping.md)
- [High-level programs to neural surrogates](high-level-programs-to-neural-surrogates.md)
