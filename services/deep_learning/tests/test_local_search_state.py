"""
Tests for local search state.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)


def test_local_search_state_creation() -> None:
    """
    Local search state can be created.
    """

    state = LocalSearchState(
        state_id=1,
        solution=(
            1,
            -1,
            1,
        ),
        energy=-10.0,
        iteration=5,
    )

    assert state.state_id == 1

    assert state.solution == (
        1,
        -1,
        1,
    )

    assert state.energy == -10.0

    assert state.iteration == 5
