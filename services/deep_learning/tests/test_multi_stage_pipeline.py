"""
Tests for multi-stage optimization pipeline.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.pipeline_result import (
    PipelineResult,
)
from dl.optimization.multi_stage_pipeline import (
    MultiStageOptimizationPipeline,
)


def test_pipeline_execution() -> None:
    """
    Pipeline selects best candidate.
    """

    pipeline = MultiStageOptimizationPipeline()

    result = pipeline.execute(
        candidates=(
            (
                "qubo",
                -10.0,
            ),
            (
                "annealing",
                -15.0,
            ),
            (
                "tensor",
                -12.0,
            ),
        ),
    )

    assert isinstance(
        result,
        PipelineResult,
    )

    assert result.selected_solver == ("annealing")

    assert result.stages_completed == 5


def test_empty_pipeline_fails() -> None:
    """
    Empty candidate list fails.
    """

    pipeline = MultiStageOptimizationPipeline()

    with pytest.raises(
        ValueError,
    ):
        pipeline.execute(
            candidates=(),
        )
