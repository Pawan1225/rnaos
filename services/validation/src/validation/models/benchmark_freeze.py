"""
RNAOS benchmark freeze model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkFreeze:
    """
    Immutable benchmark freeze record.
    """

    freeze_id: str

    benchmark_version: str

    total_experiments: int

    artifact_count: int

    status: str
