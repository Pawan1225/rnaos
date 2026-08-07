"""
Tests for hill climbing engine.
"""

from __future__ import annotations

from dl.models.optimization.hill_climbing_result import (
    HillClimbingResult,
)
from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.optimization.hill_climbing_engine import (
    HillClimbingEngine,
)


def test_hill_climbing() -> None:
    """
    Hill climbing executes.
    """

    state = LocalSearchState(
        state_id=1,
        solution=(
            1,
            -1,
            1,
        ),
        energy=-10.0,
        iteration=1,
    )

    engine = HillClimbingEngine()

    result = engine.optimize(
        state,
        iterations=5,
    )

    assert isinstance(
        result,
        HillClimbingResult,
    )

    assert result.iterations == 5

    assert result.best_state.state_id == 1

    assert result.best_state.energy == -10.0

    assert result.improved is False
