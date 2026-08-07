"""
RNAOS velocity update result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class VelocityUpdateResult:
    """
    Immutable velocity update result.
    """

    particle_id: int

    velocity: tuple[float, ...]
