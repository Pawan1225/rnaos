"""
RNAOS meta crossover result model.
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
class MetaCrossoverResult:
    """
    Immutable meta crossover result.
    """

    parent_one: AlgorithmPerformanceGenome

    parent_two: AlgorithmPerformanceGenome

    offspring: AlgorithmPerformanceGenome

    crossover_point: int
