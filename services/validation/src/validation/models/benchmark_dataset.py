"""
RNAOS benchmark dataset model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkDataset:
    """
    Immutable RNA benchmark dataset.
    """

    dataset_id: str

    version: str

    sequences: tuple[str, ...]

    sequence_lengths: tuple[int, ...]

    source: str

    random_seed: int

    metadata: tuple[str, ...]
