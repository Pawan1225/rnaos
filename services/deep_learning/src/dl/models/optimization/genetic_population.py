"""
RNAOS genetic population model.
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
class GeneticPopulation:
    """
    Immutable genetic population.
    """

    genomes: tuple[Genome, ...]

    generation: int
