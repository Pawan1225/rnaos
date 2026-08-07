"""
Tests quantum resource analysis generator.
"""

from validation.analyzers.quantum_resource_analysis_generator import (
    QuantumResourceAnalysisGenerator,
)


def test_quantum_resource_analysis_generation():

    results = [
        {
            "estimated_qubits": 40,
            "sequence_length": 20,
        },
        {
            "estimated_qubits": 80,
            "sequence_length": 40,
        },
    ]

    generator = QuantumResourceAnalysisGenerator()

    output = generator.generate(results)

    assert output.sample_count == 2
    assert output.maximum_qubits == 80
    assert output.average_qubits == 60.0
