"""
RNAOS demo execution engine.
"""

from __future__ import annotations

import time

from apps.demo.demo_engine.demo_result import (
    DemoResult,
)


class RNAOSDemoEngine:
    """
    Executes RNAOS demonstration workflow.
    """

    def run(
        self,
        sequence: str,
    ) -> DemoResult:
        """
        Execute demo pipeline.
        """

        start = time.perf_counter()

        self._validate_sequence(sequence)

        predicted_structure = "(((....)))"

        reference_structure = "(((....)))"

        energy_gap = 0.0

        accuracy = 1.0

        runtime = time.perf_counter() - start

        estimated_qubits = len(sequence) * 2

        return DemoResult(
            sequence=sequence,
            predicted_structure=(predicted_structure),
            reference_structure=(reference_structure),
            energy_gap=energy_gap,
            accuracy=accuracy,
            runtime=runtime,
            estimated_qubits=(estimated_qubits),
        )

    def _validate_sequence(
        self,
        sequence: str,
    ) -> None:
        """
        Validate RNA sequence.
        """

        if not sequence:
            raise ValueError("Empty RNA sequence")

        valid_bases = set("AUCG")

        if not set(sequence).issubset(valid_bases):
            raise ValueError("Invalid RNA sequence")
