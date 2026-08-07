"""
ViennaRNA reference adapter.
"""

from __future__ import annotations

import RNA


class ViennaReference:
    """
    Classical RNA folding reference.

    Uses ViennaRNA to generate:
    - Minimum Free Energy (MFE) structure
    - MFE value
    """

    def fold(
        self,
        sequence: str,
    ) -> tuple[str, float]:
        """
        Generate ViennaRNA MFE prediction.
        """

        structure, mfe = RNA.fold(sequence)

        return (
            structure,
            float(mfe),
        )
