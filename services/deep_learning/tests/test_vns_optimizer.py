"""
Tests for VNS optimizer.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.neighborhood_configuration import (
    NeighborhoodConfiguration,
)
from dl.models.optimization.vns_result import (
    VNSResult,
)
from dl.optimization.vns_optimizer import (
    VNSOptimizer,
)


def test_vns_optimizer() -> None:
    """
    VNS optimizer executes.
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

    configuration = NeighborhoodConfiguration(
        levels=(
            1,
            2,
            3,
        ),
        max_iterations=50,
    )

    optimizer = VNSOptimizer()

    result = optimizer.optimize(
        state,
        configuration,
    )

    assert isinstance(
        result,
        VNSResult,
    )

    assert result.best_state == state

    assert result.neighborhood_level == 3

    assert result.iterations == 50
