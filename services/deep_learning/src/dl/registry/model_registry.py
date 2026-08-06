"""
RNAOS unified model registry.
"""

from __future__ import annotations

from dl.models.model_registry_entry import (
    ModelRegistryEntry,
)


class ModelRegistry:
    """
    Stores deep learning model metadata.
    """

    def __init__(
        self,
    ) -> None:
        self._models: dict[
            str,
            ModelRegistryEntry,
        ] = {}

    def register(
        self,
        entry: ModelRegistryEntry,
    ) -> None:
        """
        Register a model.
        """

        self._models[entry.name] = entry

    def get(
        self,
        name: str,
    ) -> ModelRegistryEntry:
        """
        Retrieve model metadata.
        """

        return self._models[name]

    def list_models(
        self,
    ) -> tuple[str, ...]:
        """
        List registered models.
        """

        return tuple(
            self._models.keys(),
        )
