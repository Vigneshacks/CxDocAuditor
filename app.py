from pathlib import Path

from core.scanner import discover_equipment


SYSTEM_FOLDER = Path(
    r"Z:\Shared\Datacenters Solutions Projects\Stargate Campus Phase 1.1\25-TESTING AND COMMISSIONING\29. Cx Alloy inputs\SG1-B\09. Special Systems\7. Aspiration Detection System"
)

equipment = discover_equipment(SYSTEM_FOLDER)

print()

for eq in equipment:

    print(eq.name)