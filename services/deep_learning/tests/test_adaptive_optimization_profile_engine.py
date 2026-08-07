"""
Tests for adaptive optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.adaptive_optimization_profile import (
    AdaptiveOptimizationProfile,
)
from dl.models.optimization.intelligence_score import (
    IntelligenceScore,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)
from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)
from dl.optimization.adaptive_optimization_profile_engine import (
    AdaptiveOptimizationProfileEngine,
)


def test_adaptive_profile_generation() -> None:
    """
    Adaptive optimization profile is generated.
    """

    intelligence = IntelligenceScore(
        overall_score=0.88,
        solver_strength=0.90,
        learning_strength=0.85,
        evolution_strength=0.89,
    )

    learning = LearningProfile(
        total_experiences=20,
        best_solver="genetic",
        average_reward=0.91,
        confidence=0.91,
    )

    meta = MetaIntelligenceProfile(
        best_algorithm="hybrid_genetic_pso",
        generations=40,
        best_fitness=0.96,
        confidence=0.96,
    )

    engine = AdaptiveOptimizationProfileEngine()

    profile = engine.generate(
        intelligence_score=intelligence,
        learning_profile=learning,
        meta_profile=meta,
    )

    assert isinstance(
        profile,
        AdaptiveOptimizationProfile,
    )

    assert profile.best_solver == "genetic"

    assert profile.intelligence_score == 0.88

    assert profile.learning_confidence == 0.91

    assert profile.meta_confidence == 0.96

    assert profile.adaptability > 0
