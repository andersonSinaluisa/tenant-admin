import uuid
from django.db import models
from .tenant_django_model import Tenant
from .plan_django_model import TenantPlan


class TenantLicencia(models.Model):
    class Estado(models.TextChoices):
        ACTIVA = 'activa', 'Activa'
        EXPIRADA = 'expirada', 'Expirada'
        PENDIENTE = 'pendiente', 'Pendiente'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='licencias', on_delete=models.CASCADE)
    plan = models.ForeignKey(TenantPlan, related_name='licencias', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    renovacion_automatica = models.BooleanField(default=False)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return f"{self.tenant.nombre} - {self.plan.nombre}"
