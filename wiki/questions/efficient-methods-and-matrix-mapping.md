---
title: "Efficient FSM-to-network methods and how functions become matrices"
type: question
created: 2026-10-07
updated: 2026-10-09
status: active
sources: ["raw/boolean-network-optimization/document.txt", "raw/verilog2nn/document.txt", "raw/differentiable-fsm/document.txt", "raw/spectral-wfa-rnn/document.txt", "raw/threshold-logic-synthesis/document.txt", "raw/threshold-interconnect-synthesis/document.txt", "raw/multi-output-circuit-minimization/document.txt", "raw/relu-training-hardness/document.txt", "raw/cajal-compiling-to-linear-neurons/document.txt"]
---

# Efficient FSM-to-network methods and how functions become matrices

## Question and recommendation

Which methods are most efficient when size means synapses? How do they turn functions into matrices, and is there one layer per function?

There is no established universal winner in this collection. For exact construction with few nonzero weighted connections, our proposed starting point is a compact state encoding plus joint optimization of next-state and output logic, retaining shared intermediate results. Compare it with the simple one-hot construction from the [size analysis](fsm-size-vs-synapses.md). Binary storage alone does not guarantee simple transition logic: the encoding changes the functions that must be implemented.

| Candidate | When it is useful | Main qualification |
| --- | --- | --- |
| Boolean circuit synthesis followed by sparse gate mapping | Structured transition/output functions with reusable subexpressions | Encoding, logic sharing, depth and relay wiring determine the final edge count |
| Threshold-aware or LUT-to-neural technology mapping | Combining several primitive gates into useful local functions; explicitly optimizing interconnects | Optimize connection count rather than just neurons; activation restrictions matter |
| Symbol-selected transition matrices / second-order recurrence | A direct algebraic baseline, or weighted series with a compact linear representation | Tensor coefficients and ordinary fixed-weight neural synapses are different resource models |

The [verilog2nn README](../sources/verilog2nn.md) describes the first route for combinational circuits, without demonstrating an FSM state/reset wrapper here. The [ICLR 2025 paper](../sources/boolean-network-optimization.md), sections 2–3, uses local Boolean-function representations and lossless optimization objectives related to neurons and connections. [Threshold synthesis](../sources/threshold-logic-synthesis.md) considers fan-in and weight costs, and [interconnect-driven synthesis](../sources/threshold-interconnect-synthesis.md) targets wiring. These are candidates, not a reproduced ranking of compilers on our machines.

Fewer edges can trade off against more depth, larger weights or relay nodes. Runtime also depends on sparse-kernel support, batch size and memory layout: fewer nonzero weights do not by themselves imply faster dense matrix execution. We have no performance measurements yet.

## Corrected recap: exactness, optimality and training

On 2026-10-09 the user asked whether smallest-network conversion implies $P=NP$, training is the most efficient algorithm-to-network method, and exact compilation must pass through Boolean logic and usually gives an inefficient network. That recap needs three corrections:

1. **Global minimality and polynomial-time minimality are different claims.** A polynomial-time optimizer for a problem proved NP-hard under deterministic reductions would imply $P=NP$. We have not proved that statement for our general FSM-to-minimum-synapse-network problem. Even the circuit-minimization result in the collection needs care because its reductions are randomized. See [complexity scope](../concepts/complexity-limits.md).
2. **Training is an option for approximation, not an established universal efficiency winner.** It has its own data and optimization costs, does not guarantee a smallest network, and can have hard worst-case global optimization problems. A trained model can happen to implement a function exactly on its declared domain; training loss alone does not certify sequence equivalence. [Training-hardness source](../sources/relu-training-hardness.md), [surrogate comparison](high-level-programs-to-neural-surrogates.md).
3. **Exactness does not require an explicit Boolean-circuit intermediate representation or force a large network.** Direct transition matrices/tensors preserve machine semantics algebraically, although their bilinear update differs from an ordinary fixed affine layer. Restricted functional-language compilation offers another source-structured route. [Tensor construction](../sources/differentiable-fsm.md), [Cajal](../sources/cajal-compiling-to-linear-neurons.md).

An elementary exact counterexample to inevitable inefficiency is a two-state unary toggle machine. Represent its state by a bit $h_t$, emit $h_t$ as its Moore output, and use

$$h_{t+1}=\operatorname{ReLU}(1-h_t),\qquad h_0\in\{0,1\}.$$

For state 0 this yields 1, and for state 1 it yields 0; induction establishes the intended alternating behavior for every input length. This is our direct derivation: one recurrent unit with one self-connection of weight $-1$ and bias $1$. Under our convention the bias is excluded from synapse count; a separately instantiated output/readout or state-copy interface would add its wiring. No training or Boolean-IR lowering is needed to set these parameters.

The [binary counter example](fsm-size-vs-synapses.md) gives a larger structured family with compact exact logic, under its depth/connectivity assumptions. These examples do not prove that arbitrary FSMs have small networks, nor that neural execution beats native code. They show why exactness alone is not an explanation of inefficiency. We have no declared machine distribution or comparative benchmark supporting “almost always inefficient.”

The working distinction is: **exact construction seeks correct behavior; exact minimization additionally seeks the smallest representation; approximate surrogate fitting trades behavioral error against cost.** Each route needs its own size and runtime measurements. General high-level code must retain the finite-memory/finite-domain assumptions if it is to be treated as an FSM.

The follow-up [smallest networks versus fastest algorithms](smallest-networks-fastest-algorithms-and-p-vs-np.md) explains why synapse minimization does not automatically optimize time or decide P versus NP, and how uniform construction and general circuit lower bounds could make the connection precise.

## An affine layer does not implement every function

For column-vector signals, a layer computes

$$z=\phi(Wx+b).$$

Each row is an output unit; each column is an incoming signal. A nonzero entry is a weighted connection under our counting convention. The activation supplies nonlinearity. A matrix alone gives a linear map, and a bias makes it affine; arbitrary Boolean functions require suitable nonlinear units, intermediate signals or input-dependent selection.

Two independent AND functions on Boolean inputs fit in the same layer:

$$\begin{bmatrix}a\land b\\c\land d\end{bmatrix}
=\operatorname{ReLU}\left(
\begin{bmatrix}1&1&0&0\\0&0&1&1\end{bmatrix}
\begin{bmatrix}a\\b\\c\\d\end{bmatrix}
-\begin{bmatrix}1\\1\end{bmatrix}\right).$$

There are four nonzero connections, excluding biases. If another gate needs both results, its row $[1\;1]$ with bias $-1$ follows in the next layer. Thus parallel functions share a layer, while dependencies introduce additional depth.

A single XOR function can use two affine stages and one hidden activation:

$$a\oplus b=[1\;1]\operatorname{ReLU}\left(
\begin{bmatrix}1&-1\\-1&1\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}\right).$$

These examples are our explicit matrix derivations from Boolean/ReLU identities, not additional source theorems. They apply to Boolean inputs. The output stage in the XOR example is linear.

## Mapping an FSM transition table directly to matrices

Let $h$ be a one-hot state vector with $n$ components. For each input symbol $a$, define a matrix with next states as rows and current states as columns:

$$(T_a)_{r,q}=\mathbf{1}[\delta(q,a)=r].$$

Then

$$h_{t+1}=T_{a_t}h_t.$$

For a parity machine, input 0 preserves the state and input 1 swaps it:

$$T_0=\begin{bmatrix}1&0\\0&1\end{bmatrix},\qquad
T_1=\begin{bmatrix}0&1\\1&0\end{bmatrix}.$$

For a complete deterministic FSM every column of each $T_a$ has one nonzero entry. Storing all $k$ matrices densely uses $kn^2$ slots, although only $kn$ entries are nonzero. An emission matrix $R_a$ similarly has rows for output symbols and columns for current states, with $y_t=R_{a_t}h_t$ for a Mealy machine.

With one-hot input $x$, selection becomes

$$h_{t+1}=\left(\sum_a x_aT_a\right)h_t.$$

This is bilinear in state and input: a tensor contraction / second-order recurrence, not one ordinary affine layer applied to concatenated $[h;x]$. This column-vector orientation is our rendering of the [differentiable FSM tutorial's tensor semantics](../sources/differentiable-fsm.md). The [weighted-automata/RNN equivalence](../sources/spectral-wfa-rnn.md) concerns linear second-order RNNs. Algebraic minimization concerns a weighted-series representation and should not be treated as a synapse-minimization guarantee for an arbitrary Mealy-machine architecture.

## Converting that recurrence to ordinary fixed matrices

An exact sparse ReLU construction can instead introduce one hidden signal for each state/input pair:

$$z_{q,a}=\operatorname{ReLU}(h_q+x_a-1).$$

Write $u=[h;x]$. Matrix $W_1\in\mathbb{R}^{nk\times(n+k)}$ has two ones per row: one selecting $h_q$ and one selecting $x_a$. All biases are $-1$. Matrix $W_2\in\mathbb{R}^{(n+o)\times nk}$ routes each hidden signal into its specified next state and emitted symbol, with two ones per column. Here $o$ is the output-alphabet size. The full step is

$$[h_{t+1};y_t]=W_2\operatorname{ReLU}(W_1[h_t;x_t]-\mathbf{1}).$$

It has exactly $4nk$ nonzero weighted connections under this unoptimized construction, excluding biases and separately counted delayed state-copy wiring. This is our derivation; see the [earlier size analysis](fsm-size-vs-synapses.md) for correctness, assumptions and limits. Two weight matrices implement the whole transition/output function together, regardless of how many entries or named functions appear in the specification.

## LUT-based mapping and layer scheduling

The ICLR 2025 paper, section 2.2 (printed pages 3–4), reviews this pipeline:

1. Map a Boolean DAG into small $k$-input lookup tables, with $k$ bounded by a chosen limit.
2. Convert each local truth table into a multilinear polynomial.
3. Build local networks $\zeta(x)=W_2\sigma(W_1x+b_1)$, with Heaviside hidden activations and linear readouts.
4. Run functions at the same DAG depth in parallel, sharing signals where possible.
5. Merge adjacent linear stages when no activation separates them.

For example, $a\lor b=a+b-ab$ on Boolean inputs. Monomial detectors form hidden features and their coefficients form the readout weights. This representation can have exponentially many monomials for a large truth table; small LUTs control the local expansion. It is not always the smallest network for a function: a threshold neuron can implement OR directly.

For a LUT DAG of depth $d$, the reviewed unmerged construction has $2d$ affine stages, while layer merging gives $d+1$. It inserts identity vertices when needed to eliminate skip connections. Fusion uses $W'=W_1^{(d+1)}W_2^{(d)}$; products can densify, so reducing layer count does not automatically reduce synapses. The depth formulas are specific to this construction. [Source, section 2.2](../sources/boolean-network-optimization.md).

```mermaid
flowchart LR
    A[Current state and input] --> B[Parallel operations at dependency depth 1]
    B --> C[Parallel operations at dependency depth 2]
    C --> D[Next state and emitted output]
    D --> E[Store next state]
    E --> A
```

One recurrence step reuses the same network cell for each new input. Unrolling time for visualization repeats the cell; it does not require a new set of learned weights per symbol. Its internal combinational depth is separate from the number of input symbols processed.

## Validation and remaining work

The explicit $W_1,W_2$ construction was checked on all 1,024 legal state/input cases across the 256 two-state binary Mealy tables. The parallel/dependent AND examples and XOR matrices were checked on all binary inputs. These checks validate the formulas, not optimality, a production compiler or hardware speed.

The next experiment should compare one-hot and compact encodings on the same machine, with exact step equivalence and counts for nonzero edges, biases, depth, weight precision and state feedback. For an actual efficiency ranking, specify allowed activations, latency, arithmetic precision and target hardware, then benchmark comparable implementations.

## Related pages

- [Boolean circuits as neural networks](../concepts/boolean-circuit-compilation.md)
- [Weighted automata and second-order recurrence](../concepts/weighted-automata.md)
- [State encoding](../concepts/state-encoding.md)
- [Research roadmap](research-roadmap.md)
