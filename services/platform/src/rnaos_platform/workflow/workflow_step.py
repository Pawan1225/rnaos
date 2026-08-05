"""
RNAOS workflow step.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from rnaos_platform.workflow.workflow_context import WorkflowContext

WorkflowAction = Callable[
    [WorkflowContext],
    None,
]


@dataclass(
    slots=True,
)
class WorkflowStep:
    """A single executable workflow step."""

    name: str

    action: WorkflowAction | None = None

    service: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    def execute(
        self,
        context: WorkflowContext,
    ) -> None:
        """Execute the workflow step."""

        if self.action is not None:
            self.action(
                context,
            )
