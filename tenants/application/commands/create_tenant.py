from dataclasses import dataclass


@dataclass
class CreateTenantCommand:
    nombre: str
    dominio: str
    schema_name: str
