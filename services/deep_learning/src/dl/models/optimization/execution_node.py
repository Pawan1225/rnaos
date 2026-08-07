"""
RNAOS solver execution node model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExecutionNode:
    """
    Immutable solver execution node.
    """

    node_id: int

    solver_name: str

    category: str

    priority: int
