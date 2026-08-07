"""
RNAOS particle swarm optimization model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class Particle:
    """
    Immutable PSO particle.
    """

    particle_id: int

    position: tuple[float, ...]

    velocity: tuple[float, ...]

    best_position: tuple[float, ...]

    fitness: float
