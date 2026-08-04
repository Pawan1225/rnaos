from decision.api import (
    DecisionAPI,
)
from decision.models import (
    Explanation,
)


def test_build_graph():
    """DecisionAPI should build a complete reasoning graph."""

    api = DecisionAPI()

    graph = api.build_graph(
        Explanation(
            recommendation="Solver",
            confidence=0.90,
        ),
        Explanation(
            recommendation="Optimization",
            confidence=1.00,
        ),
        Explanation(
            recommendation="Folding",
            confidence=0.95,
        ),
    )

    assert len(graph.nodes) == 3

    assert len(graph.edges) == 2


def test_api_exists():
    """DecisionAPI should expose all public interfaces."""

    api = DecisionAPI()

    assert api is not None

    assert hasattr(
        api,
        "explain_solver",
    )

    assert hasattr(
        api,
        "explain_folding",
    )

    assert hasattr(
        api,
        "explain_optimization",
    )

    assert hasattr(
        api,
        "build_graph",
    )
