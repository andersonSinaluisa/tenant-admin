from rest_framework import serializers
from tenants.infrastructure.persistence.configuracion_django_model import TenantConfiguracion


class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantConfiguracion
        fields = '__all__'
