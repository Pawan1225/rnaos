"""
RNAOS algorithm performance genome model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AlgorithmPerformanceGenome:
    """
    Immutable algorithm performance genome.
    """

    genome_id: int

    algorithm_name: str

    genes: tuple[float, ...]

    fitness: float

    generation: int
