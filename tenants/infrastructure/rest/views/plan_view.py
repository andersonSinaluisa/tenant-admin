from rest_framework import viewsets
from tenants.infrastructure.repositories.plan_repository_impl import DjangoPlanRepository
from tenants.infrastructure.rest.serializers.plan_serializer import PlanSerializer


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlanSerializer
    queryset = DjangoPlanRepository().list()
