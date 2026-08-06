"""
RNAOS deep learning encoder abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseEncoder(ABC):
    """
    Abstract interface for neural encoders.

    Encoders transform biological inputs into
    learned representations.
    """

    @abstractmethod
    def encode(
        self,
        inputs: Any,
    ) -> Any:
        """
        Encode biological input into a representation.
        """
        raise NotImplementedError

    @abstractmethod
    def output_dimension(
        self,
    ) -> int:
        """
        Return embedding dimension.
        """
        raise NotImplementedError

    @abstractmethod
    def save(
        self,
        path: str,
    ) -> None:
        """
        Save encoder parameters.
        """
        raise NotImplementedError

    @abstractmethod
    def load(
        self,
        path: str,
    ) -> None:
        """
        Load encoder parameters.
        """
        raise NotImplementedError
