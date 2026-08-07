"""
RNAOS QUBO intelligence profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QUBOProfile:
    """
    Immutable QUBO intelligence profile.
    """

    problem_name: str

    variable_count: int

    matrix_size: int

    minimum_energy: float

    maximum_energy: float
