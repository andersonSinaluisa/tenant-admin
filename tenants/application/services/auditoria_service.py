from tenants.domain.repositories.auditoria_repository import AuditoriaRepository


class AuditoriaService:
    def __init__(self, repository: AuditoriaRepository):
        self.repository = repository

    def list(self, tenant_id):
        return self.repository.list(tenant_id)

    def retrieve(self, tenant_id, auditoria_id):
        return self.repository.retrieve(tenant_id, auditoria_id)

    def delete(self, tenant_id, auditoria_id):
        auditoria = self.repository.retrieve(tenant_id, auditoria_id)
        self.repository.delete(auditoria)
