from rest_framework import serializers
from tenants.infrastructure.persistence.auditoria_django_model import TenantAuditoria


class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantAuditoria
        fields = '__all__'
