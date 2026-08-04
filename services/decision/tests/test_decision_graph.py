from decision.graph import (
    DecisionGraph,
    DecisionNode,
)
from decision.models.explanation import (
    Explanation,
)


def test_graph():
    """Test basic graph construction."""

    graph = DecisionGraph()

    graph.add_node(
        DecisionNode(
            identifier="rna",
            explanation=Explanation(
                recommendation="RNA Input",
                confidence=1.0,
            ),
        )
    )

    graph.add_node(
        DecisionNode(
            identifier="solver",
            explanation=Explanation(
                recommendation="Exact Solver",
                confidence=0.95,
            ),
        )
    )

    graph.add_edge(
        "rna",
        "solver",
        "produces",
    )

    assert len(graph.nodes) == 2
    assert len(graph.edges) == 1
    assert graph.children("rna") == ["solver"]
    assert graph.parents("solver") == ["rna"]


def test_has_node():
    """Test node lookup."""

    graph = DecisionGraph()

    graph.add_node(
        DecisionNode(
            identifier="optimization",
            explanation=Explanation(
                recommendation="QUBO",
                confidence=1.0,
            ),
        )
    )

    assert graph.has_node("optimization")
    assert not graph.has_node("missing")


def test_node_retrieval():
    """Test retrieving a stored node."""

    graph = DecisionGraph()

    node = DecisionNode(
        identifier="confidence",
        explanation=Explanation(
            recommendation="Confidence",
            confidence=0.92,
        ),
    )

    graph.add_node(node)

    retrieved = graph.node("confidence")

    assert retrieved.identifier == "confidence"
    assert retrieved.explanation.confidence == 0.92
