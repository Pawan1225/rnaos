"""
RNAOS particle swarm optimization result model.
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
class PSOResult:
    """
    Immutable PSO optimization result.
    """

    best_particle: Particle

    iterations: int

    converged: bool
