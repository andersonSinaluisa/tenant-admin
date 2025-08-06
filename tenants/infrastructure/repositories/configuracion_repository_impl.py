from tenants.domain.repositories.configuracion_repository import ConfiguracionRepository
from tenants.infrastructure.persistence.configuracion_django_model import TenantConfiguracion


class DjangoConfiguracionRepository(ConfiguracionRepository):
    def list(self, tenant_id):
        return TenantConfiguracion.objects.filter(tenant_id=tenant_id)

    def create(self, tenant_id, **data):
        return TenantConfiguracion.objects.create(tenant_id=tenant_id, **data)

    def retrieve(self, tenant_id, config_id):
        return TenantConfiguracion.objects.get(tenant_id=tenant_id, id=config_id)

    def update(self, configuracion, **data):
        for key, value in data.items():
            setattr(configuracion, key, value)
        configuracion.save()
        return configuracion

    def delete(self, configuracion):
        configuracion.delete()

    def bulk_update(self, tenant_id, configs):
        for conf in configs:
            TenantConfiguracion.objects.update_or_create(
                tenant_id=tenant_id,
                clave=conf.get("clave"),
                defaults={"valor": conf.get("valor")},
            )
        return TenantConfiguracion.objects.filter(tenant_id=tenant_id)
