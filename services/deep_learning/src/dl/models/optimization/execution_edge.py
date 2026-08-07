"""
RNAOS solver execution edge model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExecutionEdge:
    """
    Immutable solver execution edge.
    """

    source_node: int

    target_node: int

    transition: str
