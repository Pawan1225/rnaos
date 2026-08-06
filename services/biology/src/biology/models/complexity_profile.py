"""
RNAOS complexity profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ComplexityProfile:
    """
    Research-grade characterization of RNA sequence complexity.

    Metrics
    -------
    entropy
        Shannon entropy of nucleotide distribution.

    sequence_diversity
        Fraction of unique nucleotides observed.

    repetition_score
        Degree of sequence repetitiveness.

    linguistic_complexity
        Diversity of observed k-mers.

    compression_ratio
        Approximate sequence compressibility.

    complexity_score
        Composite normalized complexity metric.
    """

    entropy: float

    sequence_diversity: float

    repetition_score: float

    linguistic_complexity: float

    compression_ratio: float

    complexity_score: float
