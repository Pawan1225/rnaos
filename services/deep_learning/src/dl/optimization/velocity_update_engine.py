"""
RNAOS particle swarm velocity update engine.
"""

from __future__ import annotations

from dl.models.optimization.velocity_update_result import (
    VelocityUpdateResult,
)


class VelocityUpdateEngine:
    """
    Calculates PSO particle velocity.
    """

    def update(
        self,
        particle_id: int,
        position: tuple[float, ...],
        velocity: tuple[float, ...],
        personal_best: tuple[float, ...],
        global_best: tuple[float, ...],
        inertia: float,
        cognitive: float,
        social: float,
    ) -> VelocityUpdateResult:
        """
        Update velocity.

        Simplified deterministic PSO update.
        """

        if not (len(position) == len(velocity) == len(personal_best) == len(global_best)):
            raise ValueError(
                "Vector dimensions must match",
            )

        new_velocity = tuple(
            inertia * v + cognitive * (p - x) + social * (g - x)
            for x, v, p, g in zip(
                position,
                velocity,
                personal_best,
                global_best,
                strict=True,
            )
        )

        return VelocityUpdateResult(
            particle_id=particle_id,
            velocity=new_velocity,
        )
