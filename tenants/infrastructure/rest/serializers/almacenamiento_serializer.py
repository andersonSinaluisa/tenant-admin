from rest_framework import serializers
from tenants.infrastructure.persistence.almacenamiento_django_model import TenantAlmacenamiento


class AlmacenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantAlmacenamiento
        fields = '__all__'
