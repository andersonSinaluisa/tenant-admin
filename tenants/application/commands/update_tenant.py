from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateTenantCommand:
    nombre: Optional[str] = None
    dominio: Optional[str] = None
    schema_name: Optional[str] = None
    estado: Optional[str] = None
