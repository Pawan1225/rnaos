"""
RNAOS QUBO profile generation engine.
"""

from __future__ import annotations

from dl.models.optimization.q_matrix import (
    QMatrix,
)
from dl.models.optimization.qubo_profile import (
    QUBOProfile,
)


class QUBOProfileEngine:
    """
    Generates QUBO intelligence profiles.
    """

    def generate(
        self,
        problem_name: str,
        matrix: QMatrix,
    ) -> QUBOProfile:
        """
        Generate QUBO metadata profile.
        """

        values = tuple(value for row in matrix.values for value in row)

        return QUBOProfile(
            problem_name=problem_name,
            variable_count=len(
                matrix.variables,
            ),
            matrix_size=len(
                matrix.values,
            ),
            minimum_energy=min(
                values,
            ),
            maximum_energy=max(
                values,
            ),
        )
