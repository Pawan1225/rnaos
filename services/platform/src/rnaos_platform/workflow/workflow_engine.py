"""
RNAOS Workflow Engine.
"""

from __future__ import annotations

from rnaos_platform.config import ConfigManager
from rnaos_platform.events import Event, EventBus, EventType
from rnaos_platform.registry import ServiceRegistry
from rnaos_platform.workflow.workflow_context import WorkflowContext
from rnaos_platform.workflow.workflow_step import WorkflowStep


class WorkflowEngine:
    """Execute RNAOS workflows."""

    def __init__(
        self,
        config: ConfigManager | None = None,
        registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
    ) -> None:
        self._config = config if config is not None else ConfigManager()

        self._registry = registry if registry is not None else ServiceRegistry()

        self._event_bus = event_bus if event_bus is not None else EventBus()

        self._steps: list[WorkflowStep] = []

    def add_step(
        self,
        step: WorkflowStep,
    ) -> None:
        """Add a workflow step."""
        self._steps.append(
            step,
        )

    def steps(
        self,
    ) -> tuple[WorkflowStep, ...]:
        """Return workflow steps."""
        return tuple(
            self._steps,
        )

    def execute(
        self,
        context: WorkflowContext | None = None,
    ) -> WorkflowContext:
        """Execute the workflow."""

        workflow = context if context is not None else WorkflowContext()

        workflow.start()

        self._event_bus.publish(
            Event(
                event_type=EventType.WORKFLOW_STARTED,
                source="workflow_engine",
                payload={
                    "workflow_id": workflow.workflow_id,
                },
            ),
        )

        try:
            for step in self._steps:
                self._event_bus.publish(
                    Event(
                        event_type=EventType.WORKFLOW_STEP_STARTED,
                        source="workflow_engine",
                        payload={
                            "workflow_id": workflow.workflow_id,
                            "step": step.name,
                        },
                    ),
                )

                step.execute(
                    workflow,
                )

                self._event_bus.publish(
                    Event(
                        event_type=EventType.WORKFLOW_STEP_COMPLETED,
                        source="workflow_engine",
                        payload={
                            "workflow_id": workflow.workflow_id,
                            "step": step.name,
                        },
                    ),
                )

            workflow.complete()

            self._event_bus.publish(
                Event(
                    event_type=EventType.WORKFLOW_COMPLETED,
                    source="workflow_engine",
                    payload={
                        "workflow_id": workflow.workflow_id,
                    },
                ),
            )

        except Exception as exc:
            workflow.fail()

            self._event_bus.publish(
                Event(
                    event_type=EventType.ERROR_OCCURRED,
                    source="workflow_engine",
                    payload={
                        "workflow_id": workflow.workflow_id,
                        "error": str(exc),
                    },
                ),
            )

            raise

        return workflow
