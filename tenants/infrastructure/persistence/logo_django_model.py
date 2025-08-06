import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='logos', on_delete=models.CASCADE)
    logo_url = models.TextField(blank=True)
    color_primario = models.CharField(max_length=50, blank=True)
    color_secundario = models.CharField(max_length=50, blank=True)
    favicon_url = models.TextField(blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"Branding for {self.tenant.nombre}"
