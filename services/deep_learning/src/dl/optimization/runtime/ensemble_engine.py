"""
RNAOS ensemble optimization engine.
"""

from __future__ import annotations

from dl.models.optimization.ensemble_result import (
    EnsembleResult,
)
from dl.models.optimization.solver_candidate import (
    SolverCandidate,
)


class EnsembleOptimizationEngine:
    """
    Combines multiple solver candidates.
    """

    def optimize(
        self,
        candidates: tuple[SolverCandidate, ...],
    ) -> EnsembleResult:
        """
        Select the best candidate.
        """

        selected = max(
            candidates,
            key=lambda candidate: candidate.score,
        )

        consensus_score = sum(candidate.score for candidate in candidates) / len(candidates)

        return EnsembleResult(
            candidates=candidates,
            selected_candidate=selected,
            consensus_score=consensus_score,
            confidence=selected.score,
            status="completed",
        )
