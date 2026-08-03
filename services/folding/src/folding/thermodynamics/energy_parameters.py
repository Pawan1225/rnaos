"""
RNA Thermodynamic Energy Parameters.

Sprint 6.1

This module provides a centralized repository of thermodynamic
parameters used throughout RNAOS.

Version 1 implements simplified canonical RNA base-pair energies.

Future versions will extend this module with:

- Turner nearest-neighbor parameters
- Stacking energies
- Hairpin loop penalties
- Internal loop penalties
- Bulge loop penalties
- Multiloop parameters
- Temperature-dependent corrections
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True, slots=True)
class BasePairEnergy:
    """
    Thermodynamic information for a canonical RNA base pair.

    Parameters
    ----------
    pair
        Canonical RNA base pair (GC, AU, GU, etc.)

    energy
        Simplified free-energy contribution (kcal/mol).

    hydrogen_bonds
        Number of hydrogen bonds.
    """

    pair: str
    energy: float
    hydrogen_bonds: int


class EnergyParameters:
    """
    Central repository of RNA thermodynamic parameters.

    Notes
    -----
    This class acts as the single source of truth for all
    thermodynamic constants used throughout RNAOS.

    Current implementation
    ----------------------
    - Canonical base-pair energies

    Planned additions
    -----------------
    - Turner nearest-neighbor tables
    - Stacking energies
    - Hairpin loop penalties
    - Internal loop penalties
    - Bulge penalties
    - Multiloop parameters
    - Temperature corrections
    """

    BASE_PAIR_ENERGIES: ClassVar[dict[str, BasePairEnergy]] = {
        "GC": BasePairEnergy(
            pair="GC",
            energy=-3.0,
            hydrogen_bonds=3,
        ),
        "CG": BasePairEnergy(
            pair="CG",
            energy=-3.0,
            hydrogen_bonds=3,
        ),
        "AU": BasePairEnergy(
            pair="AU",
            energy=-2.0,
            hydrogen_bonds=2,
        ),
        "UA": BasePairEnergy(
            pair="UA",
            energy=-2.0,
            hydrogen_bonds=2,
        ),
        "GU": BasePairEnergy(
            pair="GU",
            energy=-1.0,
            hydrogen_bonds=2,
        ),
        "UG": BasePairEnergy(
            pair="UG",
            energy=-1.0,
            hydrogen_bonds=2,
        ),
    }

    @classmethod
    def base_pair_energy(cls, pair: str) -> float:
        """
        Return the free-energy contribution for a canonical RNA base pair.

        Parameters
        ----------
        pair
            Base pair identifier (e.g. "GC", "AU", "GU").

        Returns
        -------
        float
            Free-energy contribution.

        Raises
        ------
        ValueError
            If the supplied pair is unsupported.
        """
        key = pair.upper()

        if key not in cls.BASE_PAIR_ENERGIES:
            raise ValueError(f"Unsupported RNA base pair: {pair}")

        return cls.BASE_PAIR_ENERGIES[key].energy

    @classmethod
    def hydrogen_bonds(cls, pair: str) -> int:
        """
        Return the number of hydrogen bonds for a canonical RNA base pair.
        """
        key = pair.upper()

        if key not in cls.BASE_PAIR_ENERGIES:
            raise ValueError(f"Unsupported RNA base pair: {pair}")

        return cls.BASE_PAIR_ENERGIES[key].hydrogen_bonds

    @classmethod
    def metadata(cls, pair: str) -> BasePairEnergy:
        """
        Return the complete metadata object for a base pair.

        Parameters
        ----------
        pair
            Canonical RNA base pair.

        Returns
        -------
        BasePairEnergy
            Immutable metadata object.
        """
        key = pair.upper()

        if key not in cls.BASE_PAIR_ENERGIES:
            raise ValueError(f"Unsupported RNA base pair: {pair}")

        return cls.BASE_PAIR_ENERGIES[key]

    @classmethod
    def is_supported_pair(cls, pair: str) -> bool:
        """
        Check whether a canonical RNA base pair is supported.
        """
        return pair.upper() in cls.BASE_PAIR_ENERGIES

    @classmethod
    def supported_pairs(cls) -> tuple[str, ...]:
        """
        Return all supported canonical RNA base pairs.
        """
        return tuple(sorted(cls.BASE_PAIR_ENERGIES.keys()))
