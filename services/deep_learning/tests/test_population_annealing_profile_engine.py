"""
Tests for population annealing profile engine.
"""

from __future__ import annotations

from dl.models.optimization.population_annealing_profile import (
    PopulationAnnealingProfile,
)
from dl.optimization.population_annealing_profile_engine import (
    PopulationAnnealingProfileEngine,
)


def test_population_profile_generation() -> None:
    """
    Population profile is generated.
    """

    engine = PopulationAnnealingProfileEngine()

    profile = engine.generate(
        best_energy=-20.0,
        population_size=50,
        generations=20,
        final_temperature=0.5,
    )

    assert isinstance(
        profile,
        PopulationAnnealingProfile,
    )

    assert profile.best_energy == -20.0

    assert profile.population_size == 50

    assert profile.generations == 20

    assert profile.final_temperature == 0.5

    assert profile.confidence == 0.2
