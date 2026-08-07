"""
RNAOS benchmark statistics validator.

Generates statistical evidence from
frozen benchmark experiments.
"""

from __future__ import annotations

from statistics import mean, stdev


class BenchmarkStatisticsValidator:
    """
    Calculates benchmark statistics.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate scientific statistics report.
        """

        if not results:
            raise ValueError("No benchmark results")

        accuracies = [item["accuracy"] for item in results]

        energy_gaps = [item["energy_gap"] for item in results]

        runtimes = [item["runtime_seconds"] for item in results]

        qubits = [item["estimated_qubits"] for item in results]

        return {
            "benchmark": ("RNAOS_LARGE_V1"),
            "experiments": len(results),
            "accuracy": {
                "mean": mean(accuracies),
                "std": stdev(accuracies),
            },
            "energy_gap": {
                "mean": mean(energy_gaps),
                "std": stdev(energy_gaps),
            },
            "runtime": {
                "mean_seconds": mean(runtimes),
            },
            "quantum_resources": {
                "max_estimated_qubits": max(qubits),
            },
        }
