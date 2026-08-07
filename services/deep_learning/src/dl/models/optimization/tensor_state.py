"""
RNAOS tensor optimization models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorOptimizationState:
    """
    Immutable tensor optimization state.
    """

    shape: tuple[int, ...]

    values: tuple[float, ...]

    dimension: int
