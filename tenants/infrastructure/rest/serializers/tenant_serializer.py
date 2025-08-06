from rest_framework import serializers
from tenants.infrastructure.persistence.tenant_django_model import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'
