from rest_framework import serializers
from tenants.infrastructure.persistence.licencia_django_model import TenantLicencia


class LicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantLicencia
        fields = '__all__'
