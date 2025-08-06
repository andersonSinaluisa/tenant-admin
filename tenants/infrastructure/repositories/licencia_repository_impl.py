from tenants.domain.repositories.licencia_repository import LicenciaRepository
from tenants.infrastructure.persistence.licencia_django_model import TenantLicencia


class DjangoLicenciaRepository(LicenciaRepository):
    def list(self, tenant_id):
        return TenantLicencia.objects.filter(tenant_id=tenant_id)

    def create(self, tenant_id, **data):
        return TenantLicencia.objects.create(tenant_id=tenant_id, **data)

    def retrieve(self, tenant_id, licencia_id):
        return TenantLicencia.objects.get(tenant_id=tenant_id, id=licencia_id)

    def update(self, licencia, **data):
        for key, value in data.items():
            setattr(licencia, key, value)
        licencia.save()
        return licencia

    def delete(self, licencia):
        licencia.delete()

    def renew(self, licencia, **data):
        for key, value in data.items():
            setattr(licencia, key, value)
        licencia.estado = TenantLicencia.Estado.ACTIVA
        licencia.save()
        return licencia
