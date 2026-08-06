"""
Tests for the RNAOS explainable AI engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.explainable_ai_engine import (
    ExplainableAIEngine,
)
from ai.analyzers.meta_feature_engine import (
    MetaFeatureEngine,
)
from ai.analyzers.solver_recommendation_engine import (
    SolverRecommendationEngine,
)
from ai.models.explanation_profile import (
    ExplanationProfile,
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
def explainable_engine() -> ExplainableAIEngine:
    """Create an explainable AI engine."""
    return ExplainableAIEngine()


@pytest.fixture
def explanation(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
    explainable_engine: ExplainableAIEngine,
) -> ExplanationProfile:
    """Generate an explanation profile."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    meta_profile = meta_feature_engine.analyze(
        biological_profile,
    )

    recommendation = solver_engine.analyze(
        biological_profile,
        meta_profile,
    )

    return explainable_engine.analyze(
        biological_profile,
        meta_profile,
        recommendation,
    )


def test_profile_creation(
    explanation: ExplanationProfile,
) -> None:
    """Explanation profile should be created."""
    assert explanation is not None


def test_strategy_exists(
    explanation: ExplanationProfile,
) -> None:
    """A recommendation strategy should be produced."""
    assert explanation.recommended_strategy != ""


def test_confidence_range(
    explanation: ExplanationProfile,
) -> None:
    """Confidence should be normalized."""
    assert 0.0 <= explanation.confidence <= 1.0


def test_biological_factors_exist(
    explanation: ExplanationProfile,
) -> None:
    """Biological reasoning should exist."""
    assert (
        len(
            explanation.biological_factors,
        )
        > 0
    )


def test_ai_factors_exist(
    explanation: ExplanationProfile,
) -> None:
    """AI reasoning should exist."""
    assert (
        len(
            explanation.ai_factors,
        )
        > 0
    )


def test_factor_count(
    explanation: ExplanationProfile,
) -> None:
    """Factor count should be consistent."""
    assert explanation.factor_count == len(explanation.biological_factors) + len(
        explanation.ai_factors
    )


def test_summary_exists(
    explanation: ExplanationProfile,
) -> None:
    """Recommendation summary should exist."""
    assert explanation.recommendation_summary != ""


def test_technical_summary_exists(
    explanation: ExplanationProfile,
) -> None:
    """Technical summary should exist."""
    assert explanation.technical_summary != ""


def test_deterministic_analysis(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
    explainable_engine: ExplainableAIEngine,
) -> None:
    """Explanation generation should be deterministic."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    meta_profile = meta_feature_engine.analyze(
        biological_profile,
    )

    recommendation = solver_engine.analyze(
        biological_profile,
        meta_profile,
    )

    first = explainable_engine.analyze(
        biological_profile,
        meta_profile,
        recommendation,
    )

    second = explainable_engine.analyze(
        biological_profile,
        meta_profile,
        recommendation,
    )

    assert first == second


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    meta_feature_engine: MetaFeatureEngine,
    solver_engine: SolverRecommendationEngine,
    explainable_engine: ExplainableAIEngine,
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

    explanation = explainable_engine.analyze(
        biological_profile,
        meta_profile,
        recommendation,
    )

    assert explanation.factor_count > 0


def test_profile_is_immutable(
    explanation: ExplanationProfile,
) -> None:
    """Explanation profile should be immutable."""
    with pytest.raises(
        AttributeError,
    ):
        explanation.confidence = 0.5
