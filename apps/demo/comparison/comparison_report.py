"""
RNAOS comparison report generator.
"""


def create_comparison_report(
    result,
) -> dict:
    """
    Convert comparison result into report.
    """

    return {
        "sequence": result.sequence,
        "accuracy": (result.structure_accuracy),
        "energy_gap": (result.energy_gap),
        "rnaos_runtime": (result.rnaos_runtime),
        "reference_runtime": (result.reference_runtime),
        "status": result.status,
    }
