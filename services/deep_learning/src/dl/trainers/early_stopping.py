"""
RNAOS early stopping controller.
"""

from __future__ import annotations


class EarlyStoppingController:
    """
    Controls training termination based on
    validation improvement.
    """

    def __init__(
        self,
        patience: int = 5,
        minimum_delta: float = 0.0,
    ) -> None:
        self.patience = patience

        self.minimum_delta = minimum_delta

        self.best_loss: float | None = None

        self.wait_count = 0

        self.should_stop = False

    def update(
        self,
        validation_loss: float,
    ) -> bool:
        """
        Update stopping state.

        Returns True when training should stop.
        """

        if self.best_loss is None:
            self.best_loss = validation_loss
            return False

        improvement = self.best_loss - validation_loss

        if improvement > self.minimum_delta:
            self.best_loss = validation_loss
            self.wait_count = 0

        else:
            self.wait_count += 1

        if self.wait_count >= self.patience:
            self.should_stop = True

        return self.should_stop

    def reset(
        self,
    ) -> None:
        """
        Reset controller state.
        """

        self.best_loss = None

        self.wait_count = 0

        self.should_stop = False
