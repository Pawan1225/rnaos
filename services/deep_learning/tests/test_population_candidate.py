"""
Tests for population candidate.
"""

from __future__ import annotations

from dl.models.optimization.population_candidate import (
    PopulationCandidate,
)


def test_population_candidate_creation() -> None:
    """
    Candidate can be created.
    """

    candidate = PopulationCandidate(
        candidate_id=1,
        state=(
            1,
            -1,
            1,
        ),
        energy=-10.0,
        fitness=0.95,
    )

    assert candidate.candidate_id == 1
    assert candidate.state == (
        1,
        -1,
        1,
    )
    assert candidate.energy == -10.0
    assert candidate.fitness == 0.95
