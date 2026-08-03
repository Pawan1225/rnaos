from research.experiments.experiment_runner import ExperimentRunner
from research.metrics.evaluation_metrics import MetricsFactory
from research.models.benchmark_case import BenchmarkCase


def stage_rna(context):
    context.metadata["rna"] = True
    return context


def stage_ai(context):
    assert context.metadata["rna"]
    context.metadata["ai"] = True
    return context


def stage_folding(context):
    assert context.metadata["ai"]
    context.metadata["folding"] = True
    return context


def stage_optimization(context):
    assert context.metadata["folding"]
    context.metadata["optimization"] = True
    return context


def stage_solver(context):
    assert context.metadata["optimization"]
    context.metadata["solver"] = True
    return context


def stage_evaluation(context):
    context.metrics = MetricsFactory.build(
        benchmark_id=context.benchmark_id,
        solver_name="IntegrationSolver",
        objective_value=-10.5,
        runtime_seconds=0.25,
        metadata={
            "sequence_length": len(context.sequence),
        },
    )

    context.metadata["evaluation"] = True

    return context


def test_complete_pipeline():
    runner = ExperimentRunner(
        stages=[
            stage_rna,
            stage_ai,
            stage_folding,
            stage_optimization,
            stage_solver,
            stage_evaluation,
        ]
    )

    case = BenchmarkCase(
        sequence_id="integration001",
        sequence="GGGAAAUCC",
    )

    result = runner.run(case)

    assert result.successful

    assert result.metrics.solver_name == "IntegrationSolver"

    assert result.metadata["rna"]

    assert result.metadata["ai"]

    assert result.metadata["folding"]

    assert result.metadata["optimization"]

    assert result.metadata["solver"]

    assert result.metadata["evaluation"]


def test_pipeline_without_metrics():
    runner = ExperimentRunner(
        stages=[
            stage_rna,
            stage_ai,
        ]
    )

    case = BenchmarkCase(
        sequence_id="integration002",
        sequence="AUGCGGAU",
    )

    import pytest

    with pytest.raises(RuntimeError):
        runner.run(case)
