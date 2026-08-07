"""
RNAOS ViennaRNA reference runner.
"""

from __future__ import annotations

import RNA

from validation.models.vienna_reference import (
    ViennaReference,
)


class ViennaReferenceRunner:
    """
    Executes ViennaRNA minimum free energy folding.
    """

    def run(
        self,
        sequence: str,
    ) -> ViennaReference:
        """
        Generate ViennaRNA reference.
        """

        structure, energy = RNA.fold(
            sequence,
        )

        return ViennaReference(
            sequence=sequence,
            structure=structure,
            mfe_energy=float(
                energy,
            ),
            length=len(sequence),
            engine="ViennaRNA",
            version="2.x",
        )
