"""
Tests for genetic profile engine.
"""

from __future__ import annotations

from dl.models.optimization.genetic_profile import (
    GeneticProfile,
)
from dl.optimization.genetic_profile_engine import (
    GeneticProfileEngine,
)


def test_genetic_profile_generation() -> None:
    """
    Genetic profile is generated.
    """

    engine = GeneticProfileEngine()

    profile = engine.generate(
        best_fitness=0.95,
        generations=50,
        mutations=10,
    )

    assert isinstance(
        profile,
        GeneticProfile,
    )

    assert profile.best_fitness == 0.95

    assert profile.generations == 50

    assert profile.mutations == 10

    assert profile.confidence == 0.5
