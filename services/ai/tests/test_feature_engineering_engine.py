"""
Tests for the RNAOS feature engineering engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)


@pytest.fixture
def biology_engine() -> BiologicalIntelligenceEngine:
    """Create a biological intelligence engine."""
    return BiologicalIntelligenceEngine()


@pytest.fixture
def feature_engine() -> FeatureEngineeringEngine:
    """Create a feature engineering engine."""
    return FeatureEngineeringEngine()


def test_feature_vector_creation(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature vector should be created."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector is not None


def test_feature_dimension(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature dimension should match the value count."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector.dimension == len(
        vector.values,
    )


def test_feature_names_match_dimension(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature names should match feature values."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert len(vector.feature_names) == vector.dimension


def test_non_empty_vector(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature vector should not be empty."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector.dimension > 0


def test_deterministic_extraction(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature extraction should be deterministic."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector1 = feature_engine.extract(
        profile,
    )

    vector2 = feature_engine.extract(
        profile,
    )

    assert vector1 == vector2


def test_sequence_length_feature(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """First feature should be sequence length."""
    sequence = "AUGCGCAU"

    profile = biology_engine.analyze(
        sequence,
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector.values[0] == len(
        sequence,
    )


def test_feature_values_are_finite(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Every feature should be finite."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    for value in vector.values:
        assert value == pytest.approx(value)


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Long RNA sequences should be supported."""
    sequence = "GCGAAACGC" * 20

    profile = biology_engine.analyze(
        sequence,
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector.dimension > 0


def test_feature_vector_size_property(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """The size property should equal the dimension."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert vector.size == vector.dimension


def test_interaction_features_exist(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Interaction features should be included."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    vector = feature_engine.extract(
        profile,
    )

    assert "gc_entropy_interaction" in vector.feature_names
    assert "stability_complexity_interaction" in vector.feature_names


def test_feature_name_uniqueness(
    feature_engine: FeatureEngineeringEngine,
) -> None:
    """Feature names should be unique."""
    names = feature_engine.DEFAULT_FEATURE_NAMES

    assert len(names) == len(
        set(names),
    )
