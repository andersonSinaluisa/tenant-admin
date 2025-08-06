from abc import ABC, abstractmethod


class AuditoriaRepository(ABC):
    @abstractmethod
    def list(self, tenant_id):
        ...

    @abstractmethod
    def retrieve(self, tenant_id, auditoria_id):
        ...

    @abstractmethod
    def delete(self, auditoria):
        ...
