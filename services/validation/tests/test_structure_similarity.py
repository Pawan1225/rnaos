"""
Tests for RNA structure similarity.
"""

from validation.metrics.structure_similarity import (
    StructureSimilarity,
)


def test_similarity_identical():

    metric = StructureSimilarity()

    result = metric.compare(
        "(((...)))",
        "(((...)))",
    )

    assert result["f1_score"] == 1.0


def test_similarity_difference():

    metric = StructureSimilarity()

    result = metric.compare(
        "(((...)))",
        ".........",
    )

    assert result["f1_score"] == 0.0
