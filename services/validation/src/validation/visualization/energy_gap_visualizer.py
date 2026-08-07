"""
RNAOS energy gap visualization generator.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


class EnergyGapVisualizer:
    """
    Generates energy gap distribution plots.
    """

    def generate(
        self,
        results: list[dict],
        output_path: str,
    ) -> Path:
        """
        Create energy gap visualization.
        """

        if not results:
            raise ValueError("No benchmark results")

        energy_gaps = [item["energy_gap"] for item in results]

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.figure(figsize=(8, 5))

        plt.hist(
            energy_gaps,
            bins=20,
        )

        plt.xlabel("Energy Gap")

        plt.ylabel("Frequency")

        plt.title("RNAOS Energy Gap Distribution")

        plt.grid(True)

        plt.savefig(
            path,
            bbox_inches="tight",
        )

        plt.close()

        return path
