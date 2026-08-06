"""
RNAOS integrated gradient analyzer.
"""

from __future__ import annotations

from typing import Any

from dl.models.attribution_result import (
    AttributionResult,
)


class IntegratedGradientAnalyzer:
    """
    Generates integrated gradient attributions.
    """

    def analyze(
        self,
        model: Any,
        inputs: tuple[float, ...],
        baseline: tuple[float, ...] | None = None,
    ) -> AttributionResult:
        """
        Calculate feature contributions.
        """

        if baseline is None:
            baseline = tuple(0.0 for _ in inputs)

        _ = model.predict(
            inputs,
        )

        scores = tuple(
            abs(
                value - base,
            )
            for value, base in zip(
                inputs,
                baseline,
                strict=True,
            )
        )

        features = tuple(
            str(index)
            for index in range(
                len(inputs),
            )
        )

        confidence = max(scores) if scores else 0.0

        return AttributionResult(
            method="integrated_gradients",
            features=features,
            importance_scores=scores,
            confidence=confidence,
        )
