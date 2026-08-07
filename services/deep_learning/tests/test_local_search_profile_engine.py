"""
Tests for local search profile engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_profile import (
    LocalSearchProfile,
)
from dl.optimization.local_search_profile_engine import (
    LocalSearchProfileEngine,
)


def test_local_search_profile_generation() -> None:
    """
    Local search profile is generated.
    """

    engine = LocalSearchProfileEngine()

    profile = engine.generate(
        best_energy=-15.0,
        iterations=40,
        search_strategy="variable_neighborhood_search",
    )

    assert isinstance(
        profile,
        LocalSearchProfile,
    )

    assert profile.best_energy == -15.0

    assert profile.iterations == 40

    assert profile.search_strategy == "variable_neighborhood_search"

    assert profile.confidence == 0.4
