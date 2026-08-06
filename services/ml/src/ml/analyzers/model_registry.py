"""
RNAOS machine learning model registry.
"""

from __future__ import annotations

from ml.models.registered_model import (
    RegisteredModel,
)


class ModelRegistry:
    """
    In-memory registry for trained machine learning models.
    """

    def __init__(self) -> None:
        self._models: dict[str, RegisteredModel] = {}

    def register(
        self,
        model: RegisteredModel,
    ) -> None:
        """
        Register a model.
        """

        self._models[model.metadata.model_id] = model

    def get(
        self,
        model_id: str,
    ) -> RegisteredModel:
        """
        Retrieve a registered model.
        """

        if model_id not in self._models:
            raise KeyError(f"Model not found: {model_id}")

        return self._models[model_id]

    def list_models(
        self,
    ) -> tuple[str, ...]:
        """
        List registered model identifiers.
        """

        return tuple(self._models.keys())

    def remove(
        self,
        model_id: str,
    ) -> None:
        """
        Remove a registered model.
        """

        if model_id not in self._models:
            raise KeyError(f"Model not found: {model_id}")

        del self._models[model_id]
