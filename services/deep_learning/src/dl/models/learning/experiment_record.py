"""
RNAOS continuous learning experiment contract.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentRecord:
    """
    Immutable learning experiment record.
    """

    experiment_id: str

    timestamp: str

    version: str

    sequence_length: int

    gc_content: float

    structure_complexity: float

    biological_features: tuple[str, ...]

    ai_profile: tuple[str, ...]

    ml_prediction: tuple[str, ...]

    dl_prediction: tuple[str, ...]

    selected_solver: str

    optimization_strategy: str

    parameters: tuple[str, ...]

    runtime: float

    memory: float

    iterations: int

    energy_score: float

    accuracy_score: float

    benchmark_score: float

    success: bool
