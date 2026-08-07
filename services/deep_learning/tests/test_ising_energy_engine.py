"""
Tests for Ising energy engine.
"""

from __future__ import annotations

from dl.models.optimization.ising_model import (
    IsingModel,
)
from dl.optimization.ising_energy_engine import (
    IsingEnergyEngine,
)


def test_ising_energy() -> None:
    """
    Energy calculation works.
    """

    model = IsingModel(
        variables=(
            "s1",
            "s2",
        ),
        local_fields=(
            1.0,
            1.0,
        ),
        couplings=(
            (
                0.0,
                0.5,
            ),
            (
                0.5,
                0.0,
            ),
        ),
        offset=0.0,
    )

    engine = IsingEnergyEngine()

    energy = engine.calculate(
        model,
        (
            1,
            -1,
        ),
    )

    assert energy == -1.0
