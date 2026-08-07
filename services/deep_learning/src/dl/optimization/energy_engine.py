"""
RNAOS QUBO energy evaluation engine.
"""

from __future__ import annotations

from dl.models.optimization.energy_result import (
    EnergyResult,
)
from dl.models.optimization.q_matrix import (
    QMatrix,
)


class EnergyEvaluationEngine:
    """
    Calculates QUBO energies.
    """

    def evaluate(
        self,
        matrix: QMatrix,
        state: tuple[int, ...],
    ) -> EnergyResult:
        """
        Calculate:

        E(x)=x^TQx
        """

        size = len(
            matrix.variables,
        )

        if len(state) != size:
            raise ValueError(
                "State dimension mismatch",
            )

        energy = 0.0

        for i in range(size):
            for j in range(size):
                energy += state[i] * matrix.values[i][j] * state[j]

        return EnergyResult(
            energy=energy,
            valid=True,
        )
