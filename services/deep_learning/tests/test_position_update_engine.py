"""
Tests for position update engine.
"""

from __future__ import annotations

from dl.models.optimization.position_update_result import (
    PositionUpdateResult,
)
from dl.optimization.position_update_engine import (
    PositionUpdateEngine,
)


def test_position_update() -> None:
    """
    Position is updated using velocity.
    """

    engine = PositionUpdateEngine()

    result = engine.update(
        particle_id=1,
        position=(
            1.0,
            2.0,
        ),
        velocity=(
            0.5,
            1.5,
        ),
    )

    assert isinstance(
        result,
        PositionUpdateResult,
    )

    assert result.particle_id == 1

    assert result.position == (
        1.5,
        3.5,
    )
