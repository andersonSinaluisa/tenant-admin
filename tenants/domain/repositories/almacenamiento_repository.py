from abc import ABC, abstractmethod


class AlmacenamientoRepository(ABC):
    @abstractmethod
    def get_or_create(self, tenant_id):
        ...

    @abstractmethod
    def update(self, obj, **data):
        ...
