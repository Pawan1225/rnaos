"""
RNAOS runtime scaling visualization generator.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


class RuntimeScalingVisualizer:
    """
    Generates runtime scaling plots.
    """

    def generate(
        self,
        results: list[dict],
        output_path: str,
    ) -> Path:
        """
        Create runtime scaling visualization.
        """

        if not results:
            raise ValueError("No benchmark results")

        grouped: dict[int, list[float]] = {}

        for item in results:
            length = item["sequence_length"]

            grouped.setdefault(
                length,
                [],
            )

            grouped[length].append(item["runtime_seconds"])

        lengths = sorted(grouped.keys())

        runtimes = [sum(grouped[length]) / len(grouped[length]) for length in lengths]

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.figure(figsize=(8, 5))

        plt.plot(
            lengths,
            runtimes,
            marker="o",
        )

        plt.xlabel("RNA Sequence Length")

        plt.ylabel("Average Runtime (seconds)")

        plt.title("RNAOS Runtime Scaling")

        plt.grid(True)

        plt.savefig(
            path,
            bbox_inches="tight",
        )

        plt.close()

        return path
