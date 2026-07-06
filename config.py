"""
CxDoc Auditor Configuration
"""

# -----------------------------
# Application Information
# -----------------------------

APP_NAME = "CxDoc Auditor"
VERSION = "0.1.0"

# -----------------------------
# Output
# -----------------------------

OUTPUT_FOLDER = "output"
OUTPUT_FILENAME = "CxDoc_Report.xlsx"

# -----------------------------
# Supported Levels
# -----------------------------

DEFAULT_LEVELS = [
    "L2-A",
    "L2-B",
]

# -----------------------------
# Supported Document Types
# -----------------------------

DOCUMENT_TYPES = [
    "FAT",
    "MIR",
    "WIR",
]

# -----------------------------
# Excel
# -----------------------------

SUMMARY_SHEET_NAME = "Summary"
REPORT_SHEET_NAME = "Documents"