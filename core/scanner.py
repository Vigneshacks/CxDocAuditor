"""
scanner.py

Scanner Engine

Responsible for discovering equipment folders
inside a selected commissioning system.
"""

from pathlib import Path
from datetime import datetime
import time
from utils.logger import logger
from core.extractor import extract_document_ids


def discover_equipment(system_folder: Path) -> list[Path]:
    """
    Discover all equipment folders inside the selected system.
    """

    logger.info("Scanning system: %s", system_folder)

    if not system_folder.exists():
        logger.error("System folder does not exist.")
        raise FileNotFoundError(system_folder)

    equipment =  [

        folder
        for folder in system_folder.iterdir()
        if folder.is_dir()
        ]

    # logger.info("Found %d equipment folders.", len(equipment))

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

    # logger.info(
    #     "Found %d levels for %s",
    #     len(levels),
    #     equipment_folder.name,
    # )

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

    # logger.info(
    #     "Found %d document folders in %s",
    #     len(document_folders),
    #     level_folder.name,
    # )

    return document_folders

def scan_system(system_folder: Path) -> list[dict]:
    """
    Scan the selected system folder and build an inventory.
    """
    start_time = time.perf_counter()
    building = system_folder.parent.parent.name
    discipline = system_folder.parent.name
    system = system_folder.name
    discipline = discipline.split(". ",1)[1]
    system = system.split(". ",1)[1]

    equipment_folders = discover_equipment(system_folder)

    system_inventory = []

    for equipment in equipment_folders:

        level_inventory = {}

        levels = discover_levels(equipment)

        for level in levels:

            document_inventory = {}

            document_folders = discover_document_folders(level)

            for folder in document_folders:

                document_inventory[folder.name] = {

                    "folder": folder,
                    "documents": extract_document_ids(folder),
                                                    }
                

            level_inventory[level.name] = document_inventory

        equipment_data= {
            
                "reference": equipment.name,
                "path": equipment,
                "levels": level_inventory,
            }
        system_inventory.append(
    equipment_data
)
        
    scan_time = round(
        time.perf_counter() - start_time,
        2,
                    )
    logger.info(
        "System scan completed. %d equipment discovered.",
        len(system_inventory),
    )

    return {

    "metadata": {

        "building": building,

        "discipline": discipline,

        "system": system,

        "generated_at": datetime.now(),

        "scan_time": scan_time,

        "equipment_count": len(system_inventory),

        "root_folder": str(system_folder),

    },

    "inventory": system_inventory,

}