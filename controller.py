from pathlib import Path

from core.scanner import scan_system
from excel.writer import generate_excel_report


def generate_report(
    system_folder,
    output_folder,
    progress_callback=None,
):

    report_data = scan_system(
    system_folder,
    progress_callback,
)

    inventory = report_data["inventory"]

    metadata = report_data["metadata"]

    report = generate_excel_report(
    inventory,
    output_folder,
)

    return report