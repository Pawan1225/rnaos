"""
RNAOS explanation report model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.attribution_result import (
    AttributionResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class ExplanationReport:
    """
    Immutable explanation report.
    """

    prediction_task: str

    prediction_value: float

    explanations: tuple[AttributionResult, ...]

    confidence: float

    completed: bool
