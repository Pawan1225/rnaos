"""
RNAOS tabu search engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.tabu_search_result import (
    TabuSearchResult,
)


class TabuSearchEngine:
    """
    Performs tabu-based local search.
    """

    def optimize(
        self,
        state: LocalSearchState,
        iterations: int,
        tabu_size: int,
    ) -> TabuSearchResult:
        """
        Execute tabu search.

        This sprint establishes the orchestration layer.
        Neighbor evaluation and tabu-memory integration will
        be expanded in later optimization sprints.
        """

        if iterations <= 0:
            raise ValueError(
                "Iterations must be positive",
            )

        if tabu_size <= 0:
            raise ValueError(
                "Tabu size must be positive",
            )

        best = state

        return TabuSearchResult(
            best_state=best,
            iterations=iterations,
            tabu_size=tabu_size,
        )
