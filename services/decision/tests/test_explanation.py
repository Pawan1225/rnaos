from decision.models import (
    DecisionReason,
    Evidence,
    Explanation,
)


def test_create_evidence():
    """Evidence objects should be created successfully."""

    evidence = Evidence(
        name="Problem Size",
        value=58,
        description="Number of optimization variables.",
        source="OptimizationProfiler",
        weight=0.95,
    )

    assert evidence.name == "Problem Size"
    assert evidence.value == 58
    assert evidence.weight == 0.95


def test_create_decision_reason():
    """DecisionReason should store supporting evidence."""

    evidence = Evidence(
        name="Problem Size",
        value=58,
        description="Number of optimization variables.",
        source="OptimizationProfiler",
    )

    reason = DecisionReason(
        title="Large Optimization Problem",
        description="Exact solvers become impractical.",
        importance=0.90,
        evidence=[evidence],
    )

    assert reason.title == "Large Optimization Problem"
    assert len(reason.evidence) == 1
    assert reason.evidence[0].name == "Problem Size"


def test_create_explanation():
    """Explanation should aggregate recommendation details."""

    evidence = Evidence(
        name="Problem Size",
        value=58,
        description="Number of optimization variables.",
        source="OptimizationProfiler",
    )

    reason = DecisionReason(
        title="Large Optimization Problem",
        description="Metaheuristics scale better.",
        evidence=[evidence],
    )

    explanation = Explanation(
        recommendation="Simulated Annealing",
        confidence=0.92,
        reasons=[reason],
        alternatives=[
            "Genetic Algorithm",
            "Tabu Search",
        ],
        tradeoffs=[
            "Fast runtime",
            "Near-optimal solution",
        ],
        metadata={
            "problem_size": 58,
        },
    )

    assert explanation.recommendation == "Simulated Annealing"
    assert explanation.confidence == 0.92
    assert len(explanation.reasons) == 1
    assert explanation.alternatives[0] == "Genetic Algorithm"
    assert explanation.metadata["problem_size"] == 58


def test_default_values():
    """Optional collections should default to empty."""

    explanation = Explanation(
        recommendation="Simulated Annealing",
    )

    assert explanation.reasons == []
    assert explanation.alternatives == []
    assert explanation.tradeoffs == []
    assert explanation.metadata == {}
    assert explanation.confidence == 1.0


def test_nested_serialization():
    """Nested models should serialize correctly."""

    evidence = Evidence(
        name="Density",
        value=0.81,
        description="QUBO density.",
        source="OptimizationProfiler",
    )

    reason = DecisionReason(
        title="Dense Graph",
        description="Dense QUBOs benefit from metaheuristics.",
        evidence=[evidence],
    )

    explanation = Explanation(
        recommendation="Simulated Annealing",
        reasons=[reason],
    )

    data = explanation.model_dump()

    assert data["recommendation"] == "Simulated Annealing"
    assert data["reasons"][0]["title"] == "Dense Graph"
    assert data["reasons"][0]["evidence"][0]["name"] == "Density"
