from tenants.domain.repositories.plan_repository import PlanRepository


class PlanService:
    def __init__(self, repository: PlanRepository):
        self.repository = repository

    def list(self):
        return self.repository.list()

    def retrieve(self, plan_id):
        return self.repository.retrieve(plan_id)
