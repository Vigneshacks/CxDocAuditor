from pathlib import Path

from controller import generate_report


def generate_inventory_report(
    system_folder: Path,
    output_folder: Path,
):

    return generate_report(
        system_folder,
        output_folder,
    )