"""
RNAOS low-rank approximation engine.
"""

from __future__ import annotations

from dl.models.optimization.low_rank_tensor import (
    LowRankTensor,
)


class LowRankApproximationEngine:
    """
    Performs tensor compression.
    """

    def approximate(
        self,
        values: tuple[float, ...],
        target_rank: int,
    ) -> LowRankTensor:
        """
        Create low-rank approximation.
        """

        original_rank = len(
            values,
        )

        if target_rank <= 0:
            raise ValueError(
                "Target rank must be positive",
            )

        if target_rank > original_rank:
            raise ValueError(
                "Target rank exceeds original rank",
            )

        compressed_values = values[:target_rank]

        return LowRankTensor(
            original_rank=original_rank,
            compressed_rank=target_rank,
            compression_ratio=(target_rank / original_rank),
            values=compressed_values,
        )
