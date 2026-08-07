"""
RNAOS quantum-inspired feature models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QuantumFeatureVector:
    """
    Immutable quantum-inspired feature vector.
    """

    values: tuple[float, ...]

    dimension: int

    normalization: float
