"""
Tests for tensor optimization profile.
"""

from __future__ import annotations

from dl.models.optimization.tensor_profile import (
    TensorOptimizationProfile,
)
from dl.optimization.tensor_profile_engine import (
    TensorProfileEngine,
)


def test_tensor_profile_generation() -> None:
    """
    Tensor profile is generated.
    """

    engine = TensorProfileEngine()

    profile = engine.generate(
        tensor_rank=4,
        compressed_rank=2,
        compression_ratio=0.5,
        search_candidates=100,
        best_score=1.0,
    )

    assert isinstance(
        profile,
        TensorOptimizationProfile,
    )

    assert profile.compressed_rank == 2

    assert profile.search_candidates == 100
