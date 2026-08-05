import pytest
from rnaos_platform.events import (
    Event,
    EventBus,
    EventType,
)
from rnaos_platform.workflow import (
    WorkflowContext,
    WorkflowEngine,
    WorkflowStatus,
    WorkflowStep,
)


def test_workflow_execution() -> None:
    engine = WorkflowEngine()

    def step_one(context: WorkflowContext) -> None:
        context.data["rna"] = "loaded"

    def step_two(context: WorkflowContext) -> None:
        context.data["optimization"] = "done"

    engine.add_step(
        WorkflowStep(
            name="RNA",
            action=step_one,
        ),
    )

    engine.add_step(
        WorkflowStep(
            name="Optimization",
            action=step_two,
        ),
    )

    context = engine.execute()

    assert context.status == WorkflowStatus.COMPLETED
    assert context.data["rna"] == "loaded"
    assert context.data["optimization"] == "done"


def test_steps() -> None:
    engine = WorkflowEngine()

    engine.add_step(
        WorkflowStep(
            name="Decision",
        ),
    )

    assert len(engine.steps()) == 1


def test_workflow_events() -> None:
    bus = EventBus()

    received: list[EventType] = []

    def handler(event: Event) -> None:
        received.append(event.event_type)

    bus.subscribe(
        EventType.WORKFLOW_STARTED,
        handler,
    )

    bus.subscribe(
        EventType.WORKFLOW_COMPLETED,
        handler,
    )

    engine = WorkflowEngine(
        event_bus=bus,
    )

    engine.execute()

    assert EventType.WORKFLOW_STARTED in received
    assert EventType.WORKFLOW_COMPLETED in received


def test_failed_workflow() -> None:
    engine = WorkflowEngine()

    def failing_step(
        context: WorkflowContext,
    ) -> None:
        raise RuntimeError(
            "failure",
        )

    engine.add_step(
        WorkflowStep(
            name="Failure",
            action=failing_step,
        ),
    )

    with pytest.raises(
        RuntimeError,
    ):
        engine.execute()


def test_existing_context() -> None:
    engine = WorkflowEngine()

    context = WorkflowContext()

    engine.execute(
        context=context,
    )

    assert context.status == WorkflowStatus.COMPLETED


def test_step_metadata() -> None:
    step = WorkflowStep(
        name="RNA",
        metadata={
            "priority": 1,
        },
    )

    assert step.metadata["priority"] == 1


def test_context_metadata() -> None:
    context = WorkflowContext()

    context.metadata["user"] = "research"

    assert context.metadata["user"] == "research"
