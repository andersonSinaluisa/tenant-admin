from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tenants.application.services.modulo_service import ModuloService
from tenants.infrastructure.repositories.modulo_repository_impl import DjangoModuloRepository
from tenants.infrastructure.rest.serializers.modulo_serializer import ModuloSerializer


class ModuloViewSet(viewsets.ViewSet):
    service = ModuloService(DjangoModuloRepository())

    def list(self, request, tenant_id=None):
        modulos = self.service.list(tenant_id)
        serializer = ModuloSerializer(modulos, many=True)
        return Response(serializer.data)

    def create(self, request, tenant_id=None):
        modulo = self.service.create(tenant_id, request.data)
        serializer = ModuloSerializer(modulo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, tenant_id=None, pk=None):
        modulo = self.service.retrieve(tenant_id, pk)
        serializer = ModuloSerializer(modulo)
        return Response(serializer.data)

    def update(self, request, tenant_id=None, pk=None):
        modulo = self.service.update(tenant_id, pk, request.data)
        serializer = ModuloSerializer(modulo)
        return Response(serializer.data)

    def destroy(self, request, tenant_id=None, pk=None):
        self.service.delete(tenant_id, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def enable(self, request, tenant_id=None, pk=None):
        modulo = self.service.enable(tenant_id, pk)
        serializer = ModuloSerializer(modulo)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def disable(self, request, tenant_id=None, pk=None):
        modulo = self.service.disable(tenant_id, pk)
        serializer = ModuloSerializer(modulo)
        return Response(serializer.data)
