from folding.profilers.folding_profiler import FoldingProfiler
from optimization.validation import QUBOValidator


def test_validation() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    report = QUBOValidator().validate(
        folding,
    )

    assert isinstance(report.vienna_mfe, float)
    assert isinstance(report.estimated_energy, float)

    assert report.absolute_error >= 0.0
    assert report.relative_error >= 0.0


def test_candidate_count() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    report = QUBOValidator().validate(
        folding,
    )

    assert report.candidate_pairs == folding.search_space.variable_count


def test_conflict_count() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    report = QUBOValidator().validate(
        folding,
    )

    assert report.conflicts == folding.search_space.conflict_count
