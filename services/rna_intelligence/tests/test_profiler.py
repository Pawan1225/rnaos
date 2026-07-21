from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_rna_profiler():
    profiler = RNAProfiler()

    profile = profiler.profile("GGGAAAUCC")

    # Sequence
    assert profile.sequence.length == 9
    assert profile.sequence.sequence == "GGGAAAUCC"

    # Validation
    assert profile.validation.is_valid
    assert profile.validation.errors == []

    # Features
    assert profile.features.length == 9
    assert profile.features.base_counts["G"] == 3
    assert profile.features.base_counts["A"] == 3
    assert profile.features.base_counts["U"] == 1
    assert profile.features.base_counts["C"] == 2

    assert abs(profile.features.gc_content - (5 / 9)) < 1e-6
    assert abs(profile.features.au_content - (4 / 9)) < 1e-6

    assert profile.features.sequence_entropy > 0
