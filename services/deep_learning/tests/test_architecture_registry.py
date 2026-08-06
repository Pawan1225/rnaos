"""
Tests for RNAOS architecture registry.
"""

from __future__ import annotations

import pytest
from dl.architectures.mlp import (
    MLPModel,
)
from dl.registry.architecture_registry import (
    ArchitectureRegistry,
)


def test_register_architecture() -> None:
    """
    Architecture can be registered.
    """

    registry = ArchitectureRegistry()

    registry.register(
        "mlp",
        MLPModel,
    )

    assert "mlp" in registry.list_architectures()


def test_get_architecture() -> None:
    """
    Architecture can be retrieved.
    """

    registry = ArchitectureRegistry()

    registry.register(
        "mlp",
        MLPModel,
    )

    model = registry.get(
        "mlp",
    )

    assert model is MLPModel


def test_missing_architecture() -> None:
    """
    Missing architecture raises error.
    """

    registry = ArchitectureRegistry()

    with pytest.raises(
        KeyError,
    ):
        registry.get(
            "unknown",
        )
