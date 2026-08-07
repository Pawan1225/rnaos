"""
RNAOS quantum resource analysis generator.
"""

from __future__ import annotations

from validation.models.quantum_resource_analysis import (
    QuantumResourceAnalysis,
)


class QuantumResourceAnalysisGenerator:
    """
    Generates quantum resource scaling analysis.
    """

    def generate(
        self,
        results: list[dict],
    ) -> QuantumResourceAnalysis:
        """
        Generate quantum resource statistics.
        """

        if not results:
            raise ValueError("No benchmark results")

        qubits = [item["estimated_qubits"] for item in results]

        variables = [item["sequence_length"] for item in results]

        depths = [item["sequence_length"] * 2 for item in results]

        average_qubits = sum(qubits) / len(qubits)

        average_variables = sum(variables) / len(variables)

        average_depth = sum(depths) / len(depths)

        scaling_factor = max(qubits) / min(qubits) if min(qubits) > 0 else 0.0

        return QuantumResourceAnalysis(
            analysis_id=("QUANTUM_RESOURCE_SCALING_001"),
            sample_count=len(results),
            average_qubits=round(
                average_qubits,
                4,
            ),
            maximum_qubits=max(qubits),
            average_variables=round(
                average_variables,
                4,
            ),
            average_depth=round(
                average_depth,
                4,
            ),
            scaling_factor=round(
                scaling_factor,
                4,
            ),
            benchmark_version="1.0.0",
        )
