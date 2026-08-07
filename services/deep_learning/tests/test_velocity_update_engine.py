"""
Tests for velocity update engine.
"""

from __future__ import annotations

from dl.models.optimization.velocity_update_result import (
    VelocityUpdateResult,
)
from dl.optimization.velocity_update_engine import (
    VelocityUpdateEngine,
)


def test_velocity_update() -> None:
    """
    Velocity is updated.
    """

    engine = VelocityUpdateEngine()

    result = engine.update(
        particle_id=1,
        position=(
            1.0,
            1.0,
        ),
        velocity=(
            0.5,
            0.5,
        ),
        personal_best=(
            2.0,
            2.0,
        ),
        global_best=(
            3.0,
            3.0,
        ),
        inertia=0.5,
        cognitive=1.0,
        social=1.0,
    )

    assert isinstance(
        result,
        VelocityUpdateResult,
    )

    assert result.particle_id == 1

    assert result.velocity == (
        3.25,
        3.25,
    )
