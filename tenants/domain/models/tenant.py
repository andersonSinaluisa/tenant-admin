from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Tenant:
    id: UUID
    nombre: str
    dominio: str
    schema_name: str
    estado: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
