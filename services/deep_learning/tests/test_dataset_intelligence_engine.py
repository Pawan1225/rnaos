"""
Tests for dataset intelligence engine.
"""

from __future__ import annotations

from dl.engines.dataset_intelligence_engine import (
    DatasetIntelligenceEngine,
)
from dl.models.dataset_profile import (
    DatasetProfile,
)


def test_dataset_analysis() -> None:
    """
    Dataset profile is generated.
    """

    engine = DatasetIntelligenceEngine()

    profile = engine.analyze(
        dataset_name="rfam",
        sample_count=5000,
        feature_dimension=50,
    )

    assert isinstance(
        profile,
        DatasetProfile,
    )

    assert profile.dataset_name == "rfam"

    assert profile.sample_count == 5000

    assert profile.readiness_score == 1.0


def test_small_dataset_score() -> None:
    """
    Small datasets get lower readiness.
    """

    engine = DatasetIntelligenceEngine()

    profile = engine.analyze(
        dataset_name="test_dataset",
        sample_count=100,
        feature_dimension=10,
    )

    assert profile.readiness_score < 1.0
