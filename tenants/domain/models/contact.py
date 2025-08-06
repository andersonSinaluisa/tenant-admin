from dataclasses import dataclass
from uuid import UUID


@dataclass
class Contact:
    id: UUID
    tenant_id: UUID
    nombre: str
    email: str
    telefono: str
    rol: str
