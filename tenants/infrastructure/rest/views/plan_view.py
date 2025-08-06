from rest_framework import viewsets
from rest_framework.response import Response

from tenants.application.services.plan_service import PlanService



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
