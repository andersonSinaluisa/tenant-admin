from rest_framework import serializers
from tenants.infrastructure.persistence.modulo_django_model import TenantModulo


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantModulo
        fields = '__all__'
