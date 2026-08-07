"""
RNAOS visualization report model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class VisualizationReport:
    """
    Immutable visualization report.
    """

    report_id: str

    experiment_id: str

    figures: tuple[str, ...]

    formats: tuple[str, ...]

    metadata: tuple[str, ...]
