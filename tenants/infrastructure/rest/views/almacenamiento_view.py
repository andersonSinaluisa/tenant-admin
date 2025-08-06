from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tenants.application.services.almacenamiento_service import AlmacenamientoService
from tenants.infrastructure.repositories.almacenamiento_repository_impl import DjangoAlmacenamientoRepository
from tenants.infrastructure.rest.serializers.almacenamiento_serializer import AlmacenamientoSerializer


class AlmacenamientoViewSet(viewsets.ViewSet):
    service = AlmacenamientoService(DjangoAlmacenamientoRepository())

    def list(self, request, tenant_id=None):
        obj = self.service.get(tenant_id)
        serializer = AlmacenamientoSerializer(obj)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='actualizar')
    def actualizar(self, request, tenant_id=None):
        obj = self.service.update(tenant_id, request.data)
        serializer = AlmacenamientoSerializer(obj)
        return Response(serializer.data)
