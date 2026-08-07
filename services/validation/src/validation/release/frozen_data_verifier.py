"""
RNAOS frozen benchmark data verifier.

Validates scientific benchmark artifacts
before evidence generation.
"""

from __future__ import annotations


class FrozenDataVerifier:
    """
    Verifies frozen benchmark data.
    """

    REQUIRED_FIELDS = {
        "experiment_id",
        "sequence",
        "sequence_length",
        "rnaos_structure",
        "reference_structure",
        "rnaos_energy",
        "reference_energy",
        "energy_gap",
        "accuracy",
        "runtime_seconds",
        "estimated_qubits",
    }

    EXPECTED_LENGTHS = {
        20,
        40,
        60,
        80,
    }

    def verify(
        self,
        results: list[dict],
    ) -> dict:
        """
        Verify benchmark records.
        """

        if len(results) != 400:
            raise ValueError("Benchmark must contain 400 experiments")

        distribution = {}

        missing_fields = []

        for result in results:
            missing = self.REQUIRED_FIELDS - result.keys()

            if missing:
                missing_fields.extend(list(missing))

            length = result["sequence_length"]

            distribution[length] = distribution.get(length, 0) + 1

        if set(distribution.keys()) != (self.EXPECTED_LENGTHS):
            raise ValueError("Invalid sequence length distribution")

        return {
            "status": "VERIFIED",
            "experiments": len(results),
            "length_distribution": distribution,
            "missing_fields": missing_fields,
        }
