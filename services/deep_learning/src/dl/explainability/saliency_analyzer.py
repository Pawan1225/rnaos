"""
RNAOS saliency analyzer.
"""

from __future__ import annotations

from typing import Any

from dl.models.attribution_result import (
    AttributionResult,
)


class SaliencyAnalyzer:
    """
    Generates input feature importance.
    """

    def analyze(
        self,
        model: Any,
        inputs: tuple[float, ...],
    ) -> AttributionResult:
        """
        Calculate saliency scores.
        """

        _ = model.predict(
            inputs,
        )

        scores = tuple(abs(value) for value in inputs)

        features = tuple(
            str(index)
            for index in range(
                len(inputs),
            )
        )

        confidence = max(scores) if scores else 0.0

        return AttributionResult(
            method="saliency",
            features=features,
            importance_scores=scores,
            confidence=confidence,
        )
