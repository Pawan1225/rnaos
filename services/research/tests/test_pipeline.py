from research.datasets.loader import load_dataset
from research.experiments.experiment_runner import ExperimentRunner
from research.metrics.evaluation_metrics import MetricsFactory
from research.pipeline import ResearchPipeline


class DummyRunner(ExperimentRunner):
    """Simple runner for pipeline integration tests."""

    def __init__(self) -> None:
        # Override the parent initializer because we don't need the
        # full RNAOS execution stack for this integration test.
        pass

    def run(self, case):
        return MetricsFactory.build(
            benchmark_id=case.sequence_id,
            solver_name="DummySolver",
            objective_value=-4.8,
            runtime_seconds=0.1,
            reference_objective=-5.0,
            solved=True,
            metadata={
                "sequence_length": case.length,
                "candidate_pairs": 10,
                "conflicts": 5,
                "qubo_size": 10,
            },
        )


def test_pipeline():
    dataset = load_dataset("toy")

    pipeline = ResearchPipeline(
        runner=DummyRunner(),
    )

    results = pipeline.run(
        dataset,
        title="RNAOS Pipeline Test",
        authors=["J. K. Pawan Kumar"],
    )

    assert len(results["metrics"]) == len(dataset)

    assert results["summary"].sample_size == len(dataset)

    assert results["report"].title == "RNAOS Pipeline Test"

    assert "# RNAOS Pipeline Test" in results["markdown"]

    assert "runtime" in results["visualizations"]

    assert "accuracy" in results["visualizations"]

    assert "error" in results["visualizations"]

    for metric in results["metrics"]:
        assert metric.benchmark_id != ""
        assert metric.solver_name == "DummySolver"
        assert metric.runtime_seconds > 0
        assert metric.accuracy >= 0.0
