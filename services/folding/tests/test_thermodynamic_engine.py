from folding.energy.energy_engine import ThermodynamicEngine


def test_energy_profile():
    sequence = "GGGAAAUCC"

    structure = "(((...)))"

    engine = ThermodynamicEngine()

    profile = engine.evaluate(
        sequence,
        structure,
    )

    assert isinstance(profile.mfe, float)

    assert isinstance(
        profile.candidate_energy,
        float,
    )

    assert isinstance(
        profile.energy_gap,
        float,
    )

    assert isinstance(
        profile.normalized_gap,
        float,
    )


def test_mfe_gap_zero():
    sequence = "GGGAAAUCC"

    engine = ThermodynamicEngine()

    result = engine.vienna.fold(sequence)

    profile = engine.evaluate(
        sequence,
        result.dot_bracket,
    )

    assert abs(profile.energy_gap) < 1e-6

    assert profile.is_optimal
