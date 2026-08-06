"""
RNAOS machine learning experiment model.
"""

from __future__ import annotations

from dataclasses import dataclass

from ml.models.automl_configuration import (
    AutoMLConfiguration,
)


@dataclass(slots=True, frozen=True)
class MLExperiment:
    """
    Immutable machine learning experiment metadata.

    Represents a single AutoML training run, capturing the
    configuration, dataset version, best-performing model,
    execution time, and experiment timestamp.
    """

    experiment_id: str

    dataset_version: str

    configuration: AutoMLConfiguration

    best_model_name: str

    total_training_time: float

    timestamp: str
