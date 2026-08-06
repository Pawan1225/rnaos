"""
RNAOS deep learning model abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseDeepLearningModel(ABC):
    """
    Abstract interface for all RNAOS deep learning models.

    Every neural architecture must implement this
    standardized contract.
    """

    @abstractmethod
    def train(
        self,
        dataset: Any,
    ) -> Any:
        """
        Train the model.
        """
        raise NotImplementedError

    @abstractmethod
    def predict(
        self,
        inputs: Any,
    ) -> Any:
        """
        Generate predictions.
        """
        raise NotImplementedError

    @abstractmethod
    def evaluate(
        self,
        dataset: Any,
    ) -> dict[str, float]:
        """
        Evaluate model performance.
        """
        raise NotImplementedError

    @abstractmethod
    def save(
        self,
        path: Path,
    ) -> None:
        """
        Save model checkpoint.
        """
        raise NotImplementedError

    @abstractmethod
    def load(
        self,
        path: Path,
    ) -> None:
        """
        Load model checkpoint.
        """
        raise NotImplementedError
