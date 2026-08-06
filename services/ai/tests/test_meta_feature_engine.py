"""
Tests for the RNAOS meta feature engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.meta_feature_engine import (
    MetaFeatureEngine,
)
from ai.models.meta_feature_profile import (
    MetaFeatureProfile,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)


@pytest.fixture
def biology_engine() -> BiologicalIntelligenceEngine:
    """Create a biological intelligence engine."""
    return BiologicalIntelligenceEngine()


@pytest.fixture
def meta_feature_engine() -> MetaFeatureEngine:
    """Create a meta feature engine."""
    return MetaFeatureEngine()


@pytest.fixture
def meta_profile(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
) -> MetaFeatureProfile:
    """Generate a meta feature profile."""
    profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    return meta_feature_engine.analyze(
        profile,
    )


def test_profile_creation(
    meta_profile: MetaFeatureProfile,
) -> None:
    """Profile should be created."""
    assert meta_profile is not None


def test_feature_count(
    meta_profile: MetaFeatureProfile,
) -> None:
    """Feature count should remain fixed."""
    assert meta_profile.feature_count == 6


@pytest.mark.parametrize(
    "attribute",
    [
        "folding_difficulty",
        "structural_complexity",
        "optimization_complexity",
        "stability_complexity_index",
        "quantum_suitability",
        "ai_readiness_score",
    ],
)
def test_feature_range(
    meta_profile: MetaFeatureProfile,
    attribute: str,
) -> None:
    """All meta features should be normalized."""
    value = getattr(
        meta_profile,
        attribute,
    )

    assert 0.0 <= value <= 1.0


def test_deterministic_analysis(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
) -> None:
    """Analysis should be deterministic."""
    profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    first = meta_feature_engine.analyze(
        profile,
    )

    second = meta_feature_engine.analyze(
        profile,
    )

    assert first == second


def test_quantum_suitability_exists(
    meta_profile: MetaFeatureProfile,
) -> None:
    """Quantum suitability should be computed."""
    assert meta_profile.quantum_suitability >= 0.0


def test_ai_readiness_exists(
    meta_profile: MetaFeatureProfile,
) -> None:
    """AI readiness score should be computed."""
    assert meta_profile.ai_readiness_score >= 0.0


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
) -> None:
    """Long RNA sequences should be supported."""
    profile = biology_engine.analyze(
        "GCGAAACGC" * 25,
    )

    meta_profile = meta_feature_engine.analyze(
        profile,
    )

    assert meta_profile.feature_count == 6


def test_profile_is_immutable(
    meta_profile: MetaFeatureProfile,
) -> None:
    """Meta feature profile should be immutable."""
    with pytest.raises(
        AttributeError,
    ):
        meta_profile.ai_readiness_score = 0.5
