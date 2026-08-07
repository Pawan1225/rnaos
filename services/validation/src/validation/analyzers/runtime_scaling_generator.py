"""
RNAOS runtime scaling generator.

Generates runtime analysis
for benchmark experiments.
"""

from __future__ import annotations


class RuntimeScalingGenerator:
    """
    Generates runtime scaling analysis.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate runtime report.
        """

        if not results:
            raise ValueError("No benchmark results")

        runtimes = [item["runtime_seconds"] for item in results]

        by_length: dict[str, list[float]] = {}

        for item in results:
            length = str(item["sequence_length"])

            by_length.setdefault(
                length,
                [],
            )

            by_length[length].append(item["runtime_seconds"])

        return {
            "metric": "runtime_scaling",
            "total_samples": len(results),
            "average_runtime": round(
                sum(runtimes) / len(runtimes),
                4,
            ),
            "scaling_by_length": {
                key: round(
                    sum(values) / len(values),
                    4,
                )
                for key, values in by_length.items()
            },
        }
