"""
RNAOS self-learning model router.
"""

from __future__ import annotations

from dl.models.model_route import (
    ModelRoute,
)


class ModelRouterEngine:
    """
    Selects best model based on workload.
    """

    def route(
        self,
        task: str,
        sequence_length: int,
        dataset_size: int,
    ) -> ModelRoute:
        """
        Select optimal model.
        """

        if "structure" in task:
            return ModelRoute(
                selected_model="gnn",
                score=0.95,
                reasoning=("Structural tasks benefit from graph representations."),
            )

        if sequence_length > 1000:
            return ModelRoute(
                selected_model="transformer",
                score=0.9,
                reasoning=("Long sequences require attention mechanisms."),
            )

        if dataset_size < 1000:
            return ModelRoute(
                selected_model="cnn",
                score=0.75,
                reasoning=("CNN provides efficient learning for smaller datasets."),
            )

        return ModelRoute(
            selected_model="transformer",
            score=0.8,
            reasoning=("Transformer selected as general sequence model."),
        )
