"""
Tests for quantum resource scaling.
"""

from validation.analyzers.quantum_resource_scaling_engine import (
    QuantumResourceScalingEngine,
)


def test_quantum_resource_scaling():

    engine = QuantumResourceScalingEngine()

    result = engine.analyze(
        qubits=(
            20,
            40,
            80,
        ),
        variables=(
            40,
            80,
            160,
        ),
        depths=(
            10,
            20,
            40,
        ),
    )

    assert result.sample_count == 3

    assert result.average_qubits == (140 / 3)

    assert result.maximum_qubits == 80

    assert result.average_variables == (280 / 3)

    assert result.scaling_factor == 4.0

    assert result.benchmark_version == ("1.0.0")
