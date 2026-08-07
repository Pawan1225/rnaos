"""
Tests for RNAOS demo engine.
"""

from apps.demo.demo_engine.rnaos_demo_engine import (
    RNAOSDemoEngine,
)


def test_demo_engine():

    engine = RNAOSDemoEngine()

    result = engine.run("GGCAU")

    assert result.sequence == ("GGCAU")

    assert result.accuracy == 1.0

    assert result.energy_gap == 0.0

    assert result.estimated_qubits == 10
