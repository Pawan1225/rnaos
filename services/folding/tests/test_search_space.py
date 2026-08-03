from folding.basepairs import BasePairGenerator
from folding.search.search_space_builder import SearchSpaceBuilder


def test_search_space():
    generator = BasePairGenerator()

    candidates = generator.generate("GGGAAAUCC")

    search_space = SearchSpaceBuilder().build(candidates)

    assert search_space.variable_count == len(candidates)

    assert search_space.conflict_count >= 0


def test_conflicts_are_valid():
    generator = BasePairGenerator(minimum_loop_length=1)

    candidates = generator.generate("GGGAAAUCC")

    search_space = SearchSpaceBuilder().build(candidates)

    for edge in search_space.conflicts:
        assert edge.first != edge.second


def test_search_space_density():
    generator = BasePairGenerator(minimum_loop_length=1)

    candidates = generator.generate("GGGAAAUCC")

    search_space = SearchSpaceBuilder().build(candidates)

    assert search_space.density >= 0.0
