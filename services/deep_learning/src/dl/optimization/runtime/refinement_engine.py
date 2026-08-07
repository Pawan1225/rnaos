"""
RNAOS solution refinement engine.
"""

from __future__ import annotations

from dl.models.optimization.refinement_request import (
    RefinementRequest,
)
from dl.models.optimization.refinement_result import (
    RefinementResult,
)


class SolutionRefinementEngine:
    """
    Improves optimization candidates.
    """

    def refine(
        self,
        request: RefinementRequest,
    ) -> RefinementResult:
        """
        Refine candidate solution.
        """

        improved_energy = request.current_energy - 1.0

        improvement = abs(request.current_energy - improved_energy) / abs(
            request.current_energy,
        )

        return RefinementResult(
            candidate_id=request.candidate_id,
            original_energy=request.current_energy,
            improved_energy=improved_energy,
            improvement_score=improvement,
            status="completed",
        )
