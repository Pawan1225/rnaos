"""
ViennaRNA based energy evaluator.
"""

from __future__ import annotations

import RNA


class ViennaEnergyEvaluator:
    """
    Evaluates RNA secondary structure energy
    using ViennaRNA.
    """

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:
        """
        Calculate free energy.
        """

        fc = RNA.fold_compound(
            sequence,
        )

        return float(
            fc.eval_structure(
                structure,
            )
        )
