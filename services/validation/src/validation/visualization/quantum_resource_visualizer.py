"""
RNAOS quantum resource visualization generator.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


class QuantumResourceVisualizer:
    """
    Generates quantum resource scaling plots.
    """

    def generate(
        self,
        results: list[dict],
        output_path: str,
    ) -> Path:
        """
        Create quantum resource visualization.
        """

        if not results:
            raise ValueError("No benchmark results")

        grouped: dict[int, list[int]] = {}

        for item in results:
            length = item["sequence_length"]

            grouped.setdefault(
                length,
                [],
            )

            grouped[length].append(item["estimated_qubits"])

        lengths = sorted(grouped.keys())

        qubits = [sum(grouped[length]) / len(grouped[length]) for length in lengths]

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.figure(figsize=(8, 5))

        plt.plot(
            lengths,
            qubits,
            marker="o",
        )

        plt.xlabel("RNA Sequence Length")

        plt.ylabel("Estimated Qubits")

        plt.title("RNAOS Quantum Resource Scaling")

        plt.grid(True)

        plt.savefig(
            path,
            bbox_inches="tight",
        )

        plt.close()

        return path
