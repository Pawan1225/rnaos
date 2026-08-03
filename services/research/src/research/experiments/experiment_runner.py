"""
Research experiment runner.
"""

from __future__ import annotations

from collections.abc import Callable

from research.models.benchmark_case import BenchmarkCase
from research.models.experiment_context import ExperimentContext
from research.models.experiment_result import ExperimentResult

PipelineStage = Callable[[ExperimentContext], ExperimentContext]


class ExperimentRunner:
    """
    Executes an experiment by applying a sequence of pipeline stages.
    """

    def __init__(
        self,
        stages: list[PipelineStage] | None = None,
    ) -> None:
        self._stages = stages or []

    def add_stage(
        self,
        stage: PipelineStage,
    ) -> None:
        """Register a pipeline stage."""
        self._stages.append(stage)

    def run(
        self,
        case: BenchmarkCase,
    ) -> ExperimentResult:
        """
        Execute a benchmark experiment.
        """
        context = ExperimentContext(
            benchmark_case=case,
        )

        for stage in self._stages:
            context = stage(context)

        if context.metrics is None:
            raise RuntimeError("Experiment completed without evaluation metrics.")

        return ExperimentResult(
            benchmark_id=context.benchmark_id,
            metrics=context.metrics,
            metadata=context.metadata,
        )
