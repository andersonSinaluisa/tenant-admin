from tenants.domain.repositories.modulo_repository import ModuloRepository
from tenants.infrastructure.persistence.modulo_django_model import TenantModulo


class DjangoModuloRepository(ModuloRepository):
    def list(self, tenant_id):
        return TenantModulo.objects.filter(tenant_id=tenant_id)

    def create(self, tenant_id, **data):
        return TenantModulo.objects.create(tenant_id=tenant_id, **data)

    def retrieve(self, tenant_id, modulo_id):
        return TenantModulo.objects.get(tenant_id=tenant_id, id=modulo_id)

    def update(self, modulo, **data):
        for key, value in data.items():
            setattr(modulo, key, value)
        modulo.save()
        return modulo

    def delete(self, modulo):
        modulo.delete()

    def enable(self, modulo):
        modulo.habilitado = True
        modulo.save()
        return modulo

    def disable(self, modulo):
        modulo.habilitado = False
        modulo.save()
        return modulo
