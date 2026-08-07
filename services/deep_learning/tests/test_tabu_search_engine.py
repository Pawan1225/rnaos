"""
Tests for tabu search engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.tabu_search_result import (
    TabuSearchResult,
)
from dl.optimization.tabu_search_engine import (
    TabuSearchEngine,
)


def test_tabu_search() -> None:
    """
    Tabu search executes.
    """

    state = LocalSearchState(
        state_id=1,
        solution=(
            1,
            -1,
            1,
        ),
        energy=-8.0,
        iteration=1,
    )

    engine = TabuSearchEngine()

    result = engine.optimize(
        state,
        iterations=10,
        tabu_size=5,
    )

    assert isinstance(
        result,
        TabuSearchResult,
    )

    assert result.best_state == state

    assert result.iterations == 10

    assert result.tabu_size == 5
