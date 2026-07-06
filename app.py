from pathlib import Path


from core.scanner import scan_system


SYSTEM_FOLDER = Path(
    r"Z:\Shared\Datacenters Solutions Projects\Stargate Campus Phase 1.1\25-TESTING AND COMMISSIONING\29. Cx Alloy inputs\SG1-B\09. Special Systems\7. Aspiration Detection System"
)

inventory = scan_system(SYSTEM_FOLDER)

print()


# for equipment in inventory:

#     print("=" * 60)

#     print(equipment["reference"])

#     print("-" * 60)

#     for level_name, document_folders in equipment["levels"].items():

#         print(level_name)

#         for folder in document_folders:

#             print(f"    {folder.name}")

#     print()
    


from core.extractor import extract_document_ids

folder = Path(
    r"Z:\Shared\Datacenters Solutions Projects\Stargate Campus Phase 1.1\25-TESTING AND COMMISSIONING\29. Cx Alloy inputs\SG1-B\09. Special Systems\7. Aspiration Detection System\SG1B-P01-G-04- NW1-ASDP-28\L2-A\MIR"
)

ids = extract_document_ids(folder)

print(ids)