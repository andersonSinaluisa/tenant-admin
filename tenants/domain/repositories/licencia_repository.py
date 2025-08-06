from abc import ABC, abstractmethod


class LicenciaRepository(ABC):
    @abstractmethod
    def list(self, tenant_id):
        ...

    @abstractmethod
    def create(self, tenant_id, **data):
        ...

    @abstractmethod
    def retrieve(self, tenant_id, licencia_id):
        ...

    @abstractmethod
    def update(self, licencia, **data):
        ...

    @abstractmethod
    def delete(self, licencia):
        ...

    @abstractmethod
    def renew(self, licencia, **data):
        ...
