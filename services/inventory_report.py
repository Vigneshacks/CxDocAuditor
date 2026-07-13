from pathlib import Path

from controller import generate_report


def generate_inventory_report(
    system_folder,
    output_folder,
    progress_callback=None,
):

   return generate_report(
    system_folder,
    output_folder,
    progress_callback,
)