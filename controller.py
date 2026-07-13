from pathlib import Path

from core.scanner import scan_system
from excel.writer import generate_excel_report


def generate_report(
    system_folder: Path,
    output_folder: Path,
):

    report_data = scan_system(system_folder)

    inventory = report_data["inventory"]

    metadata = report_data["metadata"]

    report = generate_excel_report(
    inventory,
    output_folder,
)

    return report