"""
Tests for solution refinement engine.
"""

from __future__ import annotations

from dl.models.optimization.refinement_request import (
    RefinementRequest,
)
from dl.models.optimization.refinement_result import (
    RefinementResult,
)
from dl.optimization.runtime.refinement_engine import (
    SolutionRefinementEngine,
)


def test_solution_refinement() -> None:
    """
    Engine improves candidate energy.
    """

    request = RefinementRequest(
        candidate_id=1,
        structure=(
            "A",
            "U",
            "G",
        ),
        current_energy=-45.2,
        strategy="local_search",
    )

    engine = SolutionRefinementEngine()

    result = engine.refine(
        request,
    )

    assert isinstance(
        result,
        RefinementResult,
    )

    assert result.improved_energy < (result.original_energy)

    assert result.status == ("completed")
