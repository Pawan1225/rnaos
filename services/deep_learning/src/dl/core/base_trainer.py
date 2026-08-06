"""
RNAOS deep learning trainer abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTrainer(ABC):
    """
    Abstract interface for deep learning trainers.

    Defines the lifecycle of neural model training.
    """

    @abstractmethod
    def train(
        self,
        model: Any,
        dataset: Any,
    ) -> Any:
        """
        Train a deep learning model.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(
        self,
        model: Any,
        dataset: Any,
    ) -> dict[str, float]:
        """
        Validate model performance.
        """
        raise NotImplementedError

    @abstractmethod
    def save_checkpoint(
        self,
        model: Any,
        path: str,
    ) -> None:
        """
        Save training checkpoint.
        """
        raise NotImplementedError

    @abstractmethod
    def load_checkpoint(
        self,
        path: str,
    ) -> Any:
        """
        Load training checkpoint.
        """
        raise NotImplementedError
