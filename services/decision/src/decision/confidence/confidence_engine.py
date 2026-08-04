"""
Decision Confidence Engine.
"""

from __future__ import annotations


class ConfidenceEngine:
    """
    Unified confidence scoring engine for RNAOS.

    The engine estimates confidence using measurable evidence
    rather than fixed values. The resulting score can be reused
    across solver, optimization, and folding explainers.
    """

    def score(
        self,
        *,
        problem_size: int,
        relative_error: float,
        deterministic_solver: bool,
    ) -> float:
        """
        Compute a confidence score in the range [0.0, 1.0].
        """

        confidence = 1.0

        #
        # Penalize larger optimization problems.
        #

        if problem_size > 100:
            confidence -= 0.10

        if problem_size > 500:
            confidence -= 0.10

        #
        # Penalize optimization disagreement.
        #

        confidence -= min(
            relative_error,
            0.40,
        )

        #
        # Deterministic algorithms increase confidence.
        #

        if deterministic_solver:
            confidence += 0.05

        #
        # Clamp score.
        #

        return max(
            0.0,
            min(confidence, 1.0),
        )
