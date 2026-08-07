from validation.release.frozen_data_verifier import (
    FrozenDataVerifier,
)


def test_frozen_data_verification():

    results = []

    lengths = (
        20,
        40,
        60,
        80,
    )

    experiment_id = 1

    for length in lengths:
        for _ in range(100):
            results.append(
                {
                    "experiment_id": experiment_id,
                    "sequence": "GGCAU",
                    "sequence_length": length,
                    "rnaos_structure": "(((...)))",
                    "reference_structure": "(((...)))",
                    "rnaos_energy": -1.0,
                    "reference_energy": -1.2,
                    "energy_gap": 0.2,
                    "accuracy": 0.95,
                    "runtime_seconds": 0.1,
                    "estimated_qubits": (length * 2),
                }
            )

            experiment_id += 1

    verifier = FrozenDataVerifier()

    output = verifier.verify(results)

    assert output["status"] == ("VERIFIED")

    assert output["experiments"] == 400

    assert output["length_distribution"] == {
        20: 100,
        40: 100,
        60: 100,
        80: 100,
    }
