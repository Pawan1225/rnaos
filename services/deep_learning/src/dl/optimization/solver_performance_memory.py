"""
RNAOS solver performance memory engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_experience import (
    OptimizationExperience,
)
from dl.models.optimization.solver_performance_memory import (
    SolverPerformanceMemory,
)


class SolverPerformanceMemoryEngine:
    """
    Stores optimization experiences.
    """

    def add(
        self,
        memory: SolverPerformanceMemory,
        experience: OptimizationExperience,
    ) -> SolverPerformanceMemory:
        """
        Add a new optimization experience.
        """

        return SolverPerformanceMemory(
            experiences=(memory.experiences + (experience,)),
        )

    def size(
        self,
        memory: SolverPerformanceMemory,
    ) -> int:
        """
        Return the number of stored experiences.
        """

        return len(memory.experiences)
