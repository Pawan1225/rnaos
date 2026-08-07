"""
RNAOS validation pipeline orchestrator.
"""

from __future__ import annotations

from validation.analyzers.result_comparison_engine import (
    ResultComparisonEngine,
)
from validation.datasets.benchmark_dataset_manager import (
    BenchmarkDatasetManager,
)
from validation.models.validation_summary import (
    ValidationSummary,
)
from validation.runners.rnaos_experiment_runner import (
    RNAOSExperimentRunner,
)
from validation.runners.vienna_reference_runner import (
    ViennaReferenceRunner,
)


class ValidationPipeline:
    """
    Executes complete RNAOS validation workflow.
    """

    def __init__(self) -> None:
        self.dataset_manager = BenchmarkDatasetManager()

        self.vienna_runner = ViennaReferenceRunner()

        self.rnaos_runner = RNAOSExperimentRunner()

        self.comparator = ResultComparisonEngine()

    def run(
        self,
        count: int = 5,
        length: int = 20,
    ) -> ValidationSummary:
        """
        Execute validation pipeline.
        """

        dataset = self.dataset_manager.generate(
            count=count,
            length=length,
        )

        energy_gaps: list[float] = []

        accuracies: list[float] = []

        successful = 0

        for sequence in dataset.sequences:
            reference = self.vienna_runner.run(
                sequence,
            )

            result = self.rnaos_runner.run(
                sequence,
            )

            comparison = self.comparator.compare(
                reference,
                result,
            )

            energy_gaps.append(
                comparison.energy_gap,
            )

            accuracies.append(
                comparison.structure_accuracy,
            )

            successful += 1

        return ValidationSummary(
            total_experiments=count,
            successful_experiments=successful,
            average_energy_gap=(sum(energy_gaps) / len(energy_gaps)),
            average_accuracy=(sum(accuracies) / len(accuracies)),
            version="1.0.0",
        )
