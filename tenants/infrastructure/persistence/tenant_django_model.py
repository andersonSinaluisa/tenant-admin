import uuid
from django.db import models


class Tenant(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        SUSPENDIDO = 'suspendido', 'Suspendido'
        ELIMINADO = 'eliminado', 'Eliminado'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    dominio = models.CharField(max_length=255)
    schema_name = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ACTIVO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'tenants'

    def __str__(self):
        return self.nombre
