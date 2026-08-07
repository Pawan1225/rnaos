"""
Tests for result comparison model.
"""

from __future__ import annotations

from dl.models.optimization.optimization_candidate import (
    OptimizationCandidate,
)
from dl.models.optimization.result_comparison import (
    ResultComparison,
)


def test_result_comparison() -> None:
    """
    Result comparison can be created.
    """

    candidate_one = OptimizationCandidate(
        candidate_id=1,
        solver_name="ising",
        fitness=0.91,
        quality=0.89,
    )

    candidate_two = OptimizationCandidate(
        candidate_id=2,
        solver_name="genetic",
        fitness=0.96,
        quality=0.93,
    )

    comparison = ResultComparison(
        candidates=(
            candidate_one,
            candidate_two,
        ),
        best_candidate=candidate_two,
        comparison_metric="fitness",
    )

    assert (
        len(
            comparison.candidates,
        )
        == 2
    )

    assert comparison.best_candidate.solver_name == "genetic"

    assert comparison.comparison_metric == "fitness"
