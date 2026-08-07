"""
Tests for execution node model.
"""

from __future__ import annotations

from dl.models.optimization.execution_node import (
    ExecutionNode,
)


def test_execution_node_creation() -> None:
    """
    Execution node can be created.
    """

    node = ExecutionNode(
        node_id=1,
        solver_name="ising",
        category="quantum",
        priority=1,
    )

    assert node.node_id == 1

    assert node.solver_name == "ising"

    assert node.category == "quantum"

    assert node.priority == 1
