from rest_framework import viewsets, status
from rest_framework.response import Response

from tenants.application.services.contact_service import ContactService
from tenants.infrastructure.repositories.contact_repository_impl import DjangoContactRepository
from tenants.infrastructure.rest.serializers.contact_serializer import ContactoSerializer


class ContactoViewSet(viewsets.ViewSet):
    service = ContactService(DjangoContactRepository())

    def list(self, request, tenant_id=None):
        contactos = self.service.list(tenant_id)
        serializer = ContactoSerializer(contactos, many=True)
        return Response(serializer.data)

    def create(self, request, tenant_id=None):
        contacto = self.service.create(tenant_id, request.data)
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, tenant_id=None, pk=None):
        contacto = self.service.retrieve(tenant_id, pk)
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)

    def update(self, request, tenant_id=None, pk=None):
        contacto = self.service.update(tenant_id, pk, request.data)
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)

    def destroy(self, request, tenant_id=None, pk=None):
        self.service.delete(tenant_id, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
