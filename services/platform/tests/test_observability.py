from rnaos_platform.observability import (
    LogLevel,
    Observability,
    TraceRecord,
)


def test_log() -> None:
    obs = Observability()

    obs.log(
        level=LogLevel.INFO,
        component="solver",
        message="Completed",
    )

    logs = obs.logs()

    assert len(logs) == 1
    assert logs[0].level == LogLevel.INFO
    assert logs[0].component == "solver"


def test_metric() -> None:
    obs = Observability()

    obs.metric(
        name="runtime",
        value=0.25,
        unit="seconds",
    )

    metrics = obs.metrics()

    assert len(metrics) == 1
    assert metrics[0].name == "runtime"
    assert metrics[0].value == 0.25
    assert metrics[0].unit == "seconds"


def test_trace() -> None:
    obs = Observability()

    trace = TraceRecord(
        component="workflow",
        operation="execute",
    )

    obs.trace(trace)

    traces = obs.traces()

    assert len(traces) == 1
    assert traces[0].component == "workflow"


def test_trace_id() -> None:
    obs = Observability()

    obs.log(
        level=LogLevel.INFO,
        component="workflow",
        message="Started",
        trace_id="trace-001",
    )

    logs = obs.logs()

    assert logs[0].trace_id == "trace-001"


def test_workflow_id() -> None:
    obs = Observability()

    obs.log(
        level=LogLevel.INFO,
        component="workflow",
        message="Started",
        workflow_id="workflow-001",
    )

    logs = obs.logs()

    assert logs[0].workflow_id == "workflow-001"


def test_metric_labels() -> None:
    obs = Observability()

    obs.metric(
        name="solver.runtime",
        value=0.42,
        labels={
            "solver": "annealing",
        },
    )

    metrics = obs.metrics()

    assert metrics[0].labels["solver"] == "annealing"


def test_clear() -> None:
    obs = Observability()

    obs.log(
        level=LogLevel.INFO,
        component="workflow",
        message="Started",
    )

    obs.metric(
        name="runtime",
        value=1.0,
    )

    obs.trace(
        TraceRecord(),
    )

    obs.clear()

    assert len(obs.logs()) == 0
    assert len(obs.metrics()) == 0
    assert len(obs.traces()) == 0


def test_multiple_logs() -> None:
    obs = Observability()

    obs.log(
        level=LogLevel.INFO,
        component="workflow",
        message="Start",
    )

    obs.log(
        level=LogLevel.ERROR,
        component="solver",
        message="Failure",
    )

    assert len(obs.logs()) == 2


def test_multiple_metrics() -> None:
    obs = Observability()

    obs.metric(
        name="runtime",
        value=1.0,
    )

    obs.metric(
        name="accuracy",
        value=0.99,
    )

    assert len(obs.metrics()) == 2


def test_multiple_traces() -> None:
    obs = Observability()

    obs.trace(
        TraceRecord(
            component="workflow",
        ),
    )

    obs.trace(
        TraceRecord(
            component="solver",
        ),
    )

    assert len(obs.traces()) == 2
