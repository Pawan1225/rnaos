"""
RNAOS neural architecture registry.
"""

from __future__ import annotations

from dl.core.base_model import (
    BaseDeepLearningModel,
)


class ArchitectureRegistry:
    """
    Registry for deep learning architectures.
    """

    def __init__(
        self,
    ) -> None:
        self._architectures: dict[
            str,
            type[BaseDeepLearningModel],
        ] = {}

    def register(
        self,
        name: str,
        architecture: type[BaseDeepLearningModel],
    ) -> None:
        """
        Register architecture.
        """

        self._architectures[name] = architecture

    def get(
        self,
        name: str,
    ) -> type[BaseDeepLearningModel]:
        """
        Retrieve architecture.
        """

        if name not in self._architectures:
            raise KeyError(
                f"Architecture not found: {name}",
            )

        return self._architectures[name]

    def list_architectures(
        self,
    ) -> tuple[str, ...]:
        """
        List available architectures.
        """

        return tuple(
            self._architectures.keys(),
        )
