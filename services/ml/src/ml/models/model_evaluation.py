"""
RNAOS machine learning model evaluation model.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModelEvaluation:
    """
    Immutable model evaluation result.

    Stores evaluation metrics and metadata
    produced by the Model Evaluation Engine.
    """

    model_name: str
    metrics: Mapping[str, float]
    evaluation_version: str
    sample_count: int
