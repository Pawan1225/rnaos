"""
RNAOS benchmark result collection model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ResultCollectionSummary:
    """
    Immutable result collection summary.
    """

    collection_id: str

    total_results: int

    stored_results: int

    failed_results: int

    benchmark_version: str
