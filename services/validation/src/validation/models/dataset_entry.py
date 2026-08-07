"""
RNA benchmark dataset entry model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DatasetEntry:
    """
    Immutable RNA dataset sample.
    """

    sequence_id: str

    sequence: str

    length: int

    category: str

    seed: int

    metadata: tuple[str, ...]
