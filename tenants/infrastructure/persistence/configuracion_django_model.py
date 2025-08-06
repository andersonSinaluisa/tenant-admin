import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantConfiguracion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='configuraciones', on_delete=models.CASCADE)
    clave = models.CharField(max_length=255)
    valor = models.TextField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.clave}={self.valor}"
