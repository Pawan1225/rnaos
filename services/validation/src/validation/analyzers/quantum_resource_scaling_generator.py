"""
RNAOS quantum resource scaling generator.

Generates estimated quantum resource
requirements for benchmark experiments.
"""

from __future__ import annotations


class QuantumResourceScalingGenerator:
    """
    Generates quantum resource scaling analysis.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate quantum resource report.
        """

        if not results:
            raise ValueError("No benchmark results")

        resources: dict[str, list[int]] = {}

        for item in results:
            length = str(item["sequence_length"])

            resources.setdefault(
                length,
                [],
            )

            resources[length].append(item["estimated_qubits"])

        return {
            "metric": ("quantum_resource_scaling"),
            "total_samples": len(results),
            "resource_scaling": {key: max(values) for key, values in resources.items()},
        }
