"""
RNAOS scientific result freeze model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ScientificResultFreeze:
    """
    Immutable scientific result freeze.
    """

    freeze_id: str

    benchmark_id: str

    total_experiments: int

    result_version: str

    status: str
