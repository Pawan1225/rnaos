"""
RNAOS experiment record model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentRecord:
    """
    Immutable experiment metadata.
    """

    experiment_id: str

    model_name: str

    dataset_name: str

    metrics: tuple[str, ...]

    status: str
