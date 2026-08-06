"""
Tests for the RNAOS solver recommendation engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.meta_feature_engine import (
    MetaFeatureEngine,
)
from ai.analyzers.solver_recommendation_engine import (
    SolverRecommendationEngine,
)
from ai.models.solver_recommendation_features import (
    SolverRecommendationFeatures,
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
def solver_engine() -> SolverRecommendationEngine:
    """Create a solver recommendation engine."""
    return SolverRecommendationEngine()


@pytest.fixture
def recommendation(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
) -> SolverRecommendationFeatures:
    """Generate solver recommendation features."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    meta_profile = meta_feature_engine.analyze(
        biological_profile,
    )

    return solver_engine.analyze(
        biological_profile,
        meta_profile,
    )


def test_profile_creation(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Recommendation profile should be created."""
    assert recommendation is not None


def test_feature_count(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Feature count should remain fixed."""
    assert recommendation.feature_count == 8


@pytest.mark.parametrize(
    "attribute",
    [
        "optimization_difficulty",
        "search_space_complexity",
        "constraint_density",
        "expected_runtime",
        "classical_affinity",
        "quantum_affinity",
        "hybrid_affinity",
        "recommendation_confidence",
    ],
)
def test_feature_range(
    recommendation: SolverRecommendationFeatures,
    attribute: str,
) -> None:
    """All recommendation features should be normalized."""
    value = getattr(
        recommendation,
        attribute,
    )

    assert 0.0 <= value <= 1.0


def test_deterministic_analysis(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
) -> None:
    """Recommendation generation should be deterministic."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    meta_profile = meta_feature_engine.analyze(
        biological_profile,
    )

    first = solver_engine.analyze(
        biological_profile,
        meta_profile,
    )

    second = solver_engine.analyze(
        biological_profile,
        meta_profile,
    )

    assert first == second


def test_quantum_affinity_exists(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Quantum affinity should be computed."""
    assert recommendation.quantum_affinity >= 0.0


def test_classical_affinity_exists(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Classical affinity should be computed."""
    assert recommendation.classical_affinity >= 0.0


def test_hybrid_affinity_exists(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Hybrid affinity should be computed."""
    assert recommendation.hybrid_affinity >= 0.0


def test_recommendation_confidence_exists(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Recommendation confidence should be computed."""
    assert recommendation.recommendation_confidence >= 0.0


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
) -> None:
    """Long RNA sequences should be supported."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGC" * 25,
    )

    meta_profile = meta_feature_engine.analyze(
        biological_profile,
    )

    recommendation = solver_engine.analyze(
        biological_profile,
        meta_profile,
    )

    assert recommendation.feature_count == 8


def test_profile_is_immutable(
    recommendation: SolverRecommendationFeatures,
) -> None:
    """Recommendation profile should be immutable."""
    with pytest.raises(
        AttributeError,
    ):
        recommendation.quantum_affinity = 0.5
