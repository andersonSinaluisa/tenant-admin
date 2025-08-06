from abc import ABC, abstractmethod


class ModuloRepository(ABC):
    @abstractmethod
    def list(self, tenant_id):
        ...

    @abstractmethod
    def create(self, tenant_id, **data):
        ...

    @abstractmethod
    def retrieve(self, tenant_id, modulo_id):
        ...

    @abstractmethod
    def update(self, modulo, **data):
        ...

    @abstractmethod
    def delete(self, modulo):
        ...

    @abstractmethod
    def enable(self, modulo):
        ...

    @abstractmethod
    def disable(self, modulo):
        ...
