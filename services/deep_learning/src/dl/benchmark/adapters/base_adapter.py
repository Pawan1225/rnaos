"""
RNAOS benchmark adapter interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BenchmarkAdapter(ABC):
    """
    Base interface for benchmark methods.
    """

    @property
    @abstractmethod
    def name(
        self,
    ) -> str:
        """
        Return adapter name.
        """

        raise NotImplementedError

    @abstractmethod
    def run(
        self,
        sequence: str,
    ):
        """
        Execute benchmark method.

        Args:
            sequence:
                RNA sequence input.
        """

        raise NotImplementedError
