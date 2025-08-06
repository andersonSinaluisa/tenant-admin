from abc import ABC, abstractmethod


class PlanRepository(ABC):
    @abstractmethod
    def list(self):
        """Return iterable of plans"""

    @abstractmethod
    def retrieve(self, plan_id):
        """Return a plan"""
