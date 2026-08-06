"""
RNAOS intelligence request model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.intelligence_configuration import (
    IntelligenceConfiguration,
)


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceRequest:
    """
    Immutable high-level intelligence request.
    """

    sequence: str

    task: str

    configuration: IntelligenceConfiguration

    metadata: tuple[str, ...] = ()
