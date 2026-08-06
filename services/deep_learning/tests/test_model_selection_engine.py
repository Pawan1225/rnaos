"""
Tests for model selection engine.
"""

from __future__ import annotations

from dl.engines.model_selection_engine import (
    ModelSelectionEngine,
)
from dl.models.model_selection import (
    ModelSelection,
)


def test_structure_task_selects_gnn() -> None:
    """
    Structural tasks use graph models.
    """

    engine = ModelSelectionEngine()

    result = engine.select(
        "rna_structure_prediction",
    )

    assert isinstance(
        result,
        ModelSelection,
    )

    assert result.model_family == "gnn"


def test_sequence_task_selects_transformer() -> None:
    """
    Sequence tasks use transformers.
    """

    engine = ModelSelectionEngine()

    result = engine.select(
        "rna_sequence_analysis",
    )

    assert result.model_family == "transformer"


def test_default_selection() -> None:
    """
    Unknown tasks use default model.
    """

    engine = ModelSelectionEngine()

    result = engine.select(
        "unknown_task",
    )

    assert result.model_family == "mlp"
