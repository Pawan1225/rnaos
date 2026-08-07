"""
RNAOS position update result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PositionUpdateResult:
    """
    Immutable position update result.
    """

    particle_id: int

    position: tuple[float, ...]
