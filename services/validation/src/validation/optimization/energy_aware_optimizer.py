"""
Energy aware RNA structure optimizer.
"""

from __future__ import annotations


class EnergyAwareOptimizer:
    """
    Selects lowest energy RNA structure.
    """

    def __init__(
        self,
        generator,
        validator,
        evaluator,
    ) -> None:

        self.generator = generator
        self.validator = validator
        self.evaluator = evaluator

    def optimize(
        self,
        sequence: str,
    ) -> str:
        """
        Generate and select best structure.
        """

        candidates = self.generator.generate(
            sequence,
        )

        best_structure = "." * len(sequence)

        best_energy = float(
            "inf",
        )

        for structure in candidates:
            if not self.validator.validate(
                sequence,
                structure,
            ):
                continue

            energy = self.evaluator.evaluate(
                sequence,
                structure,
            )

            if energy < best_energy:
                best_energy = energy
                best_structure = structure

        return best_structure
