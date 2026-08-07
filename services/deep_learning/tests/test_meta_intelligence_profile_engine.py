"""
Tests for meta intelligence profile engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)
from dl.optimization.meta_intelligence_profile_engine import (
    MetaIntelligenceProfileEngine,
)


def test_meta_profile_generation() -> None:
    """
    Meta intelligence profile is generated.
    """

    engine = MetaIntelligenceProfileEngine()

    profile = engine.generate(
        best_algorithm="hybrid_genetic_pso",
        generations=50,
        best_fitness=0.97,
    )

    assert isinstance(
        profile,
        MetaIntelligenceProfile,
    )

    assert profile.best_algorithm == "hybrid_genetic_pso"

    assert profile.generations == 50

    assert profile.best_fitness == 0.97

    assert profile.confidence == 0.97


def test_meta_profile_empty_algorithm() -> None:
    """
    Empty algorithm name is rejected.
    """

    engine = MetaIntelligenceProfileEngine()

    with pytest.raises(ValueError):
        engine.generate(
            best_algorithm="",
            generations=10,
            best_fitness=0.90,
        )


def test_meta_profile_invalid_generations() -> None:
    """
    Non-positive generations are rejected.
    """

    engine = MetaIntelligenceProfileEngine()

    with pytest.raises(ValueError):
        engine.generate(
            best_algorithm="genetic",
            generations=0,
            best_fitness=0.90,
        )


def test_meta_profile_invalid_fitness() -> None:
    """
    Negative fitness is rejected.
    """

    engine = MetaIntelligenceProfileEngine()

    with pytest.raises(ValueError):
        engine.generate(
            best_algorithm="genetic",
            generations=10,
            best_fitness=-0.10,
        )
