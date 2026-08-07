"""
RNAOS benchmark experiment configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkConfig:
    """
    Immutable benchmark configuration.
    """

    config_id: str

    dataset_size: int

    sequence_length: int

    random_seed: int

    solver: str

    optimization_method: str

    version: str
