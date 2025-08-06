from tenants.domain.repositories.contact_repository import ContactRepository
from tenants.infrastructure.persistence.contact_django_model import TenantContacto


class DjangoContactRepository(ContactRepository):
    def list(self, tenant_id):
        return TenantContacto.objects.filter(tenant_id=tenant_id)

    def create(self, tenant_id, **data):
        return TenantContacto.objects.create(tenant_id=tenant_id, **data)

    def retrieve(self, tenant_id, contact_id):
        return TenantContacto.objects.get(tenant_id=tenant_id, id=contact_id)

    def update(self, contact, **data):
        for key, value in data.items():
            setattr(contact, key, value)
        contact.save()
        return contact

    def delete(self, contact):
        contact.delete()
