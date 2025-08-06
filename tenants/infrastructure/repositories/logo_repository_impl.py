from tenants.domain.repositories.logo_repository import LogoRepository
from tenants.infrastructure.persistence.logo_django_model import TenantLogo


class DjangoLogoRepository(LogoRepository):
    def get(self, tenant_id):
        return TenantLogo.objects.filter(tenant_id=tenant_id).first()

    def save(self, tenant_id, **data):
        logo = self.get(tenant_id)
        if logo:
            for key, value in data.items():
                setattr(logo, key, value)
        else:
            logo = TenantLogo(tenant_id=tenant_id, **data)
        logo.save()
        return logo

    def delete(self, tenant_id):
        logo = self.get(tenant_id)
        if logo:
            logo.delete()
