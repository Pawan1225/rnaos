"""
RNAOS energy evaluator.
"""

from __future__ import annotations


class RNAOSEnergyEvaluator:
    """
    Evaluates RNA structure energy.

    Current implementation:
    deterministic baseline.

    Future:
    - ViennaRNA adapter
    - quantum-inspired energy model
    """

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:
        """
        Calculate structure energy.
        """

        pairs = structure.count("(")

        if pairs == 0:
            return 0.0

        return float(-1 * pairs)
