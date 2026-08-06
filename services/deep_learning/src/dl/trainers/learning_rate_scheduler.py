"""
RNAOS learning rate scheduler.
"""

from __future__ import annotations


class LearningRateScheduler:
    """
    Controls learning rate updates during training.
    """

    def __init__(
        self,
        initial_learning_rate: float = 0.001,
        decay_factor: float = 0.5,
    ) -> None:
        self.initial_learning_rate = initial_learning_rate

        self.decay_factor = decay_factor

        self.current_learning_rate = initial_learning_rate

    def step(
        self,
    ) -> float:
        """
        Apply learning rate decay.
        """

        self.current_learning_rate *= self.decay_factor

        return self.current_learning_rate

    def get_learning_rate(
        self,
    ) -> float:
        """
        Return current learning rate.
        """

        return self.current_learning_rate

    def reset(
        self,
    ) -> None:
        """
        Reset learning rate.
        """

        self.current_learning_rate = self.initial_learning_rate
