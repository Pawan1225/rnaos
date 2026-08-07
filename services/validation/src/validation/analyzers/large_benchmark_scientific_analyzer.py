"""
RNAOS large benchmark scientific analyzer.

Generates publication metrics from
benchmark experiment results.
"""

from __future__ import annotations


class LargeBenchmarkScientificAnalyzer:
    """
    Extracts scientific benchmark metrics.
    """

    def analyze(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate scientific analysis.
        """

        if not results:
            raise ValueError("No benchmark results")

        return {
            "accuracy_analysis": (self._accuracy_analysis(results)),
            "energy_gap_analysis": (self._energy_analysis(results)),
            "runtime_scaling": (self._runtime_analysis(results)),
            "quantum_resource_scaling": (self._quantum_analysis(results)),
        }

    def _accuracy_analysis(
        self,
        results: list[dict],
    ) -> dict:
        """
        Calculate accuracy statistics.
        """

        accuracies = [item["accuracy"] for item in results]

        return {
            "metric": "accuracy",
            "total_samples": len(results),
            "average_accuracy": round(
                sum(accuracies) / len(accuracies),
                4,
            ),
        }

    def _energy_analysis(
        self,
        results: list[dict],
    ) -> dict:
        """
        Calculate energy gap statistics.
        """

        gaps = [item["energy_gap"] for item in results]

        return {
            "metric": "energy_gap",
            "average_gap": round(
                sum(gaps) / len(gaps),
                4,
            ),
            "minimum_gap": min(gaps),
            "maximum_gap": max(gaps),
        }

    def _runtime_analysis(
        self,
        results: list[dict],
    ) -> dict:
        """
        Calculate runtime scaling.
        """

        scaling = {}

        for item in results:
            length = str(item["sequence_length"])

            scaling.setdefault(
                length,
                [],
            )

            scaling[length].append(item["runtime_seconds"])

        return {
            "runtime_scaling": {
                key: round(
                    sum(values) / len(values),
                    4,
                )
                for key, values in scaling.items()
            }
        }

    def _quantum_analysis(
        self,
        results: list[dict],
    ) -> dict:
        """
        Calculate quantum resources.
        """

        scaling = {}

        for item in results:
            length = str(item["sequence_length"])

            scaling[length] = item["estimated_qubits"]

        return {"estimated_resources": scaling}
