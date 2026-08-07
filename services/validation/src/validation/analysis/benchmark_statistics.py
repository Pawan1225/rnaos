"""
RNAOS benchmark statistics analyzer.
"""

from __future__ import annotations

from collections import defaultdict


class BenchmarkStatistics:
    """
    Generates benchmark statistics
    grouped by sequence length.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate length based statistics.
        """

        grouped = defaultdict(list)

        for result in results:
            grouped[result["sequence_length"]].append(result)

        statistics = {}

        for length, items in grouped.items():
            count = len(items)

            statistics[str(length)] = {
                "samples": count,
                "average_accuracy": (sum(x["accuracy"] for x in items) / count),
                "average_f1_score": (sum(x["structure_f1"] for x in items) / count),
                "average_energy_gap": (sum(x["energy_gap"] for x in items) / count),
                "average_runtime_seconds": (sum(x["runtime_seconds"] for x in items) / count),
                "average_estimated_qubits": (sum(x["estimated_qubits"] for x in items) / count),
            }

        return statistics
