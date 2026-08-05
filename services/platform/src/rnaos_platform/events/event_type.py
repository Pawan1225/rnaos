"""
RNAOS platform event types.
"""

from __future__ import annotations

from enum import StrEnum


class EventType(StrEnum):
    """Supported platform event types."""

    # ------------------------------------------------------------------
    # RNA
    # ------------------------------------------------------------------

    RNA_LOADED = "rna.loaded"
    RNA_VALIDATED = "rna.validated"

    # ------------------------------------------------------------------
    # Folding
    # ------------------------------------------------------------------

    FOLDING_STARTED = "folding.started"
    FOLDING_COMPLETED = "folding.completed"

    # ------------------------------------------------------------------
    # Optimization
    # ------------------------------------------------------------------

    OPTIMIZATION_STARTED = "optimization.started"
    OPTIMIZATION_COMPLETED = "optimization.completed"

    # ------------------------------------------------------------------
    # Solver
    # ------------------------------------------------------------------

    SOLVER_SELECTED = "solver.selected"
    SOLVER_STARTED = "solver.started"
    SOLVER_COMPLETED = "solver.completed"

    # ------------------------------------------------------------------
    # Decision
    # ------------------------------------------------------------------

    DECISION_GENERATED = "decision.generated"

    # ------------------------------------------------------------------
    # Experiment
    # ------------------------------------------------------------------

    EXPERIMENT_STARTED = "experiment.started"
    EXPERIMENT_COMPLETED = "experiment.completed"

    # ------------------------------------------------------------------
    # Analytics
    # ------------------------------------------------------------------

    ANALYTICS_UPDATED = "analytics.updated"

    # ------------------------------------------------------------------
    # Workflow
    # ------------------------------------------------------------------

    WORKFLOW_STARTED = "workflow.started"

    WORKFLOW_STEP_STARTED = "workflow.step.started"

    WORKFLOW_STEP_COMPLETED = "workflow.step.completed"

    WORKFLOW_COMPLETED = "workflow.completed"

    # ------------------------------------------------------------------
    # Services
    # ------------------------------------------------------------------

    SERVICE_REGISTERED = "service.registered"
    SERVICE_UNREGISTERED = "service.unregistered"

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    CONFIG_UPDATED = "config.updated"

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    HEALTH_CHANGED = "health.changed"

    # ------------------------------------------------------------------
    # Errors
    # ------------------------------------------------------------------

    ERROR_OCCURRED = "error.occurred"
