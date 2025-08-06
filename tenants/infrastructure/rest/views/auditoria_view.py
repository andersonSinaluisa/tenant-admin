from rest_framework import viewsets, status
from rest_framework.response import Response

from tenants.application.services.auditoria_service import AuditoriaService
from tenants.infrastructure.repositories.auditoria_repository_impl import DjangoAuditoriaRepository
from tenants.infrastructure.rest.serializers.auditoria_serializer import AuditoriaSerializer


class AuditoriaViewSet(viewsets.ViewSet):
    service = AuditoriaService(DjangoAuditoriaRepository())

    def list(self, request, tenant_id=None):
        eventos = self.service.list(tenant_id)
        serializer = AuditoriaSerializer(eventos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, tenant_id=None, pk=None):
        evento = self.service.retrieve(tenant_id, pk)
        serializer = AuditoriaSerializer(evento)
        return Response(serializer.data)

    def destroy(self, request, tenant_id=None, pk=None):
        self.service.delete(tenant_id, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
