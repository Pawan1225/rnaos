from folding.basepairs import BasePairGenerator


def test_generate_candidates():
    sequence = "GGGAAAUCC"

    generator = BasePairGenerator()

    candidates = generator.generate(sequence)

    assert len(candidates) > 0


def test_pairing_rules():
    sequence = "AUGC"

    generator = BasePairGenerator(
        minimum_loop_length=1,
    )

    candidates = generator.generate(sequence)

    allowed = {
        ("A", "U"),
        ("U", "A"),
        ("G", "C"),
        ("C", "G"),
        ("G", "U"),
        ("U", "G"),
    }

    for candidate in candidates:
        assert (
            candidate.left_base,
            candidate.right_base,
        ) in allowed


def test_loop_constraint():
    sequence = "AAAAAU"

    generator = BasePairGenerator(
        minimum_loop_length=4,
    )

    candidates = generator.generate(sequence)

    for pair in candidates:
        assert pair.distance >= 4


def test_pair_type():
    generator = BasePairGenerator(
        minimum_loop_length=1,
    )

    candidates = generator.generate("AUGC")

    for candidate in candidates:
        assert "-" in candidate.pair_type
