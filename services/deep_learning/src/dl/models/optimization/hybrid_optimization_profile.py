"""
RNAOS hybrid optimization profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class HybridOptimizationProfile:
    """
    Immutable hybrid optimization capability profile.
    """

    system_name: str

    version: str

    optimization_layers: tuple[str, ...]

    active_engines: tuple[str, ...]

    supported_strategies: tuple[str, ...]

    validation_status: str
