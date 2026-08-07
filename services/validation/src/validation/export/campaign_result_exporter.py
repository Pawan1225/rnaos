"""
RNAOS campaign result exporter.
"""

from __future__ import annotations

from dataclasses import asdict


class CampaignResultExporter:
    """
    Converts campaign results into
    persistent benchmark records.
    """

    def export(
        self,
        campaign_result,
    ) -> list[dict]:
        """
        Convert campaign results.

        Preserves complete experiment
        scientific records.
        """

        return [
            {
                **asdict(result),
                "status": "COMPLETED",
            }
            for result in campaign_result.experiment_results
        ]
