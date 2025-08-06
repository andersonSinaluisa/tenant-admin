from tenants.domain.repositories.contact_repository import ContactRepository


class ContactService:
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def list(self, tenant_id):
        return self.repository.list(tenant_id)

    def create(self, tenant_id, data):
        return self.repository.create(tenant_id, **data)

    def retrieve(self, tenant_id, contact_id):
        return self.repository.retrieve(tenant_id, contact_id)

    def update(self, tenant_id, contact_id, data):
        contact = self.repository.retrieve(tenant_id, contact_id)
        return self.repository.update(contact, **data)

    def delete(self, tenant_id, contact_id):
        contact = self.repository.retrieve(tenant_id, contact_id)
        self.repository.delete(contact)
