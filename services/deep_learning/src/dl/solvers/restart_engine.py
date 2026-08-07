"""
RNAOS restart strategy engine.
"""

from __future__ import annotations

from dl.models.optimization.restart_strategy import (
    RestartDecision,
)


class RestartStrategyEngine:
    """
    Determines optimization restarts.
    """

    def __init__(
        self,
        patience: int = 100,
    ) -> None:
        self.patience = patience

    def evaluate(
        self,
        iterations_without_improvement: int,
    ) -> RestartDecision:
        """
        Decide whether restart is required.
        """

        if iterations_without_improvement >= self.patience:
            return RestartDecision(
                restart=True,
                reason="stagnation",
            )

        return RestartDecision(
            restart=False,
            reason="progressing",
        )
