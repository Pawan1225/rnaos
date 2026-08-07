"""
RNAOS meta mutation result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)


@dataclass(
    slots=True,
    frozen=True,
)
class MetaMutationResult:
    """
    Immutable meta mutation result.
    """

    original: AlgorithmPerformanceGenome

    mutated: AlgorithmPerformanceGenome

    mutation_rate: float
