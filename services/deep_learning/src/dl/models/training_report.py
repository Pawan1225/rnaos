"""
RNAOS training report model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.training_result import (
    TrainingResult,
)
from dl.models.validation_result import (
    ValidationResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class TrainingReport:
    """
    Immutable complete training report.
    """

    training_result: TrainingResult

    validation_result: ValidationResult

    checkpoint_id: str

    completed: bool
