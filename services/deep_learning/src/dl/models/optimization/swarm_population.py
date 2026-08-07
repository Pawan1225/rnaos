"""
RNAOS swarm population model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.particle import (
    Particle,
)


@dataclass(
    slots=True,
    frozen=True,
)
class SwarmPopulation:
    """
    Immutable PSO swarm population.
    """

    particles: tuple[Particle, ...]

    global_best_position: tuple[float, ...]

    global_best_fitness: float

    generation: int
