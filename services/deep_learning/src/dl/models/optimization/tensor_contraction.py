"""
RNAOS tensor contraction models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorContractionResult:
    """
    Immutable tensor contraction result.
    """

    left_size: int

    right_size: int

    output_size: int

    values: tuple[float, ...]
