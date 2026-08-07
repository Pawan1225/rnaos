"""
RNAOS quantum-inspired feature mapper.
"""

from __future__ import annotations

from dl.models.optimization.quantum_feature import (
    QuantumFeatureVector,
)


class QuantumFeatureMapper:
    """
    Maps neural embeddings into
    optimization feature space.
    """

    def map(
        self,
        embedding: tuple[float, ...],
    ) -> QuantumFeatureVector:
        """
        Transform embedding.
        """

        if not embedding:
            raise ValueError(
                "Embedding cannot be empty",
            )

        magnitude = sum(value * value for value in embedding) ** 0.5

        if magnitude == 0:
            raise ValueError(
                "Embedding magnitude cannot be zero",
            )

        normalized = tuple(value / magnitude for value in embedding)

        return QuantumFeatureVector(
            values=normalized,
            dimension=len(
                normalized,
            ),
            normalization=magnitude,
        )
