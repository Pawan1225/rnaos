"""
RNAOS optimization request validator.
"""

from __future__ import annotations

from dl.models.optimization.optimization_request import (
    OptimizationIntelligenceRequest,
)


class OptimizationRequestValidator:
    """
    Validates optimization requests.
    """

    def validate(
        self,
        request: OptimizationIntelligenceRequest,
    ) -> bool:
        """
        Validate request fields.
        """

        if request.sequence_length <= 0:
            raise ValueError(
                "Sequence length must be positive",
            )

        if request.complexity_score < 0:
            raise ValueError(
                "Complexity cannot be negative",
            )

        if request.folding_difficulty < 0:
            raise ValueError(
                "Folding difficulty cannot be negative",
            )

        return True
