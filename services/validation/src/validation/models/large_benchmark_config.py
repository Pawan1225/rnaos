"""
RNAOS large benchmark configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LargeBenchmarkConfig:
    """
    Immutable large benchmark configuration.
    """

    benchmark_id: str

    sequence_lengths: tuple[int, ...]

    samples_per_length: int

    random_seed: int

    solver_version: str

    benchmark_version: str

    total_experiments: int
