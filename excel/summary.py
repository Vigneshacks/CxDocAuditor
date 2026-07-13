"""
summary.py

Build summary statistics from the scanned inventory.
"""


def build_summary(inventory: list[dict]) -> dict:
    """
    Build summary statistics from inventory. 

    Parameters
    ----------
    inventory : list[dict]

    Returns
    -------
    dict
    """

    summary = {
        "equipment_count": len(inventory),
        "levels": {}
    }

    for equipment in inventory:

        for level_name, document_types in equipment["levels"].items():

            if level_name not in summary["levels"]:

                summary["levels"][level_name] = {
                    "FAT": 0,
                    "MIR": 0,
                    "WIR": 0,
                    "Missing FAT": 0,
                    "Missing MIR": 0,
                    "Missing WIR": 0,
                }

            for doc_type in ["FAT", "MIR", "WIR"]:

                info = document_types.get(doc_type)

                if info is None:

                    summary["levels"][level_name][
                        f"Missing {doc_type}"
                    ] += 1

                    continue

                if info["documents"]:

                    summary["levels"][level_name][doc_type] += 1

                else:

                    summary["levels"][level_name][
                        f"Missing {doc_type}"
                    ] += 1

    return summary