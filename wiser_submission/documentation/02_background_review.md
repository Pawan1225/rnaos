# Background Review

## RNA Secondary Structure

RNA molecules are single-stranded nucleic acids composed of four nucleotides:

- Adenine (A)
- Uracil (U)
- Cytosine (C)
- Guanine (G)

Although RNA is single stranded, nucleotides can form internal base pairs that allow the molecule to fold into complex secondary structures.

RNA secondary structure describes the pattern of paired and unpaired nucleotides without requiring complete three-dimensional molecular modeling.

---

## Base Pairing and Structural Representation

RNA secondary structures are commonly represented using dot-bracket notation.

In this representation:

- A dot (`.`) represents an unpaired nucleotide.
- Matching parentheses (`(` and `)`) represent paired nucleotides.

Example:

~~~text
...(((...)))...
~~~

The above structure represents paired stem regions separated by unpaired nucleotides.

Dot-bracket notation provides a compact representation that can be processed computationally and used in optimization pipelines.

---

## Minimum Free Energy Folding

RNA secondary structure prediction is commonly formulated as an energy minimization problem.

The Minimum Free Energy (MFE) structure is the structure with the lowest predicted thermodynamic free energy among possible conformations.

The optimization objective can be represented as:

~~~text
Find structure S such that:

Energy(S) is minimized
~~~

Valid structures must satisfy biological constraints such as:

- valid nucleotide pairing
- no invalid base pairing
- balanced structural representation

---

## ViennaRNA Framework

ViennaRNA is a widely used classical RNA folding framework.

RNAOS uses ViennaRNA for:

- generating reference MFE structures
- evaluating candidate structure energies
- benchmarking optimization results

ViennaRNA provides a reliable classical baseline for evaluating quantum-inspired approaches.

---

## RNA Folding as an Optimization Problem

RNA folding can be viewed as a constrained optimization problem.

Input:

~~~text
RNA sequence
~~~

Search space:

~~~text
Possible secondary structures
~~~

Objective:

~~~text
Minimize thermodynamic energy
~~~

Constraints:

~~~text
Biological structure rules
~~~

This formulation creates a connection between RNA folding and combinatorial optimization problems.

---

## Quantum Optimization Motivation

Many optimization problems become computationally challenging as the search space increases.

Quantum and quantum-inspired optimization methods provide alternative approaches for exploring complex search spaces.

Potential approaches include:

- Quantum Approximate Optimization Algorithm (QAOA)
- Variational Quantum Algorithms
- Quantum Annealing
- Tensor-network-inspired optimization

RNAOS investigates this connection by developing an optimization framework that can be evaluated using classical resources today while remaining compatible with future quantum implementations.
