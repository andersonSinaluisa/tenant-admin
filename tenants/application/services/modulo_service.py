from tenants.domain.repositories.modulo_repository import ModuloRepository


class ModuloService:
    def __init__(self, repository: ModuloRepository):
        self.repository = repository

    def list(self, tenant_id):
        return self.repository.list(tenant_id)

    def create(self, tenant_id, data):
        return self.repository.create(tenant_id, **data)

    def retrieve(self, tenant_id, modulo_id):
        return self.repository.retrieve(tenant_id, modulo_id)

    def update(self, tenant_id, modulo_id, data):
        modulo = self.repository.retrieve(tenant_id, modulo_id)
        return self.repository.update(modulo, **data)

    def delete(self, tenant_id, modulo_id):
        modulo = self.repository.retrieve(tenant_id, modulo_id)
        self.repository.delete(modulo)

    def enable(self, tenant_id, modulo_id):
        modulo = self.repository.retrieve(tenant_id, modulo_id)
        return self.repository.enable(modulo)

    def disable(self, tenant_id, modulo_id):
        modulo = self.repository.retrieve(tenant_id, modulo_id)
        return self.repository.disable(modulo)
