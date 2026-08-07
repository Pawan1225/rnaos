"""
Tests for PSO optimizer.
"""

from __future__ import annotations

from dl.models.optimization.particle import (
    Particle,
)
from dl.models.optimization.pso_result import (
    PSOResult,
)
from dl.models.optimization.swarm_population import (
    SwarmPopulation,
)
from dl.optimization.pso_optimizer import (
    PSOOptimizer,
)


def test_pso_optimizer() -> None:
    """
    Best particle is selected.
    """

    swarm = SwarmPopulation(
        particles=(
            Particle(
                particle_id=1,
                position=(
                    0.1,
                    0.2,
                ),
                velocity=(
                    0.0,
                    0.0,
                ),
                best_position=(
                    0.1,
                    0.2,
                ),
                fitness=0.5,
            ),
            Particle(
                particle_id=2,
                position=(
                    1.0,
                    1.5,
                ),
                velocity=(
                    0.1,
                    0.1,
                ),
                best_position=(
                    1.0,
                    1.5,
                ),
                fitness=0.95,
            ),
        ),
        global_best_position=(
            1.0,
            1.5,
        ),
        global_best_fitness=0.95,
        generation=1,
    )

    optimizer = PSOOptimizer()

    result = optimizer.optimize(
        swarm,
        iterations=25,
    )

    assert isinstance(
        result,
        PSOResult,
    )

    assert result.best_particle.particle_id == 2

    assert result.iterations == 25

    assert result.converged is True
