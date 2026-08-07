"""
Tests for QUBO profile engine.
"""

from __future__ import annotations

from dl.models.optimization.q_matrix import (
    QMatrix,
)
from dl.models.optimization.qubo_profile import (
    QUBOProfile,
)
from dl.optimization.qubo_profile_engine import (
    QUBOProfileEngine,
)


def test_generate_qubo_profile() -> None:
    """
    QUBO profile is generated.
    """

    engine = QUBOProfileEngine()

    matrix = QMatrix(
        variables=(
            "x0",
            "x1",
        ),
        values=(
            (
                -3.0,
                0.0,
            ),
            (
                0.0,
                -2.0,
            ),
        ),
    )

    profile = engine.generate(
        problem_name="rna_folding",
        matrix=matrix,
    )

    assert isinstance(
        profile,
        QUBOProfile,
    )

    assert profile.variable_count == 2

    assert profile.minimum_energy == -3.0
