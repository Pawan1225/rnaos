"""
RNAOS attention visualization engine.
"""

from __future__ import annotations

from typing import Any

from dl.models.attribution_result import (
    AttributionResult,
)


class AttentionVisualizationEngine:
    """
    Converts attention weights into explanations.
    """

    def analyze(
        self,
        model: Any,
        sequence_length: int,
    ) -> AttributionResult:
        """
        Generate attention attribution.
        """

        attention = model.get_attention()

        scores = tuple(float(value) for value in attention[:sequence_length])

        features = tuple(
            str(index)
            for index in range(
                sequence_length,
            )
        )

        confidence = max(scores) if scores else 0.0

        return AttributionResult(
            method="attention",
            features=features,
            importance_scores=scores,
            confidence=confidence,
        )
