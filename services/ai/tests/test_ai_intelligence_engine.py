"""
Tests for the RNAOS AI intelligence engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.ai_intelligence_engine import (
    AIIntelligenceEngine,
)
from ai.models.ai_intelligence_profile import (
    AIIntelligenceProfile,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)


@pytest.fixture
def biology_engine() -> BiologicalIntelligenceEngine:
    """Create a biological intelligence engine."""
    return BiologicalIntelligenceEngine()


@pytest.fixture
def ai_engine() -> AIIntelligenceEngine:
    """Create the unified AI intelligence engine."""
    return AIIntelligenceEngine()


@pytest.fixture
def ai_profile(
    biology_engine: BiologicalIntelligenceEngine,
    ai_engine: AIIntelligenceEngine,
) -> AIIntelligenceProfile:
    """Generate a unified AI intelligence profile."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    return ai_engine.analyze(
        biological_profile,
    )


def test_profile_creation(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """AI profile should be created."""
    assert ai_profile is not None


def test_component_count(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Component count should remain fixed."""
    assert ai_profile.component_count == 6


def test_feature_vector_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Feature vector should exist."""
    assert ai_profile.feature_vector is not None


def test_embedding_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Embedding should exist."""
    assert ai_profile.embedding is not None


def test_knowledge_graph_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Knowledge graph should exist."""
    assert ai_profile.knowledge_graph is not None


def test_meta_features_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Meta features should exist."""
    assert ai_profile.meta_features is not None


def test_solver_recommendation_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Solver recommendation should exist."""
    assert ai_profile.solver_recommendation is not None


def test_explanation_present(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """Explanation profile should exist."""
    assert ai_profile.explanation is not None


def test_deterministic_analysis(
    biology_engine: BiologicalIntelligenceEngine,
    ai_engine: AIIntelligenceEngine,
) -> None:
    """AI intelligence generation should be deterministic."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGCGAAAUUUGCGC",
    )

    first = ai_engine.analyze(
        biological_profile,
    )

    second = ai_engine.analyze(
        biological_profile,
    )

    assert first == second


def test_long_sequence(
    biology_engine: BiologicalIntelligenceEngine,
    ai_engine: AIIntelligenceEngine,
) -> None:
    """Long RNA sequences should be supported."""
    biological_profile = biology_engine.analyze(
        "GCGAAACGC" * 25,
    )

    ai_profile = ai_engine.analyze(
        biological_profile,
    )

    assert ai_profile.component_count == 6


def test_profile_is_immutable(
    ai_profile: AIIntelligenceProfile,
) -> None:
    """AI profile should be immutable."""
    with pytest.raises(
        AttributeError,
    ):
        ai_profile.feature_vector = None
