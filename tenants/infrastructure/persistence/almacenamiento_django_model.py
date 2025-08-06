import uuid
from django.db import models
from .tenant_django_model import Tenant


class TenantAlmacenamiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='almacenamiento', on_delete=models.CASCADE)
    uso_actual_bytes = models.BigIntegerField()
    limite_bytes = models.BigIntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.uso_actual_bytes}/{self.limite_bytes}"
