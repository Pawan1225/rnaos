"""
Tests for validation pipeline.
"""

from validation.pipelines.validation_pipeline import (
    ValidationPipeline,
)


def test_validation_pipeline() -> None:
    """
    Complete validation workflow executes.
    """

    pipeline = ValidationPipeline()

    summary = pipeline.run(
        count=3,
        length=10,
    )

    assert summary.total_experiments == 3

    assert summary.successful_experiments == 3

    assert summary.average_accuracy >= 0.0

    assert summary.version == ("1.0.0")
