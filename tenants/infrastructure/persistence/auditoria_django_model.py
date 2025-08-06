import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantAuditoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='auditorias', on_delete=models.CASCADE)
    usuario_id = models.UUIDField()
    accion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_evento = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.accion} - {self.fecha_evento}"
