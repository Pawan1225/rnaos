"""
RNAOS differential recombination result model.
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
class RecombinationResult:
    """
    Immutable recombination result.
    """

    target_id: int

    trial_vector: DifferentialVector

    changed_dimensions: int
