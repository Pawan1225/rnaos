"""
RNAOS machine learning experiment record.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ExperimentRecord:
    """
    Immutable record of a machine learning experiment.

    Stores reproducibility metadata for every ML run.
    """

    experiment_id: str

    model_name: str

    dataset_version: str

    feature_count: int

    sample_count: int

    training_time: float

    metrics: tuple[tuple[str, float], ...]

    created_at: str

    status: str

    @property
    def metric_count(
        self,
    ) -> int:
        """
        Number of recorded metrics.
        """

        return len(
            self.metrics,
        )

    @property
    def is_completed(
        self,
    ) -> bool:
        """
        Whether the experiment completed successfully.
        """

        return self.status == "completed"
