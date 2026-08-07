"""
RNAOS runtime scaling analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RuntimeScalingAnalysis:
    """
    Immutable runtime scaling result.
    """

    analysis_id: str

    sample_count: int

    average_runtime: float

    minimum_runtime: float

    maximum_runtime: float

    scaling_factor: float

    benchmark_version: str
