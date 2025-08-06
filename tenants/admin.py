from django.contrib import admin
from .models import (
    Tenant,
    TenantContacto,
    TenantConfiguracion,
    TenantPlan,
    TenantLicencia,
    TenantModulo,
    TenantLogo,
    TenantAlmacenamiento,
    TenantAuditoria,
)

admin.site.register(Tenant)
admin.site.register(TenantContacto)
admin.site.register(TenantConfiguracion)
admin.site.register(TenantPlan)
admin.site.register(TenantLicencia)
admin.site.register(TenantModulo)
admin.site.register(TenantLogo)
admin.site.register(TenantAlmacenamiento)
admin.site.register(TenantAuditoria)
