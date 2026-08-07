"""
Tests for effect size.
"""

from __future__ import annotations

from dl.models.benchmark.effect_size import (
    EffectSize,
)


def test_effect_size() -> None:
    """
    Effect size can be created.
    """

    effect = EffectSize(
        cohens_d=0.8,
        improvement_ratio=0.15,
        relative_gain=15.0,
    )

    assert effect.cohens_d == 0.8

    assert effect.improvement_ratio == 0.15

    assert effect.relative_gain == 15.0
