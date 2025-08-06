from tenants.domain.repositories.tenant_repository import TenantRepository
from tenants.infrastructure.persistence.tenant_django_model import Tenant


class DjangoTenantRepository(TenantRepository):
    def list(self):
        return Tenant.objects.all()

    def retrieve(self, tenant_id):
        return Tenant.objects.get(id=tenant_id)

    def create(self, **kwargs):
        return Tenant.objects.create(**kwargs)

    def update(self, tenant, **kwargs):
        for attr, value in kwargs.items():
            setattr(tenant, attr, value)
        tenant.save()
        return tenant

    def delete(self, tenant):
        tenant.delete()
