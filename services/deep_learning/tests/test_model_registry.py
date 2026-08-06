"""
Tests for model registry.
"""

from __future__ import annotations

from dl.models.model_registry_entry import (
    ModelRegistryEntry,
)
from dl.registry.model_registry import (
    ModelRegistry,
)


def test_register_model() -> None:
    """
    Model can be registered.
    """

    registry = ModelRegistry()

    entry = ModelRegistryEntry(
        name="rna_transformer",
        version="1.0",
        model_type="transformer",
        description="RNA sequence transformer",
    )

    registry.register(
        entry,
    )

    result = registry.get(
        "rna_transformer",
    )

    assert result == entry


def test_list_models() -> None:
    """
    Registry lists models.
    """

    registry = ModelRegistry()

    registry.register(
        ModelRegistryEntry(
            name="rna_cnn",
            version="1.0",
            model_type="cnn",
            description="RNA CNN",
        ),
    )

    assert registry.list_models() == ("rna_cnn",)
