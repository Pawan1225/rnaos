"""
RNAOS QUBO optimization models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QUBOModel:
    """
    Immutable QUBO representation.

    Represents:

    minimize x^T Q x
    """

    variables: tuple[str, ...]

    matrix: tuple[tuple[float, ...], ...]

    offset: float = 0.0
