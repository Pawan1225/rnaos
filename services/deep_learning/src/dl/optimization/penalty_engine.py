"""
RNAOS constraint penalty engine.
"""

from __future__ import annotations

from dl.models.optimization.penalty import (
    PenaltyConfiguration,
)


class ConstraintPenaltyEngine:
    """
    Generates QUBO constraint penalties.
    """

    def create(
        self,
        constraint_name: str,
        penalty_value: float,
    ) -> PenaltyConfiguration:
        """
        Create penalty configuration.
        """

        if penalty_value <= 0:
            raise ValueError(
                "Penalty must be positive",
            )

        return PenaltyConfiguration(
            constraint_name=constraint_name,
            penalty_value=penalty_value,
        )
