"""
Tests for particle model.
"""

from __future__ import annotations

from dl.models.optimization.particle import (
    Particle,
)


def test_particle_creation() -> None:
    """
    Particle can be created.
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

    assert particle.particle_id == 1

    assert particle.position == (
        0.5,
        1.0,
    )

    assert particle.velocity == (
        0.1,
        0.2,
    )

    assert particle.best_position == (
        0.5,
        1.0,
    )

    assert particle.fitness == 0.9
