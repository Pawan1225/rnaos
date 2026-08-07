"""
RNAOS tensor optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.tensor_profile import (
    TensorOptimizationProfile,
)


class TensorProfileEngine:
    """
    Generates tensor optimization profiles.
    """

    def generate(
        self,
        tensor_rank: int,
        compressed_rank: int,
        compression_ratio: float,
        search_candidates: int,
        best_score: float,
    ) -> TensorOptimizationProfile:
        """
        Generate tensor profile.
        """

        return TensorOptimizationProfile(
            tensor_rank=tensor_rank,
            compressed_rank=compressed_rank,
            compression_ratio=(compression_ratio),
            search_candidates=(search_candidates),
            best_score=best_score,
        )
