import pytest
from research.datasets.benchmark_dataset import BenchmarkDataset
from research.models.benchmark_case import BenchmarkCase


def make_case(
    sequence_id: str,
    sequence: str,
    *,
    source: str = "synthetic",
    family: str | None = None,
) -> BenchmarkCase:
    return BenchmarkCase(
        sequence_id=sequence_id,
        sequence=sequence,
        source=source,
        family=family,
    )


# ---------------------------------------------------------
# BenchmarkCase
# ---------------------------------------------------------


def test_sequence_is_converted_to_uppercase():
    case = make_case("case1", "augc")
    assert case.sequence == "AUGC"


def test_invalid_sequence_raises_error():
    with pytest.raises(ValueError):
        make_case("case1", "AUGTX")


def test_empty_sequence_raises_error():
    with pytest.raises(ValueError):
        make_case("case1", "")


def test_length_property():
    case = make_case("case1", "AUGCGG")
    assert case.length == 6


def test_gc_content():
    case = make_case("case1", "GGCCAA")
    assert case.gc_content == pytest.approx(4 / 6)


# ---------------------------------------------------------
# BenchmarkDataset
# ---------------------------------------------------------


def test_add_case():
    dataset = BenchmarkDataset("Test")

    case = make_case("case1", "AUGC")
    dataset.add_case(case)

    assert len(dataset) == 1


def test_duplicate_case():
    dataset = BenchmarkDataset("Test")

    case = make_case("case1", "AUGC")

    dataset.add_case(case)

    with pytest.raises(ValueError):
        dataset.add_case(case)


def test_get_case():
    dataset = BenchmarkDataset("Test")

    case = make_case("case1", "AUGC")

    dataset.add_case(case)

    assert dataset.get_case("case1") is case


def test_remove_case():
    dataset = BenchmarkDataset("Test")

    case = make_case("case1", "AUGC")

    dataset.add_case(case)
    dataset.remove_case("case1")

    assert len(dataset) == 0


def test_iteration():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA"))
    dataset.add_case(make_case("b", "GGGG"))

    ids = {case.sequence_id for case in dataset}

    assert ids == {"a", "b"}


def test_filter_by_source():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA", source="RNA STRAND"))

    dataset.add_case(make_case("b", "GGGG", source="synthetic"))

    results = dataset.filter(source="RNA STRAND")

    assert len(results) == 1
    assert results[0].sequence_id == "a"


def test_filter_by_family():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA", family="tRNA"))

    dataset.add_case(make_case("b", "GGGG", family="rRNA"))

    results = dataset.filter(family="tRNA")

    assert len(results) == 1
    assert results[0].family == "tRNA"


def test_filter_by_length():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA"))
    dataset.add_case(make_case("b", "GGGGGGGG"))
    dataset.add_case(make_case("c", "AUGCAUGCAUGC"))

    results = dataset.filter(min_length=6)

    assert len(results) == 2


def test_average_length():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA"))
    dataset.add_case(make_case("b", "GGGGGG"))

    assert dataset.average_length == pytest.approx(5.0)


def test_average_gc_content():
    dataset = BenchmarkDataset("Test")

    dataset.add_case(make_case("a", "AAAA"))
    dataset.add_case(make_case("b", "GGGG"))

    assert dataset.average_gc_content == pytest.approx(0.5)


def test_empty_dataset_statistics():
    dataset = BenchmarkDataset("Empty")

    assert dataset.average_length == 0.0
    assert dataset.average_gc_content == 0.0
