from tenants.domain.repositories.almacenamiento_repository import AlmacenamientoRepository


class AlmacenamientoService:
    def __init__(self, repository: AlmacenamientoRepository):
        self.repository = repository

    def get(self, tenant_id):
        return self.repository.get_or_create(tenant_id)

    def update(self, tenant_id, data):
        obj = self.repository.get_or_create(tenant_id)
        return self.repository.update(obj, **data)
