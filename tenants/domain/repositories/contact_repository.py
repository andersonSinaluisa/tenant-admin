from abc import ABC, abstractmethod


class ContactRepository(ABC):
    @abstractmethod
    def list(self, tenant_id):
        ...

    @abstractmethod
    def create(self, tenant_id, **data):
        ...

    @abstractmethod
    def retrieve(self, tenant_id, contact_id):
        ...

    @abstractmethod
    def update(self, contact, **data):
        ...

    @abstractmethod
    def delete(self, contact):
        ...
