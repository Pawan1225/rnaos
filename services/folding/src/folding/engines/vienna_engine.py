"""
ViennaRNA Engine.

Provides a clean interface to the ViennaRNA library.
"""

from __future__ import annotations

import RNA

from folding.interfaces.folding_engine import FoldingEngine
from folding.models import BasePair, RNASecondaryStructure


class ViennaEngine(FoldingEngine):
    """
    Folding engine backed by the ViennaRNA library.
    """

    def fold(self, sequence: str) -> RNASecondaryStructure:
        """
        Predict the minimum free energy secondary structure.
        """

        dot_bracket, mfe = RNA.fold(sequence)

        return RNASecondaryStructure(
            sequence=sequence,
            dot_bracket=dot_bracket,
            mfe=float(mfe),
            base_pairs=self._extract_base_pairs(dot_bracket),
        )

    def mfe(self, sequence: str) -> float:
        """
        Return the minimum free energy.
        """

        _, mfe = RNA.fold(sequence)

        return float(mfe)

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:
        """
        Evaluate the free energy of a supplied structure.
        """

        fc = RNA.fold_compound(sequence)

        return float(fc.eval_structure(structure))

    @staticmethod
    def _extract_base_pairs(
        dot_bracket: str,
    ) -> list[BasePair]:
        """
        Convert dot-bracket notation into BasePair objects.
        """

        stack: list[int] = []
        pairs: list[BasePair] = []

        for index, symbol in enumerate(dot_bracket):
            if symbol == "(":
                stack.append(index)

            elif symbol == ")":
                left = stack.pop()
                pairs.append(BasePair(left=left, right=index))

        return sorted(
            pairs,
            key=lambda pair: pair.left,
        )
