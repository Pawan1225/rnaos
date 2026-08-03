from research.experiments.experiment_runner import ExperimentRunner
from research.metrics.evaluation_metrics import MetricsFactory
from research.models.benchmark_case import BenchmarkCase


def evaluation_stage(context):
    context.metrics = MetricsFactory.build(
        benchmark_id=context.benchmark_id,
        solver_name="DummySolver",
        objective_value=-5.0,
        runtime_seconds=0.01,
    )

    context.metadata["stage"] = "evaluation"

    return context


def test_runner():
    runner = ExperimentRunner(
        stages=[
            evaluation_stage,
        ]
    )

    case = BenchmarkCase(
        sequence_id="toy001",
        sequence="GGGAAAUCC",
    )

    result = runner.run(case)

    assert result.metrics.solver_name == "DummySolver"

    assert result.metadata["stage"] == "evaluation"


def test_add_stage():
    runner = ExperimentRunner()

    runner.add_stage(evaluation_stage)

    case = BenchmarkCase(
        sequence_id="toy001",
        sequence="GGGAAAUCC",
    )

    result = runner.run(case)

    assert result.successful
