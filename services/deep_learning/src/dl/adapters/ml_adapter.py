"""
RNAOS machine learning adapter.

Bridges classical machine learning outputs
with the deep learning platform.
"""

from __future__ import annotations

from typing import Any


class MLAdapter:
    """
    Converts ML representations into
    deep learning compatible inputs.
    """

    def convert_features(
        self,
        features: Any,
    ) -> dict[str, Any]:
        """
        Convert classical ML features
        into neural input format.
        """

        return {
            "features": features,
        }

    def convert_dataset(
        self,
        dataset: Any,
    ) -> dict[str, Any]:
        """
        Convert ML dataset representation
        into deep learning input format.
        """

        return {
            "dataset": dataset,
        }

    def convert_prediction(
        self,
        prediction: Any,
    ) -> dict[str, Any]:
        """
        Convert ML prediction output
        for hybrid intelligence workflows.
        """

        return {
            "prediction": prediction,
        }
