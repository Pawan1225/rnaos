"""
RNAOS benchmark pipeline configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkPipelineConfig:
    """
    Immutable benchmark configuration.
    """

    config_id: str

    dataset_id: str

    methods: tuple[str, ...]

    metrics: tuple[str, ...]

    enable_statistics: bool

    enable_visualization: bool

    export_formats: tuple[str, ...]

    random_seed: int

    metadata: tuple[str, ...]
