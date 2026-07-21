"""
RNA Complexity Estimation Engine

Estimates the computational complexity of optimizing an RNA sequence.
"""

from __future__ import annotations

from dataclasses import dataclass

from rna_intelligence.profilers.rna_profiler import RNAProfile


@dataclass(slots=True)
class ComplexityEstimate:
    """Complexity assessment for an RNA sequence."""

    score: float
    category: str
    explanation: str


class ComplexityEstimator:
    """Estimate RNA optimization complexity."""

    def estimate(self, profile: RNAProfile) -> ComplexityEstimate:
        """
        Estimate optimization complexity from an RNA profile.
        """

        features = profile.features

        # Normalize sequence length
        length_score = min(features.length / 500.0, 1.0)

        # Normalize entropy
        entropy_score = min(features.sequence_entropy / 2.0, 1.0)

        # Balanced GC content is considered more complex
        gc_balance = 1.0 - abs(features.gc_content - 0.5) * 2.0
        gc_balance = max(0.0, gc_balance)

        score = 0.50 * length_score + 0.30 * entropy_score + 0.20 * gc_balance

        score = round(score, 3)

        if score < 0.33:
            category = "easy"
        elif score < 0.66:
            category = "moderate"
        else:
            category = "hard"

        return ComplexityEstimate(
            score=score,
            category=category,
            explanation=(
                f"Length={features.length}, "
                f"Entropy={features.sequence_entropy:.3f}, "
                f"GC={features.gc_content:.3f}"
            ),
        )
