"""
Tests for PSO profile engine.
"""

from __future__ import annotations

from dl.models.optimization.pso_profile import (
    PSOProfile,
)
from dl.optimization.pso_profile_engine import (
    PSOProfileEngine,
)


def test_pso_profile_generation() -> None:
    """
    PSO profile is generated.
    """

    engine = PSOProfileEngine()

    profile = engine.generate(
        best_fitness=0.98,
        iterations=50,
        swarm_size=20,
    )

    assert isinstance(
        profile,
        PSOProfile,
    )

    assert profile.best_fitness == 0.98

    assert profile.iterations == 50

    assert profile.swarm_size == 20

    assert profile.confidence == 0.5
