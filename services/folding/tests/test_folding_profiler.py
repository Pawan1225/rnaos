from folding.profilers.folding_profiler import FoldingProfiler


def test_folding_profile():
    sequence = "GGGAAAUCC"

    profile = FoldingProfiler().profile(sequence)

    assert profile.secondary_structure.length == len(sequence)

    assert profile.search_space.variable_count > 0

    assert profile.thermodynamics.mfe <= 0


def test_energy_gap_zero():
    sequence = "GGGAAAUCC"

    profile = FoldingProfiler().profile(sequence)

    assert abs(profile.thermodynamics.energy_gap) < 1e-6

    assert profile.thermodynamics.is_optimal
