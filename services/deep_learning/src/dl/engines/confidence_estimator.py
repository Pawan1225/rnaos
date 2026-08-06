"""
RNAOS prediction confidence estimator.
"""

from __future__ import annotations


class ConfidenceEstimator:
    """
    Estimates prediction reliability.
    """

    def estimate(
        self,
        prediction_value: float,
    ) -> float:
        """
        Generate normalized confidence score.
        """

        confidence = abs(
            prediction_value,
        )

        return min(
            max(
                confidence,
                0.0,
            ),
            1.0,
        )
