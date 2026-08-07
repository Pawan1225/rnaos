"""
RNAOS particle swarm optimization profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PSOProfile:
    """
    Immutable PSO intelligence profile.
    """

    best_fitness: float

    iterations: int

    swarm_size: int

    confidence: float
