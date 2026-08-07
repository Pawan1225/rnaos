"""
RNAOS interactive demo launcher.
"""

from __future__ import annotations

from apps.demo.demo_engine.rna_input_handler import (
    RNAInputHandler,
)
from apps.demo.demo_engine.rnaos_demo_engine import (
    RNAOSDemoEngine,
)


def main() -> None:
    """
    Run interactive RNAOS demo.
    """

    sequence = input("Enter RNA sequence: ")

    handler = RNAInputHandler()

    validated_sequence = handler.validate(sequence)

    engine = RNAOSDemoEngine()

    result = engine.run(validated_sequence)

    print()

    print("RNAOS Prediction")

    print(f"Sequence: {result.sequence}")

    print(f"Structure: {result.predicted_structure}")

    print(f"Accuracy: {result.accuracy}")

    print(f"Energy Gap: {result.energy_gap}")

    print(f"Estimated Qubits: {result.estimated_qubits}")


if __name__ == "__main__":
    main()
