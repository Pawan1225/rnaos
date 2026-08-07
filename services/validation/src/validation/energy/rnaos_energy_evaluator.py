"""
RNAOS energy evaluator.
"""

from __future__ import annotations

import RNA


class RNAOSEnergyEvaluator:
    """
    Evaluates energy of RNAOS candidate structures.
    """

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:
        """
        Calculate thermodynamic energy
        of a candidate structure.
        """

        compound = RNA.fold_compound(sequence)

        energy = compound.eval_structure(structure)

        return float(energy)
