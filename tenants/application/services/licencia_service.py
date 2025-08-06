from tenants.domain.repositories.licencia_repository import LicenciaRepository


class LicenciaService:
    def __init__(self, repository: LicenciaRepository):
        self.repository = repository

    def list(self, tenant_id):
        return self.repository.list(tenant_id)

    def create(self, tenant_id, data):
        return self.repository.create(tenant_id, **data)

    def retrieve(self, tenant_id, licencia_id):
        return self.repository.retrieve(tenant_id, licencia_id)

    def update(self, tenant_id, licencia_id, data):
        lic = self.repository.retrieve(tenant_id, licencia_id)
        return self.repository.update(lic, **data)

    def delete(self, tenant_id, licencia_id):
        lic = self.repository.retrieve(tenant_id, licencia_id)
        self.repository.delete(lic)

    def renew(self, tenant_id, licencia_id, data):
        lic = self.repository.retrieve(tenant_id, licencia_id)
        return self.repository.renew(lic, **data)
