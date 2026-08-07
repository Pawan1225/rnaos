"""
RNAOS differential mutation result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)


@dataclass(
    slots=True,
    frozen=True,
)
class MutationVectorResult:
    """
    Immutable differential mutation result.
    """

    base_vector_id: int

    mutant_vector: DifferentialVector
