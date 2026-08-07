"""
Tests for execution edge model.
"""

from __future__ import annotations

from dl.models.optimization.execution_edge import (
    ExecutionEdge,
)


def test_execution_edge_creation() -> None:
    """
    Execution edge can be created.
    """

    edge = ExecutionEdge(
        source_node=1,
        target_node=2,
        transition="refinement",
    )

    assert edge.source_node == 1

    assert edge.target_node == 2

    assert edge.transition == "refinement"
