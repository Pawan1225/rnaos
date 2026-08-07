"""
RNAOS batch experiment result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BatchResult:
    """
    Immutable batch execution summary.
    """

    batch_id: str

    total_sequences: int

    completed_sequences: int

    failed_sequences: int

    version: str
