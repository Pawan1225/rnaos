"""
Tests for hybrid optimization profile.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_profile import (
    HybridOptimizationProfile,
)


def test_hybrid_optimization_profile() -> None:
    """
    Profile can be created.
    """

    profile = HybridOptimizationProfile(
        system_name="RNAOS",
        version="14.6",
        optimization_layers=(
            "biological",
            "ai",
            "ml",
            "deep_learning",
            "quantum_inspired",
            "hybrid",
        ),
        active_engines=(
            "solver_runtime",
            "execution_manager",
            "ensemble_engine",
            "pipeline_engine",
            "refinement_engine",
            "hybrid_engine",
        ),
        supported_strategies=(
            "multi_solver",
            "ensemble",
            "multi_stage",
        ),
        validation_status="passed",
    )

    assert profile.system_name == ("RNAOS")

    assert profile.version == ("14.6")

    assert (
        len(
            profile.optimization_layers,
        )
        == 6
    )

    assert (
        len(
            profile.active_engines,
        )
        == 6
    )

    assert profile.validation_status == ("passed")
