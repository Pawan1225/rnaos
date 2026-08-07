"""
Tests for intelligence feature model.
"""

from __future__ import annotations

from dl.models.optimization.intelligence_feature import (
    IntelligenceFeature,
)


def test_intelligence_feature_creation() -> None:
    """
    Intelligence feature can be created.
    """

    feature = IntelligenceFeature(
        feature_name="solver_diversity",
        value=0.95,
        category="optimization",
    )

    assert feature.feature_name == ("solver_diversity")

    assert feature.value == 0.95

    assert feature.category == ("optimization")
