"""
Solver capability definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

from solver.models.solver_family import SolverFamily


@dataclass(slots=True, frozen=True)
class SolverCapabilities:
    """Describes the capabilities of a solver."""

    solver_family: SolverFamily

    supports_sparse_qubo: bool = True

    supports_dense_qubo: bool = True

    supports_binary_variables: bool = True

    supports_continuous_variables: bool = False

    deterministic: bool = False

    parallel: bool = False

    gpu_accelerated: bool = False

    quantum: bool = False

    hybrid: bool = False

    max_problem_size: int = 10_000
