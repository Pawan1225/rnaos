"""
RNAOS research pipeline.
"""

from __future__ import annotations

from research.analysis.statistical_analyzer import StatisticalAnalyzer
from research.datasets.benchmark_dataset import BenchmarkDataset
from research.experiments.experiment_runner import ExperimentRunner
from research.reporting.report_generator import ReportGenerator
from research.reporting.research_report import ResearchReport
from research.visualization.visualizer import Visualizer


class ResearchPipeline:
    """
    Execute the complete RNAOS research workflow.
    """

    def __init__(
        self,
        runner: ExperimentRunner,
    ) -> None:
        self.runner = runner

        self.analyzer = StatisticalAnalyzer()

        self.report_generator = ReportGenerator()

        self.visualizer = Visualizer()

    def run(
        self,
        dataset: BenchmarkDataset,
        *,
        title: str = "RNAOS Benchmark Report",
        authors: list[str] | None = None,
    ) -> dict[str, object]:
        """
        Execute the complete research workflow.
        """

        metrics = [self.runner.run(case) for case in dataset]

        summary = self.analyzer.summarize(metrics)

        report = ResearchReport(
            title=title,
            summary=summary,
            authors=authors or [],
        )

        markdown = self.report_generator.to_markdown(report)

        visualizations = self.visualizer.dashboard(summary)

        return {
            "metrics": metrics,
            "summary": summary,
            "report": report,
            "markdown": markdown,
            "visualizations": visualizations,
        }
