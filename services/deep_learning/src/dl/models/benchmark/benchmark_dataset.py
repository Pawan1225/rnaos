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
    Immutable benchmark dataset definition.
    """

    dataset_id: str

    name: str

    version: str

    samples: tuple[str, ...]

    source: str

    status: str
