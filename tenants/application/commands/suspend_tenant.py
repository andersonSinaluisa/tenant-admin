from dataclasses import dataclass


@dataclass
class SuspendTenantCommand:
    reason: str = ""
