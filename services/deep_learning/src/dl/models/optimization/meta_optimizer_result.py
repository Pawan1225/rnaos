"""
RNAOS meta optimizer result model.
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
class MetaOptimizerResult:
    """
    Immutable meta optimizer result.
    """

    best_genome: AlgorithmPerformanceGenome

    generations: int

    improved: bool
