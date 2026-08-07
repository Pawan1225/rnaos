"""
RNAOS intelligence evaluation engine.
"""

from __future__ import annotations

from dl.models.optimization.adaptive_optimization_profile import (
    AdaptiveOptimizationProfile,
)
from dl.models.optimization.intelligence_evaluation import (
    IntelligenceEvaluation,
)


class IntelligenceEvaluationEngine:
    """
    Evaluates unified optimization intelligence.
    """

    def evaluate(
        self,
        profile: AdaptiveOptimizationProfile,
    ) -> IntelligenceEvaluation:
        """
        Evaluate adaptive optimization profile.
        """

        overall_score = (
            profile.intelligence_score + profile.learning_confidence + profile.evolution_confidence
        ) / 3.0

        passed = overall_score >= 0.80

        recommendation = "Deploy" if passed else "Improve"

        return IntelligenceEvaluation(
            overall_score=overall_score,
            passed=passed,
            recommendation=recommendation,
        )
