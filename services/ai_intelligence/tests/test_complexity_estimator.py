from ai_intelligence.complexity.complexity_estimator import (
    ComplexityEstimator,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_complexity_estimation():
    profiler = RNAProfiler()

    profile = profiler.profile("GGGAAAUCC")

    estimator = ComplexityEstimator()

    result = estimator.estimate(profile)

    assert 0.0 <= result.score <= 1.0

    assert result.category in {
        "easy",
        "moderate",
        "hard",
    }

    assert "Length" in result.explanation


def test_complexity_score_range(rna_profile):
    result = ComplexityEstimator().estimate(rna_profile)

    assert 0.0 <= result.score <= 1.0


def test_complexity_category(rna_profile):
    result = ComplexityEstimator().estimate(rna_profile)

    assert result.category in {
        "easy",
        "moderate",
        "hard",
    }
