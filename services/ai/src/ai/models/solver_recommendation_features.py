"""
RNAOS solver recommendation feature model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SolverRecommendationFeatures:
    """
    Immutable AI-derived solver recommendation features.

    These features characterize the optimization problem
    and estimate the suitability of different solver
    families.
    """

    optimization_difficulty: float

    search_space_complexity: float

    constraint_density: float

    expected_runtime: float

    classical_affinity: float

    quantum_affinity: float

    hybrid_affinity: float

    recommendation_confidence: float

    @property
    def feature_count(
        self,
    ) -> int:
        """
        Number of recommendation features.
        """
        return 8
