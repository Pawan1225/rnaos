"""
RNAOS demo launcher.
"""

from __future__ import annotations

from apps.demo.demo_engine.rnaos_demo_engine import (
    RNAOSDemoEngine,
)


def main() -> None:
    """
    Run RNAOS demo.
    """

    sequence = "GGAGCAAAACUUGUCGAUUG"

    engine = RNAOSDemoEngine()

    result = engine.run(sequence)

    print("RNAOS Demo Complete")

    print(f"Sequence: {result.sequence}")

    print(f"Structure: {result.predicted_structure}")

    print(f"Accuracy: {result.accuracy}")

    print(f"Energy Gap: {result.energy_gap}")

    print(f"Estimated Qubits: {result.estimated_qubits}")


if __name__ == "__main__":
    main()
