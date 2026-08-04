from decision.explainers import FoldingExplainer
from folding.profilers.folding_profiler import FoldingProfiler


def test_folding_explanation():
    """Test RNA folding explanation generation."""

    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    explanation = FoldingExplainer().explain(
        folding,
    )

    assert explanation.recommendation == "RNA Secondary Structure Prediction"

    assert explanation.confidence > 0.0

    assert len(explanation.reasons) == 4

    assert explanation.metadata["candidate_pairs"] == folding.search_space.variable_count

    assert explanation.metadata["conflicts"] == folding.search_space.conflict_count

    assert explanation.metadata["mfe"] == folding.thermodynamics.mfe


def test_dot_bracket_metadata():
    """Dot-bracket notation should be preserved."""

    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    explanation = FoldingExplainer().explain(
        folding,
    )

    assert explanation.metadata["dot_bracket"] == folding.secondary_structure.dot_bracket


def test_tradeoffs_present():
    """Trade-offs should always be generated."""

    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    explanation = FoldingExplainer().explain(
        folding,
    )

    assert len(explanation.tradeoffs) > 0


def test_confidence_range():
    """Confidence must remain within [0,1]."""

    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    explanation = FoldingExplainer().explain(
        folding,
    )

    assert 0.0 <= explanation.confidence <= 1.0
