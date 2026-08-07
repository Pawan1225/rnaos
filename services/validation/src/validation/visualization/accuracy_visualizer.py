"""
RNAOS accuracy visualization generator.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


class AccuracyVisualizer:
    """
    Generates accuracy versus length plots.
    """

    def generate(
        self,
        results: list[dict],
        output_path: str,
    ) -> Path:
        """
        Create accuracy visualization.
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

            grouped[length].append(item["accuracy"])

        lengths = sorted(grouped.keys())

        accuracies = [sum(grouped[length]) / len(grouped[length]) for length in lengths]

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.figure(figsize=(8, 5))

        plt.plot(
            lengths,
            accuracies,
            marker="o",
        )

        plt.xlabel("RNA Sequence Length")

        plt.ylabel("Accuracy")

        plt.title("RNAOS Accuracy vs Sequence Length")

        plt.grid(True)

        plt.savefig(
            path,
            bbox_inches="tight",
        )

        plt.close()

        return path
