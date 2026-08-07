"""
RNAOS visualization dataset model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class VisualizationDataset:
    """
    Immutable dataset for scientific visualization.
    """

    dataset_id: str

    benchmark_version: str

    sequence_lengths: tuple[int, ...]

    accuracy_values: tuple[float, ...]

    energy_gaps: tuple[float, ...]

    runtime_values: tuple[float, ...]

    qubit_estimates: tuple[int, ...]

    solvers: tuple[str, ...]

    metadata: tuple[str, ...]
