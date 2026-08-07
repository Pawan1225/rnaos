"""
RNAOS tensor optimization profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorOptimizationProfile:
    """
    Immutable tensor optimization profile.
    """

    tensor_rank: int

    compressed_rank: int

    compression_ratio: float

    search_candidates: int

    best_score: float
