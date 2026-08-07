"""
Tests for solver candidate.
"""

from __future__ import annotations

from dl.models.optimization.solver_candidate import (
    SolverCandidate,
)


def test_solver_candidate() -> None:
    """
    Candidate can be created.
    """

    candidate = SolverCandidate(
        candidate_id=1,
        source_solver="ising",
        structure=(
            "A",
            "U",
            "G",
        ),
        energy=-45.2,
        score=0.95,
    )

    assert candidate.candidate_id == 1

    assert candidate.source_solver == "ising"

    assert (
        len(
            candidate.structure,
        )
        == 3
    )

    assert candidate.energy == -45.2

    assert candidate.score == 0.95
