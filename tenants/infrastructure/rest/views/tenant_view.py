from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tenants.application.commands.create_tenant import CreateTenantCommand
from tenants.application.commands.update_tenant import UpdateTenantCommand
from tenants.application.commands.suspend_tenant import SuspendTenantCommand
from tenants.application.services.tenant_service import TenantService
from tenants.infrastructure.repositories.tenant_repository_impl import DjangoTenantRepository
from tenants.infrastructure.rest.serializers.tenant_serializer import TenantSerializer


class TenantViewSet(viewsets.ViewSet):
    service = TenantService(DjangoTenantRepository())

    def list(self, request):
        tenants = self.service.list_tenants()
        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)

    def create(self, request):
        command = CreateTenantCommand(**request.data)
        tenant = self.service.create_tenant(command)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        tenant = self.service.get_tenant(pk)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    def update(self, request, pk=None):
        command = UpdateTenantCommand(**request.data)
        tenant = self.service.update_tenant(pk, command)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        self.service.delete_tenant(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def suspend(self, request, pk=None):
        command = SuspendTenantCommand(**request.data)
        self.service.suspend_tenant(pk, command)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        self.service.activate_tenant(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
