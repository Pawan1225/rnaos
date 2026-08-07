"""
RNAOS scientific benchmark report model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ScientificReport:
    """
    Immutable scientific report.
    """

    report_id: str

    title: str

    experiment_id: str

    summary: str

    results: tuple[str, ...]

    statistics: tuple[str, ...]

    figures: tuple[str, ...]

    conclusions: tuple[str, ...]

    metadata: tuple[str, ...]
