import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantModulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='modulos', on_delete=models.CASCADE)
    nombre_modulo = models.CharField(max_length=255)
    habilitado = models.BooleanField(default=True)
    fecha_activacion = models.DateTimeField(null=True, blank=True)
    fecha_desactivacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.nombre_modulo} ({'on' if self.habilitado else 'off'})"
