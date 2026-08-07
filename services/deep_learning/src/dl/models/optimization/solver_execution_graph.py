"""
RNAOS solver execution graph model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.execution_edge import (
    ExecutionEdge,
)
from dl.models.optimization.execution_node import (
    ExecutionNode,
)


@dataclass(
    slots=True,
    frozen=True,
)
class SolverExecutionGraph:
    """
    Immutable solver execution graph.
    """

    nodes: tuple[
        ExecutionNode,
        ...,
    ]

    edges: tuple[
        ExecutionEdge,
        ...,
    ]

    stages: int
