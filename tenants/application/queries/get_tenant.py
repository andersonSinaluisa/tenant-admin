from dataclasses import dataclass


@dataclass
class GetTenantQuery:
    tenant_id: str
