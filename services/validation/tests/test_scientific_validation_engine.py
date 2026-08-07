from validation.release.scientific_validation_engine import (
    ScientificValidationEngine,
)


def test_scientific_validation():

    result = {
        "experiment_id": 1,
        "sequence": "GGCAU",
        "sequence_length": 5,
        "rnaos_structure": "(((...)))",
        "reference_structure": "(((...)))",
        "rnaos_energy": -1.0,
        "reference_energy": -1.2,
        "energy_gap": 0.2,
        "accuracy": 0.95,
        "runtime_seconds": 0.1,
        "estimated_qubits": 10,
    }

    engine = ScientificValidationEngine()

    output = engine.validate(
        [result] * 400,
        [
            "experiment_results.json",
            "benchmark_summary.json",
            "accuracy_analysis.json",
            "energy_gap_analysis.json",
            "runtime_scaling.json",
            "quantum_resource_scaling.json",
            "manifest.json",
        ],
        {"status": "FROZEN"},
    )

    assert output["status"] == "VALIDATED"

    assert output["experiments"] == 400
