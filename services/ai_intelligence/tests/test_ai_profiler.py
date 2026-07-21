from ai_intelligence.profilers.ai_profiler import AIProfiler
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_ai_profiler():
    """Test the complete AI profiling pipeline."""

    rna_profiler = RNAProfiler()

    rna_profile = rna_profiler.profile("GGGAAAUCC")

    ai_profiler = AIProfiler()

    ai_profile = ai_profiler.profile(rna_profile)

    assert ai_profile.features.dimension == 8

    assert ai_profile.embedding.dimension == 8

    assert 0 <= ai_profile.complexity.score <= 1

    assert ai_profile.recommendation.solver in {
        "classical",
        "hybrid",
        "quantum",
    }


def test_complete_ai_pipeline():
    """Ensure the entire pipeline produces a valid AIProfile."""

    rna_profile = RNAProfiler().profile("GGGAAAUCC")

    ai_profile = AIProfiler().profile(rna_profile)

    assert ai_profile.features.dimension == 8

    assert ai_profile.embedding.dimension == 8

    assert ai_profile.complexity.score >= 0.0

    assert ai_profile.recommendation.solver in {
        "classical",
        "hybrid",
        "quantum",
    }
