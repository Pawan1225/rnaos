"""
RNAOS platform event types.
"""

from __future__ import annotations

from enum import StrEnum


class EventType(StrEnum):
    """Supported platform event types."""

    # RNA
    RNA_LOADED = "rna.loaded"
    RNA_VALIDATED = "rna.validated"

    # Folding
    FOLDING_STARTED = "folding.started"
    FOLDING_COMPLETED = "folding.completed"

    # Optimization
    OPTIMIZATION_STARTED = "optimization.started"
    OPTIMIZATION_COMPLETED = "optimization.completed"

    # Solver
    SOLVER_SELECTED = "solver.selected"
    SOLVER_STARTED = "solver.started"
    SOLVER_COMPLETED = "solver.completed"

    # Experiment
    EXPERIMENT_STARTED = "experiment.started"
    EXPERIMENT_COMPLETED = "experiment.completed"

    # Analytics
    ANALYTICS_UPDATED = "analytics.updated"

    # Decision
    DECISION_GENERATED = "decision.generated"

    # Platform
    SERVICE_REGISTERED = "service.registered"
    SERVICE_UNREGISTERED = "service.unregistered"

    CONFIG_UPDATED = "config.updated"

    HEALTH_CHANGED = "health.changed"

    WORKFLOW_STARTED = "workflow.started"
    WORKFLOW_COMPLETED = "workflow.completed"

    ERROR_OCCURRED = "error.occurred"
