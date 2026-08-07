"""
Tests for hybrid profile engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_profile import (
    HybridOptimizationProfile,
)
from dl.optimization.hybrid_profile_engine import (
    HybridProfileEngine,
)


def test_hybrid_profile_generation() -> None:
    """
    Hybrid profile is generated.
    """

    engine = HybridProfileEngine()

    profile = engine.generate(
        strategy="adaptive_hybrid",
        selected_solver="annealing",
        solvers_used=(
            "qubo",
            "annealing",
            "tensor",
        ),
        final_energy=-15.0,
        confidence=0.95,
        stages_completed=5,
    )

    assert isinstance(
        profile,
        HybridOptimizationProfile,
    )

    assert profile.selected_solver == ("annealing")

    assert profile.stages_completed == 5
