"""
RNAOS large benchmark dataset model.
"""

from __future__ import annotations

from dataclasses import dataclass

from validation.models.dataset_entry import (
    DatasetEntry,
)


@dataclass(
    slots=True,
    frozen=True,
)
class LargeBenchmarkDataset:
    """
    Immutable large benchmark dataset.
    """

    dataset_id: str

    total_sequences: int

    sequence_lengths: tuple[int, ...]

    entries: tuple[DatasetEntry, ...]

    version: str
