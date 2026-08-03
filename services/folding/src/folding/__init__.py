"""
RNAOS Folding Intelligence Service.

Provides biological RNA folding functionality including
secondary structure prediction, energy evaluation,
and search-space generation.
"""

from folding.interfaces.folding_engine import FoldingEngine
from folding.services.folding_service import FoldingService

__all__ = [
    "FoldingEngine",
    "FoldingService",
]
