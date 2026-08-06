"""
RNAOS compute intelligence profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ComputeProfile:
    """
    Immutable compute recommendation.
    """

    backend: str

    device_count: int

    estimated_memory_gb: float
