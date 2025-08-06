from abc import ABC, abstractmethod


class ConfiguracionRepository(ABC):
    @abstractmethod
    def list(self, tenant_id):
        ...

    @abstractmethod
    def create(self, tenant_id, **data):
        ...

    @abstractmethod
    def retrieve(self, tenant_id, config_id):
        ...

    @abstractmethod
    def update(self, configuracion, **data):
        ...

    @abstractmethod
    def delete(self, configuracion):
        ...

    @abstractmethod
    def bulk_update(self, tenant_id, configs):
        ...
