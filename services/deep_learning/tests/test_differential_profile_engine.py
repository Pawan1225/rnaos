"""
Tests for differential profile engine.
"""

from __future__ import annotations

from dl.models.optimization.differential_profile import (
    DifferentialProfile,
)
from dl.optimization.differential_profile_engine import (
    DifferentialProfileEngine,
)


def test_differential_profile_generation() -> None:
    """
    Differential profile is generated.
    """

    engine = DifferentialProfileEngine()

    profile = engine.generate(
        best_fitness=0.97,
        generations=50,
        vector_dimension=5,
    )

    assert isinstance(
        profile,
        DifferentialProfile,
    )

    assert profile.best_fitness == 0.97

    assert profile.generations == 50

    assert profile.vector_dimension == 5

    assert profile.confidence == 0.5
