"""
RNAOS benchmark experiment configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentConfig:
    """
    Immutable scientific experiment definition.
    """

    experiment_id: str

    name: str

    version: str

    methods: tuple[str, ...]

    random_seed: int

    hardware: str

    software: str

    status: str
