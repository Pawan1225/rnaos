"""
RNAOS model selection engine.
"""

from __future__ import annotations

from dl.models.model_selection import (
    ModelSelection,
)


class ModelSelectionEngine:
    """
    Selects suitable deep learning models.
    """

    def select(
        self,
        task: str,
    ) -> ModelSelection:
        """
        Select model based on task.
        """

        if "structure" in task:
            return ModelSelection(
                model_family="gnn",
                reasoning=("Graph models suit structural RNA tasks."),
            )

        if "sequence" in task:
            return ModelSelection(
                model_family="transformer",
                reasoning=("Transformers capture sequence dependencies."),
            )

        return ModelSelection(
            model_family="mlp",
            reasoning=("Default general-purpose model."),
        )
