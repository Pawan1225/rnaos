"""
RNAOS machine learning model metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ModelMetadata:
    """
    Immutable metadata describing a trained model.

    Stores model identity, training lineage,
    configuration, and performance information
    required for reproducible ML workflows.
    """

    model_id: str

    model_name: str

    version: str

    training_time: float

    feature_count: int

    sample_count: int

    created_at: str

    algorithm: str = "unknown"

    dataset_version: str = "unknown"

    feature_version: str = "unknown"

    hyperparameters: tuple[tuple[str, str], ...] = ()

    metrics: tuple[tuple[str, float], ...] = ()

    @property
    def metric_count(
        self,
    ) -> int:
        """
        Number of stored evaluation metrics.
        """

        return len(
            self.metrics,
        )

    @property
    def parameter_count(
        self,
    ) -> int:
        """
        Number of stored hyperparameters.
        """

        return len(
            self.hyperparameters,
        )
