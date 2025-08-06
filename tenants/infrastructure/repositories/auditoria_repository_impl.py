from tenants.domain.repositories.auditoria_repository import AuditoriaRepository
from tenants.infrastructure.persistence.auditoria_django_model import TenantAuditoria


class DjangoAuditoriaRepository(AuditoriaRepository):
    def list(self, tenant_id):
        return TenantAuditoria.objects.filter(tenant_id=tenant_id)

    def retrieve(self, tenant_id, auditoria_id):
        return TenantAuditoria.objects.get(tenant_id=tenant_id, id=auditoria_id)

    def delete(self, auditoria):
        auditoria.delete()
