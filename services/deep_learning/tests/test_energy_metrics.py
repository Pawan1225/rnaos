"""
Tests for energy metrics.
"""

from __future__ import annotations

from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)


def test_energy_metrics() -> None:
    """
    Energy metrics can be created.
    """

    metrics = EnergyMetrics(
        reference_energy=-32.5,
        predicted_energy=-35.1,
        energy_gap=2.6,
        relative_error=0.08,
        improvement=0.08,
    )

    assert metrics.reference_energy == (-32.5)

    assert metrics.predicted_energy == (-35.1)

    assert metrics.energy_gap == (2.6)

    assert metrics.relative_error == (0.08)

    assert metrics.improvement == (0.08)
