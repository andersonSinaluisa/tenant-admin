from rest_framework import serializers
from tenants.infrastructure.persistence.contact_django_model import TenantContacto


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantContacto
        fields = '__all__'
