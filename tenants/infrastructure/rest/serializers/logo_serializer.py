from rest_framework import serializers
from tenants.infrastructure.persistence.logo_django_model import TenantLogo


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantLogo
        fields = '__all__'
