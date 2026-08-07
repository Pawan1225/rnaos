"""
RNAOS large benchmark campaign executor.
"""

from __future__ import annotations

from validation.evaluation.benchmark_evaluator import (
    BenchmarkEvaluator,
)
from validation.models.campaign_result import (
    CampaignResult,
)
from validation.models.experiment_result import (
    ExperimentResult,
)
from validation.models.large_dataset import (
    LargeBenchmarkDataset,
)


class CampaignExecutionEngine:
    """
    Executes large RNA benchmark campaigns.

    Responsibilities:
    - iterate over benchmark dataset
    - delegate evaluation
    - collect experiment results
    - track execution status
    """

    def __init__(self) -> None:
        self.evaluator = BenchmarkEvaluator()

    def run(
        self,
        dataset: LargeBenchmarkDataset,
    ) -> CampaignResult:
        """
        Execute benchmark campaign.
        """

        completed = 0
        failed = 0

        experiment_results: list[ExperimentResult] = []

        for index, entry in enumerate(
            dataset.entries,
            start=1,
        ):
            try:
                experiment_result = self.evaluator.evaluate(
                    entry,
                    index,
                )

                experiment_results.append(experiment_result)

                completed += 1

            except Exception:
                failed += 1

        return CampaignResult(
            campaign_id=("RNAOS_CAMPAIGN_V1"),
            total_experiments=(dataset.total_sequences),
            completed_experiments=completed,
            failed_experiments=failed,
            benchmark_version="1.0.0",
            experiment_results=tuple(experiment_results),
        )
