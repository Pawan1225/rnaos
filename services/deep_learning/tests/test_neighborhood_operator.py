"""
Tests for neighborhood operator.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.neighborhood_operator_result import (
    NeighborhoodOperatorResult,
)
from dl.optimization.neighborhood_operator import (
    NeighborhoodOperator,
)


def test_neighborhood_operator() -> None:
    """
    Neighborhood operator generates
    deterministic perturbations.
    """

    state = LocalSearchState(
        state_id=1,
        solution=(
            1,
            -1,
            1,
            -1,
        ),
        energy=-10.0,
        iteration=1,
    )

    operator = NeighborhoodOperator()

    result = operator.generate(
        state,
        level=2,
    )

    assert isinstance(
        result,
        NeighborhoodOperatorResult,
    )

    assert result.level == 2

    assert result.state.solution == (
        -1,
        1,
        1,
        -1,
    )

    assert result.state.iteration == 2
