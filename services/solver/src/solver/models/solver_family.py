"""
Solver family definitions.
"""

from __future__ import annotations

from enum import StrEnum


class SolverFamily(StrEnum):
    """Supported solver families."""

    CLASSICAL = "classical"

    EVOLUTIONARY = "evolutionary"

    EXACT = "exact"

    MATHEMATICAL = "mathematical"

    DIGITAL_ANNEALER = "digital_annealer"

    QUANTUM = "quantum"

    HYBRID = "hybrid"
