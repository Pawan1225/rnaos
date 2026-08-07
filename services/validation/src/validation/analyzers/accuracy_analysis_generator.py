"""
RNAOS accuracy analysis generator.

Generates accuracy statistics
for benchmark publication artifacts.
"""

from __future__ import annotations


class AccuracyAnalysisGenerator:
    """
    Generates accuracy analysis.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate accuracy report.
        """

        if not results:
            raise ValueError("No benchmark results")

        accuracies = [item["accuracy"] for item in results]

        by_length: dict[str, list[float]] = {}

        for item in results:
            length = str(item["sequence_length"])

            by_length.setdefault(
                length,
                [],
            )

            by_length[length].append(item["accuracy"])

        return {
            "metric": "accuracy",
            "total_samples": len(results),
            "average_accuracy": round(
                sum(accuracies) / len(accuracies),
                4,
            ),
            "accuracy_distribution": {
                key: round(
                    sum(values) / len(values),
                    4,
                )
                for key, values in by_length.items()
            },
        }
