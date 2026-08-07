"""
RNAOS plot configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PlotConfiguration:
    """
    Immutable scientific plot configuration.
    """

    plot_id: str

    title: str

    metric: str

    chart_type: str

    formats: tuple[str, ...]

    width: float

    height: float

    dpi: int

    metadata: tuple[str, ...]
