from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tenants.application.services.licencia_service import LicenciaService
from tenants.infrastructure.repositories.licencia_repository_impl import DjangoLicenciaRepository
from tenants.infrastructure.rest.serializers.licencia_serializer import LicenciaSerializer


class LicenciaViewSet(viewsets.ViewSet):
    service = LicenciaService(DjangoLicenciaRepository())

    def list(self, request, tenant_id=None):
        licencias = self.service.list(tenant_id)
        serializer = LicenciaSerializer(licencias, many=True)
        return Response(serializer.data)

    def create(self, request, tenant_id=None):
        licencia = self.service.create(tenant_id, request.data)
        serializer = LicenciaSerializer(licencia)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, tenant_id=None, pk=None):
        licencia = self.service.retrieve(tenant_id, pk)
        serializer = LicenciaSerializer(licencia)
        return Response(serializer.data)

    def update(self, request, tenant_id=None, pk=None):
        licencia = self.service.update(tenant_id, pk, request.data)
        serializer = LicenciaSerializer(licencia)
        return Response(serializer.data)

    def destroy(self, request, tenant_id=None, pk=None):
        self.service.delete(tenant_id, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def renew(self, request, tenant_id=None, pk=None):
        licencia = self.service.renew(tenant_id, pk, request.data)
        serializer = LicenciaSerializer(licencia)
        return Response(serializer.data)
