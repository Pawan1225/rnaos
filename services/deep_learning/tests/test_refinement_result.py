"""
Tests for refinement result.
"""

from __future__ import annotations

from dl.models.optimization.refinement_result import (
    RefinementResult,
)


def test_refinement_result() -> None:
    """
    Refinement result can be created.
    """

    result = RefinementResult(
        candidate_id=1,
        original_energy=-45.2,
        improved_energy=-47.1,
        improvement_score=0.92,
        status="completed",
    )

    assert result.candidate_id == 1

    assert result.original_energy == -45.2

    assert result.improved_energy == -47.1

    assert result.improvement_score == 0.92

    assert result.status == ("completed")
