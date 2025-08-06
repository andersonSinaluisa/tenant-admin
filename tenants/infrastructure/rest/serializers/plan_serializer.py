from rest_framework import serializers
from tenants.infrastructure.persistence.plan_django_model import TenantPlan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantPlan
        fields = '__all__'
