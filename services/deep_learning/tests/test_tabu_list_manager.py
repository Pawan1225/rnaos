"""
Tests for tabu list manager.
"""

from __future__ import annotations

from dl.models.optimization.tabu_list_result import (
    TabuListResult,
)
from dl.optimization.tabu_list_manager import (
    TabuListManager,
)


def test_tabu_list_manager() -> None:
    """
    Tabu states are maintained.
    """

    manager = TabuListManager()

    result = manager.add(
        states=(
            (
                1,
                -1,
            ),
        ),
        new_state=(
            -1,
            1,
        ),
        tenure=2,
    )

    assert isinstance(
        result,
        TabuListResult,
    )

    assert result.size == 2

    assert manager.contains(
        result.states,
        (
            -1,
            1,
        ),
    )

    assert not manager.contains(
        result.states,
        (
            1,
            1,
        ),
    )
