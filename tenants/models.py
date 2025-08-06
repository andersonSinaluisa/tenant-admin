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

    def __str__(self):
        return self.nombre


class TenantContacto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='contactos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.tenant.nombre})"


class TenantConfiguracion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='configuraciones', on_delete=models.CASCADE)
    clave = models.CharField(max_length=255)
    valor = models.TextField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tenant.nombre} - {self.clave}"


class TenantPlan(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    precio_anual = models.DecimalField(max_digits=10, decimal_places=2)
    limite_usuarios = models.IntegerField()
    limite_almacenamiento = models.BigIntegerField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ACTIVO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


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

    def __str__(self):
        return f"Licencia {self.tenant.nombre} - {self.plan.nombre}"


class TenantModulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='modulos', on_delete=models.CASCADE)
    nombre_modulo = models.CharField(max_length=255)
    habilitado = models.BooleanField(default=True)
    fecha_activacion = models.DateTimeField(null=True, blank=True)
    fecha_desactivacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_modulo} ({self.tenant.nombre})"


class TenantLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='logos', on_delete=models.CASCADE)
    logo_url = models.TextField(blank=True)
    color_primario = models.CharField(max_length=50, blank=True)
    color_secundario = models.CharField(max_length=50, blank=True)
    favicon_url = models.TextField(blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Logo de {self.tenant.nombre}"


class TenantAlmacenamiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='almacenamiento', on_delete=models.CASCADE)
    uso_actual_bytes = models.BigIntegerField()
    limite_bytes = models.BigIntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Almacenamiento de {self.tenant.nombre}"


class TenantAuditoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name='auditorias', on_delete=models.CASCADE)
    usuario_id = models.UUIDField()
    accion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_evento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.accion} - {self.tenant.nombre}"
