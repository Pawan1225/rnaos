"""
Tests for annealing profile engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_configuration import (
    AnnealingConfiguration,
)
from dl.models.optimization.annealing_profile import (
    AnnealingProfile,
)
from dl.solvers.annealing_profile_engine import (
    AnnealingProfileEngine,
)


def test_profile_generation() -> None:
    """
    Annealing profile is generated.
    """

    engine = AnnealingProfileEngine()

    config = AnnealingConfiguration(
        initial_temperature=10.0,
        minimum_temperature=0.01,
        cooling_rate=0.95,
        iterations=1000,
        seed=42,
    )

    profile = engine.generate(
        config=config,
        algorithm="simulated_annealing",
        cooling_strategy="exponential",
        acceptance_strategy="metropolis",
        restart_enabled=True,
        convergence_threshold=0.001,
    )

    assert isinstance(
        profile,
        AnnealingProfile,
    )

    assert profile.algorithm == ("simulated_annealing")

    assert profile.restart_enabled is True
