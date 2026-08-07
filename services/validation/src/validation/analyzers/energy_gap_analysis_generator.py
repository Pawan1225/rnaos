"""
RNAOS energy gap analysis generator.

Generates energy comparison statistics
for benchmark publication artifacts.
"""

from __future__ import annotations


class EnergyGapAnalysisGenerator:
    """
    Generates energy gap analysis.
    """

    def generate(
        self,
        results: list[dict],
    ) -> dict:
        """
        Generate energy gap report.
        """

        if not results:
            raise ValueError("No benchmark results")

        gaps = [item["energy_gap"] for item in results]

        rnaos_energy = [item["rnaos_energy"] for item in results]

        reference_energy = [item["reference_energy"] for item in results]

        return {
            "metric": "energy_gap",
            "total_samples": len(results),
            "average_gap": round(
                sum(gaps) / len(gaps),
                4,
            ),
            "minimum_gap": min(gaps),
            "maximum_gap": max(gaps),
            "average_rnaos_energy": round(
                sum(rnaos_energy) / len(rnaos_energy),
                4,
            ),
            "average_reference_energy": round(
                sum(reference_energy) / len(reference_energy),
                4,
            ),
        }
