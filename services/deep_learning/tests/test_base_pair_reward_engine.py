"""
Tests for base pair reward engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.base_pair_reward import (
    BasePairReward,
)
from dl.optimization.base_pair_reward_engine import (
    BasePairRewardEngine,
)


def test_gc_reward() -> None:
    """
    GC pairing receives strong reward.
    """

    engine = BasePairRewardEngine()

    result = engine.calculate(
        "GC",
    )

    assert isinstance(
        result,
        BasePairReward,
    )

    assert result.energy == -3.0


def test_invalid_pair() -> None:
    """
    Unsupported pairs fail.
    """

    engine = BasePairRewardEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.calculate(
            "AA",
        )
