from django.db import migrations, models
import uuid
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('dominio', models.CharField(max_length=255)),
                ('schema_name', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=20, choices=[('activo', 'Activo'), ('suspendido', 'Suspendido'), ('eliminado', 'Eliminado')], default='activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenantPlan',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio_mensual', models.DecimalField(max_digits=10, decimal_places=2)),
                ('precio_anual', models.DecimalField(max_digits=10, decimal_places=2)),
                ('limite_usuarios', models.IntegerField()),
                ('limite_almacenamiento', models.BigIntegerField()),
                ('estado', models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenantAlmacenamiento',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('uso_actual_bytes', models.BigIntegerField()),
                ('limite_bytes', models.BigIntegerField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='almacenamiento', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantAuditoria',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('usuario_id', models.UUIDField()),
                ('accion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_evento', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditorias', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantConfiguracion',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('clave', models.CharField(max_length=255)),
                ('valor', models.TextField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configuraciones', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantContacto',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=100)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantLicencia',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(max_length=20, choices=[('activa', 'Activa'), ('expirada', 'Expirada'), ('pendiente', 'Pendiente')], default='pendiente')),
                ('renovacion_automatica', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licencias', to='tenants.tenantplan')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licencias', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantLogo',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('logo_url', models.TextField(blank=True)),
                ('color_primario', models.CharField(max_length=50, blank=True)),
                ('color_secundario', models.CharField(max_length=50, blank=True)),
                ('favicon_url', models.TextField(blank=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logos', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantModulo',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('nombre_modulo', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField(default=True)),
                ('fecha_activacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_desactivacion', models.DateTimeField(blank=True, null=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='tenants.tenant')),
            ],
        ),
    ]
