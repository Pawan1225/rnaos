from folding.engines.vienna_engine import ViennaEngine


def test_fold():
    sequence = "GGGAAAUCC"

    engine = ViennaEngine()

    result = engine.fold(sequence)

    assert result.sequence == sequence
    assert len(result.dot_bracket) == len(sequence)
    assert isinstance(result.mfe, float)

    # Ensure base pairs were extracted
    assert isinstance(result.base_pairs, list)


def test_energy_evaluation():
    sequence = "GGGAAAUCC"

    engine = ViennaEngine()

    result = engine.fold(sequence)

    energy = engine.evaluate(
        sequence,
        result.dot_bracket,
    )

    assert isinstance(energy, float)


def test_mfe():
    sequence = "GGGAAAUCC"

    engine = ViennaEngine()

    mfe = engine.mfe(sequence)

    assert isinstance(mfe, float)
