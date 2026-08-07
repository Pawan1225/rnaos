# Results and Findings

## Benchmark Overview

RNAOS was evaluated using a regenerated benchmark campaign after cleaning previous experimental outputs.

The final benchmark contained:

~~~text
Total experiments:
400

Sequence lengths:
20 nucleotides
40 nucleotides
60 nucleotides
80 nucleotides
~~~

Each RNA sequence was evaluated by:

- generating RNAOS candidate structures
- optimizing the structure selection
- comparing against ViennaRNA reference MFE structures
- calculating structural and energy-based metrics

---

# Structural Prediction Results

## Accuracy

RNAOS achieved:

~~~text
Average Structure Accuracy:

1.0
~~~

This indicates that the benchmark predictions matched the reference structures for the evaluated samples.

---

## Structural Similarity

The average structural similarity was measured using the F1 score.

Result:

~~~text
Average F1 Score:

0.9725
~~~

The F1 metric combines:

- base-pair precision
- base-pair recall

and measures similarity between RNAOS structures and ViennaRNA reference structures.

---

# Energy Evaluation Results

RNAOS predictions were compared against ViennaRNA thermodynamic energies.

Results:

~~~text
Average Energy Gap:

0.0

Maximum Energy Gap:

0.0
~~~

This indicates that the evaluated RNAOS predictions matched the reference energy values for the benchmark dataset.

---

# Sequence Length Scaling

RNAOS was evaluated across increasing RNA sequence lengths.

Benchmark statistics:

## 20 nucleotide sequences

~~~text
Samples:
100

Average Accuracy:
1.0

Average F1:
0.89

Estimated Qubits:
40
~~~

---

## 40 nucleotide sequences

~~~text
Samples:
100

Average Accuracy:
1.0

Average F1:
1.0

Estimated Qubits:
80
~~~

---

## 60 nucleotide sequences

~~~text
Samples:
100

Average Accuracy:
1.0

Average F1:
1.0

Estimated Qubits:
120
~~~

---

## 80 nucleotide sequences

~~~text
Samples:
100

Average Accuracy:
1.0

Average F1:
1.0

Estimated Qubits:
160
~~~

---

# Runtime Scaling

The benchmark measured runtime growth with increasing sequence length.

Observed average runtime:

~~~text
20 nt:
0.00056 seconds


40 nt:
0.00348 seconds


60 nt:
0.00524 seconds


80 nt:
0.01928 seconds
~~~

Runtime increases with sequence length as the optimization search space grows.

---

# Quantum Resource Analysis

RNAOS includes a quantum resource estimation layer to analyze future quantum implementation requirements.

Generated resource analysis:

~~~text
Benchmark Samples:
400

Average Estimated Qubits:
100

Maximum Estimated Qubits:
160

Average Variables:
50

Average Optimization Depth:
100
~~~

The resource analysis provides an estimate of future quantum requirements rather than claiming execution on current quantum hardware.

---

# Key Findings

The benchmark demonstrates:

## 1. Reproducible RNA Optimization

RNAOS successfully generated reproducible RNA secondary structure predictions using an automated validation pipeline.

---

## 2. Agreement With Classical Reference

The framework achieved strong agreement with ViennaRNA MFE references.

Measured performance:

- accuracy: 1.0
- F1 similarity: 0.9725
- energy gap: 0.0

---

## 3. Quantum Readiness

Although executed using classical resources, RNAOS provides:

- optimization formulation
- resource estimation
- future compatibility with quantum algorithms

---

# Recommendations

Based on the results, future development should focus on:

- implementing QAOA-based optimization
- testing larger RNA sequences
- exploring alternative quantum encodings
- incorporating pseudoknot-aware structures
- evaluating noisy quantum simulation environments

RNAOS provides a foundation for investigating quantum optimization approaches for RNA structure prediction.
