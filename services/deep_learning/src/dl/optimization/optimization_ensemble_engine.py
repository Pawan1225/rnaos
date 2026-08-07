"""
RNAOS optimization ensemble engine.
"""

from __future__ import annotations

from dl.models.optimization.ensemble_result import (
    EnsembleResult,
)


class OptimizationEnsembleEngine:
    """
    Combines optimization candidates.
    """

    def select_best(
        self,
        candidates: tuple[
            tuple[str, float],
            ...,
        ],
    ) -> EnsembleResult:
        """
        Select lowest energy candidate.
        """

        if not candidates:
            raise ValueError(
                "Candidates cannot be empty",
            )

        best_solver, best_energy = min(
            candidates,
            key=lambda item: item[1],
        )

        return EnsembleResult(
            selected_solver=best_solver,
            energy=best_energy,
            candidate_count=len(
                candidates,
            ),
        )
