---
title: "How does FSM size relate to neural-network synapse count?"
type: question
created: 2026-10-07
updated: 2026-10-07
status: active
sources: ["raw/differentiable-fsm/document.txt", "raw/verilog2nn/document.txt", "raw/fsm-rnn-complexity/document.txt", "raw/efficient-fsm-simulation/document.txt"]
---

# How does FSM size relate to neural-network synapse count?

## Question and answer

Given a behavior-preserving method $M:A\mapsto N$, how does the size of a finite state machine $A$ relate to the number of synapses in the constructed network $N$?

There are method-specific relationships and bounds, but no universal proportionality based only on state count. Define

$$S_M(A)=|E(M(A))|.$$

For this analysis, a synapse is a nonzero weighted directed connection. Biases, dense matrix slots containing zero, shared parameter counts and operations performed during an unrolled execution are separate quantities. Specify separately whether state-register/feedback wiring is counted. A different counting convention changes the answer.

Let $n=|Q|$ be the number of states and $k=|\Sigma|$ the input-alphabet size. A complete deterministic machine has $T=nk$ state/input transition entries. This counts entries individually rather than grouping equally labeled edges in a diagram. Prefer reachable, behaviorally distinct states when comparing machines: unreachable or redundant states can inflate the supplied state count.

## A concrete linear construction

The following is our derivation, combining one-hot transition semantics with Boolean/ReLU gates. It is not quoted as a theorem from a paper. The ingredients are supported by the [differentiable FSM tutorial](../sources/differentiable-fsm.md) and the [verilog2nn gate identities](../sources/verilog2nn.md).

Assume a complete deterministic Mealy machine, one-hot state $h\in\{0,1\}^n$, one-hot input $x\in\{0,1\}^k$, and one-hot emitted symbols. For every state/input pair, make a hidden unit

$$z_{q,a}=\operatorname{ReLU}(h_q+x_a-1).$$

Exactly one $z$ is active for a legal state/input. Compute

$$h'_r=\sum_{(q,a):\delta(q,a)=r}z_{q,a},\qquad
y_b=\sum_{(q,a):\lambda(q,a)=b}z_{q,a}.$$

These outputs remain one-hot and implement the specified transition/emission exactly. The sums can be linear outputs or followed by ReLU without changing legal-input results.

| Part | Nonzero weighted connections |
| --- | --- |
| State/input into transition units | $2T$ |
| Transition units into next-state outputs | $T$ |
| Transition units into emitted-symbol outputs | $T$ |
| Total for the step network | $4T=4nk$ |

The unoptimized construction deliberately retains every transition unit. It has $T$ nonzero biases, excluded from the synapse count. Add $n$ connections if the implementation explicitly represents copying state outputs into separate delayed state-input nodes. With fixed $k$, the step-network count is linear in $n$.

This is an existence/example bound and a count for this particular method, not the minimum synapse count for every machine. It assumes valid one-hot initialization and legal one-hot inputs. It does not establish robustness under perturbation, fixed-precision hardware performance or behavior for invalid encodings.

## Why a different method can be much smaller

Consider a unary cyclic DFA with $n=2^b$ states that accepts input lengths divisible by $n$. Its states are all distinguishable: their remaining distance to the next accepting state differs. Thus this example does not rely on redundant states.

Encode its state using $b$ binary bits and increment modulo $2^b$ at each input. A ripple incrementer uses a constant number of bounded-fan-in Boolean/ReLU connections per bit; testing whether all bits are zero also uses linear wiring. For a feedforward DAG allowing intermediate results to feed later nodes, plus $b$ delayed state bits,

$$S_M(A)=O(b)=O(\log n).$$

This is a second original derivation. It allows multiple combinational layers per machine step, with depth growing as $O(b)$. It is not a bound for a model requiring exactly one synchronous neural layer update per FSM transition. Converting such a DAG into an adjacent-layer-only MLP may add relay connections, so the same count must not be assumed for every implementation, including the supplied repository.

For reference, each increment bit can use carry $c_i$ and state bit $h_i$, with $c_0=1$:

$$d_i=\operatorname{ReLU}(h_i+c_i-1),\quad
h'_i=h_i+c_i-2d_i,\quad c_{i+1}=d_i.$$

On binary inputs these are AND/carry and XOR operations. All intermediates needed for the bit outputs have only constant fan-in; this explains the linear connection count. A table-oriented compiler and a structure-preserving compiler can therefore give very different sizes for the same machine.

## Neurons and synapses are different bounds

For a network with $H$ computational units,

$$|E|=\sum_{v}\operatorname{fanin}(v).$$

Bounded fan-in $d$ gives $|E|\leq dH$, for connections into those units. A densely connected architecture can instead have order $H^2$ edges. Interface/readout connections must be included consistently. A neuron-count theorem cannot be relabeled as a synapse-count theorem without examining connectivity.

Horne–Hush explicitly defines fan-in using nonzero weights and studies how restrictions change node complexity. Its main results concern neuron counts and particular machine/network assumptions. [Source, section 2.2 and section 5](../sources/fsm-rnn-complexity.md). The Alon–Dewdney–Ott construction also makes connectivity and output timing part of the model. [Source, sections 4–5](../sources/efficient-fsm-simulation.md).

## Bounds versus statistical correlation

For fixed input/output alphabets, one useful mathematical object is the worst-case method size

$$F_M(n,k)=\max_{A:\,|Q_A|=n,\,|\Sigma_A|=k} S_M(A).$$

State count alone need not determine $S_M(A)$, nor guarantee monotonicity for an arbitrary compiler: transition structure, preprocessing and redundant circuitry can change it. A statistical correlation also needs a distribution of machines; no empirical correlation coefficient has been measured here.

Distinguish this fixed-method quantity from minimizing over all equivalent networks within a declared architecture, activation, precision and timing model. Without specifying those restrictions, a universal lower-bound claim would be unsupported.

For a concrete $M$, record $n$, $k$, transition entries, encoding, depth, nonzero edges, bias count, weight precision and output contract. Then derive a bound or measure it across a stated machine family.

## Validation and limits

- Exhaustively checked the one-hot equations on every state/input pair of all 256 two-state machines with binary input/output: 1,024 cases.
- Checked the ripple-increment equations on every state for bit widths 1 through 8.
- These checks support the algebra; they are not a deployed compiler, an optimality proof, a benchmark, or an empirical correlation study.

## Related pages

- [State encoding and construction cost](../concepts/state-encoding.md)
- [Exact FSM construction](../concepts/exact-fsm-construction.md)
- [Boolean-circuit compilation](../concepts/boolean-circuit-compilation.md)
- [Research roadmap](research-roadmap.md)
