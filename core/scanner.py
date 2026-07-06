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