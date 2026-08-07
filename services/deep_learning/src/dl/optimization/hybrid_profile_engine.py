"""
RNAOS hybrid optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_profile import (
    HybridOptimizationProfile,
)


class HybridProfileEngine:
    """
    Generates hybrid intelligence profiles.
    """

    def generate(
        self,
        strategy: str,
        selected_solver: str,
        solvers_used: tuple[str, ...],
        final_energy: float,
        confidence: float,
        stages_completed: int,
    ) -> HybridOptimizationProfile:
        """
        Generate hybrid optimization profile.
        """

        return HybridOptimizationProfile(
            strategy=strategy,
            selected_solver=selected_solver,
            solvers_used=solvers_used,
            final_energy=final_energy,
            confidence=confidence,
            stages_completed=stages_completed,
        )
