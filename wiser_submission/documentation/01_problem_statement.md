# Problem Statement

## Challenge Background

Messenger RNA (mRNA) secondary structure prediction is an important computational problem in modern biotechnology.

The secondary structure formed by an RNA sequence can influence:

- molecular stability
- translation efficiency
- RNA behavior
- manufacturability of RNA-based medicines

Understanding and optimizing RNA structures is therefore important for mRNA design.

---

## Computational Challenge

An RNA molecule consists of four nucleotides:

- Adenine (A)
- Uracil (U)
- Cytosine (C)
- Guanine (G)

A sequence can fold into many possible secondary structures through nucleotide pairing interactions.

As sequence length increases, the number of possible structures grows rapidly, making exhaustive exploration computationally challenging.

---

## Classical RNA Folding

Classical approaches such as ViennaRNA use thermodynamic models and dynamic programming methods to identify Minimum Free Energy (MFE) structures.

These methods provide reliable reference structures and energy calculations.

However, exploring the complete RNA folding landscape remains difficult, especially when additional constraints or optimization objectives are introduced.

---

## WISER Challenge Objective

The WISER <> Moderna challenge investigates whether quantum or quantum-inspired optimization methods can be applied to RNA secondary structure prediction.

The objective is to:

- formulate RNA folding as an optimization problem
- generate candidate secondary structures
- compare results with classical MFE references
- analyze scalability and quantum resource requirements

---

## RNAOS Objective

RNAOS (RNA Optimization System) was developed to explore a quantum-inspired approach for RNA secondary structure optimization.

The system focuses on:

- constraint-aware structure generation
- thermodynamic energy evaluation
- optimization-based candidate selection
- benchmarking against ViennaRNA reference structures

The objective is not to replace classical RNA folding methods, but to investigate how optimization and quantum-inspired techniques can support future RNA structure exploration.
