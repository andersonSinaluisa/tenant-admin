import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantContacto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='contactos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.nombre} ({self.tenant.nombre})"
