from tenants.domain.repositories.configuracion_repository import ConfiguracionRepository


class ConfiguracionService:
    def __init__(self, repository: ConfiguracionRepository):
        self.repository = repository

    def list(self, tenant_id):
        return self.repository.list(tenant_id)

    def create(self, tenant_id, data):
        return self.repository.create(tenant_id, **data)

    def retrieve(self, tenant_id, config_id):
        return self.repository.retrieve(tenant_id, config_id)

    def update(self, tenant_id, config_id, data):
        config = self.repository.retrieve(tenant_id, config_id)
        return self.repository.update(config, **data)

    def delete(self, tenant_id, config_id):
        config = self.repository.retrieve(tenant_id, config_id)
        self.repository.delete(config)

    def bulk_update(self, tenant_id, configs):
        return self.repository.bulk_update(tenant_id, configs)
