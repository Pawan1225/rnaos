"""
Tests for swarm population model.
"""

from __future__ import annotations

from dl.models.optimization.particle import (
    Particle,
)
from dl.models.optimization.swarm_population import (
    SwarmPopulation,
)


def test_swarm_population_creation() -> None:
    """
    Swarm population can be created.
    """

    particle = Particle(
        particle_id=1,
        position=(
            0.5,
            1.0,
        ),
        velocity=(
            0.1,
            0.2,
        ),
        best_position=(
            0.5,
            1.0,
        ),
        fitness=0.9,
    )

    swarm = SwarmPopulation(
        particles=(particle,),
        global_best_position=(
            0.5,
            1.0,
        ),
        global_best_fitness=0.9,
        generation=1,
    )

    assert isinstance(
        swarm,
        SwarmPopulation,
    )

    assert (
        len(
            swarm.particles,
        )
        == 1
    )

    assert swarm.global_best_position == (
        0.5,
        1.0,
    )

    assert swarm.global_best_fitness == 0.9

    assert swarm.generation == 1
