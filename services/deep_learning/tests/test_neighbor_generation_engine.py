"""
Tests for neighbor generation engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.neighbor_result import (
    NeighborResult,
)
from dl.optimization.neighbor_generation_engine import (
    NeighborGenerationEngine,
)


def test_neighbor_generation() -> None:
    """
    Neighbor states are generated.
    """

    state = LocalSearchState(
        state_id=1,
        solution=(
            1,
            -1,
            1,
        ),
        energy=-5.0,
        iteration=1,
    )

    engine = NeighborGenerationEngine()

    result = engine.generate(
        state,
    )

    assert isinstance(
        result,
        NeighborResult,
    )

    assert result.source_id == 1

    assert (
        len(
            result.neighbors,
        )
        == 3
    )

    assert result.neighbors[0].solution == (
        -1,
        -1,
        1,
    )

    assert result.neighbors[1].solution == (
        1,
        1,
        1,
    )

    assert result.neighbors[2].solution == (
        1,
        -1,
        -1,
    )

    assert all(neighbor.iteration == 2 for neighbor in result.neighbors)
