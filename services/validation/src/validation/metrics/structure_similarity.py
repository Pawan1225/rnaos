"""
RNA structure similarity metrics.
"""

from __future__ import annotations

from validation.metrics.base_pair_analyzer import (
    BasePairAnalyzer,
)


class StructureSimilarity:
    """
    Calculates RNA structure similarity.
    """

    def __init__(self) -> None:
        self.analyzer = BasePairAnalyzer()

    def compare(
        self,
        predicted: str,
        reference: str,
    ) -> dict[str, float]:
        """
        Compare two RNA structures.

        Returns:
        - precision
        - recall
        - f1_score
        - base_pair_distance
        """

        predicted_pairs = set(
            self.analyzer.extract(
                predicted,
            )
        )

        reference_pairs = set(
            self.analyzer.extract(
                reference,
            )
        )

        common_pairs = predicted_pairs & reference_pairs

        precision = len(common_pairs) / len(predicted_pairs) if predicted_pairs else 0.0

        recall = len(common_pairs) / len(reference_pairs) if reference_pairs else 0.0

        f1 = 0.0 if precision + recall == 0 else (2 * precision * recall / (precision + recall))

        distance = len(predicted_pairs ^ reference_pairs)

        return {
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "base_pair_distance": float(
                distance,
            ),
        }
