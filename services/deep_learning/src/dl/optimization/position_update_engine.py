"""
RNAOS particle swarm position update engine.
"""

from __future__ import annotations

from dl.models.optimization.position_update_result import (
    PositionUpdateResult,
)


class PositionUpdateEngine:
    """
    Updates particle position.

    Formula:

    x_new = x + v
    """

    def update(
        self,
        particle_id: int,
        position: tuple[float, ...],
        velocity: tuple[float, ...],
    ) -> PositionUpdateResult:
        """
        Calculate new particle position.
        """

        if len(position) != len(velocity):
            raise ValueError(
                "Vector dimensions must match",
            )

        new_position = tuple(
            x + v
            for x, v in zip(
                position,
                velocity,
                strict=True,
            )
        )

        return PositionUpdateResult(
            particle_id=particle_id,
            position=new_position,
        )
