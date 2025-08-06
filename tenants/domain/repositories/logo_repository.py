from abc import ABC, abstractmethod


class LogoRepository(ABC):
    @abstractmethod
    def get(self, tenant_id):
        ...

    @abstractmethod
    def save(self, tenant_id, **data):
        ...

    @abstractmethod
    def delete(self, tenant_id):
        ...
