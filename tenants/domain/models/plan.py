from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class Plan:
    id: UUID
    nombre: str
    descripcion: str
    precio_mensual: float
    precio_anual: float
    limite_usuarios: int
    limite_almacenamiento: int
    estado: str
    fecha_creacion: datetime
