from tenants.domain.repositories.almacenamiento_repository import AlmacenamientoRepository
from tenants.infrastructure.persistence.almacenamiento_django_model import TenantAlmacenamiento


class DjangoAlmacenamientoRepository(AlmacenamientoRepository):
    def get_or_create(self, tenant_id):
        obj, _ = TenantAlmacenamiento.objects.get_or_create(
            tenant_id=tenant_id, defaults={'uso_actual_bytes': 0, 'limite_bytes': 0}
        )
        return obj

    def update(self, obj, **data):
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj
