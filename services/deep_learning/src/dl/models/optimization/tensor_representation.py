"""
RNAOS tensor optimization models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorRepresentation:
    """
    Immutable tensor representation.
    """

    dimensions: tuple[int, ...]

    rank: int

    values: tuple[float, ...]
