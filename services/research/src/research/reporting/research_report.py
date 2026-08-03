"""
Research report model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from research.analysis.statistical_summary import StatisticalSummary


@dataclass(frozen=True, slots=True)
class ResearchReport:
    """
    Publication-ready research report.
    """

    title: str

    summary: StatisticalSummary

    authors: list[str] = field(default_factory=list)

    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def has_authors(self) -> bool:
        """Return True if at least one author is defined."""
        return bool(self.authors)
