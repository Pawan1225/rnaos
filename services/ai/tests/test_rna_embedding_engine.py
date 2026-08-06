"""
Tests for the RNAOS RNA embedding engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from ai.analyzers.rna_embedding_engine import (
    RNAEmbeddingEngine,
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


@pytest.fixture
def embedding_engine() -> RNAEmbeddingEngine:
    """Create an RNA embedding engine."""
    return RNAEmbeddingEngine()


def test_embedding_creation(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding should be created."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert embedding is not None


def test_embedding_dimension(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding dimension should match value count."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert embedding.dimension == len(
        embedding.values,
    )


def test_embedding_size_property(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Size property should equal dimension."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert embedding.size == embedding.dimension


def test_embedding_is_normalized(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding should have unit L2 norm."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    norm = sum(value * value for value in embedding.values) ** 0.5

    assert norm == pytest.approx(
        1.0,
    )


def test_deterministic_embedding(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding generation should be deterministic."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding1 = embedding_engine.embed(
        feature_vector,
    )

    embedding2 = embedding_engine.embed(
        feature_vector,
    )

    assert embedding1 == embedding2


def test_embedding_contains_only_finite_values(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding values should be finite."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    for value in embedding.values:
        assert value == pytest.approx(
            value,
        )


def test_embedding_dimension_matches_feature_vector(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding dimension should equal feature dimension."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert embedding.dimension == feature_vector.dimension


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Long RNA sequences should be supported."""
    profile = biology_engine.analyze(
        "GCGAAACGC" * 20,
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert embedding.dimension > 0


def test_embedding_values_are_not_empty(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Embedding should contain values."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert len(embedding.values) > 0


def test_embedding_preserves_dimension(
    biology_engine: BiologicalIntelligenceEngine,
    feature_engine: FeatureEngineeringEngine,
    embedding_engine: RNAEmbeddingEngine,
) -> None:
    """Normalization should not change dimensionality."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    embedding = embedding_engine.embed(
        feature_vector,
    )

    assert len(
        embedding.values,
    ) == len(
        feature_vector.values,
    )
