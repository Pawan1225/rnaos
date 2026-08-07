"""
Tests for final intelligence profile.
"""

from __future__ import annotations

from dl.models.optimization.final_intelligence_profile import (
    FinalIntelligenceProfile,
)


def test_final_intelligence_profile() -> None:
    """
    Final profile can be created.
    """

    profile = FinalIntelligenceProfile(
        system_name="RNAOS",
        version="14.5",
        active_solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        intelligence_score=0.95,
        validation_status="passed",
    )

    assert profile.system_name == "RNAOS"

    assert profile.version == "14.5"

    assert (
        len(
            profile.active_solvers,
        )
        == 3
    )

    assert profile.active_solvers == (
        "ising",
        "genetic",
        "tabu",
    )

    assert profile.intelligence_score == 0.95

    assert profile.validation_status == "passed"
