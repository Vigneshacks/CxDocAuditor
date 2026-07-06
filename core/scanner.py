"""
scanner.py

Scanner Engine

Responsible for discovering equipment folders
inside a selected commissioning system.
"""

from pathlib import Path

from utils.logger import logger


def discover_equipment(system_folder: Path) -> list[Path]:
    """
    Discover all equipment folders inside the selected system.
    """

    logger.info("Scanning system: %s", system_folder)

    if not system_folder.exists():
        logger.error("System folder does not exist.")
        raise FileNotFoundError(system_folder)

    equipment = sorted(
        [
            folder
            for folder in system_folder.iterdir()
            if folder.is_dir()
        ],
        key=lambda folder: folder.name
    )

    logger.info("Found %d equipment folders.", len(equipment))

    return equipment


def discover_levels(equipment_folder: Path) -> list[Path]:
    """
    Discover all level folders (L2-A, L2-B, etc.)
    inside an equipment folder.

    Parameters
    ----------
    equipment_folder : Path

    Returns
    -------
    list[Path]
    """

    levels = sorted(

        [

            folder

            for folder in equipment_folder.iterdir()

            if folder.is_dir()

        ],

        key=lambda folder: folder.name

    )

    logger.info(
        "Found %d levels for %s",
        len(levels),
        equipment_folder.name,
    )

    return levels
def discover_document_folders(level_folder: Path) -> list[Path]:

    document_folders = sorted(
        [
            folder
            for folder in level_folder.iterdir()
            if folder.is_dir()
        ],
        key=lambda folder: folder.name
    )

    logger.info(
        "Found %d document folders in %s",
        len(document_folders),
        level_folder.name,
    )

    return document_folders

def scan_system(system_folder: Path) -> list[dict]:
    """
    Scan the selected system folder and build an inventory
    of all equipment, levels, and document folders.

    Parameters
    ----------
    system_folder : Path
        Path to the selected commissioning system.

    Returns
    -------
    list[dict]
        System inventory.
    """

    equipment_folders = discover_equipment(system_folder)

    system_inventory = []

    for equipment in equipment_folders:

        level_inventory = {}

        levels = discover_levels(equipment)

        for level in levels:

            document_folders = discover_document_folders(level)

            level_inventory[level.name] = document_folders

        system_inventory.append(
            {
                "reference": equipment.name,
                "path": equipment,
                "levels": level_inventory,
            }
        )

    logger.info(
        "System scan completed. %d equipment discovered.",
        len(system_inventory),
    )

    return system_inventory