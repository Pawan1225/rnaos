"""
RNAOS low-rank tensor models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LowRankTensor:
    """
    Immutable compressed tensor representation.
    """

    original_rank: int

    compressed_rank: int

    compression_ratio: float

    values: tuple[float, ...]
