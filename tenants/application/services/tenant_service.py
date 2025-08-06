from tenants.domain.repositories.tenant_repository import TenantRepository
from tenants.application.commands.create_tenant import CreateTenantCommand
from tenants.application.commands.update_tenant import UpdateTenantCommand
from tenants.application.commands.suspend_tenant import SuspendTenantCommand


class TenantService:
    def __init__(self, repository: TenantRepository):
        self.repository = repository

    def list_tenants(self, query=None):
        return self.repository.list()

    def get_tenant(self, tenant_id):
        return self.repository.retrieve(tenant_id)

    def create_tenant(self, command: CreateTenantCommand):
        return self.repository.create(**command.__dict__)

    def update_tenant(self, tenant_id, command: UpdateTenantCommand):
        tenant = self.repository.retrieve(tenant_id)
        data = {k: v for k, v in command.__dict__.items() if v is not None}
        return self.repository.update(tenant, **data)

    def delete_tenant(self, tenant_id):
        tenant = self.repository.retrieve(tenant_id)
        self.repository.delete(tenant)

    def suspend_tenant(self, tenant_id, command: SuspendTenantCommand | None = None):
        tenant = self.repository.retrieve(tenant_id)
        return self.repository.update(tenant, estado='suspendido')

    def activate_tenant(self, tenant_id):
        tenant = self.repository.retrieve(tenant_id)
        return self.repository.update(tenant, estado='activo')
