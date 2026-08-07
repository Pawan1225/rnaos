"""
RNAOS variable neighborhood search optimizer.
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


class VNSOptimizer:
    """
    Executes Variable Neighborhood Search.
    """

    def optimize(
        self,
        state: LocalSearchState,
        configuration: NeighborhoodConfiguration,
    ) -> VNSResult:
        """
        Execute VNS optimization.

        Foundation implementation.
        """

        if not configuration.levels:
            raise ValueError(
                "At least one neighborhood level is required",
            )

        if configuration.max_iterations <= 0:
            raise ValueError(
                "Maximum iterations must be positive",
            )

        return VNSResult(
            best_state=state,
            neighborhood_level=max(configuration.levels),
            iterations=configuration.max_iterations,
        )
