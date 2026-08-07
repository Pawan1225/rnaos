"""
RNAOS unified evaluation metrics model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)
from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)
from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


@dataclass(
    slots=True,
    frozen=True,
)
class EvaluationMetrics:
    """
    Immutable complete evaluation metrics.
    """

    structural: StructuralMetrics

    energy: EnergyMetrics

    performance: PerformanceMetrics
