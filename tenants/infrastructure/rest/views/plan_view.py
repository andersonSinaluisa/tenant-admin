from rest_framework import viewsets
from rest_framework.response import Response

from tenants.application.services.plan_service import PlanService
from tenants.infrastructure.repositories.plan_repository_impl import DjangoPlanRepository
from tenants.infrastructure.rest.serializers.plan_serializer import PlanSerializer


class PlanViewSet(viewsets.ViewSet):
    service = PlanService(DjangoPlanRepository())

    def list(self, request):
        planes = self.service.list()
        serializer = PlanSerializer(planes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        plan = self.service.retrieve(pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)
