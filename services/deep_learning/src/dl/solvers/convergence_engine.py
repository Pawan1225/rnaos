"""
RNAOS convergence detection engine.
"""

from __future__ import annotations

from dl.models.optimization.convergence_result import (
    ConvergenceResult,
)


class ConvergenceDetectionEngine:
    """
    Detects optimization convergence.
    """

    def __init__(
        self,
        tolerance: float = 0.001,
    ) -> None:
        self.tolerance = tolerance

    def evaluate(
        self,
        previous_energy: float,
        current_energy: float,
    ) -> ConvergenceResult:
        """
        Evaluate energy improvement.
        """

        improvement = abs(current_energy - previous_energy)

        return ConvergenceResult(
            converged=(improvement <= self.tolerance),
            improvement=improvement,
        )
