from validation.analyzers.quantum_resource_scaling_generator import (
    QuantumResourceScalingGenerator,
)


def test_quantum_resource_scaling_generation():

    results = [
        {
            "sequence_length": 20,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 20,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 40,
            "estimated_qubits": 80,
        },
    ]

    generator = QuantumResourceScalingGenerator()

    report = generator.generate(results)

    assert report["metric"] == ("quantum_resource_scaling")

    assert report["total_samples"] == 3

    assert report["resource_scaling"]["20"] == 40

    assert report["resource_scaling"]["40"] == 80
