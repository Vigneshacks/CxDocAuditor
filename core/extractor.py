"""
extractor.py

Extracts and normalizes document IDs from PDF filenames.
"""

from pathlib import Path

from utils.logger import logger

# Suffixes that should not be part of the document ID.
IGNORED_SUFFIXES = [
    "-MIR",
    "-WIR",
    "-FAT",
]

def normalize_document_name(filename: str) -> str:
    """
    Convert a PDF filename into its base document ID.

    Examples
    --------
    SG1-SIB-MI-FA-38-0007.pdf
        -> SG1-SIB-MI-FA-38-0007

    SG1-SIB-MI-FA-38-0007-MIR.pdf
        -> SG1-SIB-MI-FA-38-0007

    SG1-SIB-MI-FA-38-0007_00 Comments.pdf
        -> SG1-SIB-MI-FA-38-0007
    """

    name = filename

    # Remove anything after "_"
    if "_" in name:
        name = name.split("_")[0]

    # Remove known suffixes
    for suffix in IGNORED_SUFFIXES:

        if name.endswith(suffix):
            name = name.removesuffix(suffix)

    return name

def extract_document_ids(document_folder: Path) -> list[str]:
    """
    Extract all unique document IDs from a document folder.
    """

    document_ids = set()

    if not document_folder.exists():

        logger.warning(
            "Folder does not exist: %s",
            document_folder,
        )

        return []

    pdf_files = document_folder.glob("*.pdf")

    for pdf in pdf_files:

        document_id = normalize_document_name(pdf.stem)

        document_ids.add(document_id)

    # logger.info(
    #     "Extracted %d document IDs from %s",
    #     len(document_ids),
    #     document_folder.name,
    # )

    return sorted(document_ids)