"""
RNAOS deep learning validation engine.
"""

from __future__ import annotations

from typing import Any

from dl.models.validation_result import (
    ValidationResult,
)


class ValidationEngine:
    """
    Executes validation workflows.
    """

    def validate(
        self,
        model: Any,
        dataset: tuple[Any, ...],
    ) -> ValidationResult:
        """
        Validate model performance.
        """

        samples = len(
            dataset,
        )

        metrics = model.evaluate(
            dataset,
        )

        return ValidationResult(
            validation_loss=metrics["loss"],
            validation_accuracy=metrics["accuracy"],
            samples_evaluated=samples,
            success=True,
        )
