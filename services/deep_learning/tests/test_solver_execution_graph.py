"""
Tests for solver execution graph.
"""

from __future__ import annotations

from dl.models.optimization.execution_edge import (
    ExecutionEdge,
)
from dl.models.optimization.execution_node import (
    ExecutionNode,
)
from dl.models.optimization.solver_execution_graph import (
    SolverExecutionGraph,
)


def test_solver_execution_graph_creation() -> None:
    """
    Solver execution graph can be created.
    """

    nodes = (
        ExecutionNode(
            node_id=1,
            solver_name="ising",
            category="quantum",
            priority=1,
        ),
        ExecutionNode(
            node_id=2,
            solver_name="genetic",
            category="evolutionary",
            priority=2,
        ),
    )

    edges = (
        ExecutionEdge(
            source_node=1,
            target_node=2,
            transition="optimization",
        ),
    )

    graph = SolverExecutionGraph(
        nodes=nodes,
        edges=edges,
        stages=2,
    )

    assert len(graph.nodes) == 2

    assert len(graph.edges) == 1

    assert graph.stages == 2

    assert graph.nodes[0].solver_name == "ising"

    assert graph.edges[0].transition == "optimization"
