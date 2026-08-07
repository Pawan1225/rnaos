"""
RNAOS benchmark pipeline model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkPipeline:
    """
    Immutable benchmark pipeline state.
    """

    pipeline_id: str

    experiment_id: str

    dataset_id: str

    methods: tuple[str, ...]

    metrics: tuple[str, ...]

    statistics: tuple[str, ...]

    visualizations: tuple[str, ...]

    report_id: str

    metadata: tuple[str, ...]
