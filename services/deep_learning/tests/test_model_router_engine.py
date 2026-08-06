"""
Tests for model router engine.
"""

from __future__ import annotations

from dl.engines.model_router_engine import (
    ModelRouterEngine,
)
from dl.models.model_route import (
    ModelRoute,
)


def test_structure_routes_to_gnn() -> None:
    """
    Structure tasks use graph models.
    """

    engine = ModelRouterEngine()

    route = engine.route(
        task="rna_structure_prediction",
        sequence_length=200,
        dataset_size=5000,
    )

    assert isinstance(
        route,
        ModelRoute,
    )

    assert route.selected_model == "gnn"


def test_long_sequence_routes_transformer() -> None:
    """
    Long sequences use transformers.
    """

    engine = ModelRouterEngine()

    route = engine.route(
        task="sequence_analysis",
        sequence_length=5000,
        dataset_size=10000,
    )

    assert route.selected_model == "transformer"


def test_small_dataset_routes_cnn() -> None:
    """
    Small datasets use efficient models.
    """

    engine = ModelRouterEngine()

    route = engine.route(
        task="classification",
        sequence_length=200,
        dataset_size=500,
    )

    assert route.selected_model == "cnn"
