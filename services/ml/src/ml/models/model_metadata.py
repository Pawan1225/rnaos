"""
RNAOS machine learning model metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ModelMetadata:
    """
    Immutable metadata for a registered machine learning model.
    """

    model_id: str

    model_name: str

    version: str

    training_time: float

    feature_count: int

    sample_count: int

    created_at: str
