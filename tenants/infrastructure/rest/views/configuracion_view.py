from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tenants.application.services.configuracion_service import ConfiguracionService
from tenants.infrastructure.repositories.configuracion_repository_impl import DjangoConfiguracionRepository
from tenants.infrastructure.rest.serializers.configuracion_serializer import ConfiguracionSerializer


class ConfiguracionViewSet(viewsets.ViewSet):
    service = ConfiguracionService(DjangoConfiguracionRepository())

    def list(self, request, tenant_id=None):
        configs = self.service.list(tenant_id)
        serializer = ConfiguracionSerializer(configs, many=True)
        return Response(serializer.data)

    def create(self, request, tenant_id=None):
        config = self.service.create(tenant_id, request.data)
        serializer = ConfiguracionSerializer(config)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, tenant_id=None, pk=None):
        config = self.service.retrieve(tenant_id, pk)
        serializer = ConfiguracionSerializer(config)
        return Response(serializer.data)

    def update(self, request, tenant_id=None, pk=None):
        config = self.service.update(tenant_id, pk, request.data)
        serializer = ConfiguracionSerializer(config)
        return Response(serializer.data)

    def destroy(self, request, tenant_id=None, pk=None):
        self.service.delete(tenant_id, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], url_path="bulk-update")
    def bulk_update(self, request, tenant_id=None):
        configs = self.service.bulk_update(tenant_id, request.data)
        serializer = ConfiguracionSerializer(configs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
