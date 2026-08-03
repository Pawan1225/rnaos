from research.models.benchmark_case import BenchmarkCase
from research.models.experiment_context import ExperimentContext


def test_context_creation():
    case = BenchmarkCase(
        sequence_id="toy_001",
        sequence="GGGAAAUCC",
    )

    context = ExperimentContext(
        benchmark_case=case,
    )

    assert context.benchmark_id == "toy_001"
    assert context.sequence == "GGGAAAUCC"
    assert context.metrics is None
    assert not context.completed


def test_context_completion():
    case = BenchmarkCase(
        sequence_id="toy_001",
        sequence="GGGAAAUCC",
    )

    context = ExperimentContext(
        benchmark_case=case,
    )

    context.metrics = object()

    assert context.completed


def test_metadata():
    case = BenchmarkCase(
        sequence_id="toy_001",
        sequence="GGGAAAUCC",
    )

    context = ExperimentContext(
        benchmark_case=case,
    )

    context.metadata["dataset"] = "toy"

    assert context.metadata["dataset"] == "toy"
