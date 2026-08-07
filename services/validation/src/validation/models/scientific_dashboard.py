"""
RNAOS scientific dashboard model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ScientificDashboard:
    """
    Immutable scientific dashboard metadata.
    """

    dashboard_id: str

    title: str

    metrics: tuple[str, ...]

    figures: tuple[str, ...]

    benchmark_version: str

    version: str
