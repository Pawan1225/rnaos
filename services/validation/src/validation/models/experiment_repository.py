"""
RNAOS experiment repository model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentRepository:
    """
    Immutable experiment storage metadata.
    """

    repository_id: str

    location: str

    experiment_count: int

    version: str
