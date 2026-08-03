"""
RNA Folding Profiler.

Coordinates all RNA folding components.
"""

from __future__ import annotations

from dataclasses import dataclass

from folding.basepairs import BasePairGenerator
from folding.energy.energy_engine import ThermodynamicEngine
from folding.energy.thermodynamic_profile import ThermodynamicProfile
from folding.engines.vienna_engine import ViennaEngine
from folding.models import RNASecondaryStructure
from folding.search.search_space import FoldingSearchSpace
from folding.search.search_space_builder import SearchSpaceBuilder


@dataclass(slots=True)
class FoldingProfile:
    """
    Complete biological representation of an RNA sequence.
    """

    secondary_structure: RNASecondaryStructure

    search_space: FoldingSearchSpace

    thermodynamics: ThermodynamicProfile


class FoldingProfiler:
    """
    Coordinates the complete RNA folding pipeline.
    """

    def __init__(self) -> None:
        self.vienna = ViennaEngine()

        self.generator = BasePairGenerator()

        self.search_builder = SearchSpaceBuilder()

        self.energy = ThermodynamicEngine()

    def profile(
        self,
        sequence: str,
    ) -> FoldingProfile:
        """
        Build the complete biological profile for an RNA sequence.
        """

        secondary_structure = self.vienna.fold(sequence)

        candidates = self.generator.generate(sequence)

        search_space = self.search_builder.build(candidates)

        thermodynamics = self.energy.evaluate(
            sequence,
            secondary_structure.dot_bracket,
        )

        return FoldingProfile(
            secondary_structure=secondary_structure,
            search_space=search_space,
            thermodynamics=thermodynamics,
        )
