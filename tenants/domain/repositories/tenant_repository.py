from abc import ABC, abstractmethod


class TenantRepository(ABC):
    @abstractmethod
    def list(self):
        """Return iterable of tenants"""

    @abstractmethod
    def retrieve(self, tenant_id):
        """Return a single tenant"""

    @abstractmethod
    def create(self, **kwargs):
        """Create a tenant"""

    @abstractmethod
    def update(self, tenant, **kwargs):
        """Update a tenant"""

    @abstractmethod
    def delete(self, tenant):
        """Delete a tenant"""
