"""
RNAOS genetic optimization result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.genome import (
    Genome,
)


@dataclass(
    slots=True,
    frozen=True,
)
class GeneticResult:
    """
    Immutable genetic optimization result.
    """

    best_genome: Genome

    generations: int

    mutations: int

    converged: bool
