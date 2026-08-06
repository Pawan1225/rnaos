"""
RNAOS deep learning dataset abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseDeepLearningDataset(ABC):
    """
    Abstract dataset interface for deep learning.

    All neural datasets in RNAOS must implement
    this contract.
    """

    @abstractmethod
    def __len__(
        self,
    ) -> int:
        """
        Return dataset size.
        """
        raise NotImplementedError

    @abstractmethod
    def __getitem__(
        self,
        index: int,
    ) -> Any:
        """
        Return one training sample.
        """
        raise NotImplementedError

    @abstractmethod
    def batch(
        self,
        batch_size: int,
    ) -> Any:
        """
        Generate training batches.
        """
        raise NotImplementedError
