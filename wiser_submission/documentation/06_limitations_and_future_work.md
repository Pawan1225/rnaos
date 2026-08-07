# Limitations and Future Work

## Current Limitations

Although RNAOS demonstrates a reproducible quantum-inspired optimization framework for RNA secondary structure prediction, several limitations remain.

---

# 1. Benchmark Dataset Limitations

The current evaluation uses synthetic RNA sequences.

Advantages:

- controlled experiments
- reproducible benchmarking
- consistent comparison with ViennaRNA references

However, future evaluation should include:

- larger RNA datasets
- biologically derived sequences
- diverse structural patterns

---

# 2. Sequence Length Limitations

The current benchmark focuses on RNA sequences up to:

~~~text
80 nucleotides
~~~

This range is suitable for demonstrating the optimization workflow and resource scaling analysis.

However, longer RNA molecules introduce:

- larger search spaces
- increased computational requirements
- more complex folding landscapes

Future work should investigate scalable optimization strategies for larger sequences.

---

# 3. Quantum Hardware Limitations

RNAOS does not currently execute on real quantum hardware.

The quantum analysis performed in this project focuses on:

- optimization formulation
- estimated variables
- qubit requirements
- resource scaling

Future implementations may evaluate:

- QAOA circuits
- variational quantum algorithms
- quantum annealing approaches
- hardware noise effects

---

# 4. Structural Model Limitations

The current RNAOS implementation focuses on standard secondary structures.

Pseudoknot structures are not included.

Pseudoknots introduce additional structural complexity because nucleotide interactions may cross existing base-pair regions.

Future work could explore:

- pseudoknot-aware formulations
- advanced constraint models
- graph-based RNA representations

---

# 5. Optimization Limitations

Current optimization uses a quantum-inspired classical workflow.

While this provides:

- reproducibility
- interpretability
- benchmark compatibility

future research should explore:

- QUBO formulations
- QAOA optimization
- variational approaches
- hybrid classical-quantum optimization loops

---

# Future Development Opportunities

## Quantum Optimization Integration

A future version of RNAOS could implement:

- QAOA-based RNA folding optimization
- VQE-based energy minimization
- quantum annealing formulations

These approaches may provide new methods for exploring large RNA folding landscapes.

---

## Machine Learning Integration

AI models could enhance RNAOS through:

- learned candidate generation
- neural structure embeddings
- energy prediction models
- optimization guidance

A hybrid AI + quantum-inspired approach could improve scalability.

---

## Advanced Biological Modeling

Future improvements may include:

- pseudoknot prediction
- additional biological constraints
- improved thermodynamic models
- experimentally validated RNA structures

---

# Overall Outlook

RNAOS establishes a foundation for investigating quantum-inspired optimization approaches for RNA secondary structure prediction.

The project demonstrates:

- reproducible benchmarking
- agreement with classical MFE references
- energy-based evaluation
- quantum resource analysis

Future development will focus on expanding biological complexity and exploring practical quantum optimization implementations.
