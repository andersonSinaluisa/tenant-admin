from rest_framework import viewsets, status
from rest_framework.response import Response

from tenants.application.services.logo_service import LogoService
from tenants.infrastructure.repositories.logo_repository_impl import DjangoLogoRepository
from tenants.infrastructure.rest.serializers.logo_serializer import LogoSerializer


class LogoViewSet(viewsets.ViewSet):
    service = LogoService(DjangoLogoRepository())

    def list(self, request, tenant_id=None):
        logo = self.service.get(tenant_id)
        if not logo:
            return Response({})
        serializer = LogoSerializer(logo)
        return Response(serializer.data)

    def create(self, request, tenant_id=None):
        logo = self.service.save(tenant_id, request.data)
        serializer = LogoSerializer(logo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, tenant_id=None):
        self.service.delete(tenant_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
