from tenants.domain.repositories.logo_repository import LogoRepository


class LogoService:
    def __init__(self, repository: LogoRepository):
        self.repository = repository

    def get(self, tenant_id):
        return self.repository.get(tenant_id)

    def save(self, tenant_id, data):
        return self.repository.save(tenant_id, **data)

    def delete(self, tenant_id):
        self.repository.delete(tenant_id)
